pkgname = "hfanc"
pkgver = "1.0.1"
pkgrel = 1
# the module refuses to load on anything but a HONOR MagicBook BRI-XX
archs = ["x86_64"]
# nothing is compiled against it; it is here so the service file's targets
# resolve to a provider when the dinit dependencies are scanned
makedepends = ["dinit-chimera"]
pkgdesc = "Fan control for the HONOR MagicBook BRI-XX"
license = "GPL-2.0-only AND MIT"
url = "https://github.com/kiradzero/hfac"
# The upstream zig package is a 0.17 master snapshot built against the system
# LLVM 22; hfanc needs the 0.16.0 release, which wants LLVM 21 and so cannot be
# built here. The second source is the official 0.16.0 linux build -- static,
# self-contained, and used only to compile this one program.
_zigver = "0.16.0"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz>{pkgname}-{pkgver}.tar.gz",
    f"https://ziglang.org/download/{_zigver}/zig-x86_64-linux-{_zigver}.tar.xz",
]
source_paths = ["", "zig-toolchain"]
sha256 = [
    "a643913dd6fada9707b748143042c46988ccdd755e478c1708ae4923602d8e72",
    "70e49664a74374b48b51e6f3fdfbf437f6395d42509050588bd49abe52ba3d00",
]

# zig writes to ~/.cache by default; keep both caches inside the build
# directory so nothing escapes the sandbox and a rebuild starts clean.
_zig_env = {
    "ZIG_LOCAL_CACHE_DIR": "zig-cache",
    "ZIG_GLOBAL_CACHE_DIR": "zig-global-cache",
}


def _zig(self, *args):
    self.do(self.chroot_srcdir / "zig-toolchain/zig", *args, env=_zig_env)


def build(self):
    # ReleaseSafe, not ReleaseFast: this program steers a fan, and a checked
    # panic that hands control back to the firmware beats undefined behaviour.
    _zig(self, "build", "-Doptimize=ReleaseSafe")


def check(self):
    # No test touches the machine; the policy is pure functions over fixtures.
    _zig(self, "build", "test")


def install(self):
    self.install_bin("zig-out/bin/hfanc")
    self.install_service(self.files_path / "hfanc")
    # The die-temperature watchdog prefers the acpitz thermal zone, which
    # thermal.ko must register first; this is the ordering hint that says so.
    self.install_file(
        "kernel/honor-ec-fan.modprobe.conf",
        "usr/lib/modprobe.d",
        name="honor-ec-fan.conf",
    )
    # The service refuses to start without the module, so autoloading it is
    # part of the package rather than something left to the administrator.
    self.install_file(
        self.files_path / "modules-load.conf",
        "usr/lib/modules-load.d",
        name="honor_ec_fan.conf",
    )
    self.install_license("LICENSE")
    self.install_file("README.md", f"usr/share/doc/{pkgname}")
    self.install_file("docs/Architecture.md", f"usr/share/doc/{pkgname}")

    # Only these three files belong in the ckms tree: handing ckms the whole
    # kernel directory also hands it build artifacts, and it then finds
    # everything up to date and registers a module it never built.
    destp = f"usr/src/honor_ec_fan-{pkgver}"
    self.install_file(
        self.files_path / "ckms.ini", destp, template={"VERSION": pkgver}
    )
    self.install_file("kernel/Makefile", destp)
    self.install_file("kernel/honor_ec_fan.c", destp)


@subpackage("hfanc-ckms")
def _(self):
    self.subdesc = "kernel sources"
    self.install_if = [self.parent, "ckms"]
    self.depends = [
        self.parent,
        "ckms",
        "gmake",
    ]

    return ["usr/src"]
