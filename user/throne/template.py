pkgname = "throne"
pkgver = "1.1.6"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE=Release"]
hostmakedepends = [
    "cmake",
    "curl",
    "go",
    "iputils",
    "ninja",
    "pkgconf",
    "protobuf-protoc",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Cross-platform GUI proxy utility"
license = "GPL-3.0-or-later"
url = "https://github.com/throneproj/Throne"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7c4a8fe1b2fc11b3197ecf70a63ff1a583b2ad9858ceedff7fddbbb2f9189efc"
# no tests
# cross: needs host protoc/moc
options = ["!check", "!cross"]


def post_extract(self):
    # Download srslist.h that cmake expects
    self.do(
        "curl",
        "-L",
        "-o",
        "srslist.h",
        "https://github.com/throneproj/routeprofiles/raw/refs/heads/rule-set/srslist.h",
        allow_network=True,
    )


def pre_build(self):
    from cbuild.util import golang

    goenv = golang.get_go_env(self)
    gobin_chroot = f"{self.chroot_cwd}/bin"

    # Download Go modules
    self.do(
        "go",
        "mod",
        "download",
        wrksrc="core/server",
        allow_network=True,
        env=goenv,
    )

    # Build protoc-gen-go
    self.do(
        "go",
        "build",
        "-v",
        "-trimpath",
        "-o",
        f"{gobin_chroot}/protoc-gen-go",
        "google.golang.org/protobuf/cmd/protoc-gen-go",
        wrksrc="core/server",
        env=goenv,
    )

    # Install protoc-gen-go-grpc (separate module, not in server's go.mod)
    self.do(
        "go",
        "install",
        "google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest",
        wrksrc="core/server",
        allow_network=True,
        env={**goenv, "GOBIN": f"{self.chroot_cwd}/bin"},
    )

    # Generate protobuf code
    self.do(
        "protoc",
        "-I",
        ".",
        f"--plugin=protoc-gen-go={gobin_chroot}/protoc-gen-go",
        f"--plugin=protoc-gen-go-grpc={gobin_chroot}/protoc-gen-go-grpc",
        "--go_out=.",
        "--go_opt=paths=source_relative",
        "--go-grpc_out=.",
        "--go-grpc_opt=paths=source_relative",
        "libcore.proto",
        wrksrc="core/server/gen",
    )


def post_build(self):
    from cbuild.util import golang

    goenv = golang.get_go_env(self)

    # Get sing-box version
    singboxver = (
        self.do(
            "go",
            "list",
            "-m",
            "-f",
            "{{.Version}}",
            "github.com/sagernet/sing-box",
            wrksrc="core/server",
            capture_output=True,
            env=goenv,
        )
        .stdout.decode()
        .strip()
    )

    ldflags = [
        "-linkmode=external",
        "-w",
        "-s",
        f"-X github.com/sagernet/sing-box/constant.Version={singboxver}",
    ]

    tags = [
        "with_clash_api",
        "with_gvisor",
        "with_quic",
        "with_wireguard",
        "with_utls",
        "with_dhcp",
        "with_tailscale",
    ]

    # Build Core component
    self.do(
        "go",
        "build",
        "-v",
        "-trimpath",
        "-buildmode=pie",
        "-mod=readonly",
        "-modcacherw",
        "-o",
        f"{self.chroot_cwd}/{self.make_dir}/Core",
        f"-ldflags={' '.join(ldflags)}",
        f"-tags={','.join(tags)}",
        wrksrc="core/server",
        env=goenv,
    )


def install(self):
    # Create app directory
    self.install_dir(throne_dir := f"usr/lib/{pkgname}")

    # Install binaries
    self.install_file(f"{self.make_dir}/Throne", throne_dir)
    self.install_file(f"{self.make_dir}/Core", throne_dir)

    # Install wrapper script
    self.install_bin(f"{self.files_path}/{pkgname}.sh", name=pkgname)

    # Install desktop file and icon
    self.install_file(
        "res/public/Throne.png",
        "usr/share/icons/hicolor/256x256/apps",
        name=f"{pkgname}.png",
    )

    self.install_file(
        f"{self.files_path}/{pkgname}.desktop", "usr/share/applications"
    )
