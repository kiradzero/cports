pkgname = "nwg-look"
pkgver = "1.1.1"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "autoconf",
    "automake",
    "go",
    "pkgconf",
    "xcur2png",
]
makedepends = [
    "cairo-devel",
    "glib-devel",
    "gobject-introspection-devel",
    "gsettings-desktop-schemas-devel",
    "gtk+3-devel",
]
pkgdesc = "GTK settings editor"
license = "MIT"
url = f"https://github.com/nwg-piotr/{pkgname}"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "568c5efe443892d74ffce6cf8ac7db2aea6071be70d97d3ba7c5efd8b351e601"
# No tests
# FIXME lintpixmaps
options = ["!check", "!lintpixmaps"]


def build(self):
    self.do("make", "build")
