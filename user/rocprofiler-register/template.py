pkgname = "rocprofiler-register"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # project rejects cbuild's default CMAKE_BUILD_TYPE=None
    "-DCMAKE_BUILD_TYPE=Release",
    "-DROCPROFILER_REGISTER_BUILD_FMT=OFF",
    "-DROCPROFILER_REGISTER_BUILD_GLOG=OFF",
    "-DROCPROFILER_REGISTER_BUILD_TESTS=OFF",
    "-DROCPROFILER_REGISTER_BUILD_SAMPLES=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["fmt-devel", "glog-devel"]
pkgdesc = "AMD ROCm profiler registration library"
license = "MIT"
url = "https://github.com/ROCm/rocm-systems"
source = f"{url}/releases/download/rocm-{pkgver}/rocprofiler-register.tar.gz>rocprofiler-register-{pkgver}.tar.gz"
sha256 = "e20ecbd5da6a18263c082b21e4a3be8b0040650a258a442ff86ee1616545db27"
# tests require amdgpu hardware
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("rocprofiler-register-devel")
def _(self):
    return self.default_devel()
