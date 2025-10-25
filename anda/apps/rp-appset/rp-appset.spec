%global commit a445d545c8e1a3339acd53cadf4e9c08698a786d
%global commit_date 20251024
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           appset
Version:        0~%commit_date.git~%shortcommit
Release:        1%?dist
Summary:        Application for customisation of appearance of Raspberry Pi Desktop
License:        BSD-3-Clause
URL:            https://github.com/raspberrypi-ui/appset
Source0:        %url/archive/%commit.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gtk3-devel
BuildRequires:  libxml2-devel
BuildRequires:  intltool
BuildRequires:  gcc

Requires:       libxml2
Requires:       gtk3

Provides:       pipanel
Provides:       rp-appset

%description
%summary.

%prep
%autosetup -n appset-%commit

%build
%meson
%meson_build

%install
%meson_install

%find_lang pipanel

%files -f pipanel.lang
%doc README
%license debian/copyright
%{_bindir}/pipanel
%{_datadir}/applications/pipanel.desktop
%{_datadir}/pipanel/ui/pipanel.ui

%changelog
* Fri Aug 15 2025 Owen Zimmerman <owen@fyralabs.com>
- Package appset
