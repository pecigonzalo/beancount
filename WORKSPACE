"""Bazel workspace for the Beancount."""
workspace(name="beancount")

load("//third_party/foreign:setup.bzl", "setup_rules_foreign")
setup_rules_foreign()

load("//third_party/cppbase:setup.bzl", "setup_cppbase")
setup_cppbase()

load("//third_party/python:setup.bzl", "setup_python")
setup_python()

load("//third_party/proto:setup.bzl", "setup_proto", "setup_riegeli")
setup_proto()
setup_riegeli()
load("@rules_proto//proto:repositories.bzl", "rules_proto_dependencies", "rules_proto_toolchains")
rules_proto_dependencies()
rules_proto_toolchains()

# We managed to get protobuf working in a single module with the fast cpp proto casters.
# Disable upb experiments for now. See {1fdb0ce4215b}
#
## load("//third_party/proto:setup.bzl", "setup_upb")
## setup_upb()
## load("@upb//bazel:workspace_deps.bzl", "upb_deps")
## upb_deps()

load("//third_party/proto:setup.bzl", "setup_flatbuffers", "setup_arrow")
setup_flatbuffers()
setup_arrow()

load("//third_party/parser:setup.bzl", "setup_parser")
setup_parser()
load("//third_party/parser:repositories.bzl", "parser_toolchains")
parser_toolchains()

# # Setup for packaging rules.
# load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
# http_archive(
#     name = "rules_pkg",
#     url = "https://github.com/bazelbuild/rules_pkg/releases/download/0.2.5/rules_pkg-0.2.5.tar.gz",
#     sha256 = "352c090cc3d3f9a6b4e676cf42a6047c16824959b438895a76c2989c6d7c246a",
# )
# load("@rules_pkg//:deps.bzl", "rules_pkg_dependencies")
# rules_pkg_dependencies()

# TODO(blais): Convert all checks to use maybe(). See upb for an example.
# load("@bazel_tools//tools/build_defs/repo:utils.bzl", "maybe")
