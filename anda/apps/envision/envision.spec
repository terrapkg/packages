%global commit 25d5aa48e30e5cc702c031c9c48ec4b2d5389cc9
%global commit_date 20240530
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           envision
Version:        %commit_date.%commit
Release:        1%?dist
Summary:        UI for building, configuring and running Monado, the open source OpenXR runtime
License:        AGPL-3.0-or-later
URL:            https://gitlab.com/gabmus/envision/
Source0:        %url/-/archive/%commit/envision-%commit.tar.gz
BuildRequires:  meson ninja-build cargo 
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gio-2.0) >= 2.66
BuildRequires:  pkgconfig(gtk4) >= 4.10.0
BuildRequires:  pkgconfig(vte-2.91-gtk4) >= 0.72.0
BuildRequires:  openssl-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
Recommends:     android-tools

%description
%summary.

%prep
%autosetup -n envision-%commit

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
