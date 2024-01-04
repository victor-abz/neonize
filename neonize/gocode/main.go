package main

/*

   #include <stdlib.h>
   #include <stdbool.h>
   #include "header/cstruct.h"

   typedef void (*ptr_to_python_function_string) (char*);

   static inline void call_c_func_string(ptr_to_python_function_string ptr, char* xStr) {
    (ptr)(xStr);
    }
	typedef void (*ptr_to_python_function_bytes)(const char*, size_t);

	static inline void call_c_func_bytes(ptr_to_python_function_bytes ptr, const char* data, size_t size) {
		(ptr)(data, size);
	}
*/
import "C"
import (
	"context"
	"fmt"
	"os"
	"os/signal"
	"strings"
	"syscall"
	"unsafe"

	"github.com/krypton-byte/neonize/neonize"
	"github.com/krypton-byte/neonize/utils"
	_ "github.com/mattn/go-sqlite3"
	"go.mau.fi/whatsmeow"
	"go.mau.fi/whatsmeow/store/sqlstore"
	"go.mau.fi/whatsmeow/types"
	"go.mau.fi/whatsmeow/types/events"

	waProto "go.mau.fi/whatsmeow/binary/proto"
	waLog "go.mau.fi/whatsmeow/util/log"
	"google.golang.org/protobuf/proto"
)

var clients = make(map[string]*whatsmeow.Client)

func getByteByAddr(addr *C.uchar, size C.int) []byte {
	var result []byte
	for i := 0; i < int(size); i++ {
		value := *(*C.uchar)(unsafe.Pointer(uintptr(unsafe.Pointer(addr)) + uintptr(i)))
		// 	fmt.Println(value)
		result = append(result, byte(value))
	}
	return result
}

func ReturnBytes(data []byte) C.struct_BytesReturn {
	size := C.size_t(len(data))
	ptr := (*C.char)(C.CBytes(data))
	// defer C.free(unsafe.Pointer(&ptr))
	return C.struct_BytesReturn{ptr, size}
}

//export Upload
func Upload(id *C.char, mediabuff *C.uchar, mediaSize C.int, mediatype C.int) C.struct_BytesReturn {
	client := clients[C.GoString(id)]
	data := getByteByAddr(mediabuff, mediaSize)
	response, err_upload := client.Upload(context.Background(), data, utils.MediaType[int(mediatype)])
	return_ := neonize.UploadReturnFunction{}
	if err_upload != nil {
		return_.Error = proto.String(err_upload.Error())
	}
	return_.UploadResponse = utils.EncodeUploadResponse(response)
	return_buf, err := proto.Marshal(&return_)
	if err != nil {
		panic(err)
	}
	return ReturnBytes(return_buf)
}

//export GenerateMessageID
func GenerateMessageID(id *C.char) *C.char {
	return C.CString(clients[C.GoString(id)].GenerateMessageID())
}

//export AcceptTOSNotice
func AcceptTOSNotice(id *C.char, noticeID *C.char, stage *C.char) *C.char {
	err := clients[C.GoString(id)].AcceptTOSNotice(C.GoString(noticeID), C.GoString(stage))
	if err != nil {
		return C.CString(err.Error())
	}
	return C.CString("")
}

//export SendMessage
func SendMessage(id *C.char, JIDByte *C.uchar, JIDSize C.int, messageByte *C.uchar, messageSize C.int) C.struct_BytesReturn {
	client := clients[C.GoString(id)]
	jid := getByteByAddr(JIDByte, JIDSize)
	var neonize_jid neonize.JID
	err := proto.Unmarshal(jid, &neonize_jid)
	if err != nil {
		panic(err)
	}
	message_bytes := getByteByAddr(messageByte, messageSize)
	var message waProto.Message
	err_message := proto.Unmarshal(message_bytes, &message)
	if err_message != nil {
		panic(err)
	}
	sendresponse, err := client.SendMessage(context.Background(), utils.DecodeJidProto(&neonize_jid), &message)
	return_ := neonize.SendMessageReturnFunction{}
	if err != nil {
		return_.Error = proto.String(err.Error())
	}
	return_.SendResponse = utils.EncodeSendResponse(sendresponse)
	return_buf, err := proto.Marshal(&return_)
	if err != nil {
		panic(err)
	}
	return ReturnBytes(return_buf)
}

