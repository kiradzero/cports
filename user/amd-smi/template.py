pkgname = "amd-smi"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # bundled ESMI is EPYC-server-only and is git-cloned at configure time
    # (no network in the sandbox), so disable it
    "-DENABLE_ESMI_LIB=OFF",
    # Chimera has no ldconfig
    "-DENABLE_LDCONFIG=OFF",
    "-DBUILD_TESTS=OFF",
    "-DBUILD_EXAMPLES=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python"]
makedepends = ["libdrm-devel"]
pkgdesc = "AMD System Management Interface library and CLI"
license = "MIT"
url = "https://github.com/ROCm/rocm-systems"
source = f"{url}/releases/download/rocm-{pkgver}/amdsmi.tar.gz>amd-smi-{pkgver}.tar.gz"
sha256 = "e1b7afe0ba9b12dc0ea9f3a49c381ff65363344b33ac435f7bbcc0ab1e4c8ff6"
# tests require amdgpu hardware
options = ["!check"]


def post_install(self):
    # the python wrapper drops a full copy of the lib next to its module in
    # /usr/share (banned path for ELF); it also finds the real versioned lib
    # in /usr/lib via a relative walk, so drop the duplicate
    (self.destdir / "usr/share/amd_smi/amdsmi/libamd_smi.so").unlink()
    self.install_license("LICENSE")


@subpackage("amd-smi-devel")
def _(self):
    return self.default_devel()
