%global commit c3f01539e3b036ae940e678f5739b37ca0300ce2

Name:           lightdm-kde-greeter
Version:        6.0.2
Release:        1%?dist
Summary:        Login screen using the LightDM framework
License:        GPL-3.0-or-later
URL:            https://invent.kde.org/plasma/%name
Source0:        %url/-/archive/v%version.tar.gz
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  gcc gcc-c++ mold
BuildRequires:  cmake extra-cmake-modules
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(Plasma)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(liblightdm-gobject-1)
BuildRequires:  systemd-rpm-macros
Requires: lightdm
Requires: plasma-workspace-qml
Requires: polkit
Provides: lightdm-greeter

%description
%summary.


%prep
# why the heck do you torture me for godsake.
%autosetup -n %name-v%version-%commit
sed 's/sbin/bin/' -i greeter/CMakeLists.txt


%build
export LDFLAGS="$LDFLAGS -fuse-ld=mold"
%cmake_kf6 \
	-DGREETER_WAYLAND_SESSIONS_FIRST=ON \
	-DGREETER_IMAGES_DIR=%_sharedstatedir/%name/images \
	-DBUILD_TESTING=OFF
%cmake_build


%install
%cmake_install

%find_lang kcm_lightdm           --with-kde
%find_lang lightdm_kde_greeter   --with-kde
%find_lang lightdm_theme_userbar --with-kde

# FIXME: why does it installs to the wrong dir
mv %buildroot/%name %buildroot%_datadir/
mkdir -p %buildroot%_sharedstatedir/%name

%post
%systemd_user_post %name-wifikeeper.service

%preun
%systemd_user_preun %name-wifikeeper.service

%postun
%systemd_user_postun_with_restart %name-wifikeeper.service


%files -f kcm_lightdm.lang -f lightdm_kde_greeter.lang -f lightdm_theme_userbar.lang
%doc README.md
%license COPYING.GPL3
%config(noreplace) %_sysconfdir/lightdm/%name.conf
%dir %_sharedstatedir/%name
%_bindir/%name
%_bindir/lightdm-kde-greeter-rootimage
%_bindir/lightdm-kde-greeter-wifikeeper
%_datadir/applications/kcm_lightdm.desktop
%_datadir/dbus-1/system-services/org.kde.kcontrol.kcmlightdm.service
%_datadir/dbus-1/system.d/org.kde.kcontrol.kcmlightdm.conf
%_datadir/polkit-1/actions/org.kde.kcontrol.kcmlightdm.policy
%_datadir/xgreeters/lightdm-kde-greeter.desktop
%_datadir/%name/
%_kf6_libexecdir/kauth/kcmlightdmhelper
%_qt6_plugindir/plasma/kcms/systemsettings/kcm_lightdm.so
%_userunitdir/lightdm-kde-greeter-wifikeeper.service

%changelog
* Tue Dec 24 2024 madonuko <mado@fyralabs.com> - 6.0.1-1
- Initial package
