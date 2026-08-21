pkgname = "python-soupsieve"
pkgver = "2.9.2"
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
sha256 = "4a55d8cf158a9c2e587fa4922f1bbb91d68ac829e2d6f25403a85747c71daf74"
# No check
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
