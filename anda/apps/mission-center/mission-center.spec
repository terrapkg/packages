%global forgeurl0 https://gitlab.com/mission-center-devs/mission-center
Version: 1.0.0
%global tag0 v%{version}

%global forgeurl1 https://gitlab.com/mission-center-devs/gng
%global commit1 dcc600e18cfa17d56d0f12a61be2702cc7a015ae


%forgemeta -a

Name:           mission-center
Release:        %autorelease
Summary:        Monitor your CPU, Memory, Disk, Network and GPU usage

License:        GPL-3.0-or-later
URL:            %{forgeurl0}
Source0:         %{forgesource0}
Source1:         %{forgesource1}
Patch0: https://gitlab.com/mission-center-devs/mission-center/-/merge_requests/319.diff
Provides: bundled(mission-center-magpie)
Provides: bundled(nvtop) = 3.2.0
#mission centere uses a patched version of nvtop

BuildRequires: meson >= 0.63
BuildRequires: cargo
BuildRequires: cmake
BuildRequires: gcc
BuildRequires:  gcc-c++
BuildRequires: pkgconfig(protobuf)
BuildRequires: pkgconfig(python3)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(egl)
BuildRequires: libadwaita-devel
BuildRequires: desktop-file-utils
BuildRequires: blueprint-compiler
BuildRequires: cargo-rpm-macros >= 24
BuildRequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: appstream-data
BuildRequires: libappstream-glib
Recommends: nethogs

%description
Monitor your CPU, Memory, Disk, Network and GPU usage


%prep
%forgesetup -z 0
mkdir -p ./subprojects/magpie
patch -p1 < %{PATCH0}
tar -x --strip-components=1  -f %{SOURCE1} -C ./subprojects/magpie
pushd ./subprojects/magpie/
%cargo_prep_online
popd
%cargo_prep_online
%{cargo_license_summary_online}
%cargo_license_online > LICENSE.dependencies

%build
%meson
%meson_build


%install
%meson_install
%find_lang missioncenter

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/io.missioncenter.MissionCenter.desktop
appstream-util validate-relax  %{buildroot}/%{_datadir}/metainfo/io.missioncenter.MissionCenter.metainfo.xml
%meson_test

# https://gitlab.com/mission-center-devs/mission-center/-/wikis/Home/Nethogs
%post
if  command -v nethogs 2>&1 >/dev/null
then
     setcap "cap_net_admin,cap_net_raw,cap_dac_read_search,cap_sys_ptrace+pe" "$(which nethogs)"
fi


%files -f missioncenter.lang
%doc README.md
%license COPYING
%license LICENSE.dependencies
%{_datadir}/missioncenter/
%{_datadir}/applications/io.missioncenter.MissionCenter.desktop
%{_datadir}/metainfo/io.missioncenter.MissionCenter.metainfo.xml
%{_datadir}/glib-2.0/schemas/io.missioncenter.MissionCenter.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/io.missioncenter.MissionCenter.svg
%{_datadir}/icons/hicolor/symbolic/apps/io.missioncenter.MissionCenter-symbolic.svg
%{_bindir}/missioncenter-magpie
%{_bindir}/missioncenter


%changelog
%autochangelog
