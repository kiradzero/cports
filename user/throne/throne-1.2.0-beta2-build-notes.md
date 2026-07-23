## Throne build notes for cports (1.1.6+ / 1.2.0-beta.2)

### Status

- 1.1.6 and 1.2.0-beta.2: build successfully, but SIGSEGV on launch on Chimera (musl)
- 1.0.13: works fine

### SIGSEGV investigation

Symptoms on 1.1.6:
```
server name:  "throne-6DOpHuvmEvJ7ZhnBKLZK7w"
Core stated changed to not running
Core stated changed to not running
SIGSEGV (Address boundary error)
```

Possible causes (musl-related):
1. **cronet/libcronet** — even without `with_naive_outbound` tag, a transitive dep might pull in glibc-linked code
2. **DNS resolver** — musl's `getaddrinfo` behaves differently; Go's CGO resolver can segfault on musl
3. **`with_tailscale` tag** — tailscale has known musl issues with netlink/DNS code

Debugging approach (TODO):
- Build 1.1.6 with tags removed one by one (try dropping `with_tailscale` first)
- Test inside cbuild chroot to avoid breaking the working install
- Check if upstream has musl/Alpine CI or known issues
- Consider filing upstream issue if confirmed musl-specific

### Sources

- 1.1.6: https://github.com/throneproj/Throne/archive/refs/tags/1.1.6.tar.gz
  sha256: 7c4a8fe1b2fc11b3197ecf70a63ff1a583b2ad9858ceedff7fddbbb2f9189efc
- 1.2.0-beta.2: https://github.com/throneproj/Throne/archive/refs/tags/1.2.0-beta.2.tar.gz
  sha256: 06ffd1054dfd78e501a5310e19205d7d3ce3871cd0be84c85ff4a9d25deb66f2

### Key upstream changes from 1.0.x

- `core/protorpc` directory removed (custom protorpc replaced with gRPC stubs)
- Now uses standard `protoc-gen-go-grpc` for service code generation
- dispatch.go uses a custom wire protocol with raw `google.golang.org/protobuf/proto`
- `server` struct embeds `gen.UnimplementedLibcoreServiceServer` (gRPC pattern)

### template.py changes needed (from 1.0.x template)

1. For beta: add `_subver = "-beta.2"` and use `{pkgver}{_subver}` in source URL
2. Remove `go mod tidy` on `core/protorpc` (directory gone)
3. Remove building `protoc-gen-protorpc` (gone)
4. Add `go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest` (separate module, needs network)
5. Update protoc invocation: replace `--protorpc_out/--protorpc_opt` with `--go-grpc_out/--go-grpc_opt`
6. Do NOT add `with_naive_outbound` tag — pulls in libcronet.a which is glibc-only (fails on musl)

### Working pre_build

```python
def pre_build(self):
    from cbuild.util import golang

    goenv = golang.get_go_env(self)
    gobin_chroot = f"{self.chroot_cwd}/bin"

    # Download Go modules
    self.do(
        "go", "mod", "download",
        wrksrc="core/server", allow_network=True, env=goenv,
    )

    # Build protoc-gen-go
    self.do(
        "go", "build", "-v", "-trimpath",
        "-o", f"{gobin_chroot}/protoc-gen-go",
        "google.golang.org/protobuf/cmd/protoc-gen-go",
        wrksrc="core/server", env=goenv,
    )

    # Install protoc-gen-go-grpc (separate module, not in server's go.mod)
    self.do(
        "go", "install",
        "google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest",
        wrksrc="core/server", allow_network=True,
        env={**goenv, "GOBIN": f"{self.chroot_cwd}/bin"},
    )

    # Generate protobuf code
    self.do(
        "protoc", "-I", ".",
        f"--plugin=protoc-gen-go={gobin_chroot}/protoc-gen-go",
        f"--plugin=protoc-gen-go-grpc={gobin_chroot}/protoc-gen-go-grpc",
        "--go_out=.", "--go_opt=paths=source_relative",
        "--go-grpc_out=.", "--go-grpc_opt=paths=source_relative",
        "libcore.proto",
        wrksrc="core/server/gen",
    )
```
