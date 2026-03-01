%global appid org.freedesktop.libfprint

Name:           libfprint-tod
Version:        1.94.10+tod1
Release:        1%?dist
URL:            https://gitlab.freedesktop.org/3v1n0/libfprint/
Source:         %{url}/-/archive/v%{version}/libfprint-v%{version}.tar.gz
Summary:        a light fork of libfprint to expose internal Drivers API in order to create drivers as shared libraries
License:        GPL-2.1
Conflicts:      libfprint

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gusb)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  terra-appstream-helper

%description
%summary.

%package devel
%pkg_devel_files

%package doc
Summary:    Documentation for %{name}

%description doc
Documentation for %{name}.

%prep
%autosetup -n libfprint-v%{version}
%meson -Ddrivers=all -Dinstalled-tests=false

%build
%meson_build

%install
%meson_install
%terra_appstream

%files
%license COPYING
%doc AUTHORS HACKING.md INSTALL MAINTAINERS NEWS NEWS.tod.md README.md README.tod.md THANKS code-of-conduct.md
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib
%{_udevhwdbdir}/60-autosuspend-libfprint-2.hwdb
%{_udevrulesdir}/70-libfprint-2.rules
%{_metainfodir}/%{appid}.metainfo.xml

%files doc
%dir %{_datadir}/gtk-doc/html/libfprint-2
%{_datadir}/gtk-doc/html/libfprint-2/*.{html,css,png,devhelp2}

%changelog
* Fri Dec 5 2025 metcya <metcya@gmail.com>
- Package libfprint-tod
