pkgname = "opencode"
pkgver = "1.18.18"
pkgrel = 0
archs = ["x86_64", "aarch64"]
pkgdesc = "AI coding agent built for the terminal"
license = "MIT"
url = "https://opencode.ai"
# prebuilt, self-contained musl binary (bun --compile bundles the runtime
# and the whole TypeScript app into one executable); building from source
# would require bun, which is not packaged for Chimera
_gh = "https://github.com/sst/opencode"

# per-arch release asset + its checksum
_asset = None
_sha = None
match self.profile().arch:
    case "x86_64":
        _asset = "opencode-linux-x64-musl"
        _sha = (
            "b6cb242a989387cd79d5f9b742f24dccda2537e4938d413cbea5b3c88ac6085a"
        )
    case "aarch64":
        _asset = "opencode-linux-arm64-musl"
        _sha = (
            "fea148fcd748d5b137a5c09ce03e03c17310f72797a8e4170debc33ae535c0dd"
        )

source = [
    f"{_gh}/releases/download/v{pkgver}/{_asset}.tar.gz",
    f"{_gh}/raw/v{pkgver}/LICENSE>opencode-LICENSE.txt",
]
sha256 = [
    _sha,
    "625f0f619133f89bbbb2abe37369613dfa1885eba1e50d02170deb62bb42cb6b",
]
# foreign prebuilt binary: it's a bun --compile executable that appends the
# JS bundle after the ELF, so stripping would corrupt it
options = ["!strip", "foreignelf", "!check", "!lto"]


def install(self):
    self.install_bin("opencode")
    self.install_license("opencode-LICENSE.txt")
