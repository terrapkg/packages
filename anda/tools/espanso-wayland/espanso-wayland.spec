Name:			espanso-wayland
Version: 		2.2.1
Release:		2%?dist
Summary:		Cross-platform Text Expander written in Rust for Wayland
License:		GPL-3.0
URL:			https://espanso.org
Source0:		https://github.com/espanso/espanso/archive/refs/tags/v%version.tar.gz
Requires:		libxkbcommon dbus libnotify wxGTK wl-clipboard
Conflicts:		espanso-x11
BuildRequires:	anda-srpm-macros cargo-rpm-macros gcc gcc-c++
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	wxGTK-devel
BuildRequires:	openssl-devel

%description
A cross-platform Text Expander written in Rust. A text expander is a program
that detects when you type a specific keyword and replaces it with something
else.

This package includes the Wayland version of espanso.


%prep
%autosetup -n espanso-%version
cd espanso
%cargo_prep_online

%build
cd espanso
%cargo_build -n -f vendored-tls,"wayland" -- --package={espanso,espanso-clipboard,espanso-config,espanso-detect,espanso-engine,espanso-info,espanso-inject,espanso-ipc,espanso-kvs,espanso-mac-utils,espanso-match,espanso-migrate,espanso-modulo,espanso-package,espanso-path,espanso-render,espanso-ui}

%install
mkdir -p %buildroot%_bindir
install -Dm755 target/rpm/espanso %buildroot%_bindir

%files
%caps(cap_dac_override=pe) %_bindir/espanso

%changelog
%autochangelog
