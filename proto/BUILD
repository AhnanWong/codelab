package(default_visibility = ["//visibility:public"])

load("@io_bazel_rules_go//proto:def.bzl", "go_proto_library")
load("@io_grpc_grpc_java//:java_grpc_library.bzl", "java_grpc_library")

proto_library(
    name = "point_proto",
    srcs = ["point.proto"],
)

go_proto_library(
    name = "point_go_proto",
    proto = ":point_proto",
    importpath = "codelab.com/proto",
    visibility = ["//visibility:public"]
)