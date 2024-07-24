%define debug_package %{nil}

Name:			xdg-desktop-portal-pantheon
Version:		7.2.0
Release:		1%?dist
Summary:		Pantheon XDG Desktop Portals
License:		GPL-3.0
URL:			https://github.com/elementary/portals
Source0:		%url/archive/refs/tags/%version.tar.gz
Requires:		gtk4 granite-7
BuildRequires:	ninja-build vala meson glib2-devel pkgconfig(granite-7) gtk4-devel pkgconfig(x11) pkgconfig(systemd)

%description
Backend implementation for xdg-desktop-portal for Pantheon desktop environment.

%prep
%autosetup -n portals-%version

%build
%meson --prefix=/usr
%meson_build

%install
%meson_install

%check
%meson_test


%files
%doc README.md
%license COPYING
/usr/share/xdg-desktop-portal/portals/pantheon.portal
/usr/share/dbus-1/services/org.freedesktop.impl.portal.desktop.pantheon.service
/usr/lib/systemd/user/xdg-desktop-portal-pantheon.service
/usr/libexec/xdg-desktop-portal-pantheon
/usr/share/metainfo/io.elementary.portals.metainfo.xml
/usr/share/locale/*/LC_MESSAGES/xdg-desktop-portal-pantheon.mo

%changelog
* Sat Mar 25 2023 windowsboy111 <windowsboy111@fyralabs.com> - 7.0.0-1
- Initial package
