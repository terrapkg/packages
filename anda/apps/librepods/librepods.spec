%global appid com.github.librepods

Name:           librepods
Summary:        AirPods liberated from Apple's ecosystem
Version:        0.1.0
Release:        1%?dist
License:        GPL-3.0-only
URL:            https://github.com/kavishdevar/librepods
Source0:        %url/archive/refs/tags/linux-v%version.tar.gz
Source1:        com.github.librepods.metainfo.xml

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtconnectivity-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  openssl-devel
BuildRequires:  anda-srpm-macros
BuildRequires:  terra-appstream-helper

Requires: glibc
Requires: openssl
Requires: qt6-qtbase
Requires: qt6-qtconnectivity
Requires: qt6-qtdeclarative

%description
LibrePods unlocks Apple's exclusive AirPods features on non-Apple devices.
Get access to noise control modes, adaptive transparency, ear detection,
hearing aid, customized transparency mode, battery status, and more - all the
premium features you paid for but Apple locked to their ecosystem.

%prep
%autosetup -n %{name}-linux-v%{version}

%build
pushd linux
%cmake
%cmake_build
popd

%install
install -Dm644 linux-rust/assets/icon.png %{buildroot}%{_iconsdir}/hicolor/512x512/apps/librepods.png
pushd linux
%cmake_install
popd
%terra_appstream -o %{SOURCE1}

%files
%doc README.md linux/README.md CHANGELOG.md
%license LICENSE
%{_bindir}/librepods
%{_datadir}/applications/me.kavishdevar.librepods.desktop
%{_metainfodir}/com.github.librepods.metainfo.xml
%{_iconsdir}/hicolor/512x512/apps/librepods.png

%changelog
* Wed Nov 19 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
