Name:			espanso-x11
Version: 		2.2.1
Release:		1%?dist
Summary:		Cross-platform Text Expander written in Rust for X11
License:		GPL-3.0
URL:			https://espanso.org
Source0:		https://github.com/espanso/espanso/archive/refs/tags/v%version.tar.gz
Requires:		libxkbcommon dbus libnotify wxGTK xdotool xclip libxcb
Conflicts:		espanso-wayland
BuildRequires:	anda-srpm-macros cargo-rpm-macros gcc gcc-c++
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	wxGTK-devel

%description
A cross-platform Text Expander written in Rust. A text expander is a program
that detects when you type a specific keyword and replaces it with something
else.

This package includes the X11 version of espanso.


%prep
%autosetup -n espanso-%version
%cargo_prep_online

%build
%cargo_build -n -f vendored-tls

%install
cd espanso
%cargo_install -n -f vendored-tls

%files
%_bindir/espanso

%changelog
%autochangelog
