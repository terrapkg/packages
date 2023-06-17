Name:    unity-scope-home
Summary: Home scope that aggregates results from multiple scopes
Version: 19.04.20190412
Release: %autorelease
License: GPL-3.0
URL:     https://launchpad.net/unity-scope-home
Source0: http://archive.ubuntu.com/ubuntu/pool/universe/u/unity-scope-home/unity-scope-home_6.8.2+%{version}.orig.tar.gz
Patch0:  https://gitlab.com/unity-for-arch/unity-scope-home/-/raw/main/fix-vala-0.56-errors.patch

BuildRequires: automake libtool gnome-common
BuildRequires: intltool
BuildRequires: make
BuildRequires: gcc
BuildRequires: g++
BuildRequires: vala
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(dee-1.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libsoup-gnome-2.4)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(unity)
BuildRequires: pkgconfig(unity-protocol-private)
BuildRequires: pkgconfig(unity-extras)

%description
%summary.
Theme and icons for Unity.

%prep
%autosetup -c -p1

%build
NOCONFIGURE=1 \
./autogen.sh

# Cannot build with Fedora's libunity
%configure --disable-static
%make_build

%install
%make_install
rm -fv %{buildroot}%{_libdir}/*.la

%files
%license COPYING
%dir %{_libexecdir}/unity-scope-home
%{_libexecdir}/unity-scope-home/unity-scope-home
%dir %{_datadir}/unity/scopes
%{_datadir}/unity/scopes/*.scope
%{_datadir}/dbus-1/services/unity-scope-home.service

%changelog
%autochangelog
