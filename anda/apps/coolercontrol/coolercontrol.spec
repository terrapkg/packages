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
Release:        3%?dist
Summary:        Cooling device control for Linux
ExclusiveArch:  x86_64 aarch64
License:        GPL-3.0-or-later
URL:            https://gitlab.com/coolercontrol/coolercontrol
Source0:        %url/-/archive/%version/coolercontrol-%version.tar.gz
Packager:       madonuko <mado@fyralabs.com>
Requires:       hicolor-icon-theme
Requires:       coolercontrold = %{version}
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  autoconf automake gcc gcc-c++
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6WebChannel)
%description %_desc

%package -n coolercontrold
Summary:        Monitor and control your cooling devices.
License:        GPL-3.0-or-later AND (Apache-2.0 OR MIT) AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND AGPL-3.0-or-later AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR MIT OR Apache-2.0) AND BSD-3-Clause AND MIT AND (BSD-3-Clause OR Apache-2.0) AND (BSD-3-Clause OR MIT) AND (CC0-1.0 OR Apache-2.0) AND ISC AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)
BuildRequires:  anda-srpm-macros cargo-rpm-macros rust-srpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libdrm_amdgpu)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  nodejs-npm
Recommends:     python3-liquidctl
%description -n coolercontrold %_desc
This is the system daemon for CoolerControl.
CoolerControl is an open-source application for monitoring and controlling supported cooling
devices. It features an intuitive interface, flexible control options, and live thermal data to keep
your system quiet, cool, and stable.


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
%make_build
popd

pushd coolercontrold
%{cargo_license_online} > LICENSE.dependencies
%{cargo_license_summary_online}
wait
cp -rfp ../coolercontrol-ui/dist/* resources/app/
%{cargo_build} --locked
popd

pushd coolercontrol
%cmake
%cmake_build
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
install -Dpm644 packaging/metadata/%rdnn-alert.svg %buildroot%_iconsdir/hicolor/scalable/apps/%rdnn-alert.svg
install -Dpm644 packaging/metadata/%rdnn-symbolic.svg %buildroot%_iconsdir/hicolor/symbolic/apps/%rdnn-symbolic.svg
install -Dpm644 packaging/metadata/%rdnn-symbolic-alert.svg %buildroot%_iconsdir/hicolor/symbolic/apps/%rdnn-symbolic-alert.svg
install -Dpm644 packaging/metadata/%rdnn.png %buildroot%_iconsdir/hicolor/256x256/apps/%rdnn.png
install -Dpm644 packaging/metadata/%rdnn-alert.png %buildroot%_iconsdir/hicolor/256x256/apps/%rdnn-alert.png
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
%doc CHANGELOG.md
%license LICENSE
%_bindir/coolercontrol
%_datadir/applications/%rdnn.desktop
%_datadir/metainfo/%rdnn.metainfo.xml
%_iconsdir/hicolor/*/apps/%rdnn.*
%_iconsdir/hicolor/*/apps/%rdnn-alert.*
%_iconsdir/hicolor/*/apps/%rdnn-symbolic.svg
%_iconsdir/hicolor/*/apps/%rdnn-symbolic-alert.svg

%files -n coolercontrold
%doc coolercontrold/README.md
%license LICENSE
%license LICENSE.dependencies
%_bindir/coolercontrold
%_unitdir/coolercontrold.service

%changelog
* Sat Feb 28 2026 Guy Boldon <gb@guyboldon.com> - 3.1.1-2
- Updated dependencies and build to match current version

* Thu Aug 15 2024 madonuko <mado@fyralabs.com> - 1.4.0-1
- Initial package
