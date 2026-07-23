pkgname = "python-soupsieve"
pkgver = "2.9"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python", "python-packaging", "python-setuptools"]
pkgdesc = "CSS selector library designed to be used with Beautiful Soup 4"
license = "MIT"
url = "https://pypi.org/project/soupsieve"
source = f"$(PYPI)/s/soupsieve/soupsieve-{pkgver}.tar.gz"
sha256 = "acee8417325c5653e1377dc31eccad59eb82cbc65942afe6174c53b3aaad63fc"
# No check
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
