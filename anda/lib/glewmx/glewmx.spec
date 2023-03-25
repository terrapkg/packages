# Can not find libraries for some reason
%global debug_package %{nil}

Name:           glewmx
Version:        1.13.0.
Release:        1%{?dist}
Summary:        OpenGL Extension Wrangler MX

License:        GPLv3+
URL:            https://launchpad.net/ubuntu/+source/glewmx
Source0:        http://archive.ubuntu.com/ubuntu/pool/universe/g/glewmx/glewmx_%{version}.orig.tar.gz
Source1:        http://archive.ubuntu.com/ubuntu/pool/universe/g/glewmx/glewmx_%{version}-5.debian.tar.xz

BuildRequires: make
BuildRequires: gcc
BuildRequires: mesa-libGLU-devel
BuildRequires: pkgconfig(glu)
BuildRequires: libXmu-devel
BuildRequires: libXi-devel

%description
OpenGL Extension Wrangler MX. The MX version is discountinued but is maintained in Ubuntu.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n glew-%{version}
tar -x -I 'xz -d -T0 -k' -f '%{SOURCE1}'

# Fix aarch64
sed -i 's!LDFLAGS.EXTRA = -L/usr/X11R6/lib -L/usr/lib!LDFLAGS.EXTRA = -L/usr/X11R6/lib64 -L/usr/lib64!' debian/patches/0001-Fix_FTBFS_on_kFreeBSD.patch
sed -i ':a;N;$!ba;s!LIBDIR = $(GLEW_DEST)/lib!LIBDIR = $(GLEW_DEST)/lib64!2' debian/patches/0001-Fix_FTBFS_on_kFreeBSD.patch

for i in debian/patches/*.patch; do patch -p1 < $i; done
sed -i 's:$(GLEW_DEST)/include/GL:$(GLEW_DEST)/include/glewmx-%{version}/GL:' Makefile

%build
# This doesn't get actually installed but is to change glewmx.pc before installation
%make_build LIBDIR="%{_libdir}"
sed -i 's:includedir=${prefix}/include:includedir=${prefix}/include/glewmx-%{version}:' glewmx.pc

%install
# Only MX is installed
%make_build DESTDIR=%{buildroot} INSTALL="/usr/bin/install -p" LIBDIR="%{_libdir}" install.mx

%files
%license LICENSE.txt
%{_libdir}/libGLEWmx.so.*

%files devel
%dir %{_includedir}/glewmx-%version
%dir %{_includedir}/glewmx-%version/GL
%{_includedir}/glewmx-%version/GL/*.h
%{_libdir}/libGLEWmx.a
%{_libdir}/libGLEWmx.so
%{_libdir}/pkgconfig/glewmx.pc

%changelog
%autochangelog
