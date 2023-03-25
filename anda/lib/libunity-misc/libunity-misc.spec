Name:			libunity-misc
Version:		4.0.5
Release:		%autorelease
Summary:		Misc Unity shell libs

License:		LGPLv2 AND LGPLv2 AND GPLv2
URL:			https://launchpad.net/libunity-misc
Source0:		http://archive.ubuntu.com/ubuntu/pool/universe/libu/libunity-misc/libunity-misc_%{version}+14.04.20140115.orig.tar.gz

BuildRequires:	make
BuildRequires:	g++
BuildRequires:	gcc
BuildRequires:	libX11-devel
BuildRequires:	gnome-common
BuildRequires:	gtk-doc
BuildRequires:	libX11-devel
BuildRequires:	gtk3-devel
BuildRequires:	glib2-devel

%description
A simple library that implements a subset of the XPath spec to allow selecting nodes in an object tree

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n libunity-misc-%{version}+14.04.20140115
find ./ -type f -exec sed -i 's/-Werror//' {} \;
NOCONFIGURE=1 \
./autogen.sh

%build
%configure \
	--disable-silent-rules \
	--disable-static
%make_build

%install
%make_install
rm -fv %{buildroot}%{_libdir}/lib*.la
%ldconfig_post

%files
%license COPYING COPYING.GPL COPYING.LGPL-2
%{_libdir}/libunity-misc.so.*

%files devel
%{_libdir}/libunity-misc.so
%{_libdir}/pkgconfig/unity-misc.pc
%dir %{_includedir}/unity-misc
%dir %{_includedir}/unity-misc/unity-misc
%{_includedir}/unity-misc/unity-misc/*.h

%changelog
%autochangelog
