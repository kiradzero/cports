pkgname = "hiprand"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DHIP_PLATFORM=amd",
    "-DBUILD_WITH_LIB=ROCM",
    "-DBUILD_TEST=OFF",
    "-DBUILD_BENCHMARK=OFF",
    "-DBUILD_FORTRAN_WRAPPER=OFF",
    "-DCMAKE_CXX_COMPILER=hipcc",
]
hostmakedepends = ["cmake", "git", "ninja", "rocm-cmake"]
makedepends = [
    "hip-devel",
    "rocm-comgr-devel",
    "rocr-runtime-devel",
    "rocrand-devel",
]
pkgdesc = "ROCm random number generator marshalling library"
license = "MIT"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/hiprand.tar.gz>hiprand-{pkgver}.tar.gz"
sha256 = "c31cec665ee0a7333fd4dfa54d46dd601710a17f56826f1d309aea4333c37360"
# thin dispatch wrapper, no kernels; tests require amdgpu hardware
options = ["!check", "!lto"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("hiprand-devel")
def _(self):
    return self.default_devel()
