pkgname = "rocsolver"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DGPU_TARGETS=gfx1103",
    "-DHIP_PLATFORM=amd",
    "-DBUILD_WITH_SPARSE=OFF",
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
    "rocminfo",
]
makedepends = [
    "fmt-devel",
    "hip-devel",
    "llvm-devel",
    "rocblas-devel",
    "rocm-comgr-devel",
    "rocprim",
    "rocr-runtime-devel",
]
pkgdesc = "ROCm LAPACK implementation"
license = "BSD-2-Clause"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/rocsolver.tar.gz>rocsolver-{pkgver}.tar.gz"
sha256 = "174ddf22656950984dea1768d9232df5278a81c747a6eb272670e80cfac262a7"
# tests require amdgpu hardware; foreignelf: may embed gfx1103 device code
options = ["!check", "!lto", "foreignelf"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("rocsolver-devel")
def _(self):
    return self.default_devel()
