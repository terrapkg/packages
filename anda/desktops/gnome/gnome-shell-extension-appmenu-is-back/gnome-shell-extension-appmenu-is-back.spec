%global extension   appmenu-is-back
%global uuid        %{extension}@fthx

Name:           gnome-shell-extension-%{extension}
Version:        2
Release:        2%{?dist}
Summary:        GNOME Shell extension to bring back the app menu
License:        GPL-3.0-only
URL:            https://github.com/fthx/appmenu-is-back

BuildArch:      noarch

Source0:        https://github.com/fthx/appmenu-is-back/archive/refs/tags/v%{version}.tar.gz
Patch0:         https://github.com/fthx/appmenu-is-back/commit/c251ff36d226dac679eb745638e3df236d3e1a20.patch

Requires:       (gnome-shell >= 46~ with gnome-shell < 47~)
Recommends:     gnome-extensions-app

%description
This extension brings back the app menu in the top panel, for GNOME 45 and later.

%prep
%autosetup -n appmenu-is-back-%{version}

%install
install -Dm644 metadata.json %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/metadata.json
install -Dm644 extension.js %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/extension.js

%files
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}

%changelog
* Mon Apr 1 2024 Lleyton Gray <lleyton@fyralabs.com> - 2-2
- Patch for GNOME 46 compatibility

* Thu Nov 16 2023 Lleyton Gray <lleyton@fyralabs.com> - 2-1
- Initial Release
