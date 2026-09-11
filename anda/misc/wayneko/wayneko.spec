%global _distro_extra_cflags -Wno-sign-compare

%global commit 0d0d917a174deadcb6f1f56f96be38052fa76d97
%global shortcommit %{sub %{commit} 0 7}
%global commitdate 20260623

Name:           wayneko
Version:        0~%{commitdate}.git%{shortcommit}
Release:        1%{?dist}
Summary:        Neko on Wayland
License:        GPL-3.0-or-later

BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  wayland-devel
BuildRequires:  /usr/bin/wayland-scanner
BuildRequires:  make
BuildRequires:  gcc

Packager:       Olivia <git@olivia.sh>

URL:        https://git.sr.ht/~leon_plickat/wayneko

Source:     %{url}/archive/%{commit}.tar.gz
Patch0000:  0000-append-to-cflags-in-makefile.patch

%description
Display an animated neko cat on the bottom of an output. Requires the Wayland
server to implement zwlr-layer-shell-unstable-v1.  All code is licensed under
the GPLv3. The neko bitmaps were taken from public domain.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
%make_build

%install
%make_install BASHCOMPDIR=%{bash_completions_dir} ZSHCOMPDIR=%{zsh_completions_dir} BINDIR=%{_bindir} MANDIR=%{_mandir} DESTDIR=%{buildroot}

%pkg_completion -Bz

%files
%license LICENSE
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Sat Aug 15 2026 Olivia <git@olivia.sh> - 0~20260623.git6330dd1-1
- Initial package
