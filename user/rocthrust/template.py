pkgname = "rocthrust"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DGPU_TARGETS=gfx1103",
    "-DHIP_PLATFORM=amd",
    "-DROCPRIM_FETCH_METHOD=PACKAGE",
    "-DBUILD_TEST=OFF",
    "-DBUILD_BENCHMARK=OFF",
    "-DBUILD_EXAMPLE=OFF",
    "-DCMAKE_CXX_COMPILER=hipcc",
]
hostmakedepends = ["cmake", "git", "ninja", "rocm-cmake"]
makedepends = ["hip-devel", "rocm-comgr-devel", "rocprim", "rocr-runtime-devel"]
depends = ["hip", "rocprim"]
pkgdesc = "ROCm Thrust port for parallel algorithms header library"
license = "Apache-2.0"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/rocthrust.tar.gz>rocthrust-{pkgver}.tar.gz"
sha256 = "13bf12e70f703144cbc9bb1c384b51e894f1c4fcbc5ea595cd6f235f8aa8f333"
# header-only INTERFACE library, tests need amdgpu hardware
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
