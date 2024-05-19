Name:			pantheon-tweaks
Version:		2.0.0
Release:		1%?dist
Summary:		A system settings panel for the Pantheon desktop environment
License:		GPL-3.0
URL:			https://github.com/pantheon-tweaks/pantheon-tweaks
Source0:		%{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires:	vala switchboard-devel pkgconfig(gee-0.8) pkgconfig(glib-2.0)
BuildRequires:	granite-devel >= 6.0.0 pkgconfig(gtk+-3.0) meson vala
Requires:		gtk3 granite

%description
A system settings panel for the Pantheon Desktop that
lets you easily and safely customise your desktop's appearance.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license COPYING
/usr/lib64/switchboard/personal/libpantheon-tweaks.so
%{_datadir}/icons/hicolor/32x32/categories/preferences-desktop-tweaks.svg
%{_datadir}/locale/*/LC_MESSAGES/pantheon-tweaks-plug.mo
%{_datadir}/metainfo/pantheon-tweaks.metainfo.xml


%changelog
* Tue Jan 17 2023 windowsboy111 <windowsboy111@fyralabs.com> - 1.0.4-1
- Initial package
