pkgname = "cardinal"
pkgver = "26.02"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["cmake", "pkgconf", "python"]
makedepends = [
    "dbus-devel",
    "fftw-devel",
    "file-devel",
    "jansson-devel",
    "libarchive-devel",
    "liblo-devel",
    "libsamplerate-devel",
    "libsndfile-devel",
    "libx11-devel",
    "libxcursor-devel",
    "libxext-devel",
    "libxrandr-devel",
    "mesa-devel",
    "speexdsp-devel",
]
depends = [
    "jansson",
    "libarchive",
    "libsamplerate",
    "python",
    "speexdsp",
]
pkgdesc = "Free and open-source virtual modular synthesizer plugin"
license = "GPL-3.0-only"
url = f"https://github.com/DISTRHO/{pkgname}"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "24c76b22f9999f133d64f703dd4dc9e87954c27a02043e2f08c8819cc8632373"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
