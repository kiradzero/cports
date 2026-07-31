pkgname = "ghostty"
pkgver = "1.4.0"
pkgrel = 0
hostmakedepends = [
    "blueprint-compiler",
    "glib-devel",
    "libxml2-progs",
    "ncurses",
    "pkgconf",
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
_zigver = "0.16.0"
source = [
    "https://github.com/ghostty-org/ghostty/archive/refs/tags/tip.tar.gz",
    f"https://ziglang.org/download/{_zigver}/zig-x86_64-linux-{_zigver}.tar.xz",
]
source_paths = ["", "zig-toolchain"]
sha256 = [
    "4a5afdd273bd4bf4ee15ce3c4b817245b3a3b57b124ae34d4f7e366d71fa2c12",
    "70e49664a74374b48b51e6f3fdfbf437f6395d42509050588bd49abe52ba3d00",
]
# No tests
options = ["!check"]

_zig_env = {
    "ZIG_LOCAL_CACHE_DIR": "zig-cache",
    "ZIG_GLOBAL_CACHE_DIR": "zig-global-cache",
}
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
    # cbuild propagates proxy variables after merging env; Zig's HTTP client
    # cannot download packages through the local proxy, so unset them here.
    self.do(
        "env",
        "-u",
        "HTTP_PROXY",
        "-u",
        "HTTPS_PROXY",
        "-u",
        "SOCKS_PROXY",
        self.chroot_srcdir / "zig-toolchain/zig",
        "build",
        *_build_args,
        env=_zig_env,
        path=[self.chroot_srcdir / "zig-toolchain"],
        allow_network=True,
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
