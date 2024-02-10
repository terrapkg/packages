%global forgeurl https://gitlab.com/ubports/development/core/suru-icon-theme
%global commit 2b832bd20443a45ea75d6da04236f687a5d0564a
%forgemeta

Name:       suru-icon-theme
Version:    20.05.1
Release:    %autorelease
Summary:    Suru icon theme for Lomiri desktop
License:    CC-BY-SA-3.0
URL:        https://gitlab.com/ubports/development/core/suru-icon-theme
Source0:    %{url}/-/archive/%commit/suru-icon-theme-%commit.tar.gz
BuildArch:  noarch

Requires:   hicolor-icon-theme

%description
Suru is a icon theme for Lomiri desktop.

%prep
%autosetup -n %{name}-%commit

%build
true

%install
mkdir -m 0755 -p %{buildroot}%{_datadir}/icons/suru
cp -r suru/* %{buildroot}%{_datadir}/icons/suru

%files
%license COPYING
%{_datadir}/icons/suru/

%changelog
%autochangelog
