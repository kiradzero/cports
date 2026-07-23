pkgname = "composable-kernel"
pkgver = "7.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # GPU_ARCHS (not GPU_TARGETS) also short-circuits the example/test/
    # tile_engine subdirs, leaving just the instance library + profiler
    "-DGPU_ARCHS=gfx1103",
    "-DCMAKE_CXX_COMPILER=hipcc",
    "-DHIP_PLATFORM=amd",
    # clang-tidy/cppcheck on every instance TU makes the build glacial
    "-DENABLE_CLANG_CPP_CHECKS=OFF",
    "-DBUILD_TESTING=OFF",
    "-DCK_USE_CODEGEN=OFF",
    # gfx1103 has no fp8/bf8 hardware and fp64 is not useful on consumer
    # RDNA; skipping those instances cuts the build substantially
    "-DDTYPES=fp16;bf16;fp32;int8",
]
hostmakedepends = [
    "cmake",
    "git",
    "ninja",
    "pkgconf",
    "python",
    "rocm-cmake",
    "rocminfo",
]
makedepends = ["hip-devel", "rocm-comgr-devel", "rocr-runtime-devel"]
pkgdesc = "AMD ROCm performance-portable device operation primitives"
license = "MIT"
url = "https://github.com/ROCm/rocm-libraries"
source = f"{url}/releases/download/rocm-{pkgver}/composablekernel.tar.gz>composable-kernel-{pkgver}.tar.gz"
sha256 = "ace080bd7a0cbd4abb94d515d9bf08158aa8d5e94901730b71403000192b2dfa"
# hipcc needs ROCM_PATH to find clang++; HCC_AMDGPU_TARGET gives no-arch
# probe compiles a default target
env = {"ROCM_PATH": "/usr", "HCC_AMDGPU_TARGET": "gfx1103"}
# ships gfx1103 device code; no test phase
options = ["!check", "foreignelf"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("composable-kernel-devel")
def _(self):
    return self.default_devel()
