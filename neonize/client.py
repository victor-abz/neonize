from __future__ import annotations

import ctypes
import re
import struct
import time
import typing
from datetime import timedelta
from io import BytesIO
from typing import Any, Optional, List

import magic
from PIL import Image
from google.protobuf.internal.containers import RepeatedCompositeFieldContainer
from linkpreview import link_preview

from ._binder import gocode, func_string, func_callback_bytes, func
from .builder import build_edit, build_revoke
from .events import Event
from .exc import (
    ContactStoreError,
    DownloadError,
    ResolveContactQRLinkError,
    SendAppStateError,
    SetDefaultDisappearingTimerError,
    SetDisappearingTimerError,
    SetGroupAnnounceError,
    SetGroupLockedError,
    SetGroupTopicError,
    SetPassiveError,
    SetPrivacySettingError,
    SetStatusMessageError,
    SubscribePresenceError,
    UnfollowNewsletterError,
    UnlinkGroupError,
    UpdateBlocklistError,
    UpdateGroupParticipantsError,
    UploadError,
    InviteLinkError,
    GetGroupInfoError,
    SetGroupPhotoError,
    GetGroupInviteLinkError,
    CreateGroupError,
    IsOnWhatsAppError,
    GetUserInfoError,
    SendMessageError,
    BuildPollVoteError,
    CreateNewsletterError,
    FollowNewsletterError,
    GetBlocklistError,
    GetProfilePictureError,
    GetStatusPrivacyError,
    GetSubGroupsError,
    GetSubscribedNewslettersError,
    LogoutError,
    MarkReadError,
    NewsletterMarkViewedError,
    NewsletterSendReactionError,
)
from .exc import (
    GetContactQrLinkError,
    GetGroupRequestParticipantsError,
    GetJoinedGroupsError,
    GetLinkedGroupParticipantsError,
    GetNewsletterInfoError,
    GetNewsletterInfoWithInviteError,
    GetNewsletterMessageUpdateError,
    GetNewsletterMessagesError,
    GetUserDevicesError,
    JoinGroupWithInviteError,
    LinkGroupError,
    NewsletterSubscribeLiveUpdatesError,
    NewsletterToggleMuteError,
)
from .proto import Neonize_pb2 as neonize_proto
from .proto.Neonize_pb2 import (
    Contact,
    ContactEntry,
    ContactEntryArray,
    ContactInfo,
    ContactsGetContactReturnFunction,
    ContactsPutPushNameReturnFunction,
    GroupParticipant,
    Blocklist,
    GroupLinkTarget,
    MessageInfo,
    JID,
    NewsletterMessage,
    NewsletterMetadata,
    PrivacySettings,
    ProfilePictureInfo,
    StatusPrivacy,
    UploadReturnFunction,
    GroupInfo,
    JoinGroupWithLinkReturnFunction,
    GetGroupInviteLinkReturnFunction,
    GetGroupInfoReturnFunction,
    DownloadReturnFunction,
    SendMessageReturnFunction,
    UploadResponse,
    SetGroupPhotoReturnFunction,
    ReqCreateGroup,
    GroupLinkedParent,
    GroupParent,
    IsOnWhatsAppReturnFunction,
    IsOnWhatsAppResponse,
    JIDArray,
    GetUserInfoReturnFunction,
    GetUserInfoSingleReturnFunction,
    SendResponse,
    Device,
)
from .proto.def_pb2 import DeviceProps
from .proto.def_pb2 import (
    Message,
    StickerMessage,
    ContextInfo,
    ExtendedTextMessage,
    VideoMessage,
    ImageMessage,
    AudioMessage,
    DocumentMessage,
    ContactMessage,
)
from .types import MessageServerID
from .utils import get_duration, gen_vcard, log, cv_to_webp, validate_link
from .utils.enum import (
    BlocklistAction,
    MediaType,
    ChatPresence,
    ChatPresenceMedia,
    LogLevel,
    ParticipantChange,
    ReceiptType,
    ClientType,
    ClientName,
    PrivacySetting,
    PrivacySettingType,
)
from .utils.iofile import get_bytes_from_name_or_url
from .utils.jid import Jid2String, JIDToNonAD
from .utils.thumbnail import generate_thumbnail


class ContactStore:
    def __init__(self, uuid: bytes) -> None:
        self.uuid = uuid
        self.__client = gocode

    def put_pushname(
        self, user: JID, pushname: str
    ) -> ContactsPutPushNameReturnFunction:
        user_bytes = user.SerializeToString()
        model = ContactsPutPushNameReturnFunction.FromString(
            self.__client.PutPushName(
                user_bytes, len(user_bytes), pushname.encode()
            ).get_bytes()
        )
        if model.Error:
            raise ContactStoreError(model.Error)
        return model

    def put_contact_name(self, user: JID, fullname: str, firstname: str):
        user_bytes = user.SerializeToString()
        err = self.__client.PutContactName(
            self.uuid,
            user_bytes,
            len(user_bytes),
            fullname.encode(),
            firstname.encode(),
        ).decode()
        if err:
            return ContactStoreError(err)

    def put_all_contact_name(self, contact_entry: List[ContactEntry]):
        entry = ContactEntryArray(ContactEntry=contact_entry).SerializeToString()
        err = self.__client.PutAllContactNames(self.uuid, entry, len(entry)).decode()
        if err:
            raise ContactStoreError(err)

    def get_contact(self, user: JID) -> ContactInfo:
        jid = user.SerializeToString()
        model = ContactsGetContactReturnFunction.FromString(
            self.__client.GetContact(self.uuid, jid, len(jid)).get_bytes()
        )
        if model.Error:
            raise ContactStoreError(model.Error)
        return model.ContactInfo

    def get_all_contacts(self) -> RepeatedCompositeFieldContainer[Contact]:
        model = neonize_proto.ContactsGetAllContactsReturnFunction.FromString(
            self.__client.GetAllContacts(self.uuid).get_bytes()
        )
        if model.Error:
            raise ContactStoreError(model.Error)
        return model.Contact


