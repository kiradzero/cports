pkgname = "python-diskcache"
pkgver = "5.6.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Disk and file backed cache library"
license = "Apache-2.0"
url = "https://pypi.org/project/diskcache"
source = f"$(PYPI)/d/diskcache/diskcache-{pkgver}.tar.gz"
sha256 = "2c3a3fa2743d8535d832ec61c2054a1641f41775aa7c556758a109941e33e4fc"
# no check
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
