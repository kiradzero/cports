pkgname = "ultralytics"
pkgver = "8.4.123"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["libusb", "python"]
pkgdesc = "Ultralytics YOLO for SOTA object detection"
license = "BSD-3-Clause"
url = "https://github.com/ultralytics/ultralytics"
source = f"$(PYPI)/u/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "f78055bf72fb5804bf5b43a0aee0f22e173f133411441807a9eb4fbb3bec7358"
# no pytests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
