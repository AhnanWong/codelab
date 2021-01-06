package(default_visibility = ["//visibility:public"])

load("@io_bazel_rules_docker//container:container.bzl", "container_image")
load("@io_bazel_rules_docker//container:container.bzl", "container_push")

java_binary(
    name = "client",
    srcs = [
        "TransClient.java"
    ],
    main_class = "rpc.java.TransClient",
    deps = [
        "//rpc/proto:transceiver_java_proto",
        "//rpc/proto:transmission_object_java_proto",
        "//rpc/proto:transceiver_java_proto_grpc",
        "@io_grpc_grpc_java//netty",
        "@io_grpc_grpc_java//api",
        "@io_grpc_grpc_java//core:core_maven",
    ],
)

java_binary(
    name = "server",
    srcs = [
        "TransServer.java",
        "TransRpcImpl.java",
    ],
    main_class = "rpc.java.TransServer",
    deps = [
        "//rpc/proto:transceiver_java_proto",
        "//rpc/proto:transmission_object_java_proto",
        "//rpc/proto:transceiver_java_proto_grpc",
        "@io_grpc_grpc_java//netty",
        "@io_grpc_grpc_java//api",
        "@io_grpc_grpc_java//stub",
        "@io_grpc_grpc_java//core:core_maven",
        "@maven//:com_google_protobuf_protobuf_java_util"
    ],
)

java_binary(
    name = "app",
    srcs = [
        "TransApp.java",
        "TransServer.java",
        "TransRpcImpl.java",
        "TransClient.java"
    ],
    main_class = "rpc.java.TransApp",
    deps = [
        "//rpc/proto:transceiver_java_proto",
        "//rpc/proto:transmission_object_java_proto",
        "//rpc/proto:transceiver_java_proto_grpc",
        "@io_grpc_grpc_java//netty",
        "@io_grpc_grpc_java//api",
        "@io_grpc_grpc_java//core:core_maven",
    ],
)

container_image(
    name = "app_image",
    base = "@kz-wyn//image",
    files = [
        "//codelab/rpc/java:hello_world"
    ],
    cmd = [
        "hello_world",
    ],
#    workdir = [
#
#    ],
#    symlinks = [
#
#    ],
#    entrypoint = [
#
#    ]
)