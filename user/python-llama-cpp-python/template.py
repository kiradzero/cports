pkgname = "python-llama-cpp-python"
pkgver = "0.3.28"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "cmake",
    "git",
    "glslang",
    "ninja",
    "pkgconf",
    "python-build",
    "python-installer",
    "python-scikit-build-core",
    "shaderc-progs",
]
makedepends = [
    "libomp-devel",
    "linux-headers",
    "spirv-headers",
    "vulkan-headers",
    "vulkan-loader-devel",
]
depends = [
    "python",
    "python-diskcache",
    "python-jinja2",
    "python-numpy",
    "python-typing-extensions",
]
pkgdesc = "Python bindings for llama.cpp with Vulkan backend"
license = "MIT"
url = "https://pypi.org/project/llama-cpp-python"
# MUST be the PyPI sdist: it vendors llama.cpp. The GitHub archive omits the
# submodule and the build will fail.
source = f"$(PYPI)/l/llama-cpp-python/llama_cpp_python-{pkgver}.tar.gz"
sha256 = "958227b394f413425d6039952096daa0b8b98328c6b99d652862aec775f1672d"
env = {"CMAKE_ARGS": "-DGGML_VULKAN=ON -DLLAVA_BUILD=OFF -DGGML_NATIVE=ON"}
# GPU/host-tool build; upstream tests need model files
options = ["!check", "!cross", "!scanshlibs"]


def post_install(self):
    pyver = next((self.destdir / "usr/lib").glob("python3*")).name
    sp = f">/usr/lib/{pyver}/site-packages"
    # scikit-build-core additionally dumps a redundant C-dev install
    # (headers, cmake/pkgconfig, duplicate .so) at the platlib root. The
    # binding loads its libs from llama_cpp/lib, so drop the duplicate tree —
    # this clears the lint rule (bare `lib` is a forbidden site-packages child)
    self.rm(f"{sp}/lib", recursive=True, force=True)
    self.rm(f"{sp}/include", recursive=True, force=True)
    self.install_license("LICENSE.md")
