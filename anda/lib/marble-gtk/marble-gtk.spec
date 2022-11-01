# This is the dumbest thing ever
# Why make a library with the same name as another library gosh
%global commit 6dcc6fefa35f0151b0549c01bd774750fe6bdef8
Name:           marble-gtk
Version:        42.alpha0
# No idea how they name the version
Release:        %autorelease
Summary:        My GTK library
License:        GPLv3
URL:            https://gitlab.gnome.org/raggesilver/marble
BuildRequires:  vala meson >= 0.50.0 pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24
BuildRequires:  pkgconfig(gio-2.0) >= 2.50

Source0:        %{url}/-/archive/%{commit}/marble-%{commit}.tar.gz

%description
%summary.
Just as Elementary has Granite I have Marble, my collection of useful functions
and reusable widgets.
# duh...

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
