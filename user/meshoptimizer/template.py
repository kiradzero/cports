pkgname = "meshoptimizer"
pkgver = "1.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DMESHOPT_BUILD_SHARED_LIBS=ON",
]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Mesh optimization library"
license = "MIT"
url = "https://github.com/zeux/meshoptimizer"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e40f71b809cdf3361b9a4def85fd44534e8733ce29d4b943c145b76859e4c2b4"


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("meshoptimizer-devel")
def _(self):
    # the shared lib has no soname (upstream doesn't set MESHOPT_SOVERSION),
    # so take_devel() can't auto-derive a so: dependency on the base pkg
    self.depends = [self.with_pkgver("meshoptimizer")]
    return self.default_devel()