class NewClient:
    def __init__(
        self,
        name: str,
        props: Optional[DeviceProps] = None,
        uuid: Optional[str] = None,
    ):
        """Initializes a new client instance.

        :param name: The name or identifier for the new client.
        :type name: str
        :param qrCallback: Optional. A callback function for handling QR code updates, defaults to None.
        :type qrCallback: Optional[Callable[[NewClient, bytes], None]], optional
        :param messageCallback: Optional. A callback function for handling incoming messages, defaults to None.
        :type messageCallback: Optional[Callable[[NewClient, MessageSource, Message], None]], optional
        :param uuid: Optional. A unique identifier for the client, defaults to None.
        :type uuid: Optional[str], optional
        """
        self.name = name
        self.device_props = props
        self.uuid = (uuid or name).encode()
        self.__client = gocode
        self.event = Event(self)
        self.blocking = self.event.blocking
        self.qr = self.event.qr
        self.contact = ContactStore(self.uuid)
        log.debug("🔨 Creating a NewClient instance")

    def __onLoginStatus(self, s: str):
        print(s)

    def __onQr(self, qr_protoaddr: int):
        """
        This method triggers an event when a QR code is detected.

        :param qr_protoaddr: The address of the QR code in memory.
        :type qr_protoaddr: int
        """
        self.event._qr(self, ctypes.string_at(qr_protoaddr))

    def _parse_mention(self, text: Optional[str] = None) -> list[str]:
        """_summary_

        :param text: _description_, defaults to None
        :type text: Optional[str], optional
        :return: _description_
        :rtype: list[str]
        """
        """
        This function parses a given text and returns a list of 'mentions' in the format of 'mention@s.whatsapp.net'.
        A 'mention' is defined as a sequence of numbers (5 to 16 digits long) that is prefixed by '@' in the text.
    
        :param text: The text to be parsed for mentions, defaults to None
        :type text: Optional[str], optional
        :return: A list of mentions in the format of 'mention@s.whatsapp.net'
        :rtype: list[str]
        """
        if text is None:
            return []
        return [
            jid.group(1) + "@s.whatsapp.net"
            for jid in re.finditer(r"@([0-9]{5,16}|0)", text)
        ]

    def _generate_link_preview(self, text: str) -> ExtendedTextMessage | None:
        youtube_url_pattern = re.compile(
            r"(?:https?:)?//(?:www\.)?(?:youtube\.com/(?:[^/\n\s]+"
            r"/\S+/|(?:v|e(?:mbed)?)/|\S*?[?&]v=)|youtu\.be/)([a-zA-Z0-9_-]{11})",
            re.IGNORECASE
        )
        links = re.findall(r"https?://\S+", text)
        valid_links = list(filter(validate_link, links))
        if valid_links:
            preview = link_preview(valid_links[0])
            preview_type = 1 if re.match(youtube_url_pattern, valid_links[0]) else 0
            msg = ExtendedTextMessage(
                title=preview.title,
                description=preview.description,
                matchedText=valid_links[0],
                canonicalUrl=preview.link.url,
                previewType=preview_type
            )
            if preview.absolute_image:
                thumbnail = get_bytes_from_name_or_url(preview.absolute_image)
                mimetype = magic.from_buffer(thumbnail, mime=True)
                if "jpeg" in mimetype or "png" in mimetype:
                    image = Image.open(BytesIO(thumbnail))
                    upload = self.upload(thumbnail, MediaType.MediaLinkThumbnail)
                    msg.MergeFrom(
                        ExtendedTextMessage(
                            jpegThumbnail=thumbnail,
                            thumbnailDirectPath=upload.DirectPath,
                            thumbnailSha256=upload.FileSHA256,
                            thumbnailEncSha256=upload.FileEncSHA256,
                            mediaKey=upload.MediaKey,
                            mediaKeyTimestamp=int(time.time()),
                            thumbnailWidth=image.size[0],
                            thumbnailHeight=image.size[1],
                        )
                    )
            return msg
        return None

    def _make_quoted_message(self, message: neonize_proto.Message) -> ContextInfo:
        return ContextInfo(
            stanzaId=message.Info.ID,
            participant=Jid2String(JIDToNonAD(message.Info.MessageSource.Sender)),
            quotedMessage=message.Message,
        )

    def send_message(
        self, to: JID, message: typing.Union[Message, str], link_preview: bool = False
    ) -> SendResponse:
        """Send a message to the specified JID.

        :param to: The JID to send the message to.
        :type to: JID
        :param message: The message to send.
        :type message: typing.Union[Message, str]
        :param link_preview: Whether to send a link preview, defaults to False
        :type link_preview: bool, optional
        :raises SendMessageError: If there was an error sending the message.
        :return: The response from the server.
        :rtype: SendResponse
        """
        to_bytes = to.SerializeToString()
        if isinstance(message, str):
            message_bytes = Message(conversation=message).SerializeToString()
            if link_preview:
                msg = ExtendedTextMessage(text=message)
                preview = self._generate_link_preview(message)
                if preview:
                    msg.MergeFrom(preview)
                message_bytes = Message(extendedTextMessage=msg).SerializeToString()
        else:
            message_bytes = message.SerializeToString()
        sendresponse = self.__client.SendMessage(
            self.uuid, to_bytes, len(to_bytes), message_bytes, len(message_bytes)
        ).get_bytes()
        model = SendMessageReturnFunction.FromString(sendresponse)
        if model.Error:
            raise SendMessageError(model.Error)
        return model.SendResponse

    def reply_message(
        self, to: JID, text: str, quoted: neonize_proto.Message, link_preview: bool = False
    ) -> SendResponse:
        """Send a reply message to a specified JID.

        :param to: The JID of the recipient.
        :type to: JID
        :param text: The text of the reply message.
        :type text: str
        :param quoted: The message to be quoted.
        :type quoted: Message
        :param link_preview: Whether to send a link preview, defaults to False
        :type link_preview: bool, optional

        :return: The response from sending the message.
        :rtype: SendResponse
        """
        message = Message(
            extendedTextMessage=ExtendedTextMessage(
                text=text,
                contextInfo=ContextInfo(
                    mentionedJid=self._parse_mention(text),
                ),
            )
        )
        message.extendedTextMessage.contextInfo.MergeFrom(
            self._make_quoted_message(quoted)
        )
        return self.send_message(to, message, link_preview)

    def edit_message(
        self, chat: JID, message_id: str, new_message: Message
    ) -> SendResponse:
        """Edit a message.

        :param chat: Chat ID
        :type chat: JID
        :param message_id: Message ID
        :type message_id: str
        :param new_message: New message
        :type new_message: Message
        :return: Response from server
        :rtype: SendResponse
        """
        return self.send_message(chat, build_edit(chat, message_id, new_message))

    def revoke_message(self, chat: JID, sender: JID, message_id: str) -> SendResponse:
        """Revoke a message.

        :param chat: Chat ID
        :type chat: JID
        :param sender: Sender ID
        :type sender: JID
        :param message_id: Message ID
        :type message_id: str
        :return: Response from server
        :rtype: SendResponse
        """
        return self.send_message(chat, self.build_revoke(chat, sender, message_id))

    def build_poll_vote_creation(
        self, name: str, options: List[str], selectable_count: int
    ) -> Message:
        """Build a poll vote creation message.

        :param name: The name of the poll.
        :type name: str
        :param options: The options for the poll.
        :type options: List[str]
        :param selectable_count: The number of selectable options.
        :type selectable_count: int
        :return: The poll vote creation message.
        :rtype: Message
        """
        options_buf = neonize_proto.ArrayString(data=options).SerializeToString()
        return Message.FromString(
            self.__client.BuildPollVoteCreation(
                self.uuid,
                name.encode(),
                options_buf,
                len(options_buf),
                selectable_count,
            ).get_bytes()
        )

    def build_poll_vote(
        self, poll_info: MessageInfo, option_names: List[str]
    ) -> Message:
        """Builds a poll vote.

        :param poll_info: The information about the poll.
        :type poll_info: MessageInfo
        :param option_names: The names of the options to vote for.
        :type option_names: List[str]
        :return: The poll vote message.
        :rtype: Message
        :raises BuildPollVoteError: If there is an error building the poll vote.
        """
        option_names_proto = neonize_proto.ArrayString(
            data=option_names
        ).SerializeToString()
        poll_info_proto = poll_info.SerializeToString()
        resp = self.__client.BuildPollVote(
            self.uuid,
            poll_info_proto,
            len(poll_info_proto),
            option_names_proto,
            len(option_names_proto),
        ).get_bytes()
        model = neonize_proto.BuildPollVoteReturnFunction.FromString(resp)
        if model.Error:
            raise BuildPollVoteError(model.Error)
        return model.PollVote

    def build_reaction(
        self, chat: JID, sender: JID, message_id: str, reaction: str
    ) -> Message:
        sender_proto = sender.SerializeToString()
        chat_proto = chat.SerializeToString()
        return Message.FromString(
            self.__client.BuildReaction(
                self.uuid,
                chat_proto,
                len(chat_proto),
                sender_proto,
                len(sender_proto),
                message_id.encode(),
                reaction.encode(),
            ).get_bytes()
        )

    def build_revoke(
        self, chat: JID, sender: JID, message_id: str, with_go: bool = False
    ) -> Message:
        """Builds a message to revoke a previous message.

        :param chat: The JID (Jabber Identifier) of the chat where the message should be revoked.
        :type chat: JID
        :param sender: The JID of the sender of the message to be revoked.
        :type sender: JID
        :param message_id: The unique identifier of the message to be revoked.
        :type message_id: str
        :return: The constructed Message object for revoking the specified message.
        :rtype: Message
        """
        if with_go:
            chat_buf = chat.SerializeToString()
            sender_buf = sender.SerializeToString()
            return Message.FromString(
                self.__client.BuildRevoke(
                    self.uuid,
                    chat_buf,
                    len(chat_buf),
                    sender_buf,
                    len(sender_buf),
                    message_id.encode(),
                ).get_bytes()
            )
        else:
            return build_revoke(chat, sender, message_id, self.get_me().JID)

    def send_sticker(
        self,
        to: JID,
        file: typing.Union[str, bytes],
        quoted: Optional[neonize_proto.Message] = None,
        name: str = "",
        packname: str = ""
    ) -> SendResponse:
        """Sends a sticker to the specified recipient.

        :param to: The JID (Jabber Identifier) of the recipient.
        :type to: JID
        :param file: Either a file path (str) or URL (str) or binary data (bytes) Image/Video/Gif.
        :type file: typing.Union[str | bytes]
        :param quoted: Optional. The message to which the sticker is a reply. Defaults to None.
        :type quoted: Optional[Message], optional
        :param name: Optional. The name of the sticker pack. Defaults to "".
        :type name: str, optional
        :param packname: Optional. The pack name of the sticker pack. Defaults to "".
        :type packname: str, optional
        :return: A function for handling the result of the sticker sending process.
        :rtype: SendResponse
        """
        image_buf = get_bytes_from_name_or_url(file)
        mimetype = magic.from_buffer(image_buf, mime=True)
        is_video = "video" in mimetype or "gif" in mimetype
        io_save = cv_to_webp(image_buf, is_video, name, packname)
        io_save.seek(0)
        save = io_save.read()
        upload = self.upload(save)
        message = Message(
            stickerMessage=StickerMessage(
                url=upload.url,
                directPath=upload.DirectPath,
                fileEncSha256=upload.FileEncSHA256,
                fileLength=upload.FileLength,
                fileSha256=upload.FileSHA256,
                mediaKey=upload.MediaKey,
                mimetype=magic.from_buffer(save, mime=True),
            )
        )
        if quoted:
            message.stickerMessage.contextInfo.MergeFrom(
                self._make_quoted_message(quoted)
            )
        return self.send_message(
            to,
            message,
        )

    def send_video(
        self,
        to: JID,
        file: str | bytes,
        caption: Optional[str] = None,
        quoted: Optional[neonize_proto.Message] = None,
        viewonce: bool = False,
    ) -> SendResponse:
        """Sends a video to the specified recipient.

        :param to: The JID (Jabber Identifier) of the recipient.
        :type to: JID
        :param file: Either a file path (str), url (str) or binary data (bytes) representing the video.
        :type file: typing.Union[str | bytes]
        :param caption: Optional. The caption of the video. Defaults to None.
        :type caption: Optional[str], optional
        :param quoted: Optional. The message to which the video is a reply. Defaults to None.
        :type quoted: Optional[Message], optional
        :param viewonce: Optional. Whether the video should be viewonce. Defaults to False.
        :type viewonce: bool, optional
        :return: A function for handling the result of the video sending process.
        :rtype: SendResponse
        """
        io = BytesIO(get_bytes_from_name_or_url(file))
        io.seek(0)
        buff = io.read()
        upload = self.upload(buff)
        message = Message(
            videoMessage=VideoMessage(
                url=upload.url,
                caption=caption,
                seconds=int(get_duration(buff)),
                directPath=upload.DirectPath,
                fileEncSha256=upload.FileEncSHA256,
                fileLength=upload.FileLength,
                fileSha256=upload.FileSHA256,
                mediaKey=upload.MediaKey,
                mimetype=magic.from_buffer(buff, mime=True),
                jpegThumbnail=generate_thumbnail(buff),
                thumbnailDirectPath=upload.DirectPath,
                thumbnailEncSha256=upload.FileEncSHA256,
                thumbnailSha256=upload.FileSHA256,
                viewOnce=viewonce,
                contextInfo=ContextInfo(
                    mentionedJid=self._parse_mention(caption),
                ),
            )
        )
        if quoted:
            message.videoMessage.contextInfo.MergeFrom(
                self._make_quoted_message(quoted)
            )
        return self.send_message(to, message)

    def send_image(
        self,
        to: JID,
        file: str | bytes,
        caption: Optional[str] = None,
        quoted: Optional[neonize_proto.Message] = None,
        viewonce: bool = False,
    ) -> SendResponse:
        """Sends an image to the specified recipient.

        :param to: The JID (Jabber Identifier) of the recipient.
        :type to: JID
        :param file: Either a file path (str), url (str) or binary data (bytes) representing the image.
        :type file: typing.Union[str | bytes]
        :param caption: Optional. The caption of the image. Defaults to None.
        :type caption: Optional[str], optional
        :param quoted: Optional. The message to which the image is a reply. Defaults to None.
        :type quoted: Optional[Message], optional
        :param viewonce: Optional. Whether the image should be viewonce. Defaults to False.
        :type viewonce: bool, optional
        :return: A function for handling the result of the image sending process.
        :rtype: SendResponse
        """
        io = BytesIO(get_bytes_from_name_or_url(file))
        io.seek(0)
        buff = io.read()
        upload = self.upload(buff)
        message = Message(
            imageMessage=ImageMessage(
                url=upload.url,
                caption=caption,
                directPath=upload.DirectPath,
                fileEncSha256=upload.FileEncSHA256,
                fileLength=upload.FileLength,
                fileSha256=upload.FileSHA256,
                mediaKey=upload.MediaKey,
                mimetype=magic.from_buffer(buff, mime=True),
                jpegThumbnail=generate_thumbnail(buff),
                thumbnailDirectPath=upload.DirectPath,
                thumbnailEncSha256=upload.FileEncSHA256,
                thumbnailSha256=upload.FileSHA256,
                viewOnce=viewonce,
                contextInfo=ContextInfo(
                    mentionedJid=self._parse_mention(caption),
                ),
            )
        )
        if quoted:
            message.imageMessage.contextInfo.MergeFrom(
                self._make_quoted_message(quoted)
            )
        return self.send_message(to, message)

    def send_audio(
        self,
        to: JID,
        file: str | bytes,
        ptt: bool = False,
        quoted: Optional[neonize_proto.Message] = None,
    ) -> SendResponse:
        """Sends an audio to the specified recipient.

        :param to: The JID (Jabber Identifier) of the recipient.
        :type to: JID
        :param file: Either a file path (str), url (str) or binary data (bytes) representing the audio.
        :type file: typing.Union[str | bytes]
        :param ptt: Optional. Whether the audio should be ptt. Defaults to False.
        :type ptt: bool, optional
        :param quoted: Optional. The message to which the audio is a reply. Defaults to None.
        :type quoted: Optional[Message], optional
        :return: A function for handling the result of the audio sending process.
        :rtype: SendResponse
        """
        io = BytesIO(get_bytes_from_name_or_url(file))
        io.seek(0)
        buff = io.read()
        upload = self.upload(buff)
        message = Message(
            audioMessage=AudioMessage(
                url=upload.url,
                seconds=int(get_duration(buff)),
                directPath=upload.DirectPath,
                fileEncSha256=upload.FileEncSHA256,
                fileLength=upload.FileLength,
                fileSha256=upload.FileSHA256,
                mediaKey=upload.MediaKey,
                mimetype=magic.from_buffer(buff, mime=True),
                ptt=ptt,
            )
        )
        if quoted:
            message.audioMessage.contextInfo.MergeFrom(
                self._make_quoted_message(quoted)
            )
        return self.send_message(to, message)

    def send_document(
        self,
        to: JID,
        file: str | bytes,
        caption: Optional[str] = None,
        title: Optional[str] = None,
        filename: Optional[str] = None,
        quoted: Optional[neonize_proto.Message] = None,
    ) -> SendResponse:
        """Sends a document to the specified recipient.

        :param to: The JID (Jabber Identifier) of the recipient.
        :type to: JID
        :param file: Either a file path (str), url (str) or binary data (bytes) representing the document.
        :type file: typing.Union[str | bytes]
        :param caption: Optional. The caption of the document. Defaults to None.
        :type caption: Optional[str], optional
        :param title: Optional. The title of the document. Defaults to None.
        :type title: Optional[str], optional
        :param filename: Optional. The filename of the document. Defaults to None.
        :type filename: Optional[str], optional
        :param quoted: Optional. The message to which the document is a reply. Defaults to None.
        :type quoted: Optional[Message], optional
        :return: A function for handling the result of the document sending process.
        :rtype: SendResponse
        """
        io = BytesIO(get_bytes_from_name_or_url(file))
        io.seek(0)
        buff = io.read()
        upload = self.upload(buff)
        message = Message(
            documentMessage=DocumentMessage(
                url=upload.url,
                caption=caption,
                directPath=upload.DirectPath,
                fileEncSha256=upload.FileEncSHA256,
                fileLength=upload.FileLength,
                fileSha256=upload.FileSHA256,
                mediaKey=upload.MediaKey,
                mimetype=magic.from_buffer(buff, mime=True).replace(
                    "application", "document"
                ),
                title=title,
                fileName=filename,
                contextInfo=ContextInfo(
                    mentionedJid=self._parse_mention(caption),
                ),
            )
        )
        if quoted:
            message.documentMessage.contextInfo.MergeFrom(
                self._make_quoted_message(quoted)
            )
        return self.send_message(to, message)

    def send_contact(
        self,
        to: JID,
        contact_name: str,
        contact_number: str,
        quoted: Optional[neonize_proto.Message] = None,
    ) -> SendResponse:
        """Sends a contact to the specified recipient.

        :param to: The JID (Jabber Identifier) of the recipient.
        :type to: JID
        :param contact_name: The name of the contact.
        :type contact_name: str
        :param contact_number: The number of the contact.
        :type contact_number: str
        :param quoted: Optional. The message to which the contact is a reply. Defaults to None.
        :type quoted: Optional[Message], optional
        :return: A function for handling the result of the contact sending process.
        :rtype: SendResponse
        """
        message = Message(
            contactMessage=ContactMessage(
                displayName=contact_name,
                vcard=gen_vcard(contact_name, contact_number),
            )
        )
        if quoted:
            message.contactMessage.contextInfo.MergeFrom(
                self._make_quoted_message(quoted)
            )
        return self.send_message(to, message)

    def upload(
        self, binary: bytes, media_type: Optional[MediaType] = None
    ) -> UploadResponse:
        """Uploads media content.

        :param binary: The binary data to be uploaded.
        :type binary: bytes
        :param media_type: Optional. The media type of the binary data, defaults to None.
        :type media_type: Optional[MediaType], optional
        :raises UploadError: Raised if there is an issue with the upload.
        :return: An UploadResponse containing information about the upload.
        :rtype: UploadResponse
        """
        if not media_type:
            mime = MediaType.from_magic(binary)
        else:
            mime = media_type
        response = self.__client.Upload(self.uuid, binary, len(binary), mime.value)
        upload_model = UploadReturnFunction.FromString(response.get_bytes())
        if upload_model.Error:
            raise UploadError(upload_model.Error)
        return upload_model.UploadResponse

    def download_any(
        self, message: Message, path: Optional[str] = None
    ) -> typing.Union[None, bytes]:
        """Downloads content from a message.

        :param message: The message containing the content to download.
        :type message: Message
        :param path: Optional. The local path to save the downloaded content, defaults to None.
        :type path: Optional[str], optional
        :raises DownloadException: Raised if there is an issue with the download.
        :return: The downloaded content as bytes, or None if the content is not available.
        :rtype: Union[None, bytes]
        """
        msg_protobuf = message.SerializeToString()
        media_buff = self.__client.DownloadAny(
            self.uuid, msg_protobuf, len(msg_protobuf)
        ).get_bytes()
        media = DownloadReturnFunction.FromString(media_buff)
        if media.Error:
            raise DownloadError(media.Error)
        if path:
            with open(path, "wb") as file:
                file.write(media.Binary)
        else:
            return media.Binary
        return None

    def download_media_with_path(
        self,
        direct_path: str,
        enc_file_hash: bytes,
        file_hash: bytes,
        media_key: bytes,
        file_length: int,
        media_type: MediaType,
        mms_type: str,
    ) -> bytes:
        """
        Downloads media with the given parameters and path. The media is downloaded from the path specified.

        :param direct_path: The direct path to the media to be downloaded.
        :type direct_path: str
        :param enc_file_hash: The encrypted hash of the file.
        :type enc_file_hash: bytes
        :param file_hash: The hash of the file.
        :type file_hash: bytes
        :param media_key: The key of the media to be downloaded.
        :type media_key: bytes
        :param file_length: The length of the file to be downloaded.
        :type file_length: int
        :param media_type: The type of the media to be downloaded.
        :type media_type: MediaType
        :param mms_type: The type of the MMS to be downloaded.
        :type mms_type: str
        :raises DownloadError: If there is an error in the download process.
        :return: The downloaded media in bytes.
        :rtype: bytes
        """
        model = neonize_proto.DownloadReturnFunction.FromString(
            self.__client.DownloadMediaWithPath(
                self.uuid,
                direct_path.encode(),
                enc_file_hash,
                len(enc_file_hash),
                file_hash,
                len(file_hash),
                media_key,
                len(media_key),
                file_length,
                media_type.value,
                mms_type.encode(),
            ).get_bytes()
        )
        if model.Error:
            raise DownloadError(model.Error)
        return model.Binary

    def generate_message_id(self) -> str:
        """Generates a unique identifier for a message.

        :return: A string representing the unique identifier for the message.
        :rtype: str
        """
        return self.__client.GenerateMessageID(self.uuid).decode()

    def send_chat_presence(
        self, jid: JID, state: ChatPresence, media: ChatPresenceMedia
    ) -> str:
        """Sends chat presence information.

        :param jid: The JID (Jabber Identifier) of the chat.
        :type jid: JID
        :param state: The chat presence state.
        :type state: ChatPresence
        :param media: The chat presence media information.
        :type media: ChatPresenceMedia
        :return: A string indicating the result or status of the presence information sending.
        :rtype: str
        """
        jidbyte = jid.SerializeToString()
        return self.__client.SendChatPresence(
            self.uuid, jidbyte, len(jidbyte), state.value, media.value
        ).decode()

    def is_on_whatsapp(
        self, numbers: List[str] = []
    ) -> RepeatedCompositeFieldContainer[IsOnWhatsAppResponse] | List:
        """Check if the provided phone numbers are on WhatsApp.

        :param numbers: List of phone numbers to check. Defaults to [].
        :type numbers: List[str], optional
        :raises IsOnWhatsAppError: Raised if there is an error while checking.
        :return: A response object containing information about WhatsApp presence.
        :rtype: IsOnWhatsAppResponse
        """
        if numbers:
            numbers_buf = " ".join(numbers).encode()
            response = self.__client.IsOnWhatsApp(
                self.uuid, numbers_buf, len(numbers_buf)
            ).get_bytes()
            model = IsOnWhatsAppReturnFunction.FromString(response)
            if model.Error:
                raise IsOnWhatsAppError(model.Error)
            return model.IsOnWhatsAppResponse
        return []

    @property
    def is_connected(self) -> bool:
        """Check if the object is currently connected.

        :return: True if the object is connected, False otherwise.
        :rtype: bool
        """
        return self.__client.IsConnected(self.uuid)

    @property
    def is_logged_in(self) -> bool:
        """Check if the user is currently logged in.

        :return: True if the user is logged in, False otherwise.
        :rtype: bool
        """
        return self.__client.IsLoggedIn(self.uuid)

    def get_user_info(
        self, jid: List[JID]
    ) -> RepeatedCompositeFieldContainer[GetUserInfoSingleReturnFunction]:
        """Retrieve information for the provided JIDs.

        :param jid: List of JIDs (Jabber IDs) for which to retrieve information.
        :type jid: List[JID]
        :raises GetUserInfoError: Raised if there is an error while retrieving user information.
        :return: A function providing information for the specified JIDs.
        :rtype: GetUserInfoSingleReturnFunction
        """
        jidbuf = JIDArray(JIDS=jid).SerializeToString()
        getUser = self.__client.GetUserInfo(self.uuid, jidbuf, len(jidbuf)).get_bytes()
        model = GetUserInfoReturnFunction.FromString(getUser)
        if model.Error:
            raise GetUserInfoError(model.Error)
        return model.UsersInfo

    def get_group_info(self, jid: JID) -> GroupInfo:
        """Retrieves information about a group.

        :param jid: The JID (Jabber Identifier) of the group.
        :type jid: JID
        :raises GetGroupInfoError: Raised if there is an issue retrieving group information.
        :return: Information about the specified group.
        :rtype: GroupInfo
        """
        jidbuf = jid.SerializeToString()
        group_info_buf = self.__client.GetGroupInfo(
            self.uuid,
            jidbuf,
            len(jidbuf),
        )
        model = GetGroupInfoReturnFunction.FromString(group_info_buf.get_bytes())
        if model.Error:
            raise GetGroupInfoError(model.Error)
        return model.GroupInfo

    def get_group_info_from_link(self, code: str) -> GroupInfo:
        """Retrieves group information from a given link.

        :param code: The link code.
        :type code: str
        :return: An object containing the group information.
        :rtype: GroupInfo
        :raises GetGroupInfoError: If there is an error retrieving the group information.
        """
        model = GetGroupInfoReturnFunction.FromString(
            self.__client.GetGroupInfoFromLink(self.uuid, code.encode()).get_bytes()
        )
        if model.Error:
            raise GetGroupInfoError(model.Error)
        return model.GroupInfo

    def get_group_info_from_invite(
        self, jid: JID, inviter: JID, code: str, expiration: int
    ) -> GroupInfo:
        """Retrieves group information from an invite.

        :param jid: The JID (Jabber ID) of the group.
        :type jid: JID
        :param inviter: The JID of the user who sent the invite.
        :type inviter: JID
        :param code: The invite code.
        :type code: str
        :param expiration: The expiration time of the invite.
        :type expiration: int

        :return: The group information.
        :rtype: GroupInfo

        :raises GetGroupInfoError: If there is an error retrieving the group information.
        """
        jidbyte = jid.SerializeToString()
        inviterbyte = inviter.SerializeToString()
        model = GetGroupInfoReturnFunction.FromString(
            self.__client.GetGroupInfoFromInvite(
                self.uuid,
                jidbyte,
                len(jidbyte),
                inviterbyte,
                len(inviterbyte),
                code.encode(),
                expiration,
            ).get_bytes()
        )
        if model.Error:
            raise GetGroupInfoError(model.Error)
        return model.GroupInfo

    def set_group_name(self, jid: JID, name: str) -> str:
        """Sets the name of a group.

        :param jid: The JID (Jabber Identifier) of the group.
        :type jid: JID
        :param name: The new name to be set for the group.
        :type name: str
        :return: A string indicating the result or an error status. Empty string if successful.
        :rtype: str
        """
        jidbuf = jid.SerializeToString()
        return self.__client.SetGroupName(
            self.uuid, jidbuf, len(jidbuf), ctypes.create_string_buffer(name.encode())
        ).decode()

    def set_group_photo(self, jid: JID, file_or_bytes: typing.Union[str, bytes]) -> str:
        """Sets the photo of a group.

        :param jid: The JID (Jabber Identifier) of the group.
        :type jid: JID
        :param file_or_bytes: Either a file path (str) or binary data (bytes) representing the group photo.
        :type file_or_bytes: typing.Union[str, bytes]
        :raises SetGroupPhotoError: Raised if there is an issue setting the group photo.
        :return: A string indicating the result or an error status.
        :rtype: str
        """
        data = get_bytes_from_name_or_url(file_or_bytes)
        jid_buf = jid.SerializeToString()
        response = self.__client.SetGroupPhoto(
            self.uuid, jid_buf, len(jid_buf), data, len(data)
        )
        model = SetGroupPhotoReturnFunction.FromString(response.get_bytes())
        if model.Error:
            raise SetGroupPhotoError(model.Error)
        return model.PictureID

    def leave_group(self, jid: JID) -> str:
        """Leaves a group.

        :param jid: The JID (Jabber Identifier) of the target group.
        :type jid: JID
        :return: A string indicating the result or an error status. Empty string if successful.
        :rtype: str
        """
        jid_buf = jid.SerializeToString()
        return self.__client.LeaveGroup(self.uuid, jid_buf, len(jid_buf)).decode()

    def get_group_invite_link(self, jid: JID, revoke: bool = False) -> str:
        """Gets or revokes the invite link for a group.

        :param jid: The JID (Jabber Identifier) of the group.
        :type jid: JID
        :param revoke: Optional. If True, revokes the existing invite link; if False, gets the invite link. Defaults to False.
        :type revoke: bool, optional
        :raises GetGroupInviteLinkError: Raised if there is an issue getting or revoking the invite link.
        :return: The group invite link or an error status.
        :rtype: str
        """
        jid_buf = jid.SerializeToString()
        response = self.__client.GetGroupInviteLink(
            self.uuid, jid_buf, len(jid_buf), revoke
        ).get_bytes()
        model = GetGroupInviteLinkReturnFunction.FromString(response)
        if model.Error:
            raise GetGroupInviteLinkError(model.Error)
        return model.InviteLink

    def join_group_with_link(self, code: str) -> JID:
        """Join a group using an invite link.

        :param code: The invite code or link for joining the group.
        :type code: str
        :raises InviteLinkError: Raised if the group membership is pending approval or if the link is invalid.
        :return: The JID (Jabber Identifier) of the joined group.
        :rtype: JID
        """
        resp = self.__client.JoinGroupWithLink(self.uuid, code.encode()).get_bytes()
        model = JoinGroupWithLinkReturnFunction.FromString(resp)
        if model.Error:
            raise InviteLinkError(model.Error)
        return model.Jid

    def join_group_with_invite(
        self, jid: JID, inviter: JID, code: str, expiration: int
    ):
        """
        This function allows a user to join a group in a chat application using an invite.
        It uses the JID (Jabber ID) of the group, the JID of the inviter, an invitation code, and an expiration time for the code.

        :param jid: The JID of the group to join.
        :type jid: JID
        :param inviter: The JID of the person who sent the invite.
        :type inviter: JID
        :param code: The invitation code.
        :type code: str
        :param expiration: The expiration time of the invitation code in seconds.
        :type expiration: int
        :raises JoinGroupWithInviteError: If there is an error in joining the group, such as an invalid code or expired invitation.
        """
        jidbytes = jid.SerializeToString()
        inviterbytes = inviter.SerializeToString()
        err = self.__client.JoinGroupWithInvite(
            self.uuid,
            jidbytes,
            len(jidbytes),
            inviterbytes,
            len(inviterbytes),
            code.encode(),
            expiration,
        ).decode()
        if err:
            raise JoinGroupWithInviteError(err)

    def link_group(self, parent: JID, child: JID):
        """
        Links a child group to a parent group.

        :param parent: The JID of the parent group
        :type parent: JID
        :param child: The JID of the child group
        :type child: JID
        :raises LinkGroupError: If there is an error while linking the groups
        """
        parent_bytes = parent.SerializeToString()
        child_bytes = child.SerializeToString()
        err = self.__client.LinkGroup(
            self.uuid, parent_bytes, len(parent_bytes), child_bytes, len(child_bytes)
        ).decode()
        if err:
            raise LinkGroupError(err)

    def logout(self):
        err = self.__client.Logout(self.uuid).decode()
        if err:
            raise LogoutError(err)

    def mark_read(
        self,
        message_ids: List[str],
        chat: JID,
        sender: JID,
        receipt: ReceiptType,
        timestamp: Optional[int] = None,
    ):
        """Marks the specified messages as read.

        :param message_ids: List of IDs of the messages to be marked as read.
        :type message_ids: List[str]
        :param chat: The chat where the messages are located.
        :type chat: JID
        :param sender: The sender of the messages.
        :type sender: JID
        :param receipt: The receipt type of the messages.
        :type receipt: ReceiptType
        :param timestamp: The timestamp when the messages were read, defaults to current time if not provided.
        :type timestamp: Optional[int], optional
        :raises MarkReadError: If there is an error while marking the messages as read.
        """
        chat_proto = chat.SerializeToString()
        sender_proto = sender.SerializeToString()
        timestamp_args = int(time.time()) if timestamp is None else timestamp
        err = self.__client.MarkRead(
            self.uuid,
            " ".join(message_ids).encode(),
            timestamp_args,
            chat_proto,
            len(chat_proto),
            sender_proto,
            len(sender_proto),
            receipt.value,
        )
        if err:
            raise MarkReadError(err.decode())

    def newsletter_mark_viewed(
        self, jid: JID, message_server_ids: List[MessageServerID]
    ):
        """
        Marks the specified newsletters as viewed by the user with the given JID.

        :param jid: The JID (Jabber ID) of the user who has viewed the newsletters.
        :type jid: JID
        :param message_server_ids: List of server IDs of the newsletters that have been viewed.
        :type message_server_ids: List[MessageServerID]
        :raises NewsletterMarkViewedError: If an error occurs while marking the newsletters as viewed.
        """
        servers = struct.pack(f"{len(message_server_ids)}b", *message_server_ids)
        jid_proto = jid.SerializeToString()
        err = self.__client.NewsletterMarkViewed(
            self.uuid, jid_proto, len(jid_proto), servers, len(servers)
        )
        if err:
            raise NewsletterMarkViewedError(err)

    def newsletter_send_reaction(
        self,
        jid: JID,
        message_server_id: MessageServerID,
        reaction: str,
        message_id: str,
    ):
        """
        Sends a reaction to a newsletter.

        :param jid: The unique identifier for the recipient of the newsletter.
        :type jid: JID
        :param message_server_id: The unique identifier for the server where the message is stored.
        :type message_server_id: MessageServerID
        :param reaction: The reaction to be sent.
        :type reaction: str
        :param message_id: The unique identifier for the message to which the reaction is being sent.
        :type message_id: str
        :raises NewsletterSendReactionError: If an error occurs while sending the reaction.
        """
        jid_proto = jid.SerializeToString()
        err = self.__client.NewsletterSendReaction(
            self.uuid,
            jid_proto,
            len(jid_proto),
            message_server_id,
            reaction.encode(),
            message_id.encode(),
        )
        if err:
            raise NewsletterSendReactionError(err)
        return

    def newsletter_subscribe_live_updates(self, jid: JID) -> int:
        """Subscribes a user to live updates of a newsletter.

        :param jid: The unique identifier of the user subscribing to the newsletter.
        :type jid: JID
        :raises NewsletterSubscribeLiveUpdatesError: If there is an error during the subscription process.
        :return: The duration for which the subscription is valid.
        :rtype: int
        """
        jid_proto = jid.SerializeToString()
        model = neonize_proto.NewsletterSubscribeLiveUpdatesReturnFunction.FromString(
            self.__client.NewsletterSubscribeLiveUpdates(
                self.uuid, jid_proto, len(jid_proto)
            ).get_bytes()
        )
        if model.Error:
            raise NewsletterSubscribeLiveUpdatesError(model.Error)
        return model.Duration

    def newsletter_toggle_mute(self, jid: JID, mute: bool):
        """Toggle the mute status of a given JID.

        :param jid: The JID (Jabber Identifier) of the user.
        :type jid: JID
        :param mute: The desired mute status. If True, the user will be muted. If False, the user will be unmuted.
        :type mute: bool
        :raises NewsletterToggleMuteError: If there is an error while toggling the mute status.
        """
        jid_proto = jid.SerializeToString()
        err = self.__client.NewsletterToggleMute(
            self.uuid, jid_proto, len(jid_proto), mute
        ).decode()
        if err:
            raise NewsletterToggleMuteError(err)

    def resolve_business_message_link(
        self, code: str
    ) -> neonize_proto.BusinessMessageLinkTarget:
        """Resolves the target of a business message link.

        :param code: The code of the business message link to be resolved.
        :type code: str
        :raises ResolveContactQRLinkError: If an error occurs while resolving the link.
        :return: The target of the business message link.
        :rtype: neonize_proto.BusinessMessageLinkTarget
        """
        model = neonize_proto.ResolveBusinessMessageLinkReturnFunction.FromString(
            self.__client.ResolveBusinessMessageLink(
                self.uuid, code.encode()
            ).get_bytes()
        )
        if model.Error:
            raise ResolveContactQRLinkError(model.Error)
        return model.MessageLinkTarget

    def resolve_contact_qr_link(self, code: str) -> neonize_proto.ContactQRLinkTarget:
        """Resolves a QR link for a specific contact.

        :param code: The QR code to be resolved.
        :type code: str
        :raises ResolveContactQRLinkError: If an error occurs while resolving the QR link.
        :return: The target contact of the QR link.
        :rtype: neonize_proto.ContactQRLinkTarget
        """
        model = neonize_proto.ResolveContactQRLinkReturnFunction.FromString(
            self.__client.ResolveContactQRLink(self.uuid, code.encode()).get_bytes()
        )
        if model.Error:
            raise ResolveContactQRLinkError(model.Error)
        return model.ContactQrLink

    def send_app_state(self, patch_info: neonize_proto.PatchInfo):
        """
        This function serializes the application state and sends it to the client. If there's an error during this process,
        it raises a SendAppStateError exception.

        :param patch_info: Contains the information about the application state that needs to be patched.
        :type patch_info: neonize_proto.PatchInfo
        :raises SendAppStateError: If there's an error while sending the application state, this exception is raised.
        """
        patch = patch_info.SerializeToString()
        err = self.__client.SendAppState(self.uuid, patch, len(patch)).decode()
        if err:
            raise SendAppStateError(err)

    def set_default_disappearing_timer(self, timer: typing.Union[timedelta, int]):
        """
        Sets a default disappearing timer for messages. The timer can be specified as a timedelta or an integer.
        If a timedelta is provided, it is converted to nanoseconds. If an integer is provided, it is used directly as the timer.

        :param timer: The duration for messages to exist before disappearing. Can be a timedelta or an integer.
        :type timer: typing.Union[timedelta, int]
        :raises SetDefaultDisappearingTimerError: If an error occurs while setting the disappearing timer.
        """
        timestamp = 0
        if isinstance(timer, timedelta):
            timestamp = int(timer.total_seconds() * 1000**3)
        else:
            timestamp = timer
        err = self.__client.SetDefaultDisappearingTimer(self.uuid, timestamp).decode()
        if err:
            raise SetDefaultDisappearingTimerError(err)

    def set_disappearing_timer(self, jid: JID, timer: typing.Union[timedelta, int]):
        """
        Set a disappearing timer for a specific JID. The timer can be set as either a timedelta object or an integer.
        If a timedelta object is provided, it's converted into nanoseconds. If an integer is provided, it's interpreted as nanoseconds.

        :param jid: The JID for which the disappearing timer is to be set
        :type jid: JID
        :param timer: The duration for the disappearing timer. Can be a timedelta object or an integer representing nanoseconds.
        :type timer: typing.Union[timedelta, int]
        :raises SetDisappearingTimerError: If there is an error in setting the disappearing timer
        """
        timestamp = 0
        jid_proto = jid.SerializeToString()
        if isinstance(timer, timedelta):
            timestamp = int(timer.total_seconds() * 1000**3)
        else:
            timestamp = timer
        err = self.__client.SetDisappearingTimer(
            self.uuid, jid_proto, len(jid_proto), timestamp
        ).decode()
        if err:
            raise SetDisappearingTimerError(err)

    def set_force_activate_delivery_receipts(self, active: bool):
        """
        This method is used to forcibly activate or deactivate the delivery receipts for a client.

        :param active: This parameter determines whether the delivery receipts should be forcibly activated or deactivated. If it's True, the delivery receipts will be forcibly activated, otherwise, they will be deactivated.
        :type active: bool
        """
        self.__client.SetForceActiveDeliveryReceipts(self.uuid, active)

    def set_group_announce(self, jid: JID, announce: bool):
        """
        Sets the announcement status of a group.

        :param jid: The unique identifier of the group
        :type jid: JID
        :param announce: The announcement status to be set. If True, announcements are enabled. If False, they are disabled.
        :type announce: bool
        :raises SetGroupAnnounceError: If there is an error while setting the announcement status
        """
        jid_proto = jid.SerializeToString()
        err = self.__client.SetGroupAnnounce(
            self.uuid, jid_proto, len(jid_proto), announce
        ).decode()
        if err:
            raise SetGroupAnnounceError(err)

    def set_group_locked(self, jid: JID, locked: bool):
        """
        Sets the locked status of a group identified by the given JID.

        :param jid: The JID (Jabber ID) of the group to be locked/unlocked.
        :type jid: JID
        :param locked: The new locked status of the group. True to lock the group, False to unlock.
        :type locked: bool
        :raises SetGroupLockedError: If the operation fails, an error with the reason for the failure is raised.
        """
        jid_proto = jid.SerializeToString()
        err = self.__client.SetGroupLocked(
            self.uuid, jid_proto, len(jid_proto), locked
        ).decode()
        if err:
            raise SetGroupLockedError(err)

    def set_group_topic(self, jid: JID, previous_id: str, new_id: str, topic: str):
        """
        Set the topic of a group in a chat application.

        :param jid: The unique identifier of the group
        :type jid: JID
        :param previous_id: The previous identifier of the topic
        :type previous_id: str
        :param new_id: The new identifier for the topic
        :type new_id: str
        :param topic: The new topic to be set
        :type topic: str
        :raises SetGroupTopicError: If there is an error setting the group topic
        """
        jid_proto = jid.SerializeToString()
        err = self.__client.SetGroupTopic(
            self.uuid,
            jid_proto,
            len(jid_proto),
            previous_id.encode(),
            new_id.encode(),
            topic.encode(),
        ).decode()
        if err:
            raise SetGroupTopicError(err)

    def set_privacy_setting(self, name: PrivacySettingType, value: PrivacySetting):
        """
        This method is used to set the privacy settings of a user.

        :param name: The name of the privacy setting to be changed.
        :type name: PrivacySettingType
        :param value: The new value for the privacy setting.
        :type value: PrivacySetting
        :raises SetPrivacySettingError: If there is an error while setting the privacy setting.
        """
        err = self.__client.SetPrivacySetting(
            self.uuid, name.value.encode(), value.value.encode()
        ).decode()
        if err:
            raise SetPrivacySettingError(err)

    def set_passive(self, passive: bool):
        """
        Sets the passive mode of the client.

        :param passive: If True, sets the client to passive mode. If False, sets the client to active mode.
        :type passive: bool
        :raises SetPassiveError: If an error occurs while setting the client to passive mode.
        """
        err = self.__client.SetPassive(self.uuid, passive)
        if err:
            raise SetPassiveError(err)

    def set_status_message(self, msg: str):
        """
        Sets a status message for a client using the client's UUID.

        :param msg: The status message to be set.
        :type msg: str
        :raises SetStatusMessageError: If there is an error while setting the status message.
        """
        err = self.__client.SetStatusMessage(self.uuid, msg.encode()).decode()
        if err:
            raise SetStatusMessageError(err)

    def subscribe_presence(self, jid: JID):
        """
        This method is used to subscribe to the presence of a certain JID (Jabber ID).

        :param jid: The Jabber ID (JID) that we want to subscribe to.
        :type jid: JID
        :raises SubscribePresenceError: If there is an error while subscribing to the presence of the JID.
        """
        jid_proto = jid.SerializeToString()
        err = self.__client.SubscribePresence(
            self.uuid, jid_proto, len(jid_proto)
        ).decode()
        if err:
            raise SubscribePresenceError(err)

    def unfollow_newsletter(self, jid: JID):
        """
        Unfollows a newsletter by providing the JID (Jabber ID) of the newsletter.

        :param jid: The Jabber ID of the newsletter to unfollow.
        :type jid: JID
        :raises UnfollowNewsletterError: If there is an error while attempting to unfollow the newsletter.
        """
        jid_proto = jid.SerializeToString()
        err = self.__client.UnfollowNewsletter(
            self.uuid, jid_proto, len(jid_proto)
        ).decode()
        if err:
            raise UnfollowNewsletterError(err)

    def unlink_group(self, parent: JID, child: JID):
        """
        This method is used to unlink a child group from a parent group.

        :param parent: The JID of the parent group from which the child group is to be unlinked.
        :type parent: JID
        :param child: The JID of the child group which is to be unlinked from the parent group.
        :type child: JID
        :raises UnlinkGroupError: If there is an error while unlinking the child group from the parent group.
        """
        parent_proto = parent.SerializeToString()
        child_proto = child.SerializeToString()
        err = self.__client.UnlinkGroup(
            self.uuid, parent_proto, len(parent_proto), child_proto, len(child_proto)
        ).decode()
        if err:
            raise UnlinkGroupError(err)

    def update_blocklist(self, jid: JID, action: BlocklistAction) -> Blocklist:
        """
        Function to update the blocklist with a given action on a specific JID.

        :param jid: The Jabber ID (JID) of the user to be blocked or unblocked.
        :type jid: JID
        :param action: The action to be performed (block or unblock) on the JID.
        :type action: BlocklistAction
        :raises UpdateBlocklistError: If there is an error while updating the blocklist.
        :return: The updated blocklist.
        :rtype: Blocklist
        """
        jid_proto = jid.SerializeToString()
        model = neonize_proto.GetBlocklistReturnFunction.FromString(
            self.__client.UpdateBlocklist(
                self.uuid, jid_proto, len(jid_proto), action.value.encode()
            ).get_bytes()
        )
        if model.Error:
            raise UpdateBlocklistError(model.Error)
        return model.Blocklist

    def update_group_participants(
        self, jid: JID, participants_changes: List[JID], action: ParticipantChange
    ) -> RepeatedCompositeFieldContainer[GroupParticipant]:
        """
        This method is used to update the list of participants in a group.
        It takes in the group's JID, a list of participant changes, and an action to perform.

        :param jid: The JID (Jabber ID) of the group to update.
        :type jid: JID
        :param participants_changes: A list of JIDs representing the participants to be added or removed.
        :type participants_changes: List[JID]
        :param action: The action to perform (add, remove, promote or demote participants).
        :type action: ParticipantChange
        :raises UpdateGroupParticipantsError: This error is raised if there is a problem updating the group participants.
        :return: A list of the updated group participants.
        :rtype: RepeatedCompositeFieldContainer[GroupParticipant]
        """
        jid_proto = jid.SerializeToString()
        jids_proto = neonize_proto.JIDArray(
            JIDS=participants_changes
        ).SerializeToString()
        model = neonize_proto.UpdateGroupParticipantsReturnFunction.FromString(
            self.__client.UpdateGroupParticipants(
                self.uuid,
                jid_proto,
                len(jid_proto),
                jids_proto,
                len(jids_proto),
                action.value.encode(),
            ).get_bytes()
        )
        if model.Error:
            raise UpdateGroupParticipantsError(model.Error)
        return model.participants

    def upload_newsletter(self, data: bytes, media_type: MediaType) -> UploadResponse:
        """Uploads the newsletter to the server.

        :param data: The newsletter content in bytes.
        :type data: bytes
        :param media_type: The type of media being uploaded.
        :type media_type: MediaType
        :raises UploadError: If there is an error during the upload process.
        :return: The response from the server after the upload.
        :rtype: UploadResponse
        """
        model = UploadReturnFunction.FromString(
            self.__client.UploadNewsletter(
                self.uuid, data, len(data), media_type.value
            ).get_bytes()
        )
        if model.Error:
            raise UploadError(model.Error)
        return model.UploadResponse

    def create_group(
        self,
        name: str,
        participants: List[JID] = [],
        linked_parent: Optional[GroupLinkedParent] = None,
        group_parent: Optional[GroupParent] = None,
    ) -> GroupInfo:
        """Create a new group.

        :param name: The name of the new group.
        :type name: str
        :param participants: Optional. A list of participant JIDs (Jabber Identifiers) to be included in the group. Defaults to an empty list.
        :type participants: List[JID], optional
        :param linked_parent: Optional. Information about a linked parent group, if applicable. Defaults to None.
        :type linked_parent: Optional[GroupLinkedParent], optional
        :param group_parent: Optional. Information about a parent group, if applicable. Defaults to None.
        :type group_parent: Optional[GroupParent], optional
        :return: Information about the newly created group.
        :rtype: GroupInfo
        """
        group_info = ReqCreateGroup(
            name=name, Participants=participants, CreateKey=self.generate_message_id()
        )
        if linked_parent:
            group_info.GroupLinkedParent.MergeFrom(linked_parent)
        if group_parent:
            group_info.GroupParent.MergeFrom(group_parent)
        group_info_buf = group_info.SerializeToString()
        resp = self.__client.CreateGroup(self.uuid, group_info_buf, len(group_info_buf))
        model = GetGroupInfoReturnFunction.FromString(resp.get_bytes())
        if model.Error:
            raise CreateGroupError(model.Error)
        return model.GroupInfo

    def get_group_request_participants(
        self, jid: JID
    ) -> RepeatedCompositeFieldContainer[JID]:
        """Get the participants of a group request.

        :param jid: The JID of the group request.
        :type jid: JID
        :return: A list of JIDs representing the participants of the group request.
        :rtype: RepeatedCompositeFieldContainer[JID]
        """
        jidbyte = jid.SerializeToString()
        model = neonize_proto.GetGroupRequestParticipantsReturnFunction.FromString(
            self.__client.GetGroupRequestParticipants(
                self.uuid, jidbyte, len(jidbyte)
            ).get_bytes()
        )
        if model.Error:
            raise GetGroupRequestParticipantsError(model.Error)
        return model.Participants

    def get_joined_groups(self) -> RepeatedCompositeFieldContainer[GroupInfo]:
        """Get the joined groups for the current user.

        :return: A list of :class:`GroupInfo` objects representing the joined groups.
        :rtype: RepeatedCompositeFieldContainer[GroupInfo]

        :raises GetJoinedGroupsError: If there was an error retrieving the joined groups.
        """
        model = neonize_proto.GetJoinedGroupsReturnFunction.FromString(
            self.__client.GetJoinedGroups(self.uuid).get_bytes()
        )
        if model.Error:
            raise GetJoinedGroupsError(model.Error)
        return model.Group

    def create_newsletter(
        self, name: str, description: str, picture: typing.Union[str, bytes]
    ) -> NewsletterMetadata:
        """Create a newsletter with the given name, description, and picture.

        :param name: The name of the newsletter.
        :type name: str
        :param description: The description of the newsletter.
        :type description: str
        :param picture: The picture of the newsletter. It can be either a URL or bytes.
        :type picture: Union[str, bytes]
        :return: The metadata of the created newsletter.
        :rtype: NewsletterMetadata
        :raises CreateNewsletterError: If there is an error creating the newsletter.
        """
        protobuf = neonize_proto.CreateNewsletterParams(
            Name=name,
            Description=description,
            Picture=get_bytes_from_name_or_url(picture),
        ).SerializeToString()
        model = neonize_proto.CreateNewsLetterReturnFunction.FromString(
            self.__client.CreateNewsletter(
                self.uuid, protobuf, len(protobuf)
            ).get_bytes()
        )
        if model.Error:
            raise CreateNewsletterError(model.Error)
        return model.NewsletterMetadata

    def follow_newsletter(self, jid: JID):
        """Follows a newsletter with the given JID.

        :param jid: The JID of the newsletter to follow.
        :type jid: JID
        :return: None
        :rtype: None
        :raises FollowNewsletterError: If there is an error following the newsletter.
        """

        jidbyte = jid.SerializeToString()
        err = self.__client.FollowNewsletter(self.uuid, jidbyte, len(jidbyte)).decode()
        if err:
            raise FollowNewsletterError(err)

    def get_newsletter_info_with_invite(self, key: str) -> NewsletterMetadata:
        """Retrieves the newsletter information with an invite using the provided key.

        :param key: The key used to identify the newsletter.
        :type key: str
        :return: The newsletter metadata.
        :rtype: NewsletterMetadata
        :raises GetNewsletterInfoWithInviteError: If there is an error retrieving the newsletter information.
        """
        model = neonize_proto.CreateNewsLetterReturnFunction.FromString(
            self.__client.GetNewsletterInfoWithInvite(
                self.uuid, key.encode()
            ).get_bytes()
        )
        if model.Error:
            raise GetNewsletterInfoWithInviteError(model.Error)
        return model.NewsletterMetadata

    def get_newsletter_message_update(
        self, jid: JID, count: int, since: int, after: int
    ) -> RepeatedCompositeFieldContainer[NewsletterMessage]:
        """Retrieves a list of newsletter messages that have been updated since a given timestamp.

        :param jid: The JID (Jabber ID) of the user.
        :type jid: JID
        :param count: The maximum number of messages to retrieve.
        :type count: int
        :param since: The timestamp (in milliseconds) to retrieve messages from.
        :type since: int
        :param after: The timestamp (in milliseconds) to retrieve messages after.
        :type after: int

        :return: A list of updated newsletter messages.
        :rtype: RepeatedCompositeFieldContainer[NewsletterMessage]

        :raises GetNewsletterMessageUpdateError: If there was an error retrieving the newsletter messages.
        """
        jidbyte = jid.SerializeToString()
        model = neonize_proto.GetNewsletterMessageUpdateReturnFunction.FromString(
            self.__client.GetNewsletterMessageUpdate(
                self.uuid, jidbyte, len(jidbyte), count, since, after
            ).get_bytes()
        )
        if model.Error:
            raise GetNewsletterMessageUpdateError(model.Error)
        return model.NewsletterMessage

    def get_newsletter_messages(
        self, jid: JID, count: int, before: MessageServerID
    ) -> RepeatedCompositeFieldContainer[NewsletterMessage]:
        """Retrieves a list of newsletter messages for a given JID.

        :param jid: The JID (Jabber Identifier) of the user.
        :type jid: JID
        :param count: The maximum number of messages to retrieve.
        :type count: int
        :param before: The ID of the message before which to retrieve messages.
        :type before: MessageServerID
        :return: A list of newsletter messages.
        :rtype: RepeatedCompositeFieldContaine[NewsletterMessage]
        """
        jidbyte = jid.SerializeToString()
        model = neonize_proto.GetNewsletterMessageUpdateReturnFunction.FromString(
            self.__client.GetNewsletterMessages(
                self.uuid, jidbyte, len(jidbyte), count, before
            ).get_bytes()
        )
        if model.Error:
            raise GetNewsletterMessagesError(model.Error)
        return model.NewsletterMessage

    def get_privacy_settings(self) -> PrivacySettings:
        """
        This function retrieves the my privacy settings.

        :return: privacy settings
        :rtype: PrivacySettings
        """
        return neonize_proto.PrivacySettings.FromString(
            self.__client.GetPrivacySettings(self.uuid).get_bytes()
        )

    def get_profile_picture(
        self,
        jid: JID,
        extra: neonize_proto.GetProfilePictureParams = neonize_proto.GetProfilePictureParams(),
    ) -> ProfilePictureInfo:
        """
        This function is used to get the profile picture of a user.

        :param jid: The unique identifier of the user whose profile picture we want to retrieve.
        :type jid: JID
        :param extra: Additional parameters, defaults to neonize_proto.GetProfilePictureParams()
        :type extra: neonize_proto.GetProfilePictureParams, optional
        :raises GetProfilePictureError: If there is an error while trying to get the profile picture.
        :return: The information about the profile picture.
        :rtype: ProfilePictureInfo
        """
        jid_bytes = jid.SerializeToString()
        extra_bytes = extra.SerializeToString()
        model = neonize_proto.GetProfilePictureReturnFunction.FromString(
            self.__client.GetProfilePicture(
                self.uuid,
                jid_bytes,
                len(jid_bytes),
                extra_bytes,
                len(extra_bytes),
            ).get_bytes()
        )
        if model.Error:
            raise GetProfilePictureError(model)
        return model.Picture

    def get_status_privacy(
        self,
    ) -> RepeatedCompositeFieldContainer[StatusPrivacy]:
        """Returns the status privacy settings of the user.

        :raises GetStatusPrivacyError: If there is an error in getting the status privacy.
        :return: The status privacy settings of the user.
        :rtype: RepeatedCompositeFieldContainer[StatusPrivacy]
        """
        model = neonize_proto.GetStatusPrivacyReturnFunction.FromString(
            self.__client.GetStatusPrivacy(self.uuid).get_bytes()
        )
        if model.Error:
            raise GetStatusPrivacyError(model.Error)
        return model.StatusPrivacy

    def get_sub_groups(
        self, community: JID
    ) -> RepeatedCompositeFieldContainer[GroupLinkTarget]:
        """
        Get the subgroups of a given community.

        :param community: The community for which to get the subgroups.
        :type community: JID
        :raises GetSubGroupsError: If there is an error while getting the subgroups.
        :return: The subgroups of the given community.
        :rtype: RepeatedCompositeFieldContainer[GroupLinkTarget]
        """
        jid = community.SerializeToString()
        model = neonize_proto.GetSubGroupsReturnFunction.FromString(
            self.__client.GetSubGroups(self.uuid, jid, len(jid)).get_bytes()
        )
        if model.Error:
            raise GetSubGroupsError(model.Error)
        return model.GroupLinkTarget

    def get_subscribed_newletters(
        self,
    ) -> RepeatedCompositeFieldContainer[NewsletterMetadata]:
        """
        This function retrieves the newsletters the user has subscribed to.

        :raises GetSubscribedNewslettersError: If there is an error while fetching the subscribed newsletters
        :return: A container with the metadata of each subscribed newsletter
        :rtype: RepeatedCompositeFieldContainer[NewsletterMetadata]
        """
        model = neonize_proto.GetSubscribedNewslettersReturnFunction.FromString(
            self.__client.GetSubscribedNewsletters(self.uuid).get_bytes()
        )
        if model.Error:
            raise GetSubscribedNewslettersError(model.Error)
        return model.Newsletter

    def get_user_devices(self, jids: List[JID]) -> RepeatedCompositeFieldContainer[JID]:
        """_summary_

        :param jids: _description_
        :type jids: List[JID]
        :raises GetUserDevicesError: _description_
        :return: _description_
        :rtype: RepeatedCompositeFieldContainer[JID]
        """
        jids_ = neonize_proto.JIDArray(JIDS=jids).SerializeToString()
        model = neonize_proto.GetUserDevicesreturnFunction.FromString(
            self.__client.GetIserDevices(self.uuid, jids_, len(jids_)).get_bytes()
        )
        if model.Error:
            raise GetUserDevicesError(model.Error)
        return model.JID

    def get_blocklist(self) -> Blocklist:
        """Retrieves the blocklist from the client.

        :return: Blocklist: The retrieved blocklist.
        :raises GetBlocklistError: If there was an error retrieving the blocklist.
        """
        model = neonize_proto.GetBlocklistReturnFunction.FromString(
            self.__client.GetBlocklist(self.uuid).get_bytes()
        )
        if model.Error:
            raise GetBlocklistError(model.Error)
        return model.Blocklist

    def get_me(self) -> Device:
        """
        This method is used to get the device information associated with a given UUID.

        :return: It returns a Device object created from the byte string response from the client's GetMe method.
        :rtype: Device
        """
        return Device.FromString(self.__client.GetMe(self.uuid).get_bytes())

    def get_contact_qr_link(self, revoke: bool = False) -> str:
        """
        This function returns a QR link for a specific contact. If the 'revoke' parameter is set to True,
        it revokes the existing QR link and generates a new one.

        :param revoke: If set to True, revokes the existing QR link and generates a new one. Defaults to False.
        :type revoke: bool, optional
        :raises GetContactQrLinkError: If there is an error in getting the QR link.
        :return: The QR link for the contact.
        :rtype: str
        """
        model = neonize_proto.GetContactQRLinkReturnFunction.FromString(
            self.__client.GetContactQRLink(self.uuid, revoke).get_bytes()
        )
        if model.Error:
            raise GetContactQrLinkError(model.Error)
        return model.Link

    def get_linked_group_participants(
        self, community: JID
    ) -> RepeatedCompositeFieldContainer[JID]:
        """Fetches the participants of a linked group in a community.

        :param community: The community in which the linked group belongs.
        :type community: JID
        :raises GetLinkedGroupParticipantsError: If there is an error while fetching the participants.
        :return: A list of participants in the linked group.
        :rtype: RepeatedCompositeFieldContainer[JID]
        """
        jidbyte = community.SerializeToString()
        model = neonize_proto.GetGroupRequestParticipantsReturnFunction.FromString(
            self.__client.GetLinkedGroupsParticipants(
                self.uuid, jidbyte, len(jidbyte)
            ).get_bytes()
        )
        if model.Error:
            raise GetLinkedGroupParticipantsError(model.Error)
        return model.Participants

    def get_newsletter_info(self, jid: JID) -> neonize_proto.NewsletterMetadata:
        """
        Fetches the metadata of a specific newsletter using its JID.

        :param jid: The unique identifier of the newsletter
        :type jid: JID
        :raises GetNewsletterInfoError: If there is an error while fetching the newsletter information
        :return: The metadata of the requested newsletter
        :rtype: neonize_proto.NewsletterMetadata
        """
        jidbyte = jid.SerializeToString()
        model = neonize_proto.CreateNewsLetterReturnFunction.FromString(
            self.__client.GetNewsletterInfo(
                self.uuid, jidbyte, len(jidbyte)
            ).get_bytes()
        )
        if model.Error:
            raise GetNewsletterInfoError(model.Error)
        return model.NewsletterMetadata

    def PairPhone(
        self,
        phone: str,
        show_push_notification: bool,
        client_name: ClientName = ClientName.LINUX,
        client_type: Optional[ClientType] = None,
    ):
        """
        Pair a phone with the client. This function will try to connect to the WhatsApp servers and pair the phone.
        If successful, it will show a push notification on the paired phone.

        :param phone: The phone number to be paired.
        :type phone: str
        :param show_push_notification: If true, a push notification will be shown on the paired phone.
        :type show_push_notification: bool
        :param client_name: The name of the client, defaults to LINUX.
        :type client_name: ClientName, optional
        :param client_type: The type of the client, defaults to None. If None, it will be set to FIREFOX or determined by the device properties.
        :type client_type: Optional[ClientType], optional
        """

        if client_type is None:
            if self.device_props is None:
                client_type = ClientType.FIREFOX
            else:
                try:
                    client_type = ClientType(self.device_props.platformType)
                except ValueError:
                    client_type = ClientType.FIREFOX

        pl = neonize_proto.PairPhoneParams(
            phone=phone,
            clientDisplayName="%s (%s)" % (client_type.name, client_name.name),
            clientType=client_type.value,
            showPushNotification=show_push_notification,
        )
        payload = pl.SerializeToString()
        d = bytearray(list(self.event.list_func))

        log.debug("trying connect to whatsapp servers")

        deviceprops = (
            DeviceProps(os="Neonize", platformType=DeviceProps.SAFARI)
            if self.device_props is None
            else self.device_props
        ).SerializeToString()

        self.__client.Neonize(
            self.name.encode(),
            self.uuid,
            LogLevel.from_logging(log.level).level,
            func_string(self.__onQr),
            func_string(self.__onLoginStatus),
            func_callback_bytes(self.event.execute),
            (ctypes.c_char * self.event.list_func.__len__()).from_buffer(d),
            len(d),
            func(self.event.blocking_func),
            deviceprops,
            len(deviceprops),
            payload,
            len(payload),
        )

    def get_message_for_retry(
        self, requester: JID, to: JID, message_id: str
    ) -> typing.Union[None, Message]:
        """
        This function retrieves a specific message for retrying transmission.
        It communicates with a client to get the message using provided requester, recipient, and message ID.

        :param requester: The JID of the entity requesting the message.
        :type requester: JID
        :param to: The JID of the intended recipient of the message.
        :type to: JID
        :param message_id: The unique identifier of the message to be retrieved.
        :type message_id: str
        :return: The message to be retried if found, None otherwise.
        :rtype: Union[None, Message]
        """
        requester_buf = requester.SerializeToString()
        to_buf = to.SerializeToString()
        model = neonize_proto.GetMessageForRetryReturnFunction.FromString(
            self.__client.GetMessageForRetry(
                self.uuid,
                requester_buf,
                len(requester_buf),
                to_buf,
                len(to_buf),
                message_id.encode(),
            ).get_bytes()
        )
        if not model.isEmpty:
            return model.Message

    def connect(self):
        """Establishes a connection to the WhatsApp servers."""
        # Convert the list of functions to a bytearray
        d = bytearray(list(self.event.list_func))
        log.debug("🔒 Attempting to connect to the WhatsApp servers.")
        # Set device properties
        deviceprops = (
            DeviceProps(os="Neonize", platformType=DeviceProps.SAFARI)
            if self.device_props is None
            else self.device_props
        ).SerializeToString()

        # Initiate connection to the server
        self.__client.Neonize(
            self.name.encode(),
            self.uuid,
            LogLevel.from_logging(log.level).level,
            func_string(self.__onQr),
            func_string(self.__onLoginStatus),
            func_callback_bytes(self.event.execute),
            (ctypes.c_char * len(self.event.list_func)).from_buffer(d),
            len(d),
            func(self.event.blocking_func),
            deviceprops,
            len(deviceprops),
            b"",
            0,
        )

    def disconnect(self) -> None:
        """
        Disconnect the client
        """
        self.__client.Disconnect(self.uuid)
