pkgname = "xcur2png"
pkgver = "0.7.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf",
    "automake",
    "pkgconf",
]
makedepends = [
    "libpng-devel",
    "libxcursor-devel",
]
pkgdesc = "Program to take PNG image from X cursor"
license = "GPL-3.0-only"
url = f"https://github.com/eworm-de/{pkgname}"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3874e8bd4f287dbd8b6d4a16ee1f450970965fd773288d85bb53143e2e631add"
# no tests
options = ["!check"]
