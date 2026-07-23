pkgname = "hipsparse"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DHIP_PLATFORM=amd",
    "-DBUILD_CUDA=OFF",
    "-DBUILD_CLIENTS_TESTS=OFF",
    "-DBUILD_CLIENTS_BENCHMARKS=OFF",
    "-DBUILD_CLIENTS_SAMPLES=OFF",
    "-DCMAKE_CXX_COMPILER=hipcc",
    # hipSPARSE enables Fortran unconditionally (Fortran API module); use
    # LLVM flang so we stay on the libc++ toolchain (no gfortran/libgcc_s)
    "-DCMAKE_Fortran_COMPILER=flang",
]
hostmakedepends = ["cmake", "flang", "git", "ninja", "rocm-cmake"]
makedepends = [
    "hip-devel",
    "rocm-comgr-devel",
    "rocr-runtime-devel",
    "rocsparse-devel",
]
pkgdesc = "ROCm sparse linear algebra marshalling library"
license = "MIT"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/hipsparse.tar.gz>hipsparse-{pkgver}.tar.gz"
sha256 = "a1a1212746e4605703a3b42644bad83b07f6e7369d651dd657cd35611504a57a"
# LLVM flang rejects the ubsan integer-hardening flags cbuild puts in the
# shared LDFLAGS (they leak into the Fortran link step); drop int hardening
hardening = ["!int"]
# thin dispatch wrapper, no kernels; tests require amdgpu hardware
options = ["!check", "!lto"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("hipsparse-devel")
def _(self):
    return self.default_devel()
