package utils

import (
	"C"

	defproto "github.com/krypton-byte/neonize/defproto"
	"github.com/krypton-byte/neonize/neonize"
	"go.mau.fi/whatsmeow"
	waProto "go.mau.fi/whatsmeow/binary/proto"
	"go.mau.fi/whatsmeow/types"
	"google.golang.org/protobuf/proto"
)
import "go.mau.fi/whatsmeow/types/events"

// Function
func EncodeUploadResponse(response whatsmeow.UploadResponse) *neonize.UploadResponse {
	return &neonize.UploadResponse{
		Url:           &response.URL,
		DirectPath:    &response.DirectPath,
		Handle:        &response.Handle,
		MediaKey:      response.MediaKey,
		FileEncSHA256: response.FileEncSHA256,
		FileSHA256:    response.FileSHA256,
		FileLength:    proto.Uint32(uint32(response.FileLength)),
	}
}

// types.go
func EncodeJidProto(data types.JID) *neonize.JID {
	isempty := data.IsEmpty()
	return &neonize.JID{
		User:       &data.User,
		RawAgent:   proto.Uint32(uint32(data.RawAgent)),
		Device:     proto.Uint32(uint32(data.Device)),
		Integrator: proto.Uint32(uint32(data.Integrator)),
		Server:     &data.Server,
		IsEmpty:    &isempty,
	}
}
func EncodeGroupName(groupName types.GroupName) *neonize.GroupName {
	return &neonize.GroupName{
		Name:      &groupName.Name,
		NameSetAt: proto.Int64(groupName.NameSetAt.Unix()),
		NameSetBy: EncodeJidProto(groupName.NameSetBy),
	}
}
func EncodeGroupTopic(topic types.GroupTopic) *neonize.GroupTopic {
	return &neonize.GroupTopic{
		Topic:        &topic.Topic,
		TopicID:      &topic.TopicID,
		TopicSetAt:   proto.Int64(topic.TopicSetAt.Unix()),
		TopicSetBy:   EncodeJidProto(topic.TopicSetBy),
		TopicDeleted: &topic.TopicDeleted,
	}
}
func EncodeGroupLocked(locked types.GroupLocked) *neonize.GroupLocked {
	return &neonize.GroupLocked{
		IsLocked: &locked.IsLocked,
	}
}
func EncodeGroupAnnounce(announce types.GroupAnnounce) *neonize.GroupAnnounce {
	return &neonize.GroupAnnounce{
		IsAnnounce:        &announce.IsAnnounce,
		AnnounceVersionID: &announce.AnnounceVersionID,
	}
}
func EncodeGroupEphemeral(ephemeral types.GroupEphemeral) *neonize.GroupEphemeral {
	return &neonize.GroupEphemeral{
		IsEphemeral:       &ephemeral.IsEphemeral,
		DisappearingTimer: &ephemeral.DisappearingTimer,
	}
}
func EncodeGroupIncognito(incognito types.GroupIncognito) *neonize.GroupIncognito {
	return &neonize.GroupIncognito{
		IsIncognito: &incognito.IsIncognito,
	}
}
func EncodeGroupParent(parent types.GroupParent) *neonize.GroupParent {
	return &neonize.GroupParent{
		IsParent:                      &parent.IsParent,
		DefaultMembershipApprovalMode: &parent.DefaultMembershipApprovalMode,
	}
}
func EncodeGroupLinkedParent(linkedParent types.GroupLinkedParent) *neonize.GroupLinkedParent {
	return &neonize.GroupLinkedParent{
		LinkedParentJID: EncodeJidProto(linkedParent.LinkedParentJID),
	}
}
func EncodeGroupIsDefaultSub(isDefaultSub types.GroupIsDefaultSub) *neonize.GroupIsDefaultSub {
	return &neonize.GroupIsDefaultSub{
		IsDefaultSubGroup: &isDefaultSub.IsDefaultSubGroup,
	}
}
func EncodeGroupParticipantAddRequest(addRequest types.GroupParticipantAddRequest) *neonize.GroupParticipantAddRequest {
	return &neonize.GroupParticipantAddRequest{
		Code:       &addRequest.Code,
		Expiration: proto.Float32(float32(addRequest.Expiration.Unix())),
	}
}
func EncodeGroupParticipant(participant types.GroupParticipant) *neonize.GroupParticipant {
	participant_group := neonize.GroupParticipant{
		LID:          EncodeJidProto(participant.LID),
		JID:          EncodeJidProto(participant.JID),
		IsAdmin:      &participant.IsAdmin,
		IsSuperAdmin: &participant.IsSuperAdmin,
		DisplayName:  &participant.DisplayName,
		Error:        proto.Int32(int32(participant.Error)),
	}
	if participant.AddRequest != nil {
		participant_group.AddRequest = EncodeGroupParticipantAddRequest(*participant.AddRequest)
	}
	return &participant_group
}

