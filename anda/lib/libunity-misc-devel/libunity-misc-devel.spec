Name:           libunity-misc-devel
Version:        1.4
Release:        %autorelease
Summary:        Misc Unity shell libs

License:        LGPLv2+
URL:            https://launchpad.net/libunity-misc
Source0:        http://archive.ubuntu.com/ubuntu/pool/universe/libu/libunity-misc/libunity-misc_4.0.5+14.04.20140115.orig.tar.gz

BuildRequires:  make
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  gnome-common
BuildRequires:  gtk-doc
BuildRequires:  libX11-devel
BuildRequires:  gtk3-devel
BuildRequires:  glib2-devel
Requires:       gtk3
Requires:       libX11

%description
A simple library that implements a subset of the XPath spec to allow selecting nodes in an object tree

%prep
%setup -q -n libunity-misc-4.0.5+14.04.20140115
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
%{_libdir}/libunity-misc.so
%{_libdir}/libunity-misc.so.4
%{_libdir}/libunity-misc.so.4.1.0
%{_libdir}/pkgconfig/unity-misc.pc
%{_includedir}/unity-misc/unity-misc/na-tray.h
%{_includedir}/unity-misc/unity-misc/na-marshal.h
%{_includedir}/unity-misc/unity-misc/na-tray-manager.h
%{_includedir}/unity-misc/unity-misc/na-tray-child.h
%{_includedir}/unity-misc/unity-misc/gnome-bg-slideshow.h

%changelog
%autochangelog
