pkgname = "ghostty"
pkgver = "1.4.0"
pkgrel = 0
hostmakedepends = [
    "blueprint-compiler",
    "glib-devel",
    "libxml2-progs",
    "ncurses",
    "pkgconf",
    "zvm",
]
makedepends = [
    "fontconfig-devel",
    "freetype-devel",
    "glslang-devel",
    "gtk4-devel",
    "gtk4-layer-shell-devel",
    "harfbuzz-devel",
    "highway-devel",
    "libadwaita-devel",
    "libcxx-devel",
    "libcxxabi-devel",
    "libpng-devel",
    "linux-headers",
    "oniguruma-devel",
    "zlib-ng-devel",
]
pkgdesc = "Fast, native, feature-rich terminal emulator pushing modern \
features"
license = "MIT"
url = "https://ghostty.org"
source = "https://github.com/ghostty-org/ghostty/archive/refs/tags/tip.tar.gz"

sha256 = "10227bcb510ab707cd515a7f39145ead56bcf8f82a64af5e608912eeb63b1400"
# No tests
options = ["!check"]
_zig_version = "0.16.1"
_build_args = [
    "-Doptimize=ReleaseFast",
    "-Dpie",
    f"-Dversion-string={pkgver}",
    "-Dcpu=native",
    "-fsys=fontconfig",
    "-fsys=freetype",
    "-fsys=glslang",
    "-fsys=gtk4-layer-shell",
    "-fsys=harfbuzz",
    "-fsys=highway",
    "-fsys=libpng",
    "-fsys=oniguruma",
    "-fsys=zlib",
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
