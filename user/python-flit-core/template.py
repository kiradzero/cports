pkgname = "python-flit-core"
pkgver = "3.12.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer"]
depends = ["python"]
pkgdesc = "Distribution-building parts of Flit"
license = "BSD-3-Clause"
url = "https://pypi.org/project/flit-core"
source = f"$(PYPI)/f/flit-core/flit_core-{pkgver}.tar.gz"
sha256 = "18f63100d6f94385c6ed57a72073443e1a71a4acb4339491615d0f16d6ff01b2"
# No check
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
