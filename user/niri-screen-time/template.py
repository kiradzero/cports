pkgname = "niri-screen-time"
pkgver = "0.0.17"
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
sha256 = "6fb3293ae53fd22ba70ff573a5ccc0a5a7a52fde52692058a1bad38f138527d3"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
