pkgname = "python-markdownify"
pkgver = "1.2.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools-scm",
    "python-vcs-versioning",
    "python-wheel",
]
depends = ["python", "python-packaging", "python-setuptools"]
pkgdesc = "Library that converts HTML to Markdown"
license = "MIT"
url = "https://pypi.org/project/markdownify"
source = f"$(PYPI)/m/markdownify/markdownify-{pkgver}.tar.gz"
sha256 = "1a176f05522c8a2cb1dd3ab9d307dcdadbed5c26ae717855bfc42b3b6d38d937"
# No check
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