// send.go
func EncodeGroupInfo(info *types.GroupInfo) *neonize.GroupInfo {
	participants := []*neonize.GroupParticipant{}
	for _, participant := range info.Participants {
		participants = append(participants, EncodeGroupParticipant(participant))
	}
	return &neonize.GroupInfo{
		JID:                  EncodeJidProto(info.JID),
		OwnerJID:             EncodeJidProto(info.OwnerJID),
		GroupName:            EncodeGroupName(info.GroupName),
		GroupTopic:           EncodeGroupTopic(info.GroupTopic),
		GroupLocked:          EncodeGroupLocked(info.GroupLocked),
		GroupAnnounce:        EncodeGroupAnnounce(info.GroupAnnounce),
		GroupEphemeral:       EncodeGroupEphemeral(info.GroupEphemeral),
		GroupIncognito:       EncodeGroupIncognito(info.GroupIncognito),
		GroupParent:          EncodeGroupParent(info.GroupParent),
		GroupLinkedParent:    EncodeGroupLinkedParent(info.GroupLinkedParent),
		GroupIsDefaultSub:    EncodeGroupIsDefaultSub(info.GroupIsDefaultSub),
		GroupCreated:         proto.Float32(float32(info.GroupCreated.Unix())),
		ParticipantVersionID: &info.ParticipantVersionID,
		Participants:         participants,
	}
}

func EncodeMessageDebugTimings(debugTimings whatsmeow.MessageDebugTimings) *neonize.MessageDebugTimings {
	return &neonize.MessageDebugTimings{
		Queue:           proto.Int64(debugTimings.Queue.Nanoseconds()),
		Marshal_:        proto.Int64(debugTimings.Marshal.Nanoseconds()),
		GetParticipants: proto.Int64(debugTimings.GetParticipants.Nanoseconds()),
		GetDevices:      proto.Int64(debugTimings.GetParticipants.Nanoseconds()),
		GroupEncrypt:    proto.Int64(debugTimings.Queue.Nanoseconds()),
		PeerEncrypt:     proto.Int64(debugTimings.PeerEncrypt.Nanoseconds()),
		Send:            proto.Int64(debugTimings.Send.Nanoseconds()),
		Resp:            proto.Int64(debugTimings.Queue.Nanoseconds()),
		Retry:           proto.Int64(debugTimings.Retry.Nanoseconds()),
	}
}
func EncodeSendResponse(sendResponse whatsmeow.SendResponse) *neonize.SendResponse {
	return &neonize.SendResponse{
		Timestamp:    proto.Int64(sendResponse.Timestamp.Unix()),
		ID:           proto.String(sendResponse.ID),
		ServerID:     proto.Int64(int64(sendResponse.ServerID)),
		DebugTimings: EncodeMessageDebugTimings(sendResponse.DebugTimings),
	}
}
func EncodeVerifiedNameCertificate(verifiedNameCertificate *waProto.VerifiedNameCertificate) *defproto.VerifiedNameCertificate {
	return &defproto.VerifiedNameCertificate{
		Details:         verifiedNameCertificate.Details,
		Signature:       verifiedNameCertificate.Signature,
		ServerSignature: verifiedNameCertificate.ServerSignature,
	}
}
func EncodeLocalizedName(localizedname *waProto.LocalizedName) *defproto.LocalizedName {
	return &defproto.LocalizedName{
		Lg:           localizedname.Lg,
		Lc:           localizedname.Lc,
		VerifiedName: localizedname.VerifiedName,
	}
}
func EncodeVerifiedNameCertificate_Details(details *waProto.VerifiedNameCertificate_Details) *defproto.VerifiedNameCertificate_Details {
	localizedName := []*defproto.LocalizedName{}
	for _, localized := range details.LocalizedNames {
		localizedName = append(localizedName, EncodeLocalizedName(localized))
	}
	return &defproto.VerifiedNameCertificate_Details{
		Serial:         details.Serial,
		Issuer:         details.Issuer,
		VerifiedName:   details.VerifiedName,
		LocalizedNames: localizedName,
		IssueTime:      details.IssueTime,
	}
}
func EncodeVerifiedName(verifiedName *types.VerifiedName) *neonize.VerifiedName {
	models := &neonize.VerifiedName{}
	if verifiedName.Details != nil {
		models.Details = EncodeVerifiedNameCertificate_Details(verifiedName.Details)
	}
	if verifiedName.Certificate != nil {
		models.Certificate = EncodeVerifiedNameCertificate(verifiedName.Certificate)
	}
	return models
}
func EncodeIsOnWhatsApp(isOnWhatsApp types.IsOnWhatsAppResponse) *neonize.IsOnWhatsAppResponse {
	model := &neonize.IsOnWhatsAppResponse{
		Query: &isOnWhatsApp.Query,
		JID:   EncodeJidProto(isOnWhatsApp.JID),
		IsIn:  &isOnWhatsApp.IsIn,
	}
	if isOnWhatsApp.VerifiedName != nil {
		model.VerifiedName = EncodeVerifiedName(isOnWhatsApp.VerifiedName)
	}
	return model
}

