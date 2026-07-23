pkgname = "niri-float-sticky"
pkgver = "0.0.8"
pkgrel = 0
build_style = "go"
hostmakedepends = [
    "go",
]
depends = [
    "niri",
]
pkgdesc = (
    "Utility to make floating windows visible across all workspaces in niri"
)
license = "MIT"
url = f"https://github.com/probeldev/{pkgname}"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2d011b9b08a7efb4f8da2a19e22d81f55d193ee1b170913f46177b903c8a6aed"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
