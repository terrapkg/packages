<<<<<<< HEAD
%global commit b3f3f1da2fa59a2cbdea73c75b7d67bc312ce2bc
%global commit_date 20251115
=======
%global commit 605d9dd8c825b650deeaa614e1b83e8dbb41e87d
%global commit_date 20260128
>>>>>>> 93ea6f333 (chore: Bump out of sync packages (#9513))
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           rasputin
Version:        0~%commit_date.git~%shortcommit
Release:        1%?dist
Summary:        Mouse and keyboard settings for Raspberry Pi Desktop
License:        BSD-3-Clause
URL:            https://github.com/raspberrypi-ui/rasputin
Source0:        %url/archive/%commit.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gtk3-devel
BuildRequires:  libxml2-devel
BuildRequires:  intltool
BuildRequires:  gcc

Requires:       libxml2

%description
%summary.

%prep
%autosetup -n rasputin-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%find_lang rpcc_rasputin

%files -f rpcc_rasputin.lang
%license debian/copyright
%{_datadir}/rpcc/ui/rasputin.ui
%{_libdir}/rpcc/librpcc_rasputin.so

%changelog
* Sun Oct 26 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