func EncodeUserInfo(userInfo types.UserInfo) *neonize.UserInfo {
	devices := []*neonize.JID{}
	for _, jid := range userInfo.Devices {
		devices = append(devices, EncodeJidProto(jid))
	}
	models := &neonize.UserInfo{
		Status:    &userInfo.Status,
		PictureID: &userInfo.PictureID,
		Devices:   devices,
	}
	if userInfo.VerifiedName != nil {
		models.VerifiedName = EncodeVerifiedName(userInfo.VerifiedName)
	}
	return models
}
func EncodeMessageSource(messageSource types.MessageSource) *neonize.MessageSource {
	return &neonize.MessageSource{
		Chat:               EncodeJidProto(messageSource.Chat),
		Sender:             EncodeJidProto(messageSource.Sender),
		IsFromMe:           &messageSource.IsFromMe,
		IsGroup:            &messageSource.IsGroup,
		BroadcastListOwner: EncodeJidProto(messageSource.BroadcastListOwner),
	}
}
func EncodeDeviceSentMeta(deviceSentMeta *types.DeviceSentMeta) *neonize.DeviceSentMeta {
	return &neonize.DeviceSentMeta{
		DestinationJID: &deviceSentMeta.DestinationJID,
		Phash:          &deviceSentMeta.Phash,
	}
}
func EncodeMessageInfo(messageInfo types.MessageInfo) *neonize.MessageInfo {
	model := &neonize.MessageInfo{
		MessageSource: EncodeMessageSource(messageInfo.MessageSource),
		ID:            &messageInfo.ID,
		ServerID:      proto.Int64(messageInfo.Timestamp.Unix()),
		Type:          &messageInfo.Type,
		Pushname:      &messageInfo.PushName,
		Timestamp:     proto.Int64(messageInfo.Timestamp.Unix()),
		Category:      &messageInfo.Category,
		Multicast:     &messageInfo.Multicast,
		MediaType:     &messageInfo.MediaType,
		Edit:          (*string)(&messageInfo.Edit),
	}
	if messageInfo.VerifiedName != nil {
		model.VerifiedName = EncodeVerifiedName(messageInfo.VerifiedName)
	}
	if messageInfo.DeviceSentMeta != nil {
		model.DeviceSentMeta = EncodeDeviceSentMeta(messageInfo.DeviceSentMeta)
	}
	return model
}

func EncodeMessage(message *waProto.Message) *defproto.Message {
	var neonizeMessage defproto.Message
	encoded, err := proto.Marshal(message)
	if err != nil {
		panic(err)
	}
	err_decode := proto.Unmarshal(encoded, &neonizeMessage)
	if err_decode != nil {
		panic(err_decode)
	}
	return &neonizeMessage
}
func EncodeNewsLetterMessageMeta(newsLetter *events.NewsletterMessageMeta) *neonize.NewsLetterMessageMeta {
	return &neonize.NewsLetterMessageMeta{
		EditTS:     proto.Int64(int64(newsLetter.EditTS.Unix())),
		OriginalTS: proto.Int64(int64(newsLetter.OriginalTS.Unix())),
	}
}
func EncodeWebMessageInfo(sourceWebMsg *waProto.WebMessageInfo) *defproto.WebMessageInfo {
	var sourcewebmsg defproto.WebMessageInfo
	sourceWebBuf, err := proto.Marshal(sourceWebMsg)
	if err != nil {
		panic(err)
	}
	err_decoded := proto.Unmarshal(sourceWebBuf, &sourcewebmsg)
	if err_decoded != nil {
		panic(err)
	}
	return &sourcewebmsg

}

func EncodeEventTypesMessage(message *events.Message) *neonize.Message {
	model := &neonize.Message{
		Info:                 EncodeMessageInfo(message.Info),
		IsEphemeral:          &message.IsEphemeral,
		IsViewOnce:           &message.IsViewOnce,
		IsViewOnceV2:         &message.IsViewOnceV2,
		IsEdit:               &message.IsEdit,
		UnavailableRequestID: &message.UnavailableRequestID,
		RetryCount:           proto.Int64(int64(message.RetryCount)),
	}
	if message.NewsletterMeta != nil {
		model.NewsLetterMeta = EncodeNewsLetterMessageMeta(message.NewsletterMeta)
	}
	if message.SourceWebMsg != nil {
		model.SourceWebMsg = EncodeWebMessageInfo(message.SourceWebMsg)
	}
	if message.Message != nil {
		model.Message = EncodeMessage(message.Message)
	}
	return model
}
