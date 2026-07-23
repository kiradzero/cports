pkgname = "ktx-software"
pkgver = "4.4.2"
pkgrel = 0
# not supported by the bundled cputypetest.cmake arch detection
archs = ["*", "!riscv64", "!loongarch64"]
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DKTX_FEATURE_TESTS=OFF",
    "-DKTX_FEATURE_TOOLS=ON",
    "-DKTX_FEATURE_TOOLS_CTS=OFF",
    "-DKTX_FEATURE_LOADTEST_APPS=OFF",
    "-DKTX_FEATURE_DOC=OFF",
    "-DKTX_FEATURE_JNI=OFF",
    "-DKTX_FEATURE_PY=OFF",
    f"-DKTX_GIT_VERSION_FULL=v{pkgver}",
]
hostmakedepends = ["cmake", "ninja", "bash"]
pkgdesc = "Library and tools for the KTX texture container format"
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/KTX-Software"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9412cb45045a503005acd47d98f9e8b47154634a50b4df21e17a1dfa8971d323"


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("ktx-software-progs")
def _(self):
    return self.default_progs()


@subpackage("ktx-software-devel")
def _(self):
    return self.default_devel()
