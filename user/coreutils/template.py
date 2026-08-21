pkgname = "coreutils"
# git snapshot of main (0.9.0 + openssl feature); date = commit date
pkgver = "0.10.0"
pkgrel = 0
_commit = "3ceaab508f7178947cbaf7e806a70bb4905f8378"
build_style = "cargo"
# unix feature set (chown, chmod, nice, stdbuf, ...) on top of the core
# utils; openssl speeds up the checksum utils via system libcrypto (cbuild
# sets OPENSSL_NO_VENDOR=1 globally, so it never links statically)
make_build_args = ["--features", "unix,openssl"]
make_install_args = ["--features", "unix,openssl"]
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["oniguruma-devel", "openssl3-devel"]
pkgdesc = "Cross-platform reimplementation of the GNU coreutils in Rust"
license = "MIT"
url = "https://github.com/uutils/coreutils"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "74bf3c06b1d7f3586d954de21b68411a8e366bddbdd2e2f3534d1fd09b9c55fe"
# no tests defined
options = ["!check", "etcfiles"]


def post_build(self):
    # documentation generator, used to emit manpages/completions on install
    self.cargo.build(args=["--bin", "uudoc", "--features", "uudoc"])


def post_install(self):
    self.install_license("LICENSE")
    # uu- prefixed symlinks so the utilities can coexist with chimerautils;
    # the multicall binary dispatches on the argv[0] suffix
    progs = (
        self.do(
            self.chroot_destdir / "usr/bin/coreutils",
            "--list",
            capture_output=True,
        )
        .stdout.decode()
        .split()
    )
    self.install_dir("usr/lib/uutils/bin")
    for prog in progs:
        self.install_link(f"usr/bin/uu-{prog}", "coreutils")
        # unprefixed names in a separate dir; prepended to PATH via the
        # profile.d/fish snippets so they take priority over chimerautils
        self.install_link(
            f"usr/lib/uutils/bin/{prog}", "../../../bin/coreutils"
        )
    self.install_file(self.files_path / "uutils.sh", "etc/profile.d")
    self.install_file(
        self.files_path / "uutils.fish", "usr/share/fish/vendor_conf.d"
    )
    # manpages and fish completions for the uu- prefixed names (the
    # unprefixed ones would clash with chimerautils/fish's own files)
    uudoc = f"target/{self.profile().triplet}/release/uudoc"
    self.install_dir("usr/share/man/man1")
    self.install_dir("usr/share/fish/vendor_completions.d")
    for prog in progs:
        ret = self.do(
            uudoc,
            "manpage",
            prog,
            env={"PROG_PREFIX": "uu-"},
            capture_output=True,
            check=False,
        )
        if ret.returncode == 0 and ret.stdout:
            (self.destdir / f"usr/share/man/man1/uu-{prog}.1").write_bytes(
                ret.stdout
            )
        ret = self.do(
            uudoc,
            "completion",
            prog,
            "fish",
            env={"PROG_PREFIX": "uu-"},
            capture_output=True,
            check=False,
        )
        if ret.returncode == 0 and ret.stdout:
            (
                self.destdir
                / f"usr/share/fish/vendor_completions.d/uu-{prog}.fish"
            ).write_bytes(ret.stdout)
