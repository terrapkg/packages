%global appid io.missioncenter.MissionCenter

%global forgeurl0 https://gitlab.com/mission-center-devs/mission-center
%global commit1 a5272b3c1d853caa4044b737cf49257bfc4c86f2

%forgemeta -a

Name:           mission-center
Version:        1.2.0
Release:        1%{?dist}
Summary:        Monitor your CPU, Memory, Disk, Network and GPU usage
SourceLicense:  GPL-3.0-or-later
License:        %{sourcelicense} AND (Apache-2.0 OR MIT) AND MIT AND Apache-2.0 AND BSL-1.0 AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)

URL:            %{forgeurl0}
Source0:        %{forgesource0}
Provides:       bundled(mission-center-magpie)
Provides:       bundled(nvtop) = 3.2.0
#mission centere uses a patched version of nvtop

BuildRequires: meson >= 0.63
BuildRequires: cargo
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
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
%git_clone %{url}.git v%{version}
ls -la
mkdir -p ./subprojects/magpie
pushd ./subprojects/magpie/
%cargo_prep_online
popd
%cargo_prep_online

%conf
%meson

%build
%meson_build
%{cargo_license_summary_online}
%{cargo_license_online} > LICENSE.dependencies

%install
%meson_install
%find_lang missioncenter

%check
%desktop_file_validate %{buildroot}/%{_datadir}/applications/io.missioncenter.MissionCenter.desktop
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
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_scalableiconsdir}/%{appid}.svg
%{_hicolordir}/symbolic/apps/%{appid}-symbolic.svg
%{_bindir}/missioncenter-magpie
%{_bindir}/missioncenter

%changelog
* Thu Jul 30 2026 Owen Zimmerman <owen@fyralabs.com> - 1.2.0-1
- Update for 1.2.0
