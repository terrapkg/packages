%global commit f240b2ec7d5cdacb8fdcc553703420dc5101ffdb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20240310
%global ver 2.0.0

Name:			pqmarble
Version:		%ver^%commit_date.%shortcommit
Release:		1%{?dist}
Summary:		My GTK library
License:		GPL-3.0
URL:			https://gitlab.gnome.org/raggesilver/marble
BuildRequires:	vala pkgconfig(gtk4) meson >= 0.50.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.24
BuildRequires:	pkgconfig(gio-2.0) >= 2.50

Source0:		%{url}/-/archive/%{commit}/marble-%{commit}.tar.gz

%description
%summary.
Just as Elementary has Granite I have Marble, my collection of useful functions
and reusable widgets.

%package devel
Summary: Development files for marble-gtk

%description devel
%summary.


%prep
%autosetup -n marble-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license COPYING
%_libdir/girepository-1.0/PQMarble-*.typelib
%_libdir/libpqmarble.so.*
%_datadir/vala/vapi/pqmarble.deps
%_datadir/vala/vapi/pqmarble.vapi

%files devel
%_prefix/include/pqmarble.h
%_libdir/libpqmarble.so
%_libdir/pkgconfig/pqmarble.pc
%_datadir/gir-1.0/PQMarble-*.gir

%changelog
%autochangelog
