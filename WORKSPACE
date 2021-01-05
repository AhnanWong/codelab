workspace(name = "codelab")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# protobuf
local_repository(
    name = "com_google_protobuf",
    path = "third_party/protobuf-3.14.0",
)
load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")
protobuf_deps()

# bazel-skylib
#load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
#http_archive(
#    name = "bazel_skylib",
#    urls = [
#        "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.0.2/bazel-skylib-1.0.2.tar.gz",
#        "https://github.com/bazelbuild/bazel-skylib/releases/download/1.0.2/bazel-skylib-1.0.2.tar.gz",
#    ],
#    sha256 = "97e70364e9249702246c0e9444bccdc4b847bed1eb03c5a3ece4f83dfe6abc44",
#)
local_repository(
    name = "io_bazel_skylib",
    path = "third_party/bazel-skylib-1.0.3",
)
load("@io_bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")
bazel_skylib_workspace()

# rules go
local_repository(
    name = "io_bazel_rules_go",
    path = "tools/rules_go-0.25.1",
)
load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")
go_rules_dependencies()
go_register_toolchains(version = "host")

load("@io_bazel_rules_go//extras:embed_data_deps.bzl", "go_embed_data_dependencies")
go_embed_data_dependencies()

#rules_proto
#local_repository(
#    name = "rules_proto",
#    path = "tools/rules_proto",
#)
#load("@rules_proto//proto:repositories.bzl", "rules_proto_dependencies", "rules_proto_toolchains")
#rules_proto_dependencies()
#rules_proto_toolchains()

#rules_grpc
local_repository (
    name = "io_grpc_grpc_java",
    path = "third_party/grpc-java-1.27.2",
)
load("@io_grpc_grpc_java//:repositories.bzl", "grpc_java_repositories")
grpc_java_repositories()

local_repository(
    name = "com_github_grpc_grpc",
    path = "third_party/grpc",
)
load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")
grpc_deps()
load("@com_github_grpc_grpc//bazel:grpc_extra_deps.bzl", "grpc_extra_deps")
grpc_extra_deps()

# gazelle
#http_archive(
#    name = "bazel_gazelle",
#    sha256 = "222e49f034ca7a1d1231422cdb67066b885819885c356673cb1f72f748a3c9d4",
#    urls = [
#        "https://mirror.bazel.build/github.com/bazelbuild/bazel-gazelle/releases/download/v0.22.3/bazel-gazelle-v0.22.3.tar.gz",
#        "https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.22.3/bazel-gazelle-v0.22.3.tar.gz",
#    ],
#)
local_repository(
    name = "bazel_gazelle",
    path = "tools/bazel-gazelle",
)
load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies")
gazelle_dependencies()

load("@io_bazel_rules_python//python:pip.bzl", "pip_import", "pip_repositories")
pip_import(
    name = "grpc_python_dependencies",
    requirements = "@com_github_grpc_grpc//:requirements.bazel.txt",
)
load("@grpc_python_dependencies//:requirements.bzl", "pip_install")
pip_repositories()
pip_install()

# jvm
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
RULES_JVM_EXTERNAL_TAG = "3.3"
RULES_JVM_EXTERNAL_SHA = "d85951a92c0908c80bd8551002d66cb23c3434409c814179c0ff026b53544dab"
http_archive(
    name = "rules_jvm_external",
    strip_prefix = "rules_jvm_external-%s" % RULES_JVM_EXTERNAL_TAG,
    sha256 = RULES_JVM_EXTERNAL_SHA,
    url = "https://github.com/bazelbuild/rules_jvm_external/archive/%s.zip" % RULES_JVM_EXTERNAL_TAG,
)

