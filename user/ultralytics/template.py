pkgname = "ultralytics"
pkgver = "8.4.103"
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
sha256 = "bfd423cf74f9be902d4688fd1fbbafac5c7097330a8c1e7e4ced3b45aa633793"
# no pytests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
