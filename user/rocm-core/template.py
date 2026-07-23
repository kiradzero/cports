pkgname = "rocm-core"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    f"-DROCM_VERSION={pkgver}",
]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "AMD ROCm core package"
subdesc = "version files"
license = "MIT"
url = "https://rocm.docs.amd.com"
source = (
    f"https://github.com/ROCm/rocm-core/archive/refs/tags/rocm-{pkgver}.tar.gz"
)
sha256 = "32dab2f00e22fb5462beffae03cc642403925d22a42662e15ac0f68d8e885dea"
# no test suite
options = ["!check"]


def post_install(self):
    self.uninstall("usr/.info")
    self.install_license("LICENSE.md")


@subpackage("rocm-core-devel")
def _(self):
    return self.default_devel()
