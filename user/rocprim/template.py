pkgname = "rocprim"
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
makedepends = ["hip-devel", "rocm-comgr-devel", "rocr-runtime-devel"]
depends = ["hip"]
pkgdesc = "ROCm parallel primitives header library"
license = "MIT"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/rocprim.tar.gz>rocprim-{pkgver}.tar.gz"
sha256 = "3ec26b7ae729aad766366110b3a5341793342ca1351cf4c72d38f28e8f26aa75"
# header-only INTERFACE library, tests need amdgpu hardware
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
