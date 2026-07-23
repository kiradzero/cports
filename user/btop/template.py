pkgname = "btop"
pkgver = "1.4.7"
pkgrel = 2
build_style = "cmake"
configure_args = ["-DBTOP_LTO=OFF", "-DBTOP_FORTIFY=OFF"]
hostmakedepends = ["cmake", "ninja", "lowdown"]
makedepends = ["linux-headers"]
checkdepends = ["gtest-devel"]
pkgdesc = "TUI monitor of system resources"
license = "Apache-2.0"
url = "https://github.com/aristocratos/btop"
source = f"{url}/archive/v{pkgver}/btop-{pkgver}.tar.gz"
sha256 = "933de2e4d1b2211a638be463eb6e8616891bfba73aef5d38060bd8319baeefc6"
# cfi-icall trips on the GPU backends: rsmi/nvml symbols are dlsym'd
# and called through casted function pointers (SIGILL on gpu init)
hardening = ["vis"]
