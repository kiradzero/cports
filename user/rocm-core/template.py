pkgname = "rocm-core"
pkgver = "6.4.1"
pkgrel = 0
build_style = "cmake"
# configure_args = [
#     "-DCMAKE_BUILD_TYPE=None",
#     "-DCMAKE_SHARED_LIBS=ON",
#     "-DCMAKE_INSTALL_PREFIX=/opt/rocm",
#     f"-DROCM_VERSION='{pkgver}'",
# ]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "AMD ROCm core package"
subdesc = "version files"
license = "MIT"
url = (
    f"https://github.com/ROCm/{pkgver}/archive/refs/tags/rocm-{pkgver}.tar.gz"
)


def install(self):
    self.install_dir(rocm_dir := f"usr/libs/{pkgname}")
