%global uuid vicinae@dagimg-dot.netlify.app

Name:           gnome-shell-extension-vicinae
Version:        1.5.3
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/dagimg-dot/vicinae-gnome-extension
Source:         %{url}/archive/refs/tags/v${version}.tar.gz
Summary:        Companion GNOME extension for Vicinae launcher
Packager:       metcya <metcya@gmail.com>

Requires:       (gnome-shell >= 48~ with gnome-shell < 50~)
Requires:       vicinae
Recommends:     gnome-extensions-app
Provides:       gnome-shell-extension-vicinae-gnome-extension

%description
Companion GNOME extension for Vicinae launcher with clipboard monitoring,
window management APIs, and paste-to-active-window capabilities.

%prep
%autosetup

%install
install -Dm 644 metadata.json %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/metadata.json
install -Dm 644 extension.js %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/extension.js

%files
%license LICENSE
%doc README.md DEVELOPMENT.md
%{_datadir}/gnome-shell/extensions/%{uuid}

%changelog
* Sat Dec 27 2025 metcya <metcya@gmail.com> - 1.5.3-1
- Package 

