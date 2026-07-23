pkgname = "roct-thunk-interface"
pkgver = "7.2.4"
pkgrel = 0
build_wrksrc = "libhsakmt"
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DCMAKE_DISABLE_FIND_PACKAGE_NUMA=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libdrm-devel", "numactl-devel"]
depends = ["numactl"]
pkgdesc = "AMD ROCm thunk interface"
license = "MIT"
url = "https://github.com/ROCm/rocm-systems"
source = f"{url}/releases/download/rocm-{pkgver}/rocr-runtime.tar.gz>rocr-runtime-{pkgver}.tar.gz"
sha256 = "3a96a3312a6c300db66a3551e8a88f25075cfdfa1197822f9f70c2a80c011860"
# no standalone test suite
options = ["!check"]


def post_patch(self):
    cwd = self.cwd / "libhsakmt"
    fp = cwd / "CMakeLists.txt"
    t = fp.read_text()
    t = t.replace('get_version ( "1.0.0" )', f'get_version ( "{pkgver}" )')
    t = t.replace("${HSAKMT_TARGET} STATIC", "${HSAKMT_TARGET}")
    fp.write_text(t)


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("roct-thunk-interface-devel")
def _(self):
    return self.default_devel()
