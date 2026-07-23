pkgname = "hiprt"
pkgver = "2.5.0_git20250425"
pkgrel = 0
_commit = "606b4886efabce918dd0634ef71c06615a47c83b"
# hiprt bakes major * 1000 + minor into its library name, and blender both
# parses this out of hiprt.h and dlopens the unversioned alias; keep in sync
# with version.txt
_libver = "02005"
_gpu_targets = ["gfx1103"]
build_style = "cmake"
configure_args = [
    "-DHIP_PATH=/usr",
    # the kernel artifact paths are built as dist/bin/${CMAKE_BUILD_TYPE}, so
    # cbuild's default of None makes the build look for them in dist/bin/None
    "-DCMAKE_BUILD_TYPE=Release",
    # bake the precompiled kernels into the solib instead of shipping loose
    # hipfb next to it; this is the combination blender builds and tests
    "-DBITCODE=OFF",
    "-DBAKE_COMPILED_KERNEL=ON",
    "-DGENERATE_BAKE_KERNEL=OFF",
    "-DPRECOMPILE=ON",
    "-DFORCE_DISABLE_CUDA=ON",
    "-DNO_UNITTEST=ON",
]
hostmakedepends = ["cmake", "hipcc", "ninja", "python"]
makedepends = ["hip-devel"]
# loaded via dlopen (hiprt_libpath.h), not linked
depends = ["hip"]
pkgdesc = "AMD HIP ray tracing library"
license = "MIT"
url = "https://github.com/GPUOpen-LibrariesAndSDKs/HIPRT"
source = f"{url}/archive/{_commit}.tar.gz>hiprt-{_commit}.tar.gz"
sha256 = "13fa34959e9efcbb684ed78a65a7cead52ddf3b773cf2052c69cdffc0475c288"
# ROCM_PATH so hipcc resolves clang++ under /usr instead of /opt/rocm, and a
# default arch so it never shells out to rocm_agent_enumerator (no hardware
# probe in the sandbox); same recipe as rocrand/rocwmma
env = {"ROCM_PATH": "/usr", "HCC_AMDGPU_TARGET": _gpu_targets[0]}
# unit tests require amdgpu hardware
options = ["!check"]


def post_patch(self):
    # compile.py hardcodes every gfx target hiprt has ever supported (~28 of
    # them) with no way to narrow it down, and each one is a full kernel
    # compile; keep only what we actually build for
    fp = self.cwd / "scripts/bitcodes/common_tools.py"
    targets = ", ".join(map(lambda a: f"'{a}'", _gpu_targets))
    src = fp.read_text()
    start = src.index("    gpus_archs = [")
    end = src.index("return gpus_archs", start)
    fp.write_text(
        src[:start] + f"    gpus_archs = [{targets}]\n\n    " + src[end:]
    )
    # -parallel-jobs only exists in AMD's clang fork; hipcc here drives the
    # system clang, which rejects it outright. it just splits codegen across
    # threads, so dropping it costs build time and nothing else
    fp = self.cwd / "scripts/bitcodes/compile.py"
    fp.write_text(
        fp.read_text().replace("-parallel-jobs=' + str(parallel_jobs) + '", "")
    )
    fp = self.cwd / "scripts/bitcodes/precompile_bitcode.py"
    fp.write_text(fp.read_text().replace("-parallel-jobs=15 ", ""))


def post_install(self):
    self.install_license("license.txt")
    # upstream drops the solib in bin; blender (and anything else linking it)
    # expects a normal library location
    self.install_dir("usr/lib")
    self.rename(
        f"usr/bin/libhiprt{_libver}64.so",
        f"usr/lib/libhiprt{_libver}64.so",
        relative=False,
    )
    # cycles dlopens the unversioned name at runtime, and blender's FindHIPRT
    # looks for it first, so it belongs next to the runtime library
    self.install_link("usr/lib/libhiprt64.so", f"libhiprt{_libver}64.so")


@subpackage("hiprt-devel")
def _(self):
    # the solib is dlopened rather than linked, so it stays in the main
    # package; only headers are devel material
    self.depends = [f"hiprt={pkgver}-r{pkgrel}"]
    return ["usr/include"]
