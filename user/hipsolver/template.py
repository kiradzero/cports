pkgname = "hipsolver"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DHIP_PLATFORM=amd",
    "-DBUILD_WITH_SPARSE=OFF",
    "-DBUILD_CLIENTS_TESTS=OFF",
    "-DBUILD_CLIENTS_BENCHMARKS=OFF",
    "-DBUILD_CLIENTS_SAMPLES=OFF",
    "-DCMAKE_CXX_COMPILER=hipcc",
    # hipSOLVER enables Fortran bindings by default; use LLVM flang so we
    # stay on the libc++ toolchain (no gfortran/libgcc_s)
    "-DCMAKE_Fortran_COMPILER=flang",
]
hostmakedepends = ["cmake", "flang", "git", "ninja", "rocm-cmake"]
makedepends = [
    "hip-devel",
    "rocblas-devel",
    "rocm-comgr-devel",
    "rocr-runtime-devel",
    "rocsolver-devel",
]
pkgdesc = "ROCm dense linear algebra solver marshalling library"
license = "MIT"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/hipsolver.tar.gz>hipsolver-{pkgver}.tar.gz"
sha256 = "7f99c576b3fd5e6a379e285531dc68ade121918f6d41209ce534d857f421ff39"
# LLVM flang rejects the ubsan integer-hardening flags cbuild puts in the
# shared LDFLAGS (they leak into the Fortran link step); drop int hardening
hardening = ["!int"]
# thin dispatch wrapper, no kernels; tests require amdgpu hardware
options = ["!check", "!lto"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("hipsolver-devel")
def _(self):
    return self.default_devel()
