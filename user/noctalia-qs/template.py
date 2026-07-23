pkgname = "noctalia-qs"
pkgver = "0.0.12"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DNO_PCH=ON",
]
hostmakedepends = [
    "cli11",
    "cmake",
    "ninja",
    "pkgconf",
    "qt6-qtshadertools",
    "spirv-tools",
]
makedepends = [
    "hicolor-icon-theme-devel",
    "jemalloc-devel",
    "libdrm-devel",
    "libxcb-devel",
    "linux-pam-devel",
    "mesa-devel",
    "pipewire-devel",
    "polkit-devel",
    "qt6-qtbase-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwayland-devel",
    "vulkan-headers",
    "wayland-devel",
    "wayland-protocols",
]
depends = [
    "hicolor-icon-theme",
    "jemalloc",
    "libdrm",
    "libxcb",
    "linux-pam",
    "mesa",
    "pipewire",
    "polkit",
    "qt6-qtbase",
    "qt6-qtdeclarative",
    "qt6-qtsvg",
    "qt6-qtwayland",
    "wayland",
]
pkgdesc = "Sleek and minimal desktop shell thoughtfully crafted for Wayland"
license = "LGPL-3.0-only"
url = f"https://github.com/noctalia-dev/{pkgname}"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5de37541537307d141618aa0d782d3c34e42a6ad21c73533cce80c0e71ee9693"
# it does not have any tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
