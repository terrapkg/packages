Name:			librda
Version:		0.0.5
Release:		2%?dist
Summary:		Remote Desktop Awareness Shared Library
Group:			System Environment/Libraries
License:		LGPL2.1+ or GPL3+
URL:			https://github.com/ArcticaProject/librda
Source0:		%url/archive/refs/tags/%version.tar.gz
Requires:		glib2 glibc
BuildRequires:	gobject-introspection-devel intltool gtk3-devel
BuildRequires:	clang gcc make autoconf libtool gettext-devel

%description
%summary.

%prep
%autosetup

%build
autoupdate
autoreconf -vfi
%configure --disable-static --enable-x2go --enable-ogon
%make_build

%install
%make_install

%files
%_bindir/rdacheck
%_includedir/rda/
%_libdir/girepository-1.0/rda-*.typelib
%_libdir/librda.so*
%_libdir/pkgconfig/rda.pc
%_datadir/gir-1.0/rda-*.gir
%_datadir/locale/*/LC_MESSAGES/librda.mo
%_mandir/man1/rdacheck.1.gz

%changelog
%autochangelog
