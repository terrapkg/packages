%global forgeurl https://gitlab.com/ubports/development/core/lomiri
%global commit 426b9f3436938f149490cee340e1fab79ee7b650
%forgemeta

Name:          lomiri
Version:       0.2.1
Release:       1%{?dist}
Summary:       A convergent desktop environment by Ubports

License:       GPLv3 AND LGPLv3
URL:           https://gitlab.com/ubports/development/core/lomiri
Source0:       %{url}/-/archive/%commit/lomiri-%commit.tar.gz
Patch0:        https://sources.debian.org/data/main/l/lomiri/0.1.2-3/debian/patches/disable-broken-test-mir2.patch
Patch1:        0001-Add-support-for-both-older-qtmir-and-newer-qtmir-wit.patch
BuildRequires: cmake
BuildRequires: cmake-extras
BuildRequires: pkgconfig
BuildRequires: g++
BuildRequires: gcc
#BuildRequires: doxygen
#BuildRequires: doxyqml
BuildRequires: pkgconfig(lomiri-schemas)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(lomiri-shell-application)
BuildRequires: pkgconfig(qtmirserver)
BuildRequires: pkgconfig(geonames)
BuildRequires: pkgconfig(lomiri-shell-launcher)
BuildRequires: pkgconfig(qmenumodel)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(lomiri-app-launch-0)
BuildRequires: pkgconfig(LomiriGestures)
BuildRequires: pkgconfig(miral)
BuildRequires: pkgconfig(miroil)
BuildRequires: pkgconfig(deviceinfo)
BuildRequires: pkgconfig(gsettings-qt)
BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: pkgconfig(libqtdbusmock-1)
BuildRequires: pkgconfig(LomiriSystemSettings)
BuildRequires: pkgconfig(liblightdm-qt5-3)
BuildRequires: pkgconfig(lomiri-connectivity-qt1)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(libusermetricsoutput-1)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(ldm-common)
BuildRequires: pkgconfig(libevdev)
BuildRequires: dbus-test-runner-devel
BuildRequires: dpkg-dev
BuildRequires: pam-devel
BuildRequires: properties-cpp-devel
BuildRequires: qt-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: systemd-rpm-macros
Recommends:    lomiri-session
# Most of these are for other libs that rpm doesn't find
Requires:      libusermetrics
Requires:      deviceinfo
Requires:      lomiri-system-settings
Requires:      qmenumodel
Requires:      xorg-x11-server-Xwayland
Requires:      ayatana-indicator-sound
Requires:      ayatana-indicator-messages
Requires:      ayatana-indicator-datetime
Requires:      ayatana-indicator-notifications
Requires:      ayatana-indicator-session
Requires:      lomiri-sounds
Requires:      lomiri-ui-toolkit
Requires:      lomiri-download-manager
Requires:      suru-icon-theme
Requires:      lomiri-schemas
# For some reason Lomiri `/usr/bin/lomiri` requires it for testability
Requires: %{name}-tests%{?_isa} = %{version}-%{release}

%description
Lomiri, Previously Unity8 is a convergent desktop environment built with Qt.

# Documentation needs doxyqml
#package doc
#Summary: Documentation files for {name}
#BuildArch: noarch

#description doc
#The {name}-doc package contains documenation files for {name}.

%package tests
Summary: Test files for %{name}
Requires: dbus-test-runner
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The %{name}-tests package contains test files for %{name}.

%prep
%autosetup -n lomiri-%commit -p1
# Ubuntu specific, may have to be updated every background image change on Gnome or Ubuntu
for i in $(grep -rl warty-final-ubuntu); do
sed -i 's!warty-final-ubuntu.png!f38/default/f38-01-day.png!' $i
done

%build
%cmake -DWerror=OFF -DDEB_HOST_MULTIARCH=%{_arch} -DCMAKE_INSTALL_LOCALSTATEDIR="%{_localstatedir}" -DDISPLAYED_DISTRO_NAME="Fedora" -DUSE_MIROIL=1
%cmake_build

