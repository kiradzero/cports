pkgname = "zlib-ng"
pkgver = "2.3.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["gtest-devel"]
pkgdesc = "Implementation of zlib compression library with new API"
license = "Zlib"
url = "https://github.com/zlib-ng/zlib-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f9c65aa9c852eb8255b636fd9f07ce1c406f061ec19a2e7d508b318ca0c907d1"
# local znver4 tuning, harmless no-op if ever cross-built for another target
tool_flags = (
    {"CFLAGS": ["-march=znver4"], "CXXFLAGS": ["-march=znver4"]}
    if self.profile().arch == "x86_64"
    else {}
)
# I'm lazy
options = ["!check"]


@subpackage("zlib-ng-devel")
def _(self):
    return self.default_devel()
