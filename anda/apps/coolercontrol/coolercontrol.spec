%bcond_without mold
%global _desc %{expand:
CoolerControl is a feature-rich cooling device control application for Linux. It has a system daemon
for background device management, as well as a GUI to expertly customize your settings.
}
%global rdnn org.coolercontrol.CoolerControl

Name:           coolercontrol
Version:        1.4.0
Release:        1%?dist
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
BuildRequires:  git-core make nodejs-npm libdrm-devel curl wget file mold
BuildRequires:  systemd-rpm-macros anda-srpm-macros cargo >= 1.75.0 cargo-rpm-macros
BuildRequires:  autoconf automake binutils bison flex gcc gcc-c++ gdb libtool pkgconf strace
BuildRequires:  pkgconfig(webkit2gtk-4.1) pkgconfig(openssl) pkgconfig(librsvg-2.0)
BuildRequires:  libappindicator-gtk3-devel
BuildRequires:  python3-devel python3-wheel python3-liquidctl python3-setproctitle python3-fastapi python3-uvicorn python3-pip
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
%description %_desc

%package liqctld
Summary:        CoolerControl daemon for interacting with liquidctl devices on a system level
Requires:       coolercontrold
%description liqctld %_desc
coolercontrol-liqctld is a CoolerControl daemon for interacting with liquidctl devices on a system level, and is
installed as the coolercontrol-liqctld application. Its main purpose is to wrap the underlying
liquidctl library providing an API interface that the main coolercontrol daemon interacts with.
It also enables parallel device communication and access to specific device properties.

%package -n coolercontrold
Summary:        Monitor and control your cooling devices.
Requires:       coolercontrol-liqctld
%description -n coolercontrold %_desc
coolercontrold is the main daemon containing the core logic for interfacing with devices, and installed as
"coolercontrold". It is meant to run in the background as a system daemon. It handles all device
communication and data management, additionally connecting to the liqctld daemon for liquidctl
supported devices. It has an API that services client programs like the coolercontrol-gui.


%prep
%autosetup

pushd coolercontrold
%cargo_prep_online &
popd

pushd coolercontrol-ui
npm ci --prefer-offline &
pushd src-tauri
%cargo_prep_online &
popd
popd

wait


%build
pushd coolercontrold
%{cargo_license_online} > LICENSE.dependencies &
%cargo_build -- &
popd

pushd coolercontrol-liqctld
%pyproject_wheel
popd

pushd coolercontrol-ui
npm run build &
pushd src-tauri
%{cargo_license_online} > LICENSE.dependencies &
wait
%cargo_build -f custom-protocol
popd
popd


%install
pushd coolercontrol-liqctld
#define _pyproject_wheeldir .
%pyproject_install
%pyproject_save_files coolercontrol_liqctld
popd

pushd coolercontrold
install -Dpm755 target/rpm/coolercontrold %buildroot%_bindir/coolercontrold
install -Dpm644 LICENSE.dependencies %buildroot%_datadir/licenses/coolercontrold/LICENSE.dependencies
popd

pushd coolercontrol-ui/src-tauri
install -Dpm755 target/rpm/coolercontrol %buildroot%_bindir/coolercontrol
install -Dpm644 LICENSE.dependencies %buildroot%_datadir/licenses/%name/LICENSE.dependencies
popd

install -Dpm644 packaging/systemd/coolercontrol-liqctld.service %buildroot%_unitdir
desktop-file-install --dir=%buildroot%_datadir/applications packaging/metadata/%rdnn.desktop
install -Dpm644 packaging/metadata/%rdnn.svg %buildroot%_iconsdir/hicolor/scalable/apps/%rdnn.svg
install -Dpm644 packaging/metadata/%rdnn.png %buildroot%_iconsdir/hicolor/256x256/apps/%rdnn.svg
for f in packaging/systemd/*.service; do
  install -Dpm644 $f %buildroot%_unitdir/$(basename $f)
done
install -Dpm644 packaging/metadata/%rdnn.metainfo.xml %buildroot%_metainfodir/%rdnn.metainfo.xml


%check
appstream-util validate-relax --nonet %buildroot%_metainfodir/%rdnn.metainfo.xml
%pyproject_check_import


%post -n coolercontrold
%systemd_post coolercontrold.service

%preun -n coolercontrold
%systemd_preun coolercontrold.service

%postun -n coolercontrold
%systemd_postun_with_restart coolercontrold.service

# coolercontrold.service automatically uses the liqctld service, so there are
# no scriptlets for liqctld.


%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%_datadir/applications/%rdnn.desktop
%_datadir/metainfo/%rdnn.metainfo.xml
%_iconsdir/hicolor/*/apps/%rdnn.svg

%files -n coolercontrold
%doc coolercontrold/README.md
%license LICENSE
%license LICENSE.dependencies
%_bindir/coolercontrold
%_unitdir/coolercontrold.service

%files liqctld -f %pyproject_files
%doc coolercontrol-liqctld/README.md
%license LICENSE
%_bindir/coolercontrol-liqctld
%_unitdir/coolercontrol-liqctld.service

%changelog
* Thu Aug 15 2024 madonuko <mado@fyralabs.com> - 1.4.0-1
- Initial package
