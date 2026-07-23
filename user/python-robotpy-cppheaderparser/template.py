pkgname = "python-robotpy-cppheaderparser"
pkgver = "5.1.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools-scm",
    "python-vcs-versioning",
    "python-wheel",
]
depends = ["python-ply"]
pkgdesc = "Python parser for C++ headers"
license = "BSD-3-Clause"
url = "https://github.com/robotpy/robotpy-cppheaderparser"
source = f"$(PYPI_SITE)/r/robotpy-cppheaderparser/robotpy-cppheaderparser-{pkgver}.tar.gz"
sha256 = "15d350b39358b45cdb1fe138af9efcce0e632c1b58830a1ba1ba098a1752698b"
# no tests in sdist
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
