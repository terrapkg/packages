%bcond_without mold
%global _desc %{expand:
CoolerControl is a feature-rich cooling device control application for Linux. It has a system daemon
for background device management, as well as a GUI to expertly customize your settings.
}
%global rdnn org.coolercontrol.CoolerControl
# Don't mangle shebangs
%global __brp_mangle_shebangs %{nil}

Name:           coolercontrol
Version:        3.1.1
Release:        2%?dist
Summary:        Cooling device control for Linux
License:        GPL-3.0-or-later
URL:            https://gitlab.com/coolercontrol/coolercontrol
Source0:		%url/-/archive/%version/coolercontrol-%version.tar.gz
Packager:       madonuko <mado@fyralabs.com>
Provides:       coolercontrol-ui
Provides:       coolercontrol-gui
Requires:       hicolor-icon-theme
Requires:       webkit2gtk4.1
Requires:       libappindicator-gtk3
Requires:       coolercontrold
BuildRequires:  nodejs-npm libdrm-devel curl wget file mold
BuildRequires:  systemd-rpm-macros anda-srpm-macros cargo >= 1.75.0 cargo-rpm-macros
BuildRequires:  binutils bison cmake flex gcc gcc-c++ libtool strace protobuf-compiler
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6WebEngineWidgets)
%description %_desc

%package -n coolercontrold
Summary:        Monitor and control your cooling devices.
BuildRequires:  pkgconfig(webkit2gtk-4.1) pkgconfig(openssl) pkgconfig(librsvg-2.0)
BuildRequires:  libappindicator-gtk3-devel
%description -n coolercontrold %_desc
coolercontrold is the main daemon containing the core logic for interfacing with devices, and installed as
"coolercontrold". It is meant to run in the background as a system daemon. It handles all device
communication and data management, additionally connecting to the liqctld daemon for liquidctl
supported devices. It has an API that services client programs like the coolercontrol-gui.


%prep
%autosetup

pushd coolercontrold
%cargo_prep_online
popd

pushd coolercontrol-ui
npm ci --prefer-offline &
popd

wait


%build
pushd coolercontrol-ui
npm run build-only &
popd

pushd coolercontrol
%cmake
%cmake_build
popd

pushd coolercontrol-ui
%make_build
popd

pushd coolercontrold
%{cargo_license_online} > LICENSE.dependencies
wait
cp -rfp ../coolercontrol-ui/dist/* resources/app/
%cargo_build
popd

%install
pushd coolercontrold
install -Dpm755 target/rpm/coolercontrold %buildroot%_bindir/coolercontrold
install -Dpm644 LICENSE.dependencies %buildroot%_datadir/licenses/coolercontrold/LICENSE.dependencies
popd

pushd coolercontrol/
%cmake_install
popd

desktop-file-install --dir=%buildroot%_datadir/applications packaging/metadata/%rdnn.desktop
install -Dpm644 packaging/metadata/%rdnn.svg %buildroot%_iconsdir/hicolor/scalable/apps/%rdnn.svg
install -Dpm644 packaging/metadata/%rdnn.png %buildroot%_iconsdir/hicolor/256x256/apps/%rdnn.svg
for f in packaging/systemd/*.service; do
  install -Dpm644 $f %buildroot%_unitdir/$(basename $f)
done
install -Dpm644 packaging/metadata/%rdnn.metainfo.xml %buildroot%_metainfodir/%rdnn.metainfo.xml


%check
appstream-util validate-relax --nonet %buildroot%_metainfodir/%rdnn.metainfo.xml


%post -n coolercontrold
%systemd_post coolercontrold.service

%preun -n coolercontrold
%systemd_preun coolercontrold.service

%postun -n coolercontrold
%systemd_postun_with_restart coolercontrold.service

%files
%doc README.md
%license LICENSE
%_bindir/coolercontrol
%_datadir/applications/%rdnn.desktop
%_datadir/metainfo/%rdnn.metainfo.xml
%_iconsdir/hicolor/*/apps/%rdnn.svg

%files -n coolercontrold
%doc coolercontrold/README.md
%license LICENSE
%license LICENSE.dependencies
%_bindir/coolercontrold
%_unitdir/coolercontrold.service

%changelog
* Thu Aug 15 2024 madonuko <mado@fyralabs.com> - 1.4.0-1
- Initial package
