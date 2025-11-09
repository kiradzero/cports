pkgname = "ghostty"
pkgver = "1.2.2"
pkgrel = 1
hostmakedepends = [
    "blueprint-compiler",
    "glib-devel",
    "libxml2-progs",
    "pkgconf",
    "zvm",
]
makedepends = [
    "fontconfig-devel",
    "freetype-devel",
    "gtk4-devel",
    "gtk4-layer-shell-devel",
    "harfbuzz-devel",
    "libadwaita-devel",
    "libcxx-devel",
    "libcxxabi-devel",
    "linux-headers",
]
pkgdesc = "Fast, native, feature-rich terminal emulator pushing modern features"
license = "MIT"
url = "https://ghostty.org"
source = f"https://github.com/ghostty-org/ghostty/archive/refs/tags/v{
    pkgver}.tar.gz"
sha256 = "1f76d0425dbaf696c44b16715ec8c38890175bd97ca1b46a7d058fb3f7a960e9"
# No tests
options = ["!check"]
_zig_version = "0.14.1"
_build_args = [
    "-Doptimize=ReleaseFast",
    "-Dpie",
    f"-Dversion-string={pkgver}",
    "-fsys=freetype",
    "-fsys=fontconfig",
    "-fsys=harfbuzz",
]


def prepare(self):
    self.do(
        "zvm", "run", _zig_version, "build", *_build_args, allow_network=True
    )


def build(self):
    pass


def install(self):
    self.install_bin(f"zig-out/bin/{pkgname}")
    self.install_license("LICENSE")
    self.install_file(
        "zig-out/share/applications/com.mitchellh.ghostty.desktop",
        "usr/share/applications",
    )
    self.install_file(
        "zig-out/share/icons/hicolor/256x256@2/apps/com.mitchellh.ghostty.png",
        "usr/share/icons/hicolor/256x256/apps",
    )
    self.install_file(
        "zig-out/share/terminfo/g/ghostty", "usr/share/terminfo/g"
    )
    self.install_file(
        "zig-out/share/terminfo/x/xterm-ghostty", "usr/share/terminfo/x"
    )


# @ subpackage("ghostty-terminfo")
# def _(self):
#     self.subdesc = "terminfo data"
#     return ["usr/share/terminfo", ""]
