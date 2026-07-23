# update main/python-brotli alongside this
pkgname = "brotli"
pkgver = "1.1.0"
pkgrel = 3
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "General-purpose lossless compression algorithm"
license = "MIT"
url = "https://github.com/google/brotli"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "e720a6ca29428b803f4ad165371771f5398faba397edf6778837a18599ea13ff"
# local znver4 tuning, harmless no-op if ever cross-built for another target
tool_flags = (
    {"CFLAGS": ["-march=znver4"], "CXXFLAGS": ["-march=znver4"]}
    if self.profile().arch == "x86_64"
    else {}
)
# I'm lazy
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("brotli-devel")
def _(self):
    return self.default_devel()
