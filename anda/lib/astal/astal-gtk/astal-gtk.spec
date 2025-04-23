%global commit 8f020e6
%global shortcommit %{sub %commit 1 7}
%global commit_date 20250411

Name:			astal
Version:		0^%commit_date.%shortcommit
Release:		1%?dist
Summary:		Building blocks for creating custom desktop shells
License:		LGPL-2.1-only
URL:			https://aylur.github.io/astal
Source0:		https://github.com/Aylur/astal/archive/%commit.tar.gz
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	meson gobject-introspection vala valadoc cmake
BuildRequires:	pkgconfig(astal-io-0.1)

%description
The Linux Suite and Framework to Craft Desktop Shells and beautiful functional Wayland Widgets with GTK!


%package	gtk3-libs
Summary:	GTK 3 shared libraries for astal
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk-layer-shell-0)
BuildRequires:	pkgconfig(wayland-protocols)

%description gtk3-libs
%summary. (GTK 3)

This package contains shared libraries for astal-gtk3.

%package	gtk3-devel
Summary:	GTK 3 development libraries for astal
Requires:	%{name}-gtk3-libs%{?_isa} = %{version}-%{release}

%description gtk3-devel
%summary. (GTK 3)

This package contains development files and documentation for astal-gtk3.


%package	gtk4-libs
Summary:	GTK 4 shared libraries for astal
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(gtk4-layer-shell-0)

%description gtk4-libs
%summary. (GTK 4)

This package contains shared libraries for astal-gtk4.

%package	gtk4-devel
Summary:	GTK 4 development libraries for astal
Requires:	%{name}-gtk4-libs%{?_isa} = %{version}-%{release}

%description gtk4-devel
%summary. (GTK 4)

This package contains development files and documentation for astal-gtk4.


%prep
%autosetup -n astal-%commit

%build
my_build() {
	cd lib/astal/$1
	%meson
	%meson_build
}
my_build gtk3 &
my_build gtk4 &
wait

%install
my_install() {
	cd lib/astal/$1
	%meson_install
}
my_install gtk3 &
my_install gtk4 &
wait


%files gtk3-libs
%license LICENSE
%_libdir/libastal.so.3
%_libdir/libastal.so.3.0.0

%files gtk3-devel
%_datadir/gir-1.0/Astal-3.0.gir
%_datadir/vala/vapi/astal-3.0.vapi
%_includedir/astal.h
%_libdir/girepository-1.0/Astal-3.0.typelib
%_libdir/libastal.so
%_libdir/pkgconfig/astal-3.0.pc


%files gtk4-libs
%license LICENSE
%_libdir/libastal-4.so.4
%_libdir/libastal-4.so.4.0.0

%files gtk4-devel
%_datadir/gir-1.0/Astal-4.0.gir
%_datadir/vala/vapi/astal-4-4.0.vapi
%_includedir/astal-4.h
%_libdir/girepository-1.0/Astal-4.0.typelib
%_libdir/libastal-4.so
%_libdir/pkgconfig/astal-4-4.0.pc
