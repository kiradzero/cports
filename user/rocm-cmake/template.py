pkgname = "rocm-cmake"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
depends = ["cmake", "rocm-core"]
pkgdesc = "CMake modules for the ROCm software stack"
license = "MIT"
url = "https://github.com/ROCm/rocm-cmake"
source = f"{url}/archive/refs/tags/rocm-{pkgver}.tar.gz"
sha256 = "e7a28cb4baf8afbc21204d37e132dae7e12b2d980a2600948fe35cc4d8ac8087"
# tests need rocm-llvm (circular) and network
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
