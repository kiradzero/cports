pkgname = "hip"
pkgver = "7.2.4"
pkgrel = 6
build_style = "cmake"
configure_args = [
    "-DCLR_BUILD_HIP=ON",
    "-DHIP_PLATFORM=amd",
    "-DROCM_PATH=/usr",
    # empty so the install does not grab hipcc; the hipcc package ships it
    "-DHIPCC_BIN_DIR=",
    "-DHIP_LLVM_ROOT=/usr",
    # needs roctracer + CppHeaderParser; revisit when packaging rocprofiler
    "-DUSE_PROF_API=OFF",
    "-DHIP_ENABLE_ROCPROFILER_REGISTER=OFF",
]
hostmakedepends = ["bash", "cmake", "ninja", "perl", "python"]
makedepends = [
    "clang-devel",
    "lld-devel",
    "llvm-devel",
    "mesa-devel",
    "rocm-comgr-devel",
    "rocm-core-devel",
    "rocr-runtime-devel",
]
# comgr is dlopened (COMGR_DYN_DLL), not linked
depends = ["rocm-comgr", "rocm-device-libs"]
pkgdesc = "AMD HIP runtime"
license = "MIT"
url = "https://github.com/ROCm/rocm-systems"
source = [
    f"{url}/releases/download/rocm-{pkgver}/clr.tar.gz>clr-{pkgver}.tar.gz",
    f"{url}/releases/download/rocm-{pkgver}/hip.tar.gz>hip-{pkgver}.tar.gz",
]
source_paths = [".", "hipsrc"]
sha256 = [
    "c9670697ee47b2d33dde84e4c815a62f594061da9ff184b133b87a227a1a1f02",
    "76c3d6909e531f30b84c908984891559d221d8c427d44abc88be5dbb123f9ad6",
]
# local znver4 tuning, harmless no-op if ever cross-built for another target
tool_flags = (
    {
        "CFLAGS": ["-mtune=znver4", "-march=znver4"],
        "CXXFLAGS": ["-mtune=znver4", "-march=znver4"],
    }
    if self.profile().arch == "x86_64"
    else {}
)
# tests require amdgpu hardware
options = ["!check"]

# version script lists hiprtc symbols that live in libhiprtc
# clr's thread-local device/context tracking defaults to the initial-exec TLS
# model, which is only valid for objects present at process startup; musl
# (unlike glibc) refuses to relocate IE TLS for anything dlopen()'d later,
# and every optional-HIP consumer (blender's hipew, ...) does exactly that
tool_flags = {
    "LDFLAGS": ["-Wl,--undefined-version"],
    "CFLAGS": ["-ftls-model=global-dynamic"],
    "CXXFLAGS": ["-ftls-model=global-dynamic"],
}


def post_patch(self):
    # musl declares basename only in libgen.h
    fp = self.cwd / "rocclr/os/os_posix.cpp"
    fp.write_text(
        fp.read_text().replace(
            "#include <unistd.h>",
            "#include <libgen.h>\n#include <unistd.h>",
            1,
        )
    )
    # the "__local" macro clobbers a private identifier libc++ uses in
    # <ranges> (join_view), breaking any HIP TU that pulls in nlohmann/json
    # or other C++20 range code; inline the attribute so no macro leaks
    fp = self.cwd / "hipamd/include/hip/amd_detail/device_library_decls.h"
    fp.write_text(
        fp.read_text()
        .replace("#define __local __attribute__((address_space(3)))\n", "")
        .replace(
            "__local void* __to_local(unsigned x) { return (__local void*)x; }",
            "__attribute__((address_space(3))) void* __to_local(unsigned x) "
            "{ return (__attribute__((address_space(3))) void*)x; }",
        )
    )
    # rocclr pins these two thread-locals to initial-exec explicitly, which
    # overrides -ftls-model; musl refuses IE TLS in dlopen()'d objects, so the
    # attribute has to go from the source, not just the flags
    for f in [
        "rocclr/platform/activity.hpp",
        "rocclr/platform/activity.cpp",
        "rocclr/thread/thread.cpp",
        "rocclr/thread/thread.hpp",
    ]:
        fp = self.cwd / f
        fp.write_text(
            fp.read_text().replace(
                ' __attribute__((tls_model("initial-exec")))', ""
            )
        )
    # the HIP-language cmake config hardcodes -unwindlib=libgcc for the link
    # step; Chimera (musl) has no libgcc_s and pairs compiler-rt with
    # libunwind, so any project using LANGUAGES HIP fails to link
    fp = self.cwd / "hipsrc/hip-lang-config.cmake.in"
    fp.write_text(
        fp.read_text().replace("-unwindlib=libgcc", "-unwindlib=libunwind")
    )


def init_configure(self):
    self.configure_args.append(f"-DHIP_COMMON_DIR={self.chroot_cwd / 'hipsrc'}")


def post_install(self):
    # windows leftovers
    for f in (self.destdir / "usr/bin").glob("*.bat"):
        f.unlink()
    self.install_license("LICENSE.md")


@subpackage("hip-devel")
def _(self):
    self.depends += ["hipcc"]
    return self.default_devel()
