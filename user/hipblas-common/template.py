pkgname = "hipblas-common"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "rocm-cmake"]
pkgdesc = "Common files for hipBLAS libraries"
license = "MIT"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/hipblas-common.tar.gz>hipblas-common-{pkgver}.tar.gz"
sha256 = "5c7806accb2123b7a0a0d814517adc85335ab9c0ed3318fcbad2282d219f397b"
# header-only, no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
