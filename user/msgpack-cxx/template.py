pkgname = "msgpack-cxx"
pkgver = "8.0.0"
pkgrel = 0
build_style = "cmake"
# header-only; boost integration is optional and pulls a heavy dep
configure_args = ["-DMSGPACK_USE_BOOST=OFF", "-DMSGPACK_BUILD_DOCS=OFF"]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "MessagePack implementation for C++"
license = "BSL-1.0"
url = "https://github.com/msgpack/msgpack-c"
source = f"{url}/releases/download/cpp-{pkgver}/msgpack-cxx-{pkgver}.tar.gz"
sha256 = "4a3c0c0ac55ef4456c2d0b93c21b5d105aa3a8f21ef8fa9758550feaf989b92f"
# header-only, no runtime artifacts to test
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE_1_0.txt")
