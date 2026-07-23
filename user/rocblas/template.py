pkgname = "rocblas"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DGPU_TARGETS=gfx1103",
    "-DHIP_PLATFORM=amd",
    "-DBUILD_WITH_PIP=OFF",
    "-DBUILD_WITH_HIPBLASLT=OFF",
    "-DBUILD_CLIENTS_TESTS=OFF",
    "-DBUILD_CLIENTS_BENCHMARKS=OFF",
    "-DBUILD_CLIENTS_SAMPLES=OFF",
    "-DTensile_LIBRARY_FORMAT=msgpack",
    "-DCMAKE_CXX_COMPILER=hipcc",
]
hostmakedepends = [
    "cmake",
    "git",
    "ninja",
    "python",
    "python-joblib",
    "python-msgpack",
    "python-pyyaml",
    "rocm-cmake",
    "rocminfo",
    "tensile",
]
makedepends = [
    "hip-devel",
    "llvm-devel",
    "msgpack-cxx",
    "rocm-comgr-devel",
    "rocm-smi-lib-devel",
    "rocr-runtime-devel",
]
depends = ["rocm-device-libs"]
pkgdesc = "AMD ROCm BLAS implementation"
license = "MIT"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/rocblas.tar.gz>rocblas-{pkgver}.tar.gz"
sha256 = "fd909c8ee626be20641d1aad20eec5b1c4535d14d4ba6f488874df230a3b3b04"
# msgpack-cxx built without boost; Tensile only grabs its include dir, not the
# INTERFACE MSGPACK_NO_BOOST define, so set it globally
tool_flags = {"CXXFLAGS": ["-DMSGPACK_NO_BOOST"]}
# tests require amdgpu hardware; foreignelf: ships gfx1103 .hsaco (amdgcn ELF)
options = ["!check", "!lto", "foreignelf"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("rocblas-devel")
def _(self):
    return self.default_devel()
