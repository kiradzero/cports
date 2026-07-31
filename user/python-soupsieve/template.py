pkgname = "python-soupsieve"
pkgver = "2.9.1"
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
sha256 = "c33e6605bbc71dd628b00c632d58ae607c22bade247e52553928f83bbb75b4ba"
# No check
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