//export Neonize
func Neonize(db *C.char, id *C.char, qrCb C.ptr_to_python_function_string, logStatus C.ptr_to_python_function_string, messageCb C.ptr_to_python_function_bytes) {
	dbLog := waLog.Stdout("Database", "DEBUG", true)
	// Make sure you add appropriate DB connector imports, e.g. github.com/mattn/go-sqlite3 for SQLite
	container, err := sqlstore.New("sqlite3", fmt.Sprintf("file:%s?_foreign_keys=on", C.GoString(db)), dbLog)
	if err != nil {
		panic(err)
	}
	// If you want multiple sessions, remember their JIDs and use .GetDevice(jid) or .GetAllDevices() instead.
	deviceStore, err := container.GetFirstDevice()
	if err != nil {
		panic(err)
	}
	clientLog := waLog.Stdout("Client", "DEBUG", true)
	client := whatsmeow.NewClient(deviceStore, clientLog)
	clients[C.GoString(id)] = client
	eventHandler := func(evt interface{}) {
		switch v := evt.(type) {
		case *events.Message:
			// fmt.Println("Received a message!", v.Message.GetConversation())
			if err != nil {
				panic(err)
			}
			// fname := "z.buf"
			// file, err := os.Create(fname)
			// if err != nil {
			// 	panic(err)
			// }
			// file.Write(data)
			// defer file.Close()
			// fmt.Println("dataproto: ", data)
			// if err != nil {
			// 	panic(err)
			// }
			messageSource := utils.EncodeEventTypesMessage(v)
			messageSourceBytes, err := proto.Marshal(messageSource)
			if err != nil {
				panic(err)
			}
			messageSourceCDATA := (*C.char)(unsafe.Pointer(&messageSourceBytes[0]))
			messageSourceCSize := C.size_t(len(messageSourceBytes))
			C.call_c_func_bytes(messageCb, messageSourceCDATA, messageSourceCSize)
			// C.free(unsafe.Pointer(CData))

		}
	}
	client.AddEventHandler(eventHandler)
	qrFuncCb := func(data string) {
		cstr := C.CString(data)
		defer C.free(unsafe.Pointer(cstr))
		C.call_c_func_string(qrCb, cstr)
	}
	logStatusCb := func(eventName string) {
		cstr := C.CString(eventName)
		defer C.free(unsafe.Pointer(cstr))
		C.call_c_func_string(logStatus, cstr)
	}
	if client.Store.ID == nil {
		// No ID stored, new login
		qrChan, _ := client.GetQRChannel(context.Background())
		err = client.Connect()
		if err != nil {
			panic(err)
		}
		for evt := range qrChan {
			if evt.Event == "code" {
				// Render the QR code here
				// e.g. qrterminal.GenerateHalfBlock(evt.Code, qrterminal.L, os.Stdout)
				// or just manually `echo 2@... | qrencode -t ansiutf8` in a terminal
				qrFuncCb(evt.Code)
				// fmt.Println(cstr)
				// C.free(unsafe.Pointer(cstr))
			} else {
				fmt.Println("Login event:", evt.Event)
				logStatusCb(evt.Event)
			}
		}
	} else {
		// Already logged in, just connect
		err = client.Connect()
		if err != nil {
			panic(err)
		}
	}

	// Listen to Ctrl+C (you can also do something else that prevents the program from exiting)
	c := make(chan os.Signal)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	<-c

	client.Disconnect()
}

//export Download
func Download(id *C.char, messageProto *C.uchar, size C.int) C.struct_BytesReturn {
	var message waProto.Message
	err := proto.Unmarshal(getByteByAddr(messageProto, size), &message)
	if err != nil {
		panic(err)
	}
	data_buff, err := clients[C.GoString(id)].DownloadAny(&message)
	return_ := neonize.DownloadReturnFunction{}
	if err != nil {
		return_.Error = proto.String(err.Error())
	}
	if data_buff != nil {
		return_.Binary = data_buff
	}
	return ReturnBytes(data_buff)

}

