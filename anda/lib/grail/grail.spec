Name:			grail
Version:		3.1.1
Release:		%autorelease
Summary:		Gesture Recognition And Instantiation Library

License:		GPL-3.0 AND LGPL-3.0-or-later
URL:			https://launchpad.net/grail
Source0:		http://archive.ubuntu.com/ubuntu/pool/universe/g/grail/grail_%{version}.orig.tar.bz2

BuildRequires:	automake libtool gnome-common
BuildRequires:	intltool
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	g++
BuildRequires:	libX11-devel
BuildRequires:	libXi-devel
BuildRequires:	libXext-devel
BuildRequires:	xorg-x11-server-devel
BuildRequires:	frame-devel

%description
Grail consists of an interface and tools for handling gesture recognition and gesture instantiation.

When a multitouch gesture is performed on a device, the recognizer emits one or several possible gestures. Once the context of the gesture is known, i.e., in what window the touches land and what gestures the clients of that window listen to, the instantiator delivers the matching set of gestures.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n grail-%{version}

%build
autoreconf --force --install
PYTHON=%{__python3}
export PYTHON

%configure \
	--disable-integration-tests \
	--disable-silent-rules \
	--with-x11 \
	--disable-static

%make_build

%install
%make_install
rm -fv %{buildroot}%{_libdir}/*.la

%files
%license COPYING COPYING.GPL3
%{_libdir}/libgrail.so.*

%files devel
%{_bindir}/grail-test-*
%{_includedir}/oif/grail.h
%{_libdir}/libgrail.so
%{_libdir}/pkgconfig/grail.pc
%{_mandir}/man1/grail-test-*.gz

%changelog
%autochangelog
