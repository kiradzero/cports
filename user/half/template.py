pkgname = "half"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "rocm-cmake"]
pkgdesc = "Half-precision floating point C++ library"
license = "MIT"
url = "https://github.com/ROCm/half"
source = f"{url}/archive/refs/tags/rocm-{pkgver}.tar.gz>half-{pkgver}.tar.gz"
sha256 = "8cbe655d3ef19675e953934cf0cb49fdf899459407fbc6848af52282269fc7f9"
# header-only, no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
