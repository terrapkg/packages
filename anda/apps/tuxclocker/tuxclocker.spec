Name:           tuxclocker
Version:        1.5.1
Release:        1%?dist
Summary:        Qt overclocking tool for GNU/Linux 
License:        GPL-3.0
URL:            https://github.com/Lurkki14/tuxclocker
# boost qt5-qtbase qt5-qtcharts
Requires:       hicolor-icon-theme
BuildRequires:  git-core meson hwdata qt5-qttools gettext anda-srpm-macros
BuildRequires:  boost-devel qt5-qtbase-devel qt5-qtcharts-devel libdrm-devel libXNVCtrl-devel openssl-devel
Recommends:     xorg-x11-drv-nvidia libdrm libXNVCtrl hwdata

%description
TuxClocker is a hardware controlling and monitoring program.
TuxClocker consists of a DBus daemon and a Qt GUI that uses the daemon.

%prep
git clone --recursive %url .
git checkout %version

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%_bindir/tuxclocker-qt
%_bindir/tuxclockerd
%_libdir/libtuxclocker.so
%_libdir/tuxclocker/
%_datadir/applications/tuxclocker.desktop
%_datadir/dbus-1/system-services/org.tuxclocker.service
%_datadir/dbus-1/system.d/org.tuxclocker.conf
%_datadir/locale/*/LC_MESSAGES/tuxclocker.mo
%_iconsdir/hicolor/scalable/apps/tuxclocker-logo.svg

%changelog
%autochangelog
