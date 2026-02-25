%global commit 1de26db2ea4166fdca85306300b12bdc24f2c955
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20250925
%global ver 11
%global extension   gpu-switcher-supergfxctl
%global uuid        %{extension}@chikobara.github.io

Name:           gnome-shell-extension-%{extension}
Version:        %ver^%commit_date.%shortcommit
Release:        2%?dist
Summary:        GPU Profile switcher Gnome-Shell-Extension for ASUS laptops using Supergfxctl
License:        GPL-3.0-only
URL:            https://github.com/chikobara/GPU-Switcher-Supergfxctl

Source0:        %url/archive/%commit.tar.gz

Requires:       (gnome-shell >= 48~ with gnome-shell < 50~) asusctl supergfxctl
Recommends:     gnome-extensions-app

BuildArch:	noarch

%description
GPU Profile switcher Gnome-Shell-Extension for ASUS laptops using Supergfxctl

%prep
%autosetup -n GPU-Switcher-Supergfxctl-%{commit} -p1

%install
install -Dm644 metadata.json %{buildroot}%{_gnomeextensionsdir}/metadata.json
install -Dm644 extension.js %{buildroot}%{_gnomeextensionsdir}/extension.js

%files
%license LICENSE
%doc README.md
%{_gnomeextensionsdir}

%changelog
* Mon Oct 27 2025 june-fish <june@fyralabs.com> - 11
- Initial Package
