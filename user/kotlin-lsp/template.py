pkgname = "kotlin-lsp"
pkgver = "0.24.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
pkgdesc = "Fast, low-memory LSP server for Kotlin, Java, and Swift"
license = "MIT"
url = f"https://github.com/Hessesian/{pkgname}"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6eecf8a8778da95e87854e1503a1efb8545bd39fecfefbf9c93557ef78bb1871"
# Fix later
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
