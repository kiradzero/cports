pkgname = "aqlprofile"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DAQLPROFILE_BUILD_TESTS=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["rocr-runtime-devel"]
pkgdesc = "AMD AQL profiling library for HSA runtime API extension"
license = "MIT"
url = "https://github.com/ROCm/rocm-systems"
source = f"{url}/releases/download/rocm-{pkgver}/aqlprofile.tar.gz>aqlprofile-{pkgver}.tar.gz"
sha256 = "ce96a97e2ae5d66f6a783882749f90ec234e9e1c59e3fd8decfc6826cd626a84"
# tests require amdgpu hardware
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
