Name:			marble-gtk
Version:		1.3.0
Release:		1%{?dist}
Summary:		My GTK library
License:		GPL-3.0
URL:			https://gitlab.gnome.org/raggesilver/marble
BuildRequires:	vala pkgconfig(gtk4) meson >= 0.50.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.24
BuildRequires:	pkgconfig(gio-2.0) >= 2.50

Provides:		pkgconfig(marble) = 42

Source0:		%{url}/-/archive/v%{version}/marble-v%{version}.tar.gz

%description
%summary.
Just as Elementary has Granite I have Marble, my collection of useful functions
and reusable widgets.

%package devel
Summary: Development files for marble-gtk

%description
%summary.


%prep
%autosetup -n marble-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license COPYING
/usr/lib64/girepository-1.0/Marble-*.typelib
/usr/lib64/libmarble.so.*
/usr/share/vala/vapi/marble.*

%files devel
/usr/include/marble.h
%_libdir/libmarble.so
%_libdir/pkgconfig/marble.pc
%_datadir/gir-1.0/Marble-%version.gir

%changelog
* Sat Oct 29 2022 windowsboy111 <windowsboy111@fyralabs.com> - 1.3.0-1
- Initial package
