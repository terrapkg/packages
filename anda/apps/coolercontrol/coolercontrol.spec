%bcond_without mold
%global _desc %{expand:
CoolerControl is a feature-rich cooling device control application for Linux. It has a system daemon
for background device management, as well as a GUI to expertly customize your settings.
}

Name:           coolercontrol
Version:        1.4.0
Release:        1%?dist
Summary:        Cooling device control for Linux
License:        GPL-3.0-or-later
URL:            https://gitlab.com/coolercontrol/coolercontrol
Source0:		%url/-/archive/%version/coolercontrol-%version.tar.gz
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  git-core make python3 nodejs-npm libdrm-devel
BuildRequires:  anda-srpm-macros cargo >= 1.75.0
BuildRequires:  webkit2gtk4.1-devel openssl-devel curl wget file libappindicator-gtk3-devel librsvg2-devel
%description %_desc

%package liqctld
Summary:        CoolerControl daemon for interacting with liquidctl devices on a system level
%description liqctld %_desc
coolercontrol-liqctld is a CoolerControl daemon for interacting with liquidctl devices on a system level, and is
installed as the coolercontrol-liqctld application. Its main purpose is to wrap the underlying
liquidctl library providing an API interface that the main coolercontrol daemon interacts with.
It also enables parallel device communication and access to specific device properties.

%package -n coolercontrold
Summary:        Monitor and control your cooling devices.
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
%make_build build-source &
popd

pushd coolercontrol-ui
npm run build &
pushd src-tauri
%{cargo_license_online} > LICENSE.dependencies &
wait
%cargo_build
mkdir -p ./target/release
mv target/rpm/coolercontrol target/release/
popd
popd


%install
pushd coolercontrold
install -Dpm755 target/rpm/coolercontrold %buildroot%_bindir/coolercontrold
install -Dpm644 LICENSE.dependencies %buildroot%_datadir/licenses/coolercontrold/LICENSE.dependencies
popd

pushd coolercontrol-ui
%make_install
install -Dpm644 LICENSE.dependencies %buildroot%_datadir/licenses/%name/LICENSE.dependencies
popd

# this already handles liqctld
make install-source DESTDIR=%{?buildroot} INSTALL="%{__install} -p"

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies

%files -n coolercontrold
%doc coolercontrold/README.md
%license LICENSE
%license LICENSE.dependencies
%_bindir/coolercontrold

#files liqctld

%changelog
* Thu Aug 15 2024 madonuko <mado@fyralabs.com> - 1.4.0-1
- Initial package