load("@rules_jvm_external//:defs.bzl", "maven_install")
load("@rules_jvm_external//:specs.bzl", "maven")
load("@io_grpc_grpc_java//:repositories.bzl", "IO_GRPC_GRPC_JAVA_ARTIFACTS")
load("@io_grpc_grpc_java//:repositories.bzl", "IO_GRPC_GRPC_JAVA_OVERRIDE_TARGETS")
maven_install(
    artifacts = [
        "com.google.api.grpc:grpc-google-cloud-pubsub-v1:0.1.24",
        "com.google.api.grpc:proto-google-cloud-pubsub-v1:0.1.24",
        "com.google.guava:guava:23.0",
        "com.google.protobuf:protobuf-java:3.11.4",
        "com.google.protobuf:protobuf-java-util:3.11.4",
        "org.apache.logging.log4j:log4j-api:2.14.0",
        "org.apache.logging.log4j:log4j-core:2.14.0",
    ] + IO_GRPC_GRPC_JAVA_ARTIFACTS,
    override_targets = IO_GRPC_GRPC_JAVA_OVERRIDE_TARGETS,
    repositories = [
        "http://maven.aliyun.com/nexus/content/groups/public",
        "https://jcenter.bintray.com/",
        "https://repo1.maven.org/maven2",
    ],
    maven_install_json = "//:maven_install.json",
    fail_on_missing_checksum = False,
    version_conflict_policy = "pinned",
)
load("@maven//:defs.bzl", "pinned_maven_install")
pinned_maven_install()


# go deps
load("@bazel_gazelle//:deps.bzl", "go_repository")
go_repository(
    name = "org_golang_x_net",
    importpath = "golang.org/x/net",
    urls = ["https://github.com/golang/net/archive/master.zip"],
    strip_prefix="net-master",
    type = "zip",
)
go_repository(
    name = "org_golang_x_text",
    importpath = "golang.org/x/text",
    urls = ["https://github.com/golang/text/archive/v0.3.2.zip"],
    strip_prefix="text-0.3.2",
    type = "zip",
)
go_repository(
    name = "org_golang_google_grpc",
    importpath = "google.golang.org/grpc",
    urls = ["https://github.com/grpc/grpc-go/archive/v1.27.0.zip"],
    strip_prefix="grpc-go-1.27.0",
    type = "zip",
)
go_repository(
    name = "com_github_golang_glog",
    importpath = "github.com/golang/glog",
    commit = "23def4e6c14b4da8ac2ed8007337bc5eb5007998"
)

go_repository(
    name = "org_uber_go_atomic",
    importpath = "go.uber.org/atomic",
    remote = "https://github.com/uber-go/atomic.git",
    vcs = "git",
    commit = "12f27ba2637fa0e13772a4f05fa46a5d18d53182"
)

go_repository(
    name = "org_uber_go_multierr",
    importpath = "go.uber.org/multierr",
    remote = "https://github.com/uber-go/multierr.git",
    vcs = "git",
    commit = "e015acf18bb3a0d1bec970702b9cd997e2031781"
)

#go_repository(
#    name = "org_uber_go_zap",
#    importpath = "github.com/uber-go/zap",
#    commit = "a68efdbdd15b7816de33cdbe7e6def2a559bdf64"
#)
go_repository(
    name = "org_uber_go_zap",
    importpath = "go.uber.org/zap",
    urls = ["https://github.com/uber-go/zap/archive/v1.16.0.zip"],
    strip_prefix="zap-1.16.0",
    type = "zip",
)

# rules docker
http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "dc97fccceacd4c6be14e800b2a00693d5e8d07f69ee187babfd04a80a9f8e250",
    strip_prefix = "rules_docker-0.14.1",
    urls = ["https://github.com/bazelbuild/rules_docker/releases/download/v0.14.1/rules_docker-v0.14.1.tar.gz"],
)
load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    container_repositories = "repositories",
)
container_repositories()

# This is NOT needed when going through the language lang_image
# "repositories" function(s).
load("@io_bazel_rules_docker//repositories:deps.bzl", container_deps = "deps")

container_deps()
load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_pull",
)