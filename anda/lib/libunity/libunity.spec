Name:    libunity
Summary: Supporting library for Unity shell
Version: 7.1.4+19.04
Release: %autorelease

License: GPL-3.0-or-later AND LGPL-3.0-or-later
URL:     https://launchpad.net/libunity
# same sources as shipped in ubuntu packages
Source0: http://archive.ubuntu.com/ubuntu/pool/main/libu/libunity/libunity_7.1.4+19.04.20190319.orig.tar.gz
Patch0:  https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/libunity/7.1.4+19.04.20190319-0ubuntu1/libunity_7.1.4+19.04.20190319-0ubuntu1.diff.gz
Patch1:  https://launchpadlibrarian.net/443817430/0001-Fix-FTB-with-recent-vala-requiring-non-public-abstra.patch
# Patch for vala 0.53.2 portability
Patch2:  https://src.fedoraproject.org/rpms/libunity/raw/rawhide/f/libunity-7.1.4-vala-053.patch

BuildRequires: automake libtool gnome-common
BuildRequires: intltool
BuildRequires: pkgconfig(dee-1.0)
BuildRequires: pkgconfig(dbusmenu-glib-0.4)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: python3-devel
BuildRequires: vala
BuildRequires: make

%description
A library for instrumenting and integrating with all aspects of the Unity
shell devel version with headers. Thanks to https://src.fedoraproject.org/rpms/libunity for the original RPM spec.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package -n python3-libunity
Summary: Python3 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3-gobject-base
%description -n python3-libunity
%{summary}.

%prep
%autosetup -c -p1

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

rm -fv %{buildroot}%{_libdir}/lib*.la %{buildroot}%{_libdir}/libunity/lib*.la

pushd %{buildroot}
ln -fs %{_libdir}/libunity/libunity-protocol-private.so.0.0.0 .%{_libdir}/libunity-protocol-private.so
ln -fs %{_libdir}/libunity/libunity-protocol-private.so.0.0.0 .%{_libdir}/libunity-protocol-private.so.0
popd

%py_byte_compile %{__python3} %{buildroot}%{python3_sitearch}/gi/overrides/

%ldconfig_post

%postun
%{?ldconfig}
%if 0%{?rhel} && 0%{?rhel} < 8
if [ $1 -eq 0 ]; then
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
%endif

%files
%doc AUTHORS README
%license COPYING*
%{_bindir}/libunity-tool
%{_bindir}/unity-scope-loader
%{_libdir}/libunity.so.*
%{_libdir}/libunity-extras.so.*
%{_libdir}/libunity-protocol-private.so.0
%{_libdir}/girepository-1.0/Unity-7.0.typelib
%{_libdir}/girepository-1.0/UnityExtras-7.0.typelib
%dir %{_libdir}/libunity/
%{_libdir}/libunity/libunity-protocol-private.so
%{_libdir}/libunity/libunity-protocol-private.so.*
%{_datadir}/glib-2.0/schemas/com.canonical.Unity.Lenses.gschema.xml
%{_datadir}/unity/
%{_datadir}/unity-scopes/

%files -n python3-libunity
%{python3_sitearch}/gi/overrides/Unity.py*
%{python3_sitearch}/gi/overrides/__pycache__/*

%files devel
%{_includedir}/unity/
%{_libdir}/libunity.so
%{_libdir}/libunity-extras.so
%{_libdir}/libunity-protocol-private.so
%{_libdir}/pkgconfig/unity.pc
%{_libdir}/pkgconfig/unity-extras.pc
%{_libdir}/pkgconfig/unity-protocol-private.pc
%{_datadir}/gir-1.0/Unity-7.0.gir
%{_datadir}/gir-1.0/UnityExtras-7.0.gir
%{_datadir}/vala/vapi/unity.*
%{_datadir}/vala/vapi/unity-extras.*
%{_datadir}/vala/vapi/unity-protocol.*
%{_datadir}/vala/vapi/unity-trace.*

%changelog
%autochangelog
