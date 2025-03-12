
%global commit bedc1fe771bf30460fc3f250d5530fb0c5c30790
%global shortcommit %{sub %commit 1 7}
%global commit_date 20250312

Name:			astal
Version:		0^%commit_date.%shortcommit
Release:		1%?dist
Summary:		Building blocks for creating custom desktop shells
License:		LGPL-2.1-only
URL:			https://aylur.github.io/astal
Source0:		https://github.com/Aylur/astal/archive/%commit.tar.gz
Provides:		astal
Requires:		%{name}-io-libs%{?_isa} = %{version}-%{release}
BuildRequires:	meson gobject-introspection vala valadoc 

%description
The Linux Suite and Framework to Craft Desktop Shells and beautiful functional Wayland Widgets with GTK!

%package	io-libs
Summary:	Shared libraries of libastal-io

%description io-libs
%summary. (IO)

This package contains shared libraries for astal-io.

%package	io-devel
Summary:	Development libraries of libastal-io
Requires:	%{name}-io-libs%{?_isa} = %{version}-%{release}

%description io-devel
%summary. (IO)
This package contains development files and documentation for astal-io.

%prep
%autosetup -n astal-%commit

%build
cd lib/astal/io
%meson
%meson_build

%install
cd lib/astal/io
%meson_install

%files
%_bindir/astal

%files io-libs
%license LICENSE
%_libdir/libastal-io.so.0
%_libdir/libastal-io.so.0.1.0

%files io-devel
%_datadir/gir-1.0/AstalIO-0.1.gir
%_datadir/vala/vapi/astal-io-0.1.vapi
%_includedir/astal-io.h
%_libdir/girepository-1.0/AstalIO-0.1.typelib
%_libdir/libastal-io.so
%_libdir/pkgconfig/astal-io-0.1.pc
