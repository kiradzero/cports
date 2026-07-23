pkgname = "python-beautifulsoup4"
pkgver = "4.15.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python", "python-packaging", "python-setuptools"]
pkgdesc = "Library that makes it easy to scrape information from web pages"
license = "MIT"
url = "https://pypi.org/project/beautifulsoup4"
source = f"$(PYPI)/b/beautifulsoup4/beautifulsoup4-{pkgver}.tar.gz"
sha256 = "288e3ca7d54b06f2ac191970bc275c1939cb46d450b255bf6718b04aa37ab4f7"
# No check
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
