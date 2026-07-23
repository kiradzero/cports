pkgname = "miopen"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DMIOPEN_BACKEND=HIP",
    "-DCMAKE_CXX_COMPILER=hipcc",
    "-DGPU_TARGETS=gfx1103",
    "-DHIP_PLATFORM=amd",
    "-DBUILD_TESTING=OFF",
    "-DBoost_USE_STATIC_LIBS=OFF",
    "-DMIOPEN_BUILD_DRIVER=ON",
    "-DMIOPEN_USE_COMPOSABLEKERNEL=OFF",
    "-DMIOPEN_USE_MLIR=OFF",
    "-DMIOPEN_USE_HIPBLASLT=OFF",
    "-DMIOPEN_ENABLE_AI_IMMED_MODE_FALLBACK=OFF",
    "-DMIOPEN_ENABLE_AI_KERNEL_TUNING=OFF",
]
hostmakedepends = [
    "cmake",
    "git",
    "ninja",
    "pkgconf",
    "python",
    "rocm-cmake",
    "rocminfo",
]
makedepends = [
    "boost-devel",
    "bzip2-devel",
    "half",
    "hip-devel",
    "llvm-devel",
    "nlohmann-json",
    "rocblas-devel",
    "rocm-comgr-devel",
    "rocr-runtime-devel",
    "rocrand-devel",
    "roctracer-devel",
    "sqlite-devel",
]
pkgdesc = "AMD ROCm machine intelligence library"
license = "MIT"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/miopen.tar.gz>miopen-{pkgver}.tar.gz"
sha256 = "3752c7463cf58f05519b6025b303f54716aa7ff47a36dfbfa71ea4bc1be21411"
# tests require amdgpu hardware
options = ["!check", "foreignelf"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("miopen-devel")
def _(self):
    return self.default_devel()
