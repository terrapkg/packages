Name:			terra-libindicator
Version:		16.10.0
Release:		%autorelease
Summary:		Shared functions for Ayatana indicators

License:		GPL-3.0
URL:			https://launchpad.net/libindicator
Source0:		http://archive.ubuntu.com/ubuntu/pool/universe/libi/libindicator/libindicator_16.10.0+18.04.20180321.1.orig.tar.gz
Source1:		https://raw.githubusercontent.com/ubports/libindicator/097906132ffb479205be15a92cae97e5daf4e154/data/indicators.target
# From GLib 2.62
Patch1:			http://archive.ubuntu.com/ubuntu/pool/universe/libi/libindicator/libindicator_16.10.0+18.04.20180321.1-0ubuntu5.diff.gz

BuildRequires:	chrpath
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(systemd)
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk2-devel
BuildRequires:	gtk3-devel
BuildRequires:	systemd-rpm-macros
BuildRequires:	gnome-common
BuildRequires:	make

%description
A set of symbols and convenience functions that all Ayatana indicators are
likely to use.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package gtk3
Summary:	GTK+3 build of %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description gtk3
A set of symbols and convenience functions that all Ayatana indicators
are likely to use. This is the GTK+ 3 build of %{name}, for use
by GTK+ 3 apps.


%package gtk3-devel
Summary:	Development files for %{name}-gtk3
Requires:	%{name}-gtk3%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description gtk3-devel
The %{name}-gtk3-devel package contains libraries and header files for
developing applications that use %{name}-gtk3.

%prep
%setup -q -c
%patch 1 -p1 -b .orig
# Remove all IDO references
# This is only needed for tools/indicator-loader.c
sed -i '6d' ./Makefile.am
sed -i 's!libindicator \\!libindicator!' Makefile.am
sed -i '59d' configure.ac
sed -ie 58's/$/) &/' configure.ac

sed -i.addvar configure.ac \
	-e '\@LIBINDICATOR_LIBS@s|\$LIBM| \$LIBM|'
sed -i 's!tests/Makefile!!' configure.ac

NOCONFIGURE=1 \
	sh autogen.sh

%build
%global _configure ../configure --libdir=%{_libdir}
rm -rf build-gtk2 build-gtk3
mkdir build-gtk2 build-gtk3

pushd build-gtk2
export CFLAGS="%{optflags} -Wno-error=deprecated-declarations"
%configure --with-gtk=2 --disable-tests --disable-static --disable-silent-rules
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
popd

pushd build-gtk3
export CFLAGS="%{optflags} -Wno-error=deprecated-declarations"
%configure --with-gtk=3 --disable-tests --disable-static --disable-silent-rules
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
popd


%install
pushd build-gtk2
make install DESTDIR=%{buildroot}
popd
(
	PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
	export PKG_CONFIG_PATH
	for var in \
		iconsdir \
		indicatordir \
		%{nil}
	do
		vardir=$(pkg-config --variable=${var} indicator-0.4)
		mkdir -p %{buildroot}${vardir}
	done
)

pushd build-gtk3
make install DESTDIR=%{buildroot}
popd
(
	PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
	export PKG_CONFIG_PATH
	for var in \
		iconsdir \
		indicatordir \
		%{nil}
	do
		vardir=$(pkg-config --variable=${var} indicator3-0.4)
		mkdir -p %{buildroot}${vardir}
	done
)

# Ubuntu doesn't package the dummy indicator
%dnl rm -f %{buildroot}%{_libdir}/libdummy-indicator*.so

# Remove libtool files
find %{buildroot} -type f -name '*.la' -delete

# Lomiri compatability
install -Dm644 %{SOURCE1} %{buildroot}%{_userunitdir}/

%ldconfig_scriptlets
%ldconfig_scriptlets gtk3

%files
%license COPYING
%doc AUTHORS COPYING NEWS ChangeLog README
%{_libdir}/libindicator.so.*
%{_prefix}/lib/indicators/
%dir %{_datadir}/libindicator/
%dir %{_datadir}/libindicator/icons/
%{_userunitdir}/indicators-pre.target
%{_userunitdir}/indicators.target

%files devel
%dir %{_includedir}/libindicator-0.4/
%dir %{_includedir}/libindicator-0.4/libindicator/
%{_includedir}/libindicator-0.4/libindicator/*.h
%{_libdir}/libindicator.so
%{_libdir}/pkgconfig/indicator-0.4.pc

%files gtk3
%doc AUTHORS COPYING NEWS ChangeLog README
%license COPYING
%{_libdir}/libindicator3.so.*
%{_prefix}/lib/indicators3/
%dir %{_datadir}/libindicator/
%dir %{_datadir}/libindicator/icons/

%files gtk3-devel
%doc README
%license COPYING
%dir %{_includedir}/libindicator3-0.4/
%dir %{_includedir}/libindicator3-0.4/libindicator/
%{_includedir}/libindicator3-0.4/libindicator/*.h
%{_libdir}/libindicator3.so
%{_libdir}/pkgconfig/indicator3-0.4.pc

%changelog
%autochangelog
