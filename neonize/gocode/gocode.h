/* Code generated by cmd/cgo; DO NOT EDIT. */

/* package command-line-arguments */


#line 1 "cgo-builtin-export-prolog"

#include <stddef.h>

#ifndef GO_CGO_EXPORT_PROLOGUE_H
#define GO_CGO_EXPORT_PROLOGUE_H

#ifndef GO_CGO_GOSTRING_TYPEDEF
typedef struct { const char *p; ptrdiff_t n; } _GoString_;
#endif

#endif

/* Start of preamble from import "C" comments.  */


#line 3 "main.go"


   #include <stdlib.h>
   #include <stdbool.h>
   #include "header/cstruct.h"

   typedef void (*ptr_to_python_function_string) (char*);

   static inline void call_c_func_string(ptr_to_python_function_string ptr, char* xStr) {
    (ptr)(xStr);
    }
	typedef void (*ptr_to_python_function_bytes)(const char*, size_t, const char*, size_t);

	static inline void call_c_func_bytes(ptr_to_python_function_bytes ptr, const char* data, size_t size, const char* msginfo, size_t msginfo_size) {
		(ptr)(data, size, msginfo, msginfo_size);
	}

#line 1 "cgo-generated-wrapper"


/* End of preamble from import "C" comments.  */


/* Start of boilerplate cgo prologue.  */
#line 1 "cgo-gcc-export-header-prolog"

#ifndef GO_CGO_PROLOGUE_H
#define GO_CGO_PROLOGUE_H

typedef signed char GoInt8;
typedef unsigned char GoUint8;
typedef short GoInt16;
typedef unsigned short GoUint16;
typedef int GoInt32;
typedef unsigned int GoUint32;
typedef long long GoInt64;
typedef unsigned long long GoUint64;
typedef GoInt64 GoInt;
typedef GoUint64 GoUint;
typedef size_t GoUintptr;
typedef float GoFloat32;
typedef double GoFloat64;
#ifdef _MSC_VER
#include <complex.h>
typedef _Fcomplex GoComplex64;
typedef _Dcomplex GoComplex128;
#else
typedef float _Complex GoComplex64;
typedef double _Complex GoComplex128;
#endif

/*
  static assertion to make sure the file is being used on architecture
  at least with matching size of GoInt.
*/
typedef char _check_for_64_bit_pointer_matching_GoInt[sizeof(void*)==64/8 ? 1:-1];

#ifndef GO_CGO_GOSTRING_TYPEDEF
typedef _GoString_ GoString;
#endif
typedef void *GoMap;
typedef void *GoChan;
typedef struct { void *t; void *v; } GoInterface;
typedef struct { void *data; GoInt len; GoInt cap; } GoSlice;

#endif

/* End of boilerplate cgo prologue.  */

#ifdef __cplusplus
extern "C" {
#endif

extern struct BytesReturn Upload(char* id, unsigned char* mediabuff, int mediaSize, int mediatype);
extern char* GenerateMessageID(char* id);
extern struct BytesReturn SendMessage(char* id, unsigned char* JIDByte, int JIDSize, unsigned char* messageByte, int messageSize);
extern void Neonize(char* db, char* id, ptr_to_python_function_string qrCb, ptr_to_python_function_string logStatus, ptr_to_python_function_bytes messageCb);
extern struct BytesReturn Download(char* id, unsigned char* messageProto, int size);
extern struct BytesReturn IsOnWhatsApp(char* id, char* numbers);
extern _Bool IsConnected(char* id);
extern _Bool IsLoggedIn(char* id);
extern struct BytesReturn GetUserInfo(char* id, unsigned char* JIDSByte, int JIDSSize);

// /GROUP
//
extern struct BytesReturn GetGroupInfo(char* id, unsigned char* JIDByte, int JIDSize);
extern char* SetGroupName(char* id, unsigned char* JIDByte, int JIDSize, char* name);
extern struct BytesReturn SetGroupPhoto(char* id, unsigned char* JIDByte, int JIDSize, unsigned char* Photo, int PhotoSize);
extern char* LeaveGroup(char* id, unsigned char* JIDByte, int JIDSize);
extern struct BytesReturn GetGroupInviteLink(char* id, unsigned char* JIDByte, int JIDSize, _Bool revoke);
extern struct BytesReturn JoinGroupWithLink(char* id, char* code);
extern char* SendChatPresence(char* id, unsigned char* JIDByte, int JIDSize, int state, int media);
extern struct BytesReturn BuildRevoke(char* id, unsigned char* ChatByte, int ChatSize, unsigned char* SenderByte, int SenderSize, char* messageID);
extern struct BytesReturn CreateGroup(char* id, unsigned char* createGroupByte, int createGroupSize);

#ifdef __cplusplus
}
#endif
