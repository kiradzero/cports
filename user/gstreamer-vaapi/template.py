pkgname = "gstreamer-vaapi"
pkgver = "1.26.11"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--auto-features=enabled",
    "-Ddefault_library=shared",
    # misc
    "-Ddoc=disabled",
]
make_check_args = ["--timeout-multiplier=5"]
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "gst-plugins-bad-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "libva-devel",
    "libxrandr-devel",
    "wayland-protocols",
]
pkgdesc = "GStreamer VA-API plugins"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/gstreamer-vaapi/gstreamer-vaapi-{pkgver}.tar.xz"
sha256 = "f12f930273c7a1d3e0d7f85b94ff9d1379d162accc932e8ca3d38993ed27fcac"
