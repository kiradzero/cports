pkgname = "niri-screen-time"
pkgver = "0.0.16"
pkgrel = 0
build_style = "go"
hostmakedepends = [
    "go",
]
depends = [
    "niri",
]
pkgdesc = "Niri screen time tracker"
license = "MIT"
url = f"https://github.com/probeldev/{pkgname}"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e3884c78562ddf3f0c2fb11215f40edb34b05906ee6604fc60065d652d16a6c2"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
