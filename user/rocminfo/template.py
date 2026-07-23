pkgname = "rocminfo"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
makedepends = ["rocr-runtime-devel"]
pkgdesc = "ROCm application for reporting HSA system information"
license = "NCSA"
url = "https://github.com/ROCm/rocm-systems"
source = f"{url}/releases/download/rocm-{pkgver}/rocminfo.tar.gz>rocminfo-{pkgver}.tar.gz"
sha256 = "8c4dbe41e03180311a61a13eb6be51faeb8e0f70850dc984076a0a09262fda5d"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("License.txt")