//export IsOnWhatsApp
func IsOnWhatsApp(id *C.char, numbers *C.char) C.struct_BytesReturn {
	onWhatsApp := []*neonize.IsOnWhatsAppResponse{}
	return_ := neonize.IsOnWhatsAppReturnFunction{}
	response, err := clients[C.GoString(id)].IsOnWhatsApp(strings.Split(C.GoString(numbers), " "))
	for _, participant := range response {
		onWhatsApp = append(onWhatsApp, utils.EncodeIsOnWhatsApp(participant))
	}
	if err != nil {
		return_.Error = proto.String(err.Error())
	}
	return_.IsOnWhatsAppResponse = onWhatsApp
	return_buf, err := proto.Marshal(&return_)
	if err != nil {
		panic(err)
	}
	return ReturnBytes(return_buf)
}

//export IsConnected
func IsConnected(id *C.char) C.bool {
	check := clients[C.GoString(id)].IsConnected()
	return C.bool(check)
}

//export IsLoggedIn
func IsLoggedIn(id *C.char) C.bool {
	check := clients[C.GoString(id)].IsConnected()
	return C.bool(check)
}

//export GetUserInfo
func GetUserInfo(id *C.char, JIDSByte *C.uchar, JIDSSize C.int) C.struct_BytesReturn {
	var NeoJIDS neonize.JIDArray
	JIDSBuf := getByteByAddr(JIDSByte, JIDSSize)
	err := proto.Unmarshal(JIDSBuf, &NeoJIDS)
	if err != nil {
		panic(err)
	}
	JIDS := []types.JID{}
	for _, jid := range NeoJIDS.JIDS {
		JIDS = append(JIDS, utils.DecodeJidProto(jid))
	}
	user_info, err := clients[C.GoString(id)].GetUserInfo(JIDS)
	return_ := neonize.GetUserInfoReturnFunction{}
	if err != nil {
		return_.Error = proto.String(err.Error())
	}
	usersinfo := []*neonize.GetUserInfoSingleReturnFunction{}
	for jid, info := range user_info {
		singlereturn := &neonize.GetUserInfoSingleReturnFunction{
			JID:      utils.EncodeJidProto(jid),
			UserInfo: utils.EncodeUserInfo(info),
		}

		usersinfo = append(usersinfo, singlereturn)
	}
	return_.UsersInfo = usersinfo
	return_buf, marshal_err := proto.Marshal(&return_)
	if marshal_err != nil {
		panic(marshal_err)
	}
	return ReturnBytes(return_buf)
}

// /GROUP
//
//export GetGroupInfo
func GetGroupInfo(id *C.char, JIDByte *C.uchar, JIDSize C.int) C.struct_BytesReturn {
	var neoJIDProto neonize.JID
	jidbyte := getByteByAddr(JIDByte, JIDSize)
	err := proto.Unmarshal(jidbyte, &neoJIDProto)
	if err != nil {
		panic(err)
	}
	decodeJid := utils.DecodeJidProto(&neoJIDProto)
	info, err_info := clients[C.GoString(id)].GetGroupInfo(decodeJid)
	groupinfo := neonize.GetGroupInfoReturnFunction{}
	if err_info != nil {
		groupinfo.Error = proto.String(err_info.Error())
	}
	if info != nil {
		groupinfo.GroupInfo = utils.EncodeGroupInfo(info)
	}
	databuf, err_ := proto.Marshal(&groupinfo)
	if err_ != nil {
		panic(err_)
	}
	return ReturnBytes(databuf)
}

//export SetGroupName
func SetGroupName(id *C.char, JIDByte *C.uchar, JIDSize C.int, name *C.char) *C.char {
	jidbyte := getByteByAddr(JIDByte, JIDSize)
	var neoJIDProto neonize.JID
	err := proto.Unmarshal(jidbyte, &neoJIDProto)
	if err != nil {
		panic(err)
	}
	status_err := clients[C.GoString(id)].SetGroupName(utils.DecodeJidProto(&neoJIDProto), C.GoString(name))
	if status_err != nil {
		return C.CString(status_err.Error())

	}
	return C.CString("")

}

