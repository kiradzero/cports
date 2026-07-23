pkgname = "zstd"
pkgver = "1.5.7"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Db_ndebug=true",
    "-Dbin_contrib=true",
    "-Dbin_tests=true",
    "-Dlz4=enabled",
    "-Dlzma=enabled",
    "-Dzlib=enabled",
]
make_dir = "mbuild"
meson_dir = "build/meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["lz4-devel", "xz-devel", "zlib-ng-compat-devel"]
renames = ["libzstd"]
pkgdesc = "Zstd compression utilities"
license = "BSD-3-Clause"
url = "http://www.zstd.net"
source = f"https://github.com/facebook/zstd/releases/download/v{pkgver}/zstd-{pkgver}.tar.gz"
sha256 = "eb33e51f49a15e023950cd7825ca74a4a2b43db8354825ac24fc1b7ee09e6fa3"
# local znver4 tuning, harmless no-op if ever cross-built for another target
tool_flags = (
    {"CFLAGS": ["-march=znver4"], "CXXFLAGS": ["-march=znver4"]}
    if self.profile().arch == "x86_64"
    else {}
)
compression = "deflate"
hardening = ["!vis", "!cfi"]
# needs gtest
options = ["!check"]


def build(self):
    self.do("make", f"-j{self.make_jobs}", "PREFIX=/usr", "lib-mt")
    self.do(
        "make",
        f"-j{self.make_jobs}",
        "PREFIX=/usr",
        "-C",
        "programs",
        "zstd-dll",
        "LIB_BINDIR=../lib",
    )
    self.do("make", f"-j{self.make_jobs}", "PREFIX=/usr", "-C", "contrib/pzstd")


def install(self):
    self.do("make", "PREFIX=/usr", f"DESTDIR={self.chroot_destdir}", "install")
    self.do(
        "make",
        "-C",
        "contrib/pzstd",
        "PREFIX=/usr",
        f"DESTDIR={self.chroot_destdir}",
        "install",
    )
    self.install_license("LICENSE")
    for tool in ["zstdgrep", "zstdless"]:
        self.uninstall(f"usr/bin/{tool}")
        self.uninstall(f"usr/share/man/man1/{tool}.1")


@subpackage("zstd-progs")
def _(self):
    self.install_if = [self.parent]

    return self.default_progs()


@subpackage("zstd-devel")
def _(self):
    self.provides = [self.with_pkgver("libzstd-devel")]

    return self.default_devel()
