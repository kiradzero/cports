pkgname = "blender"
pkgver = "5.2.0"
pkgrel = 1
_gpu_target = "gfx1103"
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-C",
    # predefined config with everything we want
    "../build_files/cmake/config/blender_full.cmake",
    # OSL only ever activates on the cpu/optix devices (has_osl is unset for
    # hip in device/hip/device.cpp), so on a hip-only setup scene.cpp always
    # falls back to SVM regardless of this flag; skip the OSL/LLVM/Clang
    # chain entirely since it can never do anything here
    "-DWITH_CYCLES_OSL=OFF",
    # no nvidia hardware and no cuda toolchain: without nvcc these only build
    # dead host stubs, and cuew probes libcuda via dlopen on every startup
    "-DWITH_CYCLES_DEVICE_CUDA=OFF",
    "-DWITH_CYCLES_DEVICE_OPTIX=OFF",
    "-DWITH_CLANG=OFF",
    "-DWITH_INSTALL_PORTABLE=OFF",
    "-DWITH_LIBS_PRECOMPILED=OFF",
    "-DWITH_LLVM=OFF",
    "-DWITH_PYTHON_INSTALL=OFF",
    "-DWITH_PYTHON_INSTALL_NUMPY=OFF",
    "-DWITH_PYTHON_INSTALL_REQUESTS=OFF",
    "-DWITH_PYTHON_INSTALL_ZSTANDARD=OFF",
    "-DWITH_SYSTEM_EIGEN3=ON",
    "-DWITH_SYSTEM_GFLAGS=ON",
    "-DWITH_SYSTEM_GLOG=ON",
    "-DWITH_SYSTEM_FREETYPE=ON",
    "-DWITH_SYSTEM_LZO=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "openimageio-progs",
    "pkgconf",
]
makedepends = [
    "alembic-devel",
    "boost-devel",
    "ceres-devel",
    "draco-devel",
    "draco-devel-static",  # cmake target draco::draco_static always expected
    "eigen",
    "ffmpeg-devel",
    "fftw-devel",
    "fmt-devel",
    "freetype-devel",
    "gmp-gmpxx-devel",
    "libepoxy-devel",
    "libharu-devel",
    "libjpeg-turbo-devel",
    "libomp-devel",
    "libpng-devel",
    "libpulse-devel",
    "libsndfile-devel",
    "libtiff-devel",
    "libwebp-devel",
    "libxkbcommon-devel",
    "meshoptimizer-devel",
    "onetbb-devel",
    "openal-soft-devel",
    "opencolorio-devel",
    "openexr-devel",
    "openimageio-devel",
    "openjpeg-devel",
    "opensubdiv-devel",
    "openvdb-devel",
    "pipewire-jack-devel",
    "potrace-devel",
    "pugixml-devel",
    "python-devel",
    "python-numpy-devel",
    "shaderc-devel",
    "vulkan-loader-devel",
    "wayland-devel",
    "wayland-protocols",
    "zstd-devel",
]
depends = [
    "python-numpy",
    "python-requests",
    "python-zstandard",
]
pkgdesc = "3D creation suite"
license = "GPL-2.0-or-later"
url = "https://www.blender.org"
source = f"https://download.blender.org/source/blender-{pkgver}.tar.xz"
sha256 = "a5f99fc5fabf5062e661ca55d70987ae8f08d33324ac4865f133bbed7498d7bf"
tool_flags = {
    "CFLAGS": ["-D_GNU_SOURCE"],
    # guilty until proven innocent
    "LDFLAGS": ["-Wl,-z,stack-size=0x200000"],
}
# var-init seems to pessimise a large stack-reuse optimisation, so repeatedly
# using a large chunk of stack via onetbb causes memset calls where otherwise
# there would be none and it makes rendering 5x slower
hardening = ["!int", "!var-init"]
# tests expect blender to be installed in /usr/bin
options = ["!check", "linkundefver"]

if self.profile().endian == "big":
    broken = "https://projects.blender.org/blender/blender/pulls/140138"

if self.profile().arch in ["aarch64", "armv7", "x86_64"]:
    makedepends += ["openimagedenoise-devel"]
    configure_args += ["-DWITH_OPENIMAGEDENOISE=ON"]
else:
    configure_args += ["-DWITH_OPENIMAGEDENOISE=OFF"]

if self.profile().arch in ["aarch64", "x86_64"]:
    makedepends += [
        "embree-devel",
        "openpgl-devel",
    ]
    configure_args += ["-DWITH_CYCLES_EMBREE=ON", "-DWITH_PATH_GUIDING=ON"]
else:
    configure_args += [
        "-DWITH_CYCLES=OFF",
        "-DWITH_CYCLES_EMBREE=OFF",
        "-DWITH_PATH_GUIDING=OFF",
    ]

if self.profile().arch == "x86_64":
    # cycles renders on the 780M through hip, and hiprt adds the hardware ray
    # tracing path on top of it. only the one arch is built: each entry in
    # CYCLES_HIP_BINARIES_ARCH is a separate full kernel compile
    configure_args += [
        "-DWITH_CYCLES_DEVICE_HIP=ON",
        "-DWITH_CYCLES_HIP_BINARIES=ON",
        "-DWITH_CYCLES_DEVICE_HIPRT=ON",
        f"-DCYCLES_HIP_BINARIES_ARCH={_gpu_target}",
        "-DHIP_ROOT_DIR=/usr",
        "-DHIPRT_ROOT_DIR=/usr",
    ]
    hostmakedepends += ["hipcc"]
    makedepends += ["hip-devel", "hiprt-devel"]
    # both are dlopened (hipew/hiprtew), so the solib scan cannot see them
    depends += ["hip", "hiprt"]
    # local build for this machine: cycles' own cpu kernels carry their own
    # -mavx2 flags and dispatch at runtime, so this is only for the rest of
    # blender (mesh ops, sculpt, depsgraph), which has no dispatch at all
    tool_flags["CFLAGS"] += ["-march=x86-64-v3", "-mtune=znver4"]
    tool_flags["CXXFLAGS"] = ["-march=x86-64-v3", "-mtune=znver4"]


def post_patch(self):
    # -parallel-jobs is an AMD clang-fork flag; hipcc drives the system clang
    # here, which rejects it outright. it only splits codegen across threads
    fp = self.cwd / "intern/cycles/kernel/device/hiprt/CMakeLists.txt"
    fp.write_text(
        fp.read_text().replace(
            "    -parallel-jobs=${HIPRT_COMPILER_PARALLEL_JOBS}\n", ""
        )
    )


def init_configure(self):
    self.configure_args += [f"-DPYTHON_VERSION={self.python_version}"]


def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/share/blender")
