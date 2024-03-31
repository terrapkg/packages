%define archive unity_7.7.0+23.04.20230222.2-0ubuntu7.tar.xz

Name:		unity-shell
Version:	7.7.0
Release:	1%?dist
Summary:	Unity is a shell that sings

License:	GPL-3.0-or-later
URL:		https://launchpad.net/unity
Source0:	http://archive.ubuntu.com/ubuntu/pool/universe/u/unity/%archive
Patch0:		0001-Remove-xpathselect-dependency.patch
Patch1:		0002-Remove-ido-dependency.patch
Patch2:		0003-Remove-social-scope.patch

BuildRequires:	cmake
BuildRequires:	g++
BuildRequires:	gcc
BuildRequires:	dee-devel
BuildRequires:	gnome-desktop3-devel
BuildRequires:	pkgconfig(zeitgeist-2.0)
BuildRequires:	libappstream-glib-devel
BuildRequires:	libdbusmenu-devel
BuildRequires:	bamf-devel
BuildRequires:	terra-libindicator-gtk3-devel
BuildRequires:	json-glib-devel
BuildRequires:	libnotify-devel
BuildRequires:	libsigc++20-devel
BuildRequires:	libunity-devel
BuildRequires:	doxygen
BuildRequires:	pam-devel
BuildRequires:	boost-devel
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(nux-4.0)
BuildRequires:	compiz9-devel
BuildRequires:	pkgconfig(unity-misc)
BuildRequires:	chrpath
BuildRequires:	systemd-rpm-macros
BuildRequires:	pkgconfig(libunity-settings-daemon)
Requires:	python3-gobject
Requires:	dconf
Requires:	gsettings-ubuntu-touch-schemas
Requires:	%{name}-data = %{version}-%{release}
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	pam
Requires:	bamf-daemon
Requires:	unity-gtk-module-common
Requires:	compiz9
Requires:	terra-libindicator-gtk3
Recommends:	unity-greeter
Recommends:	unity-scope-home

%description
Unity is a desktop experience that sings. Designed by Canonical and the Ayatana
community, Unity is all about the combination of familiarity and the future. We
bring together visual design, analysis of user experience testing, modern
graphics technologies and a deep understanding of the free software landscape to
produce what we hope will be the lightest, most elegant and most delightful way
to use your PC.

The Unity desktop experience is designed to allow for multiple implementations,
currently, Unity consists of a Compiz plugin based visual interface only, which
is heavily dependent on OpenGL.

%package core
Summary:	Core library for the Unity shell
Group:		System Environment/Libraries
Requires:	%{name}-data = %{version}-%{release}

%description core
This package contains the core library needed for Unity and Unity 2D.

%package core-devel
Summary:	Development files for the core Unity library
Group:		Development/Libraries
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	pkgconfig(dee-1.0)
Requires:	pkgconfig(glib-2.0)
Requires:	pkgconfig(sigc++-2.0)
Requires:	pkgconfig(unity)
Requires:	pkgconfig(nux-4.0)

%description core-devel
This package contains the development files the core Unity library.

%package data
Summary:	Common files for the Unity shell
BuildArch:	noarch
Group:		User Interface/Desktops
# For /usr/etc/pam.d/unity
Recommends:	gnome-keyring-pam
Requires:	%{name} = %{version}-%{release}

%description data
This package contains data (non-arch specific) files to Unity 7.

%package -n python3-uwidgets
Summary:	Widgets for Unity7
Requires:	%{name} = %{version}-%{release}

%description -n python3-uwidgets
This package contains support for widgets for Unity7, based on Blighty.

%prep
%autosetup -n unity-%{version}+23.04.20230222.2 -p1
# Correct/not use ubuntu's API
sed -i 's/ubuntu-lock-on-suspend/lock-enabled/' lockscreen/LockScreenSettings.cpp
# Not actually needed for Unity itself
sed -i '/libgeis/d' CMakeLists.txt

%build
%cmake -DUNITY_PROTOCOL_PRIVATE_LIB=%{_libdir}/libunity/libunity-protocol-private.so.0.0.0 -DCOMPIZ_BUILD_WITH_RPATH=FALSE -DCOMPIZ_PACKAGING_ENABLED=TRUE -DCOMPIZ_PLUGIN_INSTALL_TYPE=package -DUSE_GSETTINGS=TRUE -DENABLE_UNIT_TESTS=FALSE

%cmake_build

pushd uwidgets/
%py3_build
popd

%install
pushd uwidgets/
%py3_install
popd

%cmake_install

