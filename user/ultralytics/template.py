pkgname = "ultralytics"
pkgver = "8.4.110"
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
sha256 = "088903b7b3c8dea137e065051e3b2b8fa30266d7a97324fe31a260fb2f96e745"
# no pytests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