%install
%cmake_install
#cd tests/autopilot && python setup.py install
%find_lang %{name}

mkdir -m 0755 -p %{buildroot}%{_sysconfdir}/lomiri %{buildroot}%{_sysconfdir}/lomirisensors
install -Dm644 data/devices.conf %{buildroot}%{_sysconfdir}/lomiri
install -Dm644 data/test.sensors %{buildroot}%{_sysconfdir}/lomirisensors

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license COPYING COPYING.LGPL
%dir %{_sysconfdir}/lomiri
%config %{_sysconfdir}/lomiri/devices.conf
%dir %{_sysconfdir}/lomirisensors
%config %{_sysconfdir}/lomirisensors/test.sensors
%{_bindir}/indicators-client
%{_bindir}/lomiri
%{_userunitdir}/*.service
%{_libdir}/liblomiri-private.so*
%dir %{_libdir}/lomiri
%dir %{_libdir}/lomiri/qml
%{_libdir}/lomiri/qml/AccountsService/
%{_libdir}/lomiri/qml/Cursor/
%{_libdir}/lomiri/qml/GlobalShortcut/
%{_libdir}/lomiri/qml/Greeter/
%{_libdir}/lomiri/qml/LightDM/
%{_libdir}/lomiri/qml/Lomiri/
%{_libdir}/lomiri/qml/Powerd/
%{_libdir}/lomiri/qml/ProcessControl/libProcessControl-qml.so
%{_libdir}/lomiri/qml/ProcessControl/qmldir
%{_libdir}/lomiri/qml/ScreenshotDirectory/
%{_libdir}/lomiri/qml/SessionBroadcast/
%{_libdir}/lomiri/qml/UInput/
%{_libdir}/lomiri/qml/Utils/
%{_libdir}/lomiri/qml/WindowManager/
%{_libdir}/lomiri/qml/Wizard/
%{_libexecdir}/lomiri-systemd-wrapper
%{_libexecdir}/Xwayland.lomiri
%{_datadir}/accountsservice/interfaces/com.lomiri.shell.AccountsService.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/interfaces/com.lomiri.shell.AccountsService.xml
%{_datadir}/dbus-1/interfaces/com.lomiri.ProcessControl.xml
%{_datadir}/lightdm/greeters/lomiri-greeter.desktop
%{_datadir}/lightdm/lightdm.conf.d/51-lomiri-greeter.conf
%dir %{_datadir}/lomiri
%{_datadir}/lomiri/unlock-device
%{_datadir}/lomiri/qmldir
%{_datadir}/lomiri/*.qml
%{_datadir}/lomiri/ApplicationMenus/
%{_datadir}/lomiri/Components/
%{_datadir}/lomiri/Notifications/
%{_datadir}/lomiri/Stage/
%{_datadir}/lomiri/Panel/
%{_datadir}/lomiri/Tutorial/
%{_datadir}/lomiri/graphics/
%{_datadir}/lomiri/Rotation/
%{_datadir}/lomiri/Greeter/
%{_datadir}/lomiri/Wizard/
%{_datadir}/lomiri/Launcher/
%dir %{_sharedstatedir}/lomiri
%{_sharedstatedir}/lomiri/version
%{_sharedstatedir}/polkit-1/localauthority/10-vendor.d/50-com.lomiri.wizard.pkla


%files tests
%{_bindir}/lomiri-mock-indicator-service
%{_libdir}/lomiri/qml/mocks/
%{_libdir}/lomiri/qml/utils/
%dir %{_libexecdir}/lomiri
%{_libexecdir}/lomiri/uqmlscene
%dir %{_libexecdir}/lomiri/tests
%{_libexecdir}/lomiri/tests/plugins/
%{_libexecdir}/lomiri/tests/qmltests/
%{_libexecdir}/lomiri/tests/scripts/
%{_datadir}/lomiri/mocks/
%{_datadir}/lomiri/tests/

%changelog
%autochangelog
