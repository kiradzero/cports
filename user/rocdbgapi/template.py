pkgname = "rocdbgapi"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf", "git"]
makedepends = ["linux-headers", "rocm-comgr-devel", "rocr-runtime-devel"]
pkgdesc = "AMD debugger API library"
license = "MIT"
url = "https://github.com/ROCm/ROCdbgapi"
source = (
    f"{url}/archive/refs/tags/rocm-{pkgver}.tar.gz>rocdbgapi-{pkgver}.tar.gz"
)
sha256 = "25d5a1bc8a2bc9ce95c95d2c4230250fac71088bb927d4dcaf6c857090a93d4f"
# no test suite in the build
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("rocdbgapi-devel")
def _(self):
    return self.default_devel()
