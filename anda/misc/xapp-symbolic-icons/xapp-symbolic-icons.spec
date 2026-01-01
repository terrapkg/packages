Name:           xapp-symbolic-icons
Version:        1.0.7
Release:        1%{?dist}
Summary:        A set of symbolic icons which replaces the GNOME-specific Adwaita set
License:        GPL-3.0-only AND LGPL-3.0-only
URL:            https://github.com/xapp-project/xapp-symbolic-icons
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  meson
Requires:       hicolor-icon-theme

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
A set of symbolic icons which replaces the GNOME-specific Adwaita set.
All provided icons are prefixed with xsi-.
Icon names loosely follow the Adwaita names.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%transfiletriggerin -- %{_hicolordir}
gtk-update-icon-cache --force %{_hicolordir} &>/dev/null || :

%transfiletriggerpostun -- %{_hicolordir}
gtk-update-icon-cache --force %{_hicolordir} &>/dev/null || :

%files
%license COPYING COPYING.LESSER
%doc AUTHORS README.md
%{_bindir}/xsi-replace-adwaita-symbolic
%{_hicolordir}/scalable/actions/xsi-*.svg
%{_datadir}/xapp/

%changelog
* Thu Jan 01 2026 Owen Zimmerman <owen@fyralabs.com>
- Port to Terra from Fedora Rawhide

* Fri Dec 12 2025 Leigh Scott <leigh123linux@gmail.com> - 1.0.6-1
- Update to 1.0.6

* Thu Nov 27 2025 Leigh Scott <leigh123linux@gmail.com> - 1.0.5-1
- Update to 1.0.5
