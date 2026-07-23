pkgname = "python-scikit-build-core"
pkgver = "0.12.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch-vcs",
    "python-hatchling",
    "python-installer",
    "python-vcs-versioning",
]
depends = ["python", "python-packaging", "python-pathspec"]
pkgdesc = "Build backend for CMake-based Python packages"
license = "Apache-2.0"
url = "https://pypi.org/project/scikit-build-core"
source = f"$(PYPI)/s/scikit-build-core/scikit_build_core-{pkgver}.tar.gz"
sha256 = "562e0bbc9de1a354c87825ccf732080268d6582a0200f648e8c4a2dcb1e3736d"
# no .git in sdist -> hatch-vcs can't derive version
env = {"SETUPTOOLS_SCM_PRETEND_VERSION": pkgver}
# No check
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
