pkgname = "hipcc"
pkgver = "7.2.4"
pkgrel = 1
build_wrksrc = "amd/hipcc"
build_style = "cmake"
configure_args = ["-DHIPCC_BACKWARD_COMPATIBILITY=OFF"]
hostmakedepends = ["cmake", "ninja"]
depends = ["clang", "lld", "rocm-device-libs"]
pkgdesc = "HIP compiler driver"
license = "MIT"
url = "https://github.com/ROCm/llvm-project"
source = (
    f"{url}/archive/refs/tags/rocm-{pkgver}.tar.gz"
    f">llvm-project-rocm-{pkgver}.tar.gz"
)
sha256 = "526b5fe23417c41acbeb2273e470887b4593f48a297a8d9c1a1aa730d556f9fb"
# amdclang/amdclang++ resolve to clang from the hard-dep clang package
broken_symlinks = ["usr/bin/amdclang", "usr/bin/amdclang++"]
# no tests
options = ["!check"]


def post_patch(self):
    cwd = self.cwd / "amd/hipcc"
    # no libstdc++fs on libc++, C++17 fs is in the main library
    fp = cwd / "CMakeLists.txt"
    fp.write_text(fp.read_text().replace("libstdc++fs.so", ""))
    # clang lives in /usr/bin, not <rocm>/lib/llvm/bin
    fp = cwd / "src/hipBin_amd.h"
    fp.write_text(fp.read_text().replace('"lib/llvm/bin"', '"bin"'))


def post_install(self):
    # windows-only perl helper
    self.uninstall("usr/bin/hipvars.pm")
    # ROCm tools (Tensile, rocBLAS, ...) invoke the compiler as amdclang/
    # amdclang++; on Chimera those are just the system clang
    self.install_link("usr/bin/amdclang", "clang")
    self.install_link("usr/bin/amdclang++", "clang++")
    self.install_license("LICENSE.txt")
