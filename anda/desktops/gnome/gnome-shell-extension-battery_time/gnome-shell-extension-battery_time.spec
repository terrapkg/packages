%global commit 0df5f952843a296bf9f9b61b36c5fae5d851700b
%global commit_date 20250925
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global extension   battery_time
%global uuid        %{extension}@pomoke

Name:           gnome-shell-extension-%{extension}
Version:        0~%{commit_date}git.%{shortcommit}
Release:        2%?dist
Summary:        Battery remaining time extension for GNOME Shell
License:        GPL-2.0-only
URL:            https://github.com/pomoke/battery_time

BuildArch:      noarch

Source0:        %url/archive/%commit/battery_time-%commit.tar.gz
# License declared in README
Source1:        https://scancode-licensedb.aboutcode.org/gpl-2.0.LICENSE

Requires:       (gnome-shell >= 48~ with gnome-shell < 50~)
Recommends:     gnome-extensions-app

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
This extension serves as a replacement of battery remaining time, last seen in GNOME 42.
Remaining time is shown inline, so no additional menu item is created (currently).

%prep
%autosetup -n %{extension}-%{commit}

%install
install -Dm644 metadata.json %{buildroot}%{_gnomeextensionsdir}/metadata.json
install -Dm644 extension.js %{buildroot}%{_gnomeextensionsdir}/extension.js
cp %{SOURCE1} LICENSE

%files
%doc README.md
%license LICENSE
%{_gnomeextensionsdir}

%changelog
* Mon Jan 05 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
