pkgname = "tensile"
pkgver = "4.45.0"
pkgrel = 0
_rocmver = "7.2.4"
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python",
    "python-joblib",
    "python-msgpack",
    "python-pyyaml",
    "python-rich",
]
pkgdesc = "Auto-tuning tool for GEMMs and tensor contractions on GPUs"
license = "MIT"
url = "https://github.com/ROCm/rocm-libraries"
source = (
    f"{url}/releases/download/rocm-{_rocmver}/tensile.tar.gz"
    f">tensile-{pkgver}.tar.gz"
)
sha256 = "3d31f46117a5d982d01032c2fed65eae5a3c26b33d496acb9cd19f60d107cce9"
# no python tests (require GPU + amdgpu asm)
options = ["!check", "!lto"]


def post_install(self):
    self.install_license("LICENSE.md")
