Name:			xdg-desktop-portal-pantheon
Version:		7.0.0
Release:		%?dist
Summary:		Pantheon XDG Desktop Portals
License:		GPL-3.0
URL:			https://github.com/elementary/portals
Source0:		%url/archive/refs/tags/%version.tar.gz
Requires:		gtk4 glib2 granite-7 libX11
BuildRequires:	ninja-build vala meson glib2-devel pkgconfig(granite-7) gtk4-devel pkgconfig(x11) pkgconfig(systemd)

%description
Backend implementation for xdg-desktop-portal for the Pantheon desktop environment

%prep
%autosetup -n portals-%version

%build
meson build --prefix=/usr

%install
cd build
ninja install

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
