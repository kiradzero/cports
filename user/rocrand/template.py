pkgname = "rocrand"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DGPU_TARGETS=gfx1103",
    "-DHIP_PLATFORM=amd",
    "-DBUILD_TEST=OFF",
    "-DBUILD_BENCHMARK=OFF",
    "-DBUILD_FORTRAN_WRAPPER=OFF",
    "-DCMAKE_CXX_COMPILER=hipcc",
]
hostmakedepends = ["cmake", "git", "ninja", "rocm-cmake"]
makedepends = ["hip-devel", "rocm-comgr-devel", "rocr-runtime-devel"]
pkgdesc = "ROCm random number generator library"
license = "MIT"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/rocrand.tar.gz>rocrand-{pkgver}.tar.gz"
sha256 = "9b5ddd4ac403e5c1199728750234c37386effbf648aff873910c6f3299beadaf"
# rocRAND forces ENV{ROCM_PATH}=/opt/rocm when unset, sending hipcc to look
# for /opt/rocm/bin/clang++; pin it to our prefix so hipcc finds /usr/bin/clang++
env = {"ROCM_PATH": "/usr"}
# tests require amdgpu hardware; ships gfx1103 device code (foreign ELF)
options = ["!check", "!lto", "foreignelf"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("rocrand-devel")
def _(self):
    return self.default_devel()