//export SetGroupPhoto
func SetGroupPhoto(id *C.char, JIDByte *C.uchar, JIDSize C.int, Photo *C.uchar, PhotoSize C.int) C.struct_BytesReturn {
	var neoJIDProto neonize.JID
	JIDbyte := getByteByAddr(JIDByte, JIDSize)
	err := proto.Unmarshal(JIDbyte, &neoJIDProto)
	if err != nil {
		panic(err)
	}
	photo_buf := getByteByAddr(Photo, PhotoSize)
	response, err_status := clients[C.GoString(id)].SetGroupPhoto(utils.DecodeJidProto(&neoJIDProto), photo_buf)
	return_ := neonize.SetGroupPhotoReturnFunction{
		PictureID: &response,
	}
	if err_status != nil {
		return_.Error = proto.String(err_status.Error())
	}
	return_buf, err_marshal := proto.Marshal(&return_)
	if err != nil {
		panic(err_marshal)
	}
	return ReturnBytes(return_buf)
}

//export LeaveGroup
func LeaveGroup(id *C.char, JIDByte *C.uchar, JIDSize C.int) *C.char {
	var neoJIDProto neonize.JID
	JIDbyte := getByteByAddr(JIDByte, JIDSize)
	err := proto.Unmarshal(JIDbyte, &neoJIDProto)
	if err != nil {
		panic(err)
	}
	err_status := clients[C.GoString(id)].LeaveGroup(utils.DecodeJidProto(&neoJIDProto))
	if err_status != nil {
		return C.CString(err_status.Error())
	}
	return C.CString("")
}

//export GetGroupInviteLink
func GetGroupInviteLink(id *C.char, JIDByte *C.uchar, JIDSize C.int, revoke C.bool) C.struct_BytesReturn {
	var neoJIDProto neonize.JID
	JIDbyte := getByteByAddr(JIDByte, JIDSize)
	err := proto.Unmarshal(JIDbyte, &neoJIDProto)
	if err != nil {
		panic(err)
	}
	url, err := clients[C.GoString(id)].GetGroupInviteLink(utils.DecodeJidProto(&neoJIDProto), bool(revoke))
	return_ := neonize.GetGroupInviteLinkReturnFunction{
		InviteLink: &url,
	}
	if err != nil {
		return_.Error = proto.String(err.Error())
	}
	return_buf, err_marshal := proto.Marshal(&return_)
	if err_marshal != nil {
		panic(err_marshal)
	}
	return ReturnBytes(return_buf)
}

//export JoinGroupWithLink
func JoinGroupWithLink(id *C.char, code *C.char) C.struct_BytesReturn {
	jid, err := clients[C.GoString(id)].JoinGroupWithLink(C.GoString(code))

	neojid := utils.EncodeJidProto(jid)

	return_ := neonize.JoinGroupWithLinkReturnFunction{
		Jid: neojid,
	}
	if err != nil {
		return_.Error = proto.String(err.Error())
	}

	jidBuf, err_ := proto.Marshal(&return_)

	if err_ != nil {
		panic(err_)
	}
	return ReturnBytes(jidBuf)
}

//export SendChatPresence
func SendChatPresence(id *C.char, JIDByte *C.uchar, JIDSize C.int, state C.int, media C.int) *C.char {
	jidbyte := getByteByAddr(JIDByte, JIDSize)
	var neonize_jid neonize.JID
	err := proto.Unmarshal(jidbyte, &neonize_jid)
	if err != nil {
		panic(err)
	}
	err_status := clients[C.GoString(id)].SendChatPresence(
		utils.DecodeJidProto(&neonize_jid),
		utils.ChatPresence[int(state)],
		utils.ChatPresenceMedia[int(media)],
	)
	if err != nil {
		return C.CString(err_status.Error())
	}
	return C.CString("")
}

