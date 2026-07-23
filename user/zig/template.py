pkgname = "zig"
pkgver = "0.17.0_git20260712"
pkgrel = 1
# master snapshot from ziglang.org CI builds (needs LLVM 22, matching system)
_dev_ver = "0.17.0-dev.1397+4331ba0fb"
build_style = "cmake"
configure_args = [
    # dodge -Dstrip
    "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
    "-DZIG_PIE=ON",
    "-DZIG_SHARED_LLVM=ON",
    "-DZIG_TARGET_MCPU=znver4",
    # tarball has no .git for version detection
    f"-DZIG_VERSION={_dev_ver}",
]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "clang-devel",
    "linux-headers",
    "lld-devel",
    "llvm-devel",
    "ncurses-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Zig programming language toolchain"
license = "MIT"
url = "https://github.com/ziglang/zig"
source = f"https://ziglang.org/builds/zig-{_dev_ver}.tar.xz"
sha256 = "9484a2c540b25e695db8a382b6b832568b42b52a8a74518889bed805c0261c99"
# lighten up the build, only applies to bootstrap and just slows down the build
tool_flags = {"CFLAGS": ["-U_FORTIFY_SOURCE"]}
hardening = ["!int", "!scp", "!ssp", "!var-init"]
options = ["!lto"]

match self.profile().arch:
    case "x86_64" | "aarch64":
        pass
    case _:
        # disable tests on other archs, a lot of them fail
        options += ["!check"]


def check(self):
    # the full "test" suite takes hours on master and its elf2-dynamic
    # standalone tests always fail inside the sandbox; run a compact
    # sanity subset instead (compiler unit tests + sema/codegen cases + fmt)
    self.do(
        self.make_dir + "/stage3/bin/zig",
        "build",
        "test-unit",
        "test-cases",
        "test-fmt",
        "--summary",
        "all",
        # tarball has no .git; build.zig fails resolving the version without this
        f"-Dversion-string={_dev_ver}",
        "-Dcpu=baseline",
        "-Dskip-debug",
        "-Dskip-non-native",
        "-Dskip-release-safe",
        "-Dskip-release-small",
    )


def install(self):
    self.install_license("LICENSE")
    self.install_files(f"{self.make_dir}/stage3/bin", "usr")
    self.install_files(f"{self.make_dir}/stage3/lib", "usr")
