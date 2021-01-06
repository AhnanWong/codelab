package(default_visibility = ["//visibility:public"])
load("@py_deps//:requirements.bzl", "requirement")

py_binary(
    name = "server",
    srcs = [
        "server.py"
    ],
    deps = [
        "//codelab/grpc/proto:echo_service_py_grpc_proto",
        requirement("grpcio"),
#        requirement('absl-py'),
    ],
)

py_binary(
    name = "client",
    srcs = [
        "client.py"
    ],
    deps = [
        "//codelab/grpc/proto:echo_service_py_grpc_proto",
        requirement("grpcio"),
#        requirement('absl-py'),
    ],
)
