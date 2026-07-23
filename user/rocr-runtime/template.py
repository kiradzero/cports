pkgname = "rocr-runtime"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_HSAKMT=OFF",
    "-DCMAKE_DISABLE_FIND_PACKAGE_rocprofiler-register=ON",
]
hostmakedepends = ["bash", "cmake", "ninja", "pkgconf", "vim-xxd"]
makedepends = [
    "clang-devel",
    "elfutils-devel",
    "libdrm-devel",
    "lld-devel",
    "llvm-devel",
    "rocm-device-libs",
    "roct-thunk-interface-devel",
]
depends = ["rocm-device-libs"]
pkgdesc = "AMD ROCm HSA runtime"
license = "MIT"
url = "https://github.com/ROCm/rocm-systems"
source = f"{url}/releases/download/rocm-{pkgver}/rocr-runtime.tar.gz>rocr-runtime-{pkgver}.tar.gz"
sha256 = "3a96a3312a6c300db66a3551e8a88f25075cfdfa1197822f9f70c2a80c011860"
# tests require amdgpu hardware
options = ["!check"]


def post_patch(self):
    # device libs live in /usr/lib, not a bitcode subdir
    fp = self.cwd / "runtime/hsa-runtime/image/blit_src/CMakeLists.txt"
    fp.write_text(fp.read_text().replace("-O2", "--rocm-path=/usr/lib/ -O2"))


def post_install(self):
    self.install_license("runtime/hsa-runtime/LICENSE.md")


@subpackage("rocr-runtime-devel")
def _(self):
    return self.default_devel()
