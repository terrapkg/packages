%global commit 6b5f28136b9a3467ecedbc2553a19347ac54c887
%global commit_date 20260414
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           uxn-nightly
Version:        1.0^%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        An emulator for the Varvara virtual machine
URL:            https://100r.ca/site/%{name}.html
Source0:        https://git.sr.ht/~rabbits/uxn/archive/%{commit}.tar.gz
License:        MIT
BuildRequires:  SDL2-devel gcc

Packager:       arbormoss <arbormoss@woodsprite.dev>, Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n uxn-%commit

%build
# credit: based on the build script for uxn
# https://git.sr.ht/~rabbits/uxn/tree/1.0/item/build.sh

mkdir -p bin
UXNEMU_LDFLAGS="-L/usr/local/lib $(sdl2-config --cflags --libs)"
CFLAGS="%{build_cflags}"

%{__cc} ${CFLAGS} archive/uxnasm.c %{build_ldflags} -o bin/uxnasm
%dnl %{__cc} ${CFLAGS} src/uxn.c src/devices/system.c src/devices/console.c src/devices/file.c src/devices/datetime.c src/devices/mouse.c src/devices/controller.c src/devices/screen.c src/devices/audio.c src/uxnemu.c ${UXNEMU_LDFLAGS} ${FILE_LDFLAGS} %{build_ldflags} -o bin/uxnemu
%dnl %{__cc} ${CFLAGS} src/uxn.c src/devices/system.c src/devices/console.c src/devices/file.c src/devices/datetime.c src/uxncli.c ${FILE_LDFLAGS} %{build_ldflags} -o bin/uxncli

%install
install -Dm755 bin/uxnasm %{buildroot}%{_bindir}/uxnasm
%dnl install -Dm755 bin/uxncli %{buildroot}%{_bindir}/uxncli
%dnl install -Dm755 bin/uxnemu %{buildroot}%{_bindir}/uxnemu

%files
%doc README.md
%license LICENSE
%{_bindir}/uxnasm
%dnl %{_bindir}/uxncli
%dnl %{_bindir}/uxnemu

%changelog
* Mon Jul 13 2026 Owen Zimmerman <owen@fyralabs.com>
- Adopt nightly package

* Sun Dec 21 2025 arbormoss <arbormoss@woodsprite.dev>
- Intial Commit
