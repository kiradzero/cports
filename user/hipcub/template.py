pkgname = "hipcub"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DGPU_TARGETS=gfx1103",
    "-DHIP_PLATFORM=amd",
    "-DBUILD_TEST=OFF",
    "-DBUILD_BENCHMARK=OFF",
    "-DBUILD_EXAMPLE=OFF",
    "-DCMAKE_CXX_COMPILER=hipcc",
]
hostmakedepends = ["cmake", "git", "ninja", "rocm-cmake"]
makedepends = ["hip-devel", "rocm-comgr-devel", "rocprim", "rocr-runtime-devel"]
depends = ["hip", "rocprim"]
pkgdesc = "ROCm thin wrapper over rocPRIM with a CUB-compatible API"
license = "BSD-3-Clause"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/hipcub.tar.gz>hipcub-{pkgver}.tar.gz"
sha256 = "2b08b0e7fc8d97717bc9656a0cc0e502dd221770f34deb8721ced2239939d779"
# header-only INTERFACE library, tests need amdgpu hardware
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
