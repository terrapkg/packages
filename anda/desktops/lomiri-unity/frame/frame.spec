Name:           frame
Version:        2.5.0
Release:        3%?dist
Summary:        Touch Frame Library

License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://launchpad.net/frame
Source0:        http://archive.ubuntu.com/ubuntu/pool/universe/f/frame/frame_%{version}daily13.06.05+16.10.20160809.orig.tar.gz
Patch0:         http://archive.ubuntu.com/ubuntu/pool/universe/f/frame/frame_%{version}daily13.06.05+16.10.20160809-0ubuntu3.diff.gz

BuildRequires: automake libtool gnome-common
BuildRequires: intltool
BuildRequires: make
BuildRequires: gcc
BuildRequires: g++
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libXext-devel
BuildRequires: xorg-x11-server-devel
BuildRequires: asciidoc

%description
Frame handles the buildup and synchronization of a set of simultaneous touches.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{evr}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -c -p1

%conf
NOCONFIGURE=1 \
./autogen.sh

PYTHON=%{__python3}
export PYTHON

%configure \
  --disable-silent-rules \
  --disable-static

%build
%make_build

%install
%make_install
rm -fv %{buildroot}%{_libdir}/*.la

%files
%doc README
%license COPYING COPYING.GPL3
%{_libdir}/libframe.so.*

%files devel
%{_bindir}/frame-test-x11
%dir %{_includedir}/oif
%{_includedir}/oif/*.h
%{_libdir}/libframe.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/frame-test-x11.1.gz

%changelog
%autochangelog
