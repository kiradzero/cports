pkgname = "python-hatch-vcs"
pkgver = "0.5.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-hatchling"]
depends = ["python", "python-hatchling", "python-setuptools-scm"]
pkgdesc = "Hatch plugin for versioning with your SCM"
license = "MIT"
url = "https://pypi.org/project/hatch-vcs"
source = f"$(PYPI)/h/hatch-vcs/hatch_vcs-{pkgver}.tar.gz"
sha256 = "0395fa126940340215090c344a2bf4e2a77bcbe7daab16f41b37b98c95809ff9"
# No check
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
