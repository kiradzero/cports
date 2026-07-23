pkgname = "libfaketime"
pkgver = "0.9.12"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "autoconf",
    "automake",
    "pkgconf",
]
makedepends = [
    "musl-devel",
]
pkgdesc = "Retrieve thecurrent date and time"
license = "GPL-2.0-only"
url = f"https://github.com/wolfcw/{pkgname}"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4fc32218697c052adcdc5ee395581f2554ca56d086ac817ced2be0d6f1f8a9fa"
# No tests
options = ["!check"]


def build(self):
    env = {
        "CFLAGS": " -pthread",
        "LDFLAGS": " -pthread",
    }
    self.do("make", "-C", "src", "all", env=env)
