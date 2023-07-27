%global ver 1.4
%global commit 631673f7789c789b38d48da0c8340e247fdc3c74

Name:			libadwaita-nightly
Version:		%ver^%commit
Release:		1%?dist
Summary:		Building blocks for modern GNOME applications
License:		LGPL-2.1+
URL:			https://gnome.pages.gitlab.gnome.org/libadwaita/
Source0:		https://gitlab.gnome.org/GNOME/libadwaita/-/archive/%commit/libadwaita-%commit.tar.gz
BuildRequires:	meson vala cmake gi-docgen git gobject-introspection sassc terra-gtk4-devel appstream-devel desktop-file-utils libappstream-glib
Requires:		terra-gtk4
Conflicts:		libadwaita

%description
%summary.

%package devel
Summary: Development files for %{name}
 
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	vala
Recommends:	%{name}-demo = %{version}-%{release}
Recommends:	%{name}-doc = %{version}-%{release}
 
%description devel
Development files for %{name}.
 
 
%package	doc
Summary:	Documentation files for %{name}
BuildArch:	noarch
 
Recommends:	%{name}-devel = %{version}-%{release}
# Because web fonts from upstream are not bundled in the gi-docgen package,
# packages containing documentation generated with gi-docgen should depend on
# this metapackage to ensure the proper system fonts are present.
Recommends:	gi-docgen-fonts
 
%description doc
Documentation files for %{name}.
 
 
%package	demo
Summary:	Demo files for %{name}
BuildArch:	noarch
 
Requires:	%{name} = %{version}-%{release}
Suggests:	%{name}-devel = %{version}-%{release}
 
%description demo
Demo files for %{name}.


%prep
%autosetup -n libadwaita-%commit

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install
mv %buildroot%_libdir/pkgconfig/libadwaita-1.pc %buildroot%_libdir/pkgconfig/libadwaita-nightly.pc
cat %buildroot%_libdir/pkgconfig/libadwaita-nightly.pc


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING
%doc README.md AUTHORS NEWS
%dnl %{_bindir}/adwaita-nightly-demo
%dnl %{_libdir}/libadwaita-nightly.so.0*
%dnl %{_libdir}/girepository-1.0/*.typelib
%dnl %{_datadir}/locale/*/LC_MESSAGES/libadwaita.mo

%files devel
%dnl %dir %{_datadir}/gir-1.0
%dnl %{_datadir}/gir-1.0/*-*.gir
%dnl %{_datadir}/vala/vapi/libadwaita*
%dnl %{_includedir}/libadwaita-*/
%dnl %{_libdir}/libadwaita-*.so
%dnl %{_libdir}/pkgconfig/*-*.pc

%files doc
%doc HACKING.md
%dnl %{_docdir}/libadwaita-*/

%files demo
%dnl %{_datadir}/applications/*.desktop
%dnl %{_datadir}/icons/hicolor/*/apps/*.svg
%dnl %{_metainfodir}/*.metainfo.xml


%changelog
* Tue May 23 2023 windowsboy111 <windowsboy111@fyralabs.com> - 0.1.0-beta.1
- Initial package.
