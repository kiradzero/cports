pkgname = "python-vcs-versioning"
pkgver = "1.1.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python", "python-packaging", "python-setuptools"]
pkgdesc = "Manage versions by scm tags via setuptools"
license = "MIT"
url = "https://pypi.org/project/vcs-versioning"
source = f"$(PYPI)/v/vcs-versioning/vcs_versioning-{pkgver}.tar.gz"
sha256 = "fabd75a3cab7dd8ac02fe24a3a9ba936bf258667b5a62ed468c9a1da0f5775bc"
# No check
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
