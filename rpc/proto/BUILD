package(default_visibility = ["//visibility:public"])

load("@io_bazel_rules_go//proto:def.bzl", "go_proto_library")
load("@io_grpc_grpc_java//:java_grpc_library.bzl", "java_grpc_library")
load("@com_google_protobuf//:protobuf.bzl", "py_proto_library")
load("@com_github_grpc_grpc//bazel:python_rules.bzl", "py_grpc_library")
#load("@com_github_grpc_grpc//bazel:python_rules.bzl", "py_grpc_library", "py_proto_library")
#load("@rules_proto//proto:defs.bzl", "proto_library")

proto_library(
    name = "data_proto",
    srcs = [
        "common.proto", 
        "user.proto", 
        "item.proto",
        "service.proto"
    ],
)

java_proto_library(
    name = "data_java_proto",
    deps = [":data_proto"],
)

java_grpc_library(
    name = "rcd_java_grpc",
    srcs = [":data_proto"],
    deps = [":data_java_proto"],
)

go_proto_library(
    name = "rcd_go_grpc",
    compiler = "@io_bazel_rules_go//proto:go_grpc",
    proto = ":data_proto",
    importpath = "codelab.com/rpc/rcd",
    visibility = ["//visibility:public"]
)

py_proto_library(
    name = "data_py_pb2",
    srcs = [
        "common.proto",
        "item.proto",
        "user.proto",
        "service.proto"
    ],
#    deps = [":data_proto"],
    deps = ["@com_google_protobuf//:protobuf_python",],
)

py_grpc_library(
    name = "rcd_py_pb2_grpc",
    srcs = [
#        "common.proto",
#        "item.proto",
#        "user.proto",
        "service.proto",
#        ":data_proto"
    ],
    deps = [":data_py_pb2"],
)