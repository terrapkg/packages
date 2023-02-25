Name:			marble-gtk
Version:		v1.3.0
Release:		1%{?dist}
Summary:		My GTK library
License:		GPLv3
URL:			https://gitlab.gnome.org/raggesilver/marble
BuildRequires:	vala pkgconfig(gtk4) meson >= 0.50.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.24
BuildRequires:	pkgconfig(gio-2.0) >= 2.50

Source0:        %{url}/-/archive/v%{version}/marble-v%{version}.tar.gz

%description
%summary.
Just as Elementary has Granite I have Marble, my collection of useful functions
and reusable widgets.

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
/usr/include/marble.h
/usr/lib/debug/usr/lib64/libmarble.so*
/usr/lib64/girepository-1.0/Marble-*.typelib
/usr/lib64/libmarble.so*
/usr/lib64/pkgconfig/marble.pc
/usr/share/gir-1.0/Marble-*.gir
/usr/share/vala/vapi/marble.*

%changelog
* Sat Oct 29 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
