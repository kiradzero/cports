pkgname = "rocwmma"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DGPU_TARGETS=gfx1103",
    "-DHIP_PLATFORM=amd",
    "-DCMAKE_CXX_COMPILER=hipcc",
    # tests/samples need hardware and pull rocBLAS/rocm_smi
    "-DROCWMMA_BUILD_TESTS=OFF",
    "-DROCWMMA_BUILD_SAMPLES=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "rocm-cmake", "rocminfo"]
makedepends = [
    "hip-devel",
    "libomp-devel",
    "rocm-comgr-devel",
    "rocr-runtime-devel",
]
depends = ["hip"]
pkgdesc = "AMD ROCm C++ library for warp matrix multiply-accumulate"
license = "MIT"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/rocwmma.tar.gz>rocwmma-{pkgver}.tar.gz"
sha256 = "0d92dad3d7e8a16aa0aca9f09c018412630a81312cb0f8a3dae690aea9856049"
# hipcc resolves clang++ relative to ROCM_PATH; and the fp8 capability check
# try-compiles with -xhip and no --offload-arch, so give hipcc a default
# target (HCC_AMDGPU_TARGET) instead of it shelling out to rocm_agent_enumerator
env = {"ROCM_PATH": "/usr", "HCC_AMDGPU_TARGET": "gfx1103"}
# header-only library, tests need hardware
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
