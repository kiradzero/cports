pkgname = "python-joblib"
pkgver = "1.5.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Lightweight pipelining with Python functions"
license = "BSD-3-Clause"
url = "https://joblib.readthedocs.io"
source = f"$(PYPI_SITE)/j/joblib/joblib-{pkgver}.tar.gz"
sha256 = "8561a3269e6801106863fd0d6d84bb737be9e7631e33aaed3fb9ce5953688da3"
# tests pull in extra deps
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
