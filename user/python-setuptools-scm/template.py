pkgname = "python-setuptools-scm"
pkgver = "10.0.5"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-vcs-versioning",
    "python-wheel",
]
depends = ["python", "python-packaging", "python-setuptools"]
pkgdesc = "Manage versions by scm tags via setuptools"
license = "MIT"
url = "https://pypi.org/project/setuptools-scm"
source = f"$(PYPI)/s/setuptools-scm/setuptools_scm-{pkgver}.tar.gz"
sha256 = "bbba8fe754516cdefd017f4456721775e6ef9662bd7887fb52ae26813d4838c3"
# No check
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