# Not the correct directory, /usr/etc/pam.d should be /etc/pam.d
mv -f %{buildroot}%{_prefix}%{_sysconfdir}/* %{buildroot}%{_sysconfdir}
rm -rf %{buildroot}%{_prefix}%{_sysconfdir}
# Upstart init is dead a long time ago and there isn't any package that provides anything to do with it.
rm -rf %{buildroot}%{_datadir}/upstart
# Needed directory for unity-panel-service
mkdir %{buildroot}%{_datadir}/unity/indicators

%find_lang unity

chrpath --delete $RPM_BUILD_ROOT%{_libdir}/compiz/libunityshell.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/compiz/libunitymtgrabhandles.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libunity-core-6.0.so.9.0.0

%py3_shebang_fix $RPM_BUILD_ROOT%{_bindir}/unity
%py3_shebang_fix $RPM_BUILD_ROOT%{_libdir}/unity/makebootchart.py

# For some reason prefix is not set and causes linkage issues
sed -i 's!prefix=!prefix=%{_prefix}!' %{buildroot}%{_libdir}/pkgconfig/unity-core-6.0.pc
sed -i 's!exec_prefix=libexec!exec_prefix=%{_prefix}!' %{buildroot}%{_libdir}/pkgconfig/unity-core-6.0.pc
sed -i 's!libdir=%{_lib}!libdir=%{_libdir}!' %{buildroot}%{_libdir}/pkgconfig/unity-core-6.0.pc
sed -i 's!includedir=include!includedir=%{_prefix}/include!' %{buildroot}%{_libdir}/pkgconfig/unity-core-6.0.pc

%ldconfig_post

%postun
if [ ${1} -eq 0 ]; then
	glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%files
%doc AUTHORS ChangeLog HACKING README
%license COPYING COPYING.LGPL
%{_bindir}/unity
%{_libdir}/compiz/libunitymtgrabhandles.so
%{_libdir}/compiz/libunityshell.so
%{_mandir}/man1/unity.1.gz
%{_mandir}/man1/unity-panel-service.1.gz
%dir %{_libdir}/unity/
%{_libdir}/unity/compiz-config-profile-setter
%{_libdir}/unity/compiz-profile-selector
%{_libdir}/unity/systemd-prestart-check
%{_libdir}/unity/makebootchart.py
%{_libdir}/unity/unity-panel-service
%{_libdir}/unity/unity-active-plugins-safety-check
%{_libdir}/unity/upstart-prestart-check

%files core
%doc AUTHORS ChangeLog HACKING README
%license COPYING COPYING.LGPL
%{_libdir}/libunity-core-6.0.so.*

%files core-devel
%doc AUTHORS ChangeLog HACKING README
%license COPYING COPYING.LGPL
%dir %{_includedir}/Unity-6.0/
%dir %{_includedir}/Unity-6.0/UnityCore/
%{_includedir}/Unity-6.0/UnityCore/*.h
%{_libdir}/libunity-core-6.0.so
%{_libdir}/pkgconfig/unity-core-6.0.pc

%files data -f unity.lang
%doc AUTHORS ChangeLog HACKING README
%license COPYING COPYING.LGPL
%{_datadir}/ccsm/icons/hicolor/64x64/apps/plugin-unityshell.png
%{_datadir}/glib-2.0/schemas/com.canonical.Unity.gschema.xml
%{_datadir}/glib-2.0/schemas/org.compiz.unitymtgrabhandles.gschema.xml
%{_datadir}/glib-2.0/schemas/org.compiz.unityshell.gschema.xml
%dir %{_datadir}/unity/
%dir %{_datadir}/unity/indicators/
%dir %{_datadir}/unity/icons/
%{_datadir}/unity/icons/dash-widgets.json
%{_datadir}/unity/icons/*.png
%{_datadir}/unity/icons/*.svg
%{_datadir}/unity/icons/*.svg.save
%{_datadir}/unity/icons/searchingthedashlegalnotice.html
%dir %{_datadir}/unity/themes/
%{_datadir}/unity/themes/dash-widgets.json
%{_datadir}/compiz/unitymtgrabhandles.xml
%{_datadir}/compiz/unityshell.xml
%dir %{_datadir}/compiz/unitymtgrabhandles
%dir %{_datadir}/compiz/unitymtgrabhandles/images/
%{_datadir}/compiz/unitymtgrabhandles/images/handle-*.png
%{_datadir}/gnome-control-center/keybindings/50-unity-launchers.xml
%{_datadir}/compizconfig/upgrades/*.upgrade
%config %{_sysconfdir}/pam.d/unity
%config %{_sysconfdir}/compizconfig/unity*
%{_userunitdir}/unity*.service
%{_userunitdir}/unity*.target

%files -n python3-uwidgets
%doc README
%license uwidgets/LICENCE
%{_bindir}/uwidgets-runner
%{python3_sitearch}/uwidgets-*.egg-info/
%{python3_sitearch}/uwidgets/

%changelog
%autochangelog
