pkgname = "rocm-smi-lib"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libdrm-devel"]
pkgdesc = "AMD ROCm system management interface library"
license = "MIT"
url = "https://github.com/ROCm/rocm-systems"
source = (
    f"{url}/releases/download/rocm-{pkgver}/rocm-smi-lib.tar.gz"
    f">rocm-smi-lib-{pkgver}.tar.gz"
)
sha256 = "12e888ab3030b2a6b67ef37b5fb9a5d76ee7d5e90830e28c249c2c405ffcfce0"
# tests require amdgpu hardware
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("rocm-smi-lib-devel")
def _(self):
    return self.default_devel()
