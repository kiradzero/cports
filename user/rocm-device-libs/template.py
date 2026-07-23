pkgname = "rocm-device-libs"
pkgver = "7.2.4"
pkgrel = 0
build_wrksrc = "amd/device-libs"
build_style = "cmake"
hostmakedepends = [
    "clang-devel",
    "cmake",
    "lld",
    "llvm-devel",
    "ninja",
    "rocm-cmake",
]
pkgdesc = "AMD ROCm device libraries"
license = "NCSA"
url = "https://github.com/ROCm/llvm-project"
source = (
    f"{url}/archive/refs/tags/rocm-{pkgver}.tar.gz"
    f">llvm-project-rocm-{pkgver}.tar.gz"
)
sha256 = "526b5fe23417c41acbeb2273e470887b4593f48a297a8d9c1a1aa730d556f9fb"
# tests need a functional hip toolchain
options = ["!check"]


def post_patch(self):
    # install bitcode to /usr/lib/amdgcn instead of /usr/amdgcn
    for f in ["cmake/OCL.cmake", "cmake/Packages.cmake"]:
        fp = self.cwd / "amd/device-libs" / f
        fp.write_text(
            fp.read_text().replace("amdgcn/bitcode", "lib/amdgcn/bitcode")
        )


def post_install(self):
    # let clang find the device libs without --rocm-device-lib-path
    self.install_dir("usr/lib/clang/22/lib")
    self.install_link("usr/lib/clang/22/lib/amdgcn", "../../../amdgcn")
    self.install_license("LICENSE.TXT")
