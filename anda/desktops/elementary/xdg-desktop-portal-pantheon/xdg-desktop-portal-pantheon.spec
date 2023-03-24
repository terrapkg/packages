Name:			xdg-desktop-portal-pantheon
Version:		7.0.0
Release:		%?dist
Summary:		Pantheon XDG Desktop Portals
License:		GPL-3.0
URL:			https://github.com/elementary/portals
Source0:		%url/archive/refs/tags/%version.tar.gz
BuildRequires:	pkgconfig(glib-2.0) pkgconfig(gobject-2.0) pkgconfig(gio-2.0) pkgconfig(granite-7) pkgconfig(gtk4) pkgconfig(gtk4-x11) pkgconfig(gtk4-wayland) pkgconfig(x11)

%description
Backend implementation for xdg-desktop-portal for the Pantheon desktop environment

%prep
%autosetup

%build
meson build --prefix=/usr

%install
ninja install
/usr/libexec/xdg-desktop-portal-pantheon -r

%check
cd build
ninja test

%files
%doc README.md
%license COPYING
/usr/libexec/xdg-desktop-portal-pantheon

%changelog
* Sat Mar 25 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
