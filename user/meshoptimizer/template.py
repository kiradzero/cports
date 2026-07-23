pkgname = "meshoptimizer"
pkgver = "1.1"
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
sha256 = "b787011f81b4b3069c2f9065b7c191efdd4189a49be32ba5282dd5579f05261a"


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("meshoptimizer-devel")
def _(self):
    # the shared lib has no soname (upstream doesn't set MESHOPT_SOVERSION),
    # so take_devel() can't auto-derive a so: dependency on the base pkg
    self.depends = [self.with_pkgver("meshoptimizer")]
    return self.default_devel()
