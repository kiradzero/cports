pkgname = "ultralytics"
pkgver = "8.4.114"
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
sha256 = "d6351aec0ef2a256cfad7693b745cf1224398d30bf32e1ff1ddd6441ac0f31c0"
# no pytests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
