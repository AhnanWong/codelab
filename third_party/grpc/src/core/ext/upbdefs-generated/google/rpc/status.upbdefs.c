/* This file was generated by upbc (the upb compiler) from the input
 * file:
 *
 *     google/rpc/status.proto
 *
 * Do not edit -- your changes will be discarded when the file is
 * regenerated. */

#include "upb/def.h"
#include "google/rpc/status.upbdefs.h"

extern upb_def_init google_protobuf_any_proto_upbdefinit;
extern const upb_msglayout google_rpc_Status_msginit;

static const upb_msglayout *layouts[1] = {
  &google_rpc_Status_msginit,
};

static const char descriptor[272] = {'\n', '\027', 'g', 'o', 'o', 'g', 'l', 'e', '/', 'r', 'p', 'c', '/', 's', 't', 'a', 't', 'u', 's', '.', 'p', 'r', 'o', 't', 'o', 
'\022', '\n', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'r', 'p', 'c', '\032', '\031', 'g', 'o', 'o', 'g', 'l', 'e', '/', 'p', 'r', 'o', 't', 
'o', 'b', 'u', 'f', '/', 'a', 'n', 'y', '.', 'p', 'r', 'o', 't', 'o', '\"', 'f', '\n', '\006', 'S', 't', 'a', 't', 'u', 's', '\022', 
'\022', '\n', '\004', 'c', 'o', 'd', 'e', '\030', '\001', ' ', '\001', '(', '\005', 'R', '\004', 'c', 'o', 'd', 'e', '\022', '\030', '\n', '\007', 'm', 'e', 
's', 's', 'a', 'g', 'e', '\030', '\002', ' ', '\001', '(', '\t', 'R', '\007', 'm', 'e', 's', 's', 'a', 'g', 'e', '\022', '.', '\n', '\007', 'd', 
'e', 't', 'a', 'i', 'l', 's', '\030', '\003', ' ', '\003', '(', '\013', '2', '\024', '.', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'p', 'r', 'o', 
't', 'o', 'b', 'u', 'f', '.', 'A', 'n', 'y', 'R', '\007', 'd', 'e', 't', 'a', 'i', 'l', 's', 'B', '^', '\n', '\016', 'c', 'o', 'm', 
'.', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'r', 'p', 'c', 'B', '\013', 'S', 't', 'a', 't', 'u', 's', 'P', 'r', 'o', 't', 'o', 'P', 
'\001', 'Z', '7', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'g', 'o', 'l', 'a', 'n', 'g', '.', 'o', 'r', 'g', '/', 'g', 'e', 'n', 'p', 
'r', 'o', 't', 'o', '/', 'g', 'o', 'o', 'g', 'l', 'e', 'a', 'p', 'i', 's', '/', 'r', 'p', 'c', '/', 's', 't', 'a', 't', 'u', 
's', ';', 's', 't', 'a', 't', 'u', 's', '\242', '\002', '\003', 'R', 'P', 'C', 'b', '\006', 'p', 'r', 'o', 't', 'o', '3', 
};

static upb_def_init *deps[2] = {
  &google_protobuf_any_proto_upbdefinit,
  NULL
};

upb_def_init google_rpc_status_proto_upbdefinit = {
  deps,
  layouts,
  "google/rpc/status.proto",
  UPB_STRVIEW_INIT(descriptor, 272)
};
