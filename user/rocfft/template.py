pkgname = "rocfft"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DGPU_TARGETS=gfx1103",
    "-DHIP_PLATFORM=amd",
    "-DSQLITE_USE_SYSTEM_PACKAGE=ON",
    # AOT kernel-cache build (rocfft_aot_helper) SIGSEGVs doing offline
    # hiprtc/comgr compilation in the sandbox; disable it and let rocFFT
    # JIT-compile kernels via RTC on first use (cached in the user's home)
    "-DROCFFT_KERNEL_CACHE_ENABLE=OFF",
    "-DBUILD_CLIENTS_TESTS=OFF",
    "-DBUILD_CLIENTS_BENCHMARKS=OFF",
    "-DBUILD_CLIENTS_SAMPLES=OFF",
    "-DCMAKE_CXX_COMPILER=hipcc",
]
hostmakedepends = ["cmake", "git", "ninja", "python", "rocm-cmake", "rocminfo"]
makedepends = [
    "hip-devel",
    "llvm-devel",
    "rocm-comgr-devel",
    "rocr-runtime-devel",
    "sqlite-devel",
]
pkgdesc = "ROCm fast Fourier transform library"
license = "MIT"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/rocfft.tar.gz>rocfft-{pkgver}.tar.gz"
sha256 = "c37e25e7a4f09a1064c53b93b14c14cb7400f046405ea0ef3ea1f4b4a80d7528"
# tests require amdgpu hardware; ships gfx1103 device code + kernel cache (foreign ELF)
options = ["!check", "!lto", "foreignelf"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("rocfft-devel")
def _(self):
    return self.default_devel()
