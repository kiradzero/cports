pkgname = "python-typing-extensions"
pkgver = "4.15.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-flit-core"]
depends = ["python"]
pkgdesc = "Backported and experimental type hints for Python"
license = "PSF-2.0"
url = "https://pypi.org/project/typing-extensions"
source = f"$(PYPI)/t/typing-extensions/typing_extensions-{pkgver}.tar.gz"
sha256 = "0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466"
# No check
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
