pkgname = "roctracer"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DROCM_PATH=/usr",
    "-DHIP_PLATFORM=amd",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python",
    "python-robotpy-cppheaderparser",
]
makedepends = [
    "hip-devel",
    "rocm-comgr-devel",
    "rocr-runtime-devel",
]
pkgdesc = "AMD ROCm tracer callback and activity APIs"
license = "MIT"
url = "https://github.com/ROCm/rocm-systems"
source = f"{url}/releases/download/rocm-{pkgver}/roctracer.tar.gz>roctracer-{pkgver}.tar.gz"
sha256 = "81149a68ad3424d9db0b177ba40c9e03903ad4d297477f76b860ba5b7ec66847"
# tests require amdgpu hardware
options = ["!check"]


def post_patch(self):
    # libc++ has no <experimental/filesystem> and no stdc++fs library
    for f in [
        "src/hip_stats/hip_stats.cpp",
        "src/roctracer/loader.h",
        "src/tracer_tool/tracer_tool.cpp",
        "plugin/file/file.cpp",
    ]:
        fp = self.cwd / f
        fp.write_text(
            fp.read_text()
            .replace("<experimental/filesystem>", "<filesystem>")
            .replace("std::experimental::filesystem", "std::filesystem")
        )
    for f in ["src/CMakeLists.txt", "plugin/file/CMakeLists.txt"]:
        fp = self.cwd / f
        fp.write_text(fp.read_text().replace(" stdc++fs", ""))


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("roctracer-devel")
def _(self):
    return self.default_devel()
