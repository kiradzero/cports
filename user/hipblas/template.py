pkgname = "hipblas"
pkgver = "7.2.4"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DHIP_PLATFORM=amd",
    "-DBUILD_WITH_SOLVER=ON",
    "-DBUILD_CLIENTS_TESTS=OFF",
    "-DBUILD_CLIENTS_BENCHMARKS=OFF",
    "-DBUILD_CLIENTS_SAMPLES=OFF",
    "-DCMAKE_CXX_COMPILER=hipcc",
]
hostmakedepends = [
    "cmake",
    "git",
    "ninja",
    "python",
    "rocm-cmake",
]
makedepends = [
    "hip-devel",
    "hipblas-common",
    "llvm-devel",
    "rocblas-devel",
    "rocm-comgr-devel",
    "rocr-runtime-devel",
    "rocsolver-devel",
]
pkgdesc = "ROCm BLAS marshalling library"
license = "MIT"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/hipblas.tar.gz>hipblas-{pkgver}.tar.gz"
sha256 = "5627f0dc9d9bf34a5a3e100312077b275b6fff305c3f25f970824bc1c85a3676"
# tests require amdgpu hardware
options = ["!check", "!lto"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("hipblas-devel")
def _(self):
    return self.default_devel()
