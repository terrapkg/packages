# uxn stable has no update script because this version
# is permanently frozen. A nightly will be added once the
# sourcehut versioning script is done.

Name:           uxn
Version:        1.0
Release:        1%?dist
Summary:        An emulator for the Varvara virtual machine
URL:            https://100r.ca/site/%{name}.html
Source0:        https://git.sr.ht/~rabbits/%{name}/archive/%{version}.tar.gz
License:        MIT
BuildRequires:  SDL2-devel gcc

Packager:       arbormoss <arbormoss@woodsprite.dev>

%description
%summary.

%prep
%autosetup -n %name-%version

%build
# credit: based on the build script for uxn
# https://git.sr.ht/~rabbits/uxn/tree/1.0/item/build.sh

mkdir -p bin
UXNEMU_LDFLAGS="-L/usr/local/lib $(sdl2-config --cflags --libs)"
CFLAGS="%{build_cflags}"

%{__cc} ${CFLAGS} src/%{name}asm.c %{build_ldflags} -o bin/%{name}asm
%{__cc} ${CFLAGS} src/%{name}.c src/devices/system.c src/devices/console.c src/devices/file.c src/devices/datetime.c src/devices/mouse.c src/devices/controller.c src/devices/screen.c src/devices/audio.c src/%{name}emu.c ${UXNEMU_LDFLAGS} ${FILE_LDFLAGS} %{build_ldflags} -o bin/%{name}emu
%{__cc} ${CFLAGS} src/%{name}.c src/devices/system.c src/devices/console.c src/devices/file.c src/devices/datetime.c src/%{name}cli.c ${FILE_LDFLAGS} %{build_ldflags} -o bin/%{name}cli

%install
install -Dm755 bin/%{name}asm %{buildroot}%{_bindir}/%{name}asm
install -Dm755 bin/%{name}cli %{buildroot}%{_bindir}/%{name}cli
install -Dm755 bin/%{name}emu %{buildroot}%{_bindir}/%{name}emu

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}asm
%{_bindir}/%{name}cli
%{_bindir}/%{name}emu

%changelog
* Sun Dec 21 2025 arbormoss <arbormoss@woodsprite.dev>
- Intial Commit
