pkgname = "noctalia-shell"
pkgver = "4.7.7"
pkgrel = 2
depends = [
    "brightnessctl",
    "ffmpeg",
    "imagemagick",
    "noctalia-qs",
    "qt6-qtmultimedia",
    "wlr-randr",
]
pkgdesc = "Sleek and minimal desktop shell thoughtfully crafted for Wayland"
license = "MIT"
url = f"https://github.com/noctalia-dev/{pkgname}"
source = f"{url}/releases/download/v{pkgver}/noctalia-latest.tar.gz"
sha256 = "28a5087eef327fbe3ea7fd436bfad41216cb10278d10c3893feb460fbce46c08"
# No tests
options = ["!check"]


def install(self):
    dest = "etc/xdg/quickshell/noctalia-shell"

    self.install_dir(dest)

    sources = [
        "shell.qml",
        "lefthook.yml",
        "Assets",
        "Commons",
        "Helpers",
        "Modules",
        "Scripts",
        "Services",
        "Shaders",
        "Widgets",
    ]

    for src in sources:
        self.install_files(src, dest)


def post_install(self):
    self.install_license("LICENSE")
