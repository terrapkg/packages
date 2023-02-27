%global forgeurl https://gitlab.com/vala-panel-project/vala-panel
%global commit ead4e7a36b0e4b0a2ac43c5d9ca17eb753461afe

%forgemeta

Name:    vala-panel
Version: 0.5.0
Release: %autorelease
License: LGPL-3.0+
Summary: This package provides Application Menu plugin for vala-panel
URL:     %{forgeurl}
Source:  %{forgesource}

BuildRequires: meson
BuildRequires: vala
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(libwnck-3.0)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(libpeas-gtk-1.0)
BuildRequires: gtk-layer-shell-devel

%description
This is Application Menu (Global Menu) plugin.
It built using Unity protocol and libraries,
and share all Unity limitations and advancements.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
%forgeautosetup

%build
%meson -Dwnck=enabled -Dplatforms='layer-shell,x11'
%meson_build

%install
%meson_install
%find_lang %{name}
# Already packaged
rm -rf %{buildroot}%{_datadir}/vala-panel/doc

desktop-file-validate %{buildroot}%{_datadir}/applications/org.valapanel.application.desktop
# Seems to succeed with other appstream checkers and works but fails
#appstream-util validate-relax --nonet {buildroot}{_datadir}/appdata/org.valapanel.application.appdata.xml

%files -f %{name}.lang
%doc README.md LICENSE
%license LICENSE
%{_sysconfdir}/xdg/vala-panel/
%{_bindir}/vala-*
%{_libdir}/libvalapanel.so.*
%dir %{_libdir}/vala-panel
%dir %{_libdir}/vala-panel/applets
%{_libdir}/vala-panel/applets/*.so
%{_datadir}/appdata/org.valapanel.application.appdata.xml
%{_datadir}/applications/org.valapanel.application.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/96x96/apps/vala-panel.png
%{_datadir}/icons/hicolor/scalable/apps/vala-panel.svg
%{_datadir}/man/man1/*.1.gz
%dir %{_datadir}/vala-panel
%dir %{_datadir}/vala-panel/applets
%{_datadir}/vala-panel/applets/*.plugin
%dir %{_datadir}/vala-panel/images
%{_datadir}/vala-panel/images/background.png

%files devel
%dir %{_includedir}/vala-panel
%{_includedir}/vala-panel/*.h
%{_libdir}/libvalapanel.so
%{_libdir}/pkgconfig/vala-panel.pc
%{_datadir}/vala/vapi/vala-panel.*

%changelog
%autochangelog
