%global commit 5b00b740f0bde0e129a3ad070171d53d97275941
%global commit_date 20260114
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global extension   multi-monitors-bar
%global uuid        %{extension}@frederykabryan

Name:           gnome-shell-extension-%{extension}
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        Add multiple monitors overview and panel for GNOME Shell. This is an updated fork with GNOME 46 compatibility
License:        GPL-2.0-or-later
URL:            https://github.com/FrederykAbryan/multi-monitors-bar_fapv2

BuildArch:      noarch

Source0:        %url/archive/%commit/multi-monitors-bar_fapv2-%commit.tar.gz
# README declared the license, but they do not provide a license file

Requires:       (gnome-shell >= 48~ with gnome-shell < 50~)
Recommends:     gnome-extensions-app

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n multi-monitors-bar_fapv2-%commit

%build

%install
find . -name "*.gschema.xml"
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
install -Dm644 *.json %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
install -Dm644 *.js %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
install -Dm644 *.css %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
install -Dm644 schemas/*.gschema.xml -t %{buildroot}%{_datadir}/glib-2.0/schemas/

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &> /dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &> /dev/null || :

%files
%license LICENSE
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/*.gschema.xml

%changelog
* Thu Jan 01 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
