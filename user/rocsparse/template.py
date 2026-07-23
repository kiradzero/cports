pkgname = "rocsparse"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DGPU_TARGETS=gfx1103",
    "-DHIP_PLATFORM=amd",
    "-DBUILD_WITH_ROCBLAS=ON",
    "-DBUILD_WITH_ROCTX=OFF",
    "-DBUILD_CLIENTS_TESTS=OFF",
    "-DBUILD_CLIENTS_BENCHMARKS=OFF",
    "-DBUILD_CLIENTS_SAMPLES=OFF",
    "-DCMAKE_CXX_COMPILER=hipcc",
]
hostmakedepends = ["cmake", "git", "ninja", "python", "rocm-cmake", "rocminfo"]
makedepends = [
    "hip-devel",
    "llvm-devel",
    "rocblas-devel",
    "rocm-comgr-devel",
    "rocprim",
    "rocr-runtime-devel",
]
pkgdesc = "ROCm sparse linear algebra library"
license = "MIT"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/rocsparse.tar.gz>rocsparse-{pkgver}.tar.gz"
sha256 = "5342f1e536d42c86461a3482cd1921ba3f854e15b5705d792494b36c4750e6e5"
# tests require amdgpu hardware; ships gfx1103 device code (foreign ELF)
options = ["!check", "!lto", "foreignelf"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("rocsparse-devel")
def _(self):
    return self.default_devel()
