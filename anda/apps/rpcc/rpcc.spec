%global commit 0e6cd08585bccd8f56c69bf8785777c2e3e67c4a
%global commit_date 20260520
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           rpcc
Version:        0~%commit_date.git~%shortcommit
Release:        1%{?dist}
Summary:        Raspberry Pi Control Centre - an extensible settings application for the Raspberry Pi Desktop
License:        BSD-3-Clause
URL:            https://github.com/raspberrypi-ui/rpcc
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

%description
Raspberry Pi Control Centre - an extensible settings application for the Raspberry Pi Desktop

rpcc is a settings application which loads tab pages at runtime from plugin modules.

A number of packages contain plugins which are installed as standard on Raspberry Pi images:
 - pipanel - appearance settings
 - rc-gui - Raspberry Pi Configuration
 - raindrop - screen layout
 - rasputin - mouse and keyboard input
 - rpinters - printers

%prep
%autosetup -n rpcc-%commit

%conf
%meson

%build
%meson_build

%install
%meson_install

%find_lang rpcc

%files -f rpcc.lang
%doc README
%license debian/copyright
%{_bindir}/rpcc
%{_datadir}/applications/rpcc.desktop
%{_datadir}/rpcc/ui/rpcc.ui

%changelog
* Sat Oct 25 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
