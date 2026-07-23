pkgname = "cli11"
pkgver = "2.6.2"
pkgrel = 2
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DCLI11_BOOST=OFF",
    "-DCLI11_BUILD_DOCS=ON",
    "-DCLI11_BUILD_EXAMPLES=OFF",
    "-DCLI11_BUILD_EXAMPLES_JSON=OFF",
    "-DCLI11_BUILD_TESTS=OFF",
    "-DCLI11_CUDA_TESTS=OFF",
    "-DCLI11_DISABLE_IMPL_HEADERS_INSTALL=ON",
    "-DCLI11_FORCE_LIBCXX=OFF",
    "-DCLI11_FULL_INSTALL=OFF",
    "-DCLI11_INSTALL=ON",
    "-DCLI11_INSTALL_PACKAGE_TESTS=OFF",
    "-DCLI11_MODULE_TESTS=OFF",
    "-DCLI11_MODULES=OFF",
    "-DCLI11_SANITIZERS=OFF",
    "-DCLI11_SINGLE_FILE=OFF",
    "-DCLI11_SINGLE_FILE_TESTS=OFF",
    "-DCLI11_WARNINGS_AS_ERRORS=OFF",
]
hostmakedepends = [
    "cmake",
    "doxygen",
    "ninja",
    "pkgconf",
]
makedepends = [
    "catch2-devel",
]
pkgdesc = "Command line parser for C++"
license = "BSD-3-Clause"
url = "https://github.com/CLIUtils/CLI11"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c6ea6b2e5608b3ea8617999bd5f47420c71b2ebdb8dc4767c1034d1da5785711"
# it does not have any tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
