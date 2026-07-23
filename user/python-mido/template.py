pkgname = "python-mido"
pkgver = "1.3.3"
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
depends = ["python", "python-packaging", "python-setuptools"]
pkgdesc = "Library for working with MIDI messages and port"
license = "MIT"
url = "https://pypi.org/project/mido"
source = f"$(PYPI)/m/mido/mido-{pkgver}.tar.gz"
sha256 = "1aecb30b7f282404f17e43768cbf74a6a31bf22b3b783bdd117a1ce9d22cb74c"
# No check
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
