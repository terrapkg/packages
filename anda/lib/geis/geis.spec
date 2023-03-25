Name:           geis
Version:        2.2.17
Release:        %autorelease
Summary:        An implementation of the GEIS interface

License:        GPLv3 AND LGPLv3
URL:            https://launchpad.net/geis
Source0:        http://archive.ubuntu.com/ubuntu/pool/universe/g/geis/geis_%{version}+16.04.20160126.orig.tar.gz
Patch0:         http://archive.ubuntu.com/ubuntu/pool/universe/g/geis/geis_%{version}+16.04.20160126-0ubuntu8.diff.gz

BuildRequires: automake libtool gnome-common
BuildRequires: intltool
BuildRequires: make
BuildRequires: gcc
BuildRequires: g++
BuildRequires: dbus-devel
BuildRequires: grail-devel
BuildRequires: frame-devel
BuildRequires: python3-devel
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xorg-server)
Requires:      python3

%description
An implementation of the GEIS (Gesture Engine Interface and Support) interface.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n geis-%{version}+16.04.20160126 -p1

%build
NOCONFIGURE=1 \
./autogen.sh

PYTHON=%{__python3}
export PYTHON

%configure \
  --disable-silent-rules \
  --disable-static

%make_build

%install
%make_install
rm -fv %{buildroot}%{_libdir}/*.la %{buildroot}%{python3_sitearch}/*.la

%files
%license COPYING COPYING.GPL
%{_bindir}/geisview
%{_bindir}/pygeis
%{python3_sitelib}/geis/
%{python3_sitelib}/geisview/
%{_libdir}/libgeis.so.*
%{python3_sitearch}/_geis_bindings.so
%{_datadir}/applications/geisview.desktop
%{_datadir}/doc/geis/
%{_datadir}/geisview/
%{_mandir}/man1/geisview.1.gz
%{_mandir}/man1/pygeis.1.gz
%{_datadir}/pixmaps/geisview32x32.xpm

%files devel
%{_bindir}/geistest
%dir %{_includedir}/geis
%{_includedir}/geis/*.h
%{_libdir}/libgeis.so
%{_libdir}/pkgconfig/libgeis.pc
%{_mandir}/man1/geistest.1.gz

%changelog
%autochangelog
