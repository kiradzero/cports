pkgname = "draco"
pkgver = "1.5.7"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DDRACO_TESTS=OFF",
]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf"]
pkgdesc = "Library for compressing and decompressing 3D geometry"
license = "Apache-2.0"
url = "https://google.github.io/draco"
source = f"https://github.com/google/draco/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "bf6b105b79223eab2b86795363dfe5e5356050006a96521477973aba8f036fe1"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("draco-devel")
def _(self):
    return self.default_devel()
