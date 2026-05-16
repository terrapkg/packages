%global commit 56e735b355e149555c924f09b5f635ebcd3b4224
%global commit_date 20260515
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           libsingularity
Summary:        GTK4 application and widget framework for the Singularity Desktop Environment
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
License:        LGPL-2.1-or-later
URL:            https://github.com/singularityos-lab/libsingularity
Source0:        %url/archive/%commit/libsingularity-%commit.tar.gz
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-layer-shell-0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libpeas-2)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
A GTK4 application and widget framework for the Singularity Desktop Environment.

%prep
%autosetup -n libsingularity-%{commit}

%package devel
%pkg_devel_files

%conf
%meson

%build
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_libdir}/girepository-1.0/Singularity-1.0.typelib
%{_libdir}/libsingularity.so.0
%{_libdir}/libsingularity.so.0.1.0
%{_datadir}/vala/vapi/singularity-1.0.vapi

%changelog
* Sat May 16 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
