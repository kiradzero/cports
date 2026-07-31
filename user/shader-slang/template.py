pkgname = "shader-slang"
pkgver = "2026.14.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    f"-DSLANG_VERSION_NUMERIC={pkgver}",
    f"-DSLANG_VERSION_FULL={pkgver}",
    "-DSLANG_ENABLE_CUDA=OFF",
    "-DSLANG_ENABLE_DXIL=OFF",
    "-DSLANG_ENABLE_EXAMPLES=OFF",
    "-DSLANG_ENABLE_GFX=OFF",
    "-DSLANG_ENABLE_OPTIX=OFF",
    "-DSLANG_ENABLE_REPLAYER=OFF",
    "-DSLANG_ENABLE_SLANG_GLSLANG=ON",
    "-DSLANG_ENABLE_SLANG_PROXY=OFF",
    "-DSLANG_ENABLE_SLANG_RHI=OFF",
    "-DSLANG_ENABLE_SLANGC=ON",
    "-DSLANG_ENABLE_SLANGD=ON",
    "-DSLANG_ENABLE_SLANGI=OFF",
    "-DSLANG_ENABLE_SLANGRT=ON",
    "-DSLANG_ENABLE_TESTS=OFF",
    "-DSLANG_ENABLE_XLIB=OFF",
    "-DSLANG_EXCLUDE_TINT=ON",
    "-DSLANG_SLANG_LLVM_FLAVOR=DISABLE",
    "-DSLANG_STANDARD_MODULE_DEVELOP_BUILD=OFF",
    "-DSLANG_USE_SYSTEM_LZ4=ON",
    "-DSLANG_USE_SYSTEM_VULKAN_HEADERS=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python"]
makedepends = ["lz4-devel", "vulkan-headers"]
pkgdesc = "Shader language and compiler"
license = "Apache-2.0 WITH LLVM-exception"
url = "https://shader-slang.org"
_commit_glslang = "d1f52c8993a501bd52d4fbd044bfeb9ecdceb9f4"
_commit_spirv_tools = "0d6fd73ca73830ccab5fa1f00ed5ed40124e2c55"
_commit_spirv_headers = "29981f65241605e08b0ede4cfeb999fe3b723c6a"
_commit_unordered_dense = "73f3cbb237e84d483afafc743f1f14ec53e12314"
_commit_miniz = "6ef6c68f4fcbb8287aa8edf9c6670804932f41c6"
_commit_lua = "3fe7be956f23385aa1950dc31e2f25127ccfc0ea"
_commit_cmark = "924936d0427cb25a61169739a7660230bffa6ea6"
_commit_fast_float = "e0b53eaf63c6d00e0725788ef1dbb759aa321d79"
source = [
    f"https://github.com/shader-slang/slang/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/KhronosGroup/glslang/archive/{_commit_glslang}.tar.gz",
    f"https://github.com/KhronosGroup/SPIRV-Tools/archive/{_commit_spirv_tools}.tar.gz",
    f"https://github.com/KhronosGroup/SPIRV-Headers/archive/{_commit_spirv_headers}.tar.gz",
    f"https://github.com/martinus/unordered_dense/archive/{_commit_unordered_dense}.tar.gz",
    f"https://github.com/richgel999/miniz/archive/{_commit_miniz}.tar.gz",
    f"https://github.com/lua/lua/archive/{_commit_lua}.tar.gz",
    f"https://github.com/swiftlang/swift-cmark/archive/{_commit_cmark}.tar.gz",
    f"https://github.com/fastfloat/fast_float/archive/{_commit_fast_float}.tar.gz",
]
source_paths = [
    ".",
    "external/glslang",
    "external/spirv-tools",
    "external/spirv-headers",
    "external/unordered_dense",
    "external/miniz",
    "external/lua",
    "external/cmark",
    "external/fast_float",
]
sha256 = [
    "2198fa78c65a97118b0b2d4ba63567fa420f02777c3e61a2cc43c4e24268d9e5",
    "d914157124abcec9e7d3bd8ba99f023d4cada87e67f38a3b76e4b70c15fd2c07",
    "20219c0962dffb0d7644bb3116a5923cfcf0526a569baa0b2a17343dd2fa6e5d",
    "232899f1ad4104fb5bc377b94596c7621575eee62ad9a9e8f929b63a7dd8a7ad",
    "16188ed4804a670f6b00637a53e135190668dddc12b10f5233e20b403b9df9e2",
    "d9ef3c09f98b0dba3aa60e520284ed54042b0baa86116312be3f36e26393ae27",
    "4776526f89abeea61cce41a056577859180dbb2d4cb6c1dad00955872a1007bb",
    "1c51659bd47c34df1c8976f893adc43ba039a98f6eac4fa95d53d1e08ba6072a",
    "f6259a3543e75ae705ec80835d1568622b444d389922dcc314af7250c26e8643",
]
tool_flags = (
    {"CFLAGS": ["-march=znver4"], "CXXFLAGS": ["-march=znver4"]}
    if self.profile().arch == "x86_64"
    else {}
)
# The upstream test suite requires slang-rhi and graphics APIs.
options = ["!check", "!cross"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("shader-slang-devel")
def _(self):
    return self.default_devel()
