%global forgeurl https://gitlab.com/ubuntu-unity/unity-x/unityx
%global commit 46dd5199d1cce639f559eda4519aff77ef9c4433
%forgemeta

%define __python /usr/bin/python3

Name:          unityx-shell
Version:       1.7.7
Release:       1%?dist
Summary:       UnityX is a smaller shell based on Unity7

License:       GPL-3.0 AND LGPL-3.0
URL:           https://gitlab.com/ubuntu-unity/unity-x/unityx
Source0:       %{url}/-/archive/%commit/unityx-%commit.tar.bz2
Source2:       https://gitlab.xfce.org/panel-plugins/xfce4-windowck-plugin/-/commit/dee596492f006d02e2b39abd072ddd7b37fefe82.diff
Patch0:        0001-Remove-social-scope.patch


BuildRequires: cmake
BuildRequires: g++
BuildRequires: gcc
BuildRequires: chrpath
BuildRequires: pkgconfig(dee-1.0)
BuildRequires: pkgconfig(unity-settings-daemon)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: zeitgeist-devel
BuildRequires: libappstream-glib-devel
BuildRequires: libdbusmenu-devel
BuildRequires: bamf-devel
BuildRequires: terra-libindicator-gtk3-devel
BuildRequires: json-glib-devel
BuildRequires: libnotify-devel
BuildRequires: libsigc++20-devel
#BuildRequires: xpathselect-devel
#BuildRequires: libunity-devel
BuildRequires: doxygen
BuildRequires: pam-devel
BuildRequires: boost-devel
BuildRequires: pkgconfig(nux-4.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(unity-protocol-private)
BuildRequires: libunity libunity-devel
# unityx-shell-xfce4-windowck-plugin
BuildRequires: pkgconfig(libwnck-3.0)
BuildRequires: pkgconfig(libxfconf-0)
BuildRequires: pkgconfig(libxfce4util-1.0)
BuildRequires: pkgconfig(libxfce4ui-2)
BuildRequires: pkgconfig(libxfce4panel-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: xfce4-vala
BuildRequires: xfce4-dev-tools
BuildRequires: python3-devel

# Various things are missing that it won't run and it gives a segmentfault if Unity is missing?
# Needs more investigating
Requires:      unity-shell
Requires:      unity-scope-home
Requires:      python3-pydbus
Requires:      python3-psutil
Requires:      unity-asset-pool
Requires:      libunity-misc-devel
Requires:      geis-devel
Requires:      unity-settings-daemon
Requires:      unity-gtk3-module
Requires:      unity-gtk2-module
Requires:      terra-libindicator-gtk3
Requires:      plotinus%{?_isa} = %{version}-%{release}
Requires:      bamf-daemon
Requires:      xbindkeys
# For default configuration
Requires:      %{name}-xfce4-windowck-plugin%{?_isa} = %{version}-%{release}
Requires:      nemo
Requires:      blueman
Requires:      network-manager-applet
Requires:      xfce4-vala-panel-appmenu-plugin
Requires:      xfwm4

%description
UnityX is a shell based off code from Unity7 with lighter dependencies and more
customizability.

%package xfce4-windowck-plugin
Summary:  Core library for the Unity shell
Requires: %{name}%{?_isa} = %{version}-%{release}

%description xfce4-windowck-plugin
This package contains the core library needed for Unity and Unity 2D.

%package devel
Summary:  Development files for the core Unity library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig(dee-1.0)
Requires: pkgconfig(glib-2.0)
Requires: pkgconfig(sigc++-2.0)
Requires: pkgconfig(unity)
Requires: pkgconfig(nux-4.0)

%description devel
This package contains the development files the core Unity library.

%package -n plotinus
Summary:  Automatic testing for Unity

%description -n plotinus
This package contains the autopilot framework, which allows for triggering
keyboard and mouse events automatically. This package also contains the bindings
needed for writing automated tests in Python.

%prep
%autosetup -n unityx-%commit -p1

%build
# Wrong paths
sed -i 's!lib/{arch}-linux-gnu!%{_lib}!' unityx/unityx
sed -i 's!%{_lib}/bamf/bamfdaemon!libexec/bamf/bamfdaemon!' unityx/unityx
sed -i 's!unity-settings-daemon!%{_libexecdir}/unity-settings-daemon!' unityx/unityx
%py3_shebang_fix unityx/unityx

# Fix invalid argument calling dbus-update-activation-environment
sed -i 's/'--all', //' unityx/unityx

# The caches again!
rm -fv unityx/windowck-plugin/po/.intltool-merge-cache*

%cmake -DENABLE_X_SUPPORT=ON -DUNITY_PROTOCOL_PRIVATE_LIB=%{_libdir}/libunity/libunity-protocol-private.so.0.0.0 -DCOMPIZ_BUILD_WITH_RPATH=FALSE -DCOMPIZ_PACKAGING_ENABLED=TRUE -DCOMPIZ_PLUGIN_INSTALL_TYPE=package -DUSE_GSETTINGS=TRUE -DENABLE_UNIT_TESTS=FALSE
%cmake_build

pushd unityx/plotinus
# Wrong path again
sed -i 's/LIBRARY DESTINATION lib/LIBRARY DESTINATION %{_lib}/' CMakeLists.txt
%cmake
%cmake_build
popd

pushd unityx/windowck-plugin
# Upstream patch to fix icons being blurry
patch -i %{SOURCE2} -p1

NOCONFIGURE=1 \
./autogen.sh

%configure --disable-static
%make_build
popd

%install
%cmake_install

pushd unityx/plotinus
%cmake_install
popd

pushd unityx/windowck-plugin
%make_install
rm -fv %{buildroot}%{_libdir}/*.la
popd

chrpath --delete %{buildroot}%{_libdir}/libunityx-core-6.0.so.9.0.0

pushd %{buildroot}
ln -s %{_libdir}/unity .%{_libdir}/unityx
rm -rf .%{_datadir}/unityx
ln -s %{_datadir}/unity .%{_datadir}/unityx
popd

%find_lang unityx
%find_lang xfce4-windowck-plugin

%ldconfig_post

%postun
if [ ${1} -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%files -f unityx.lang
%doc AUTHORS ChangeLog README.md
%license COPYING COPYING.LGPL
%{_bindir}/unityx*
%{_libdir}/unityx
%{_libdir}/libunityx-core-6.0.so.*
%{_datadir}/glib-2.0/schemas/org.unityd.UnityX.gschema.xml
%{_datadir}/glib-2.0/schemas/org.unityd.UnityX.user-interface.gschema.xml
%{_datadir}/unityx
%{_datadir}/xsessions/unityx.desktop

%files -n plotinus
%doc unityx/plotinus/README.md
%license COPYING COPYING.LGPL
%{_bindir}/plotinus
%{_libdir}/libplotinus.so
%{_datadir}/glib-2.0/schemas/org.unityd.UnityX.plotinus.gschema.xml

%files devel
%dir %{_includedir}/UnityX-6.0/UnityCore/
%{_includedir}/UnityX-6.0/UnityCore/*.h
%{_libdir}/libunityx-core-6.0.so
%{_libdir}/pkgconfig/unityx-core-6.0.pc

%files xfce4-windowck-plugin -f xfce4-windowck-plugin.lang
%doc unityx/windowck-plugin/AUTHORS unityx/windowck-plugin/NEWS unityx/windowck-plugin/README.md
%license unityx/windowck-plugin/COPYING
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/themes/Windowck/
%{_datadir}/themes/Windowck-dark/
%{_datadir}/xfce4/panel/plugins/*.desktop

%changelog
%autochangelog
