pkgname = "rocm-comgr"
pkgver = "7.2.4"
pkgrel = 0
build_wrksrc = "amd/comgr"
build_style = "cmake"
configure_args = [
    "-DCMAKE_STRIP=",
    "-DCOMGR_DISABLE_SPIRV=ON",
    "-DBUILD_TESTING=OFF",
]
hostmakedepends = ["cmake", "ninja", "python"]
makedepends = [
    "clang-devel",
    "clang-tools-extra",
    "libedit-devel",
    "libffi8-devel",
    "libxml2-devel",
    "lld-devel",
    "llvm-devel",
    "rocm-device-libs",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
depends = ["rocm-device-libs"]
pkgdesc = "AMD ROCm code object manager"
license = "NCSA"
url = "https://github.com/ROCm/llvm-project"
source = (
    f"{url}/archive/refs/tags/rocm-{pkgver}.tar.gz"
    f">llvm-project-rocm-{pkgver}.tar.gz"
)
sha256 = "526b5fe23417c41acbeb2273e470887b4593f48a297a8d9c1a1aa730d556f9fb"
# tests need a functional hip toolchain (circular)
options = ["!check"]


def post_patch(self):
    cwd = self.cwd / "amd/comgr"
    # opencl headers come from the system clang resource dir
    fp = cwd / "cmake/opencl_header.cmake"
    fp.write_text(
        fp.read_text().replace(
            "${CLANG_CMAKE_DIR}/../../../*", "/usr/lib/clang/22/include"
        )
    )
    # llvm-22 API backports from amd-staging
    fp = cwd / "src/comgr-compiler.cpp"
    fp.write_text(
        fp.read_text()
        .replace("Driver/Options.h", "Options/Options.h")
        .replace("clang::driver::options", "clang::options")
        .replace("Driver::GetResourcesPath", "GetResourcesPath")
    )


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("rocm-comgr-devel")
def _(self):
    return self.default_devel()
