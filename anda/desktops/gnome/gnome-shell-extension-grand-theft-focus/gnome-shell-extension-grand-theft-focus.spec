%global extension   grand-theft-focus
%global uuid        %{extension}@zalckos

Name:           gnome-shell-extension-%{extension}
Version:        9
Release:        3%?dist
Summary:        GNOME extension that removes the 'Window is ready' notification and brings the window into focus instead
License:        AGPL-3.0-only
URL:            https://github.com/zalckos/GrandTheftFocus

BuildArch:      noarch

Source0:        https://github.com/zalckos/GrandTheftFocus/archive/refs/tags/v%version.tar.gz

Requires:       (gnome-shell >= 48~ with gnome-shell < 50~)
Recommends:     gnome-extensions-app

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
GNOME extension. Removes the 'Window is ready' notification and brings the window into focus instead.

%prep
%autosetup -n GrandTheftFocus-%version

%install
install -Dm644 grand-theft-focus@zalckos.github.com/metadata.json %{buildroot}%{_gnomeextensionsdir}/metadata.json
install -Dm644 grand-theft-focus@zalckos.github.com/extension.js %{buildroot}%{_gnomeextensionsdir}/extension.js

%files
%license LICENSE
%doc README.md
%{_gnomeextensionsdir}

%changelog
* Tue Dec 30 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
