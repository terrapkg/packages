%global forgeurl https://gitlab.com/vala-panel-project/vala-panel-appmenu
%global commit 0c914bb8e56d291eb1dcaf1036683a86b7c865ec
%forgemeta

Name:    vala-panel-appmenu
Version: 24.05
Release: 1%?dist
License: LGPL-3.0-or-later
Summary: Application Menu plugin for vala-panel
Group:   System/GUI/Other
URL:     %{forgeurl}
Source:  %{forgesource}

BuildRequires: fdupes
BuildRequires: bamf-daemon
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: gettext
BuildRequires: cmake
BuildRequires: vala
BuildRequires: systemd-rpm-macros
BuildRequires: pkgconfig(libxfce4panel-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: java-devel
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libxfconf-0)
BuildRequires: pkgconfig(budgie-1.0)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libbamf3)
BuildRequires: pkgconfig(libxfce4panel-2.0)
BuildRequires: pkgconfig(libxfconf-0)
BuildRequires: pkgconfig(libwnck-3.0) >= 3.4.0
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(dbusmenu-glib-0.4)
BuildRequires: pkgconfig(vala-panel)
BuildRequires: pkgconfig(libmatepanelapplet-4.0)
Provides:      vala-panel-appmenu-plugin = %{version}
Requires:      bamf-daemon

%description
Vala Panel Application Menu is a Global Menu applet for use with Vala Panel,
xfce4-panel and mate-panel (Budgie 10.x is also planned).
Unity-gtk-module is used as a backend

%package -n xfce4-vala-panel-appmenu-plugin
Summary:      Application Menu plugin for xfce4-panel
Requires:     xfce4-panel
Requires:     vala-panel-appmenu-gtk-module%{?_isa} == %{version}-%{release}

%description -n xfce4-vala-panel-appmenu-plugin
XFCE4 desktop plugin for %{name}.


%package -n mate-vala-panel-appmenu-plugin
Summary:      Application Menu plugin for xfce4-panel
Requires:     mate-panel
Requires:     vala-panel-appmenu-gtk-module%{?_isa} == %{version}-%{release}

%description -n mate-vala-panel-appmenu-plugin
Mate desktop plugin for %{name}.


%package -n budgie-vala-panel-appmenu-plugin
Summary:      Application Menu plugin for xfce4-panel
Requires:     budgie-desktop
Requires:     vala-panel-appmenu-gtk-module%{?_isa} == %{version}-%{release}

%description -n budgie-vala-panel-appmenu-plugin
Budgie desktop plugin for %{name}.


%package devel
Summary:        Development package for budgie-desktop
Requires:       vala-panel-appmenu-gtk-module%{?_isa} = %{version}-%{release}
 
%description devel
Header files, libraries, and other files for developing %{name}.


%package -n vala-panel-appmenu-gtk-module
Summary:    Gtk3MenuShell D-Bus exporter

%description -n vala-panel-appmenu-gtk-module
GTK (2, 3) module that exports GtkMenuShells over D-Bus.


%package -n vala-panel-appmenu-jayatana-module
Summary:    Vala appmenu support for Java Swing applications

%description -n vala-panel-appmenu-jayatana-module
Vala appmenu support for Java Swing applications.

%prep
%forgeautosetup

%build
%meson -Dxfce=enabled -Dvalapanel=enabled -Djayatana=enabled \
       -Dbudgie=enabled -Dmate=enabled
%meson_build

%install
%meson_install
%fdupes %buildroot%_datadir/locale/
%find_lang vala-panel-appmenu

%files -f vala-panel-appmenu.lang
%doc README.md
%license LICENSE
%dir %{_libdir}/vala-panel
%dir %{_libdir}/vala-panel/applets
%{_libdir}/vala-panel/applets/libappmenu.so
%dir %{_libexecdir}/vala-panel
%{_libexecdir}/vala-panel/appmenu-registrar
%{_docdir}/appmenu-gtk-module/
%dir %{_datadir}/licenses/appmenu-gtk-module
%{_datadir}/licenses/appmenu-gtk-module/LICENSE
%{_datadir}/dbus-1/services/com.canonical.AppMenu.Registrar.service
%{_datadir}/glib-2.0/schemas/org.valapanel.appmenu.gschema.xml
%{_datadir}/vala-panel/applets/org.valapanel.appmenu.plugin
%{_datadir}/vala/vapi/appmenu-glib-translator.*
%dnl %{_datadir}/gir-1.0/AppmenuGLibTranslator-%version.gir
%{_includedir}/appmenu-glib-translator/importer.h
%dnl %{_libdir}/girepository-1.0/AppmenuGLibTranslator-%version.typelib
%{_libdir}/libappmenu-glib-translator.*

%files -n vala-panel-appmenu-gtk-module
%{_userunitdir}/appmenu-gtk-module.service
%{_libdir}/libappmenu-gtk2-parser.so.*
%{_libdir}/libappmenu-gtk3-parser.so.*
%{_libdir}/gtk-2.0/modules/libappmenu-gtk-module.so
%{_libdir}/gtk-3.0/modules/libappmenu-gtk-module.so
%{_datadir}/glib-2.0/schemas/org.appmenu.gtk-module.gschema.xml

%files -n vala-panel-appmenu-jayatana-module
%{_datadir}/java/*.jar
%dir %{_libdir}/jayatana
%{_libdir}/jayatana/*.so

%files -n xfce4-vala-panel-appmenu-plugin
%{_libdir}/xfce4/panel/plugins/libappmenu-xfce.so
%{_datadir}/xfce4/panel/plugins/appmenu.desktop

%files -n mate-vala-panel-appmenu-plugin
%{_libdir}/mate-panel/libappmenu-mate.so
%{_datadir}/mate-panel/applets/org.vala-panel.appmenu.mate-panel-applet

%files -n budgie-vala-panel-appmenu-plugin
%dir %{_libdir}/budgie-desktop/plugins/budgie-appmenu-plugin
%{_libdir}/budgie-desktop/plugins/budgie-appmenu-plugin/appmenu-budgie.plugin
%{_libdir}/budgie-desktop/plugins/budgie-appmenu-plugin/libappmenu-budgie.so

%files devel
%dir %{_includedir}/appmenu-gtk-parser
%{_includedir}/appmenu-gtk-parser/*.h
%{_libdir}/libappmenu-gtk2-parser.so
%{_libdir}/libappmenu-gtk3-parser.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
