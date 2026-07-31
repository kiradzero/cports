pkgname = "kotlin-lsp"
pkgver = "0.25.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
pkgdesc = "Fast, low-memory LSP server for Kotlin, Java, and Swift"
license = "MIT"
url = f"https://github.com/Hessesian/{pkgname}"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "eb8c48b463ddfcc21cc4c6216b8decbd9ca5c799dabcfff7932c6abe1e506404"
# Fix later
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