//export BuildRevoke
func BuildRevoke(id *C.char, ChatByte *C.uchar, ChatSize C.int, SenderByte *C.uchar, SenderSize C.int, messageID *C.char) C.struct_BytesReturn {
	chatByte := getByteByAddr(ChatByte, ChatSize)
	senderByte := getByteByAddr(SenderByte, SenderSize)
	var Chat neonize.JID
	var Sender neonize.JID
	err := proto.Unmarshal(chatByte, &Chat)

	if err != nil {
		panic(err)
	}
	err_ := proto.Unmarshal(senderByte, &Sender)
	if err_ != nil {
		panic(err_)
	}
	message := clients[C.GoString(id)].BuildRevoke(
		utils.DecodeJidProto(&Chat),
		utils.DecodeJidProto(&Sender),
		C.GoString(messageID),
	)
	messageByte, err_marshal := proto.Marshal(message)
	if err_marshal != nil {
		panic(err_marshal)
	}
	return ReturnBytes(messageByte)
}

//export BuildPollVote
func BuildPollVote(id *C.char, pollInfo *C.uchar, pollInfoSize C.int, optionName *C.uchar, optionNameSize C.int) C.struct_BytesReturn {
	var msgInfo neonize.MessageInfo
	var optionNames neonize.ArrayString
	err := proto.Unmarshal(getByteByAddr(pollInfo, pollInfoSize), &msgInfo)
	if err != nil {
		panic(err)
	}
	err_2 := proto.Unmarshal(getByteByAddr(optionName, optionNameSize), &optionNames)
	if err_2 != nil {
		panic(err_2)
	}
	pollInfoByte := getByteByAddr(pollInfo, pollInfoSize)
	err_3 := proto.Unmarshal(pollInfoByte, &msgInfo)
	if err_3 != nil {
		panic(err_3)
	}
	optionsname := []string{}
	for _, option := range optionNames.Data {
		optionsname = append(optionsname, option)
	}
	pollInfo_, err_poll := clients[C.GoString(id)].BuildPollVote(utils.DecodeMessageInfo(&msgInfo), optionsname)
	return_ := neonize.BuildPollVoteReturnFunction{}
	if err != nil {
		return_.Error = proto.String(err_poll.Error())
	}
	if pollInfo_ != nil {
		return_.PollVote = utils.EncodeMessage(pollInfo_)
	}
	return_buf, err_decode := proto.Marshal(&return_)
	if err_decode != nil {
		panic(err_decode)
	}
	return ReturnBytes(return_buf)
}

//export CreateGroup
func CreateGroup(id *C.char, createGroupByte *C.uchar, createGroupSize C.int) C.struct_BytesReturn {
	creategrupbyte := getByteByAddr(createGroupByte, createGroupSize)
	var reqCreateGroup neonize.ReqCreateGroup
	err := proto.Unmarshal(creategrupbyte, &reqCreateGroup)
	if err != nil {
		panic(err)
	}
	group_info, err_ := clients[C.GoString(id)].CreateGroup(utils.DecodeReqCreateGroup(&reqCreateGroup))
	return_ := neonize.GetGroupInfoReturnFunction{}
	if group_info != nil {
		return_.GroupInfo = utils.EncodeGroupInfo(group_info)
	}
	if err_ != nil {
		return_.Error = proto.String(err.Error())
	}
	return_buf, err_marshal := proto.Marshal(&return_)
	if err_marshal != nil {
		panic(err_marshal)
	}
	return ReturnBytes(return_buf)
}

//export GetMe
func GetMe(id *C.char) C.struct_BytesReturn {
	cli := clients[C.GoString(id)].Store
	device := neonize.Device{
		PushName:      &cli.PushName,
		Platform:      &cli.Platform,
		BussinessName: &cli.BusinessName,
		Initialized:   &cli.Initialized,
	}
	if cli.ID != nil {
		device.JID = utils.EncodeJidProto(*cli.ID)
	}
	DeviceBuf, err := proto.Marshal(&device)
	if err != nil {
		panic(DeviceBuf)
	}
	return ReturnBytes(DeviceBuf)
}

///

func main() {

}
