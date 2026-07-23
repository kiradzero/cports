pkgname = "hipfft"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DHIP_PLATFORM=amd",
    "-DBUILD_WITH_LIB=ROCM",
    "-DBUILD_CLIENTS_TESTS=OFF",
    "-DBUILD_CLIENTS_BENCHMARKS=OFF",
    "-DBUILD_CLIENTS_SAMPLES=OFF",
    "-DCMAKE_CXX_COMPILER=hipcc",
]
hostmakedepends = ["cmake", "git", "ninja", "rocm-cmake"]
makedepends = [
    "hip-devel",
    "rocfft-devel",
    "rocm-comgr-devel",
    "rocr-runtime-devel",
]
pkgdesc = "ROCm fast Fourier transform marshalling library"
license = "MIT"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/hipfft.tar.gz>hipfft-{pkgver}.tar.gz"
sha256 = "65d08232b0f83dda214c96e869db4b68380a12a7f6526ae008ec5faf19ec30e9"
# thin dispatch wrapper, no kernels; tests require amdgpu hardware
options = ["!check", "!lto"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("hipfft-devel")
def _(self):
    return self.default_devel()
