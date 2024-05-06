%global real_name prismlauncher
%global nice_name PrismLauncher

%global commit 5ce8cd6b84cecb8ec774d69d65de5b53ed45b01d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global libnbtplusplus_commit a5e8fd52b8bf4ab5d5bcc042b2a247867589985f
%global quazip_commit 6117161af08e366c37499895b00ef62f93adc345
%global tomlplusplus_commit 7eb2ffcc09f8e9890dc0b77ff8ab00fc53b1f2b8

%global commit_date 20240506
%global snapshot_info %{commit_date}.%{shortcommit}

%bcond_without qt6

# Change this variables if you want to use custom keys
# Leave blank if you want to build Prism Launcher without MSA id or curseforge api key
%define msa_id default
%define curseforge_key default

%if %{with qt6}
%global qt_version 6
%global min_qt_version 6
%else
%global qt_version 5
%global min_qt_version 5.12
%endif

%global build_platform terra

%if %{with qt6}
Name:             prismlauncher-nightly
%else
Name:             prismlauncher-qt5-nightly
%endif
Version:          9.0^%{snapshot_info}
Release:          1%?dist
Summary:          Minecraft launcher with ability to manage multiple instances
License:          GPL-3.0-only AND Apache-2.0 AND LGPL-3.0-only AND GPL-3.0-or-later AND GPL-2.0-or-later AND ISC AND OFL-1.1 AND LGPL-2.1-only AND MIT AND BSD-2-Clause-FreeBSD AND BSD-3-Clause AND LGPL-3.0-or-later
Group:            Amusements/Games
URL:              https://prismlauncher.org/
Source0:          https://github.com/PrismLauncher/PrismLauncher/archive/%{commit}/%{real_name}-%{shortcommit}.tar.gz
Source1:          https://github.com/PrismLauncher/libnbtplusplus/archive/%{libnbtplusplus_commit}/libnbtplusplus-%{libnbtplusplus_commit}.tar.gz
Source2:          https://github.com/stachenov/quazip/archive/%{quazip_commit}/quazip-%{quazip_commit}.tar.gz
Source3:          https://github.com/marzer/tomlplusplus/archive/%{tomlplusplus_commit}/tomlplusplus-%{tomlplusplus_commit}.tar.gz
Patch0:           0001-find-cmark-with-pkgconfig.patch

BuildRequires:    cmake >= 3.15
BuildRequires:    extra-cmake-modules
BuildRequires:    gcc-c++
BuildRequires:    java-17-openjdk-devel
BuildRequires:    desktop-file-utils
BuildRequires:    libappstream-glib
BuildRequires:    cmake(ghc_filesystem)
BuildRequires:    cmake(Qt%{qt_version}Concurrent) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Core) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Gui) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Network) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Test) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Widgets) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Xml) >= %{min_qt_version}

%if %{with qt6}
BuildRequires:    cmake(Qt6Core5Compat)
%endif

BuildRequires:    pkgconfig(libcmark)
%if 0%{fedora} < 38
BuildRequires:    cmark
%endif
BuildRequires:    pkgconfig(scdoc)
BuildRequires:    pkgconfig(zlib)

Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

Requires:         qt%{qt_version}-qtimageformats
Requires:         qt%{qt_version}-qtsvg
Requires:         javapackages-filesystem
Recommends:       java-21-openjdk
Recommends:       java-17-openjdk
Suggests:         java-1.8.0-openjdk

# xrandr needed for LWJGL [2.9.2, 3) https://github.com/LWJGL/lwjgl/issues/128
Recommends:       xrandr
# libflite needed for using narrator in minecraft
Recommends:       flite
# Prism supports enabling gamemode
Suggests:         gamemode

Conflicts:        %{real_name}
Conflicts:        %{real_name}-qt5
%if %{without qt6}
Conflicts:        %{real_name}-nightly
%endif


%description
A custom launcher for Minecraft that allows you to easily manage
multiple installations of Minecraft at once (Fork of MultiMC)


%prep
%autosetup -p1 -n PrismLauncher-%{commit}

tar -xzf %{SOURCE1} -C libraries
tar -xvf %{SOURCE2} -C libraries
tar -xvf %{SOURCE3} -C libraries

rmdir libraries/{extra-cmake-modules,filesystem,libnbtplusplus,quazip,tomlplusplus,zlib}/
mv -f libraries/libnbtplusplus-%{libnbtplusplus_commit} libraries/libnbtplusplus
mv -f libraries/quazip-%{quazip_commit} libraries/quazip
mv -f libraries/tomlplusplus-%{tomlplusplus_commit} libraries/tomlplusplus

# Do not set RPATH
sed -i "s|\$ORIGIN/||" CMakeLists.txt


%build
%cmake \
  -DLauncher_QT_VERSION_MAJOR="%{qt_version}" \
  -DLauncher_BUILD_PLATFORM="%{build_platform}" \
  %if "%{msa_id}" != "default"
  -DLauncher_MSA_CLIENT_ID="%{msa_id}" \
  %endif
  %if "%{curseforge_key}" != "default"
  -DLauncher_CURSEFORGE_API_KEY="%{curseforge_key}" \
  %endif
  -DBUILD_TESTING=OFF

%cmake_build


%install
%cmake_install


%check
%ctest


%files
%doc README.md
%license LICENSE COPYING.md
%dir %{_datadir}/%{nice_name}
%{_bindir}/%{real_name}
%{_datadir}/%{nice_name}/NewLaunch.jar
%{_datadir}/%{nice_name}/JavaCheck.jar
%{_datadir}/%{nice_name}/qtlogging.ini
%{_datadir}/%{nice_name}/NewLaunchLegacy.jar
%{_datadir}/applications/org.prismlauncher.PrismLauncher.desktop
%{_metainfodir}/org.prismlauncher.PrismLauncher.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/org.prismlauncher.PrismLauncher.svg
%{_datadir}/mime/packages/modrinth-mrpack-mime.xml
%{_datadir}/qlogging-categories%{qt_version}/prismlauncher.categories
%{_mandir}/man?/prismlauncher.*


%changelog
* Wed Jul 26 2023 seth <getchoo at tuta dot io> - 8.0^20230726.4f00012-1
- remove terra-fractureiser-detector from recommends, use proper build platform,
  and add patches for epel/older fedora versions

* Sun Jul 23 2023 seth <getchoo at tuta dot io> - 8.0^20230722.273d75f-1
- update submodules, version, & use autorelease

* Wed Jun 07 2023 seth <getchoo at tuta dot io> - 7.0^20230603.954d4d7-1
- specify jdk 17 + cleanup outdated patches/scriptlets

* Sun May 14 2023 seth <getchoo at tuta dot io> - 7.0^20230513.c5aff7c-1
- add qtlogging.ini to files list

* Mon Mar 20 2023 seth <getchoo at tuta dot io> - 7.0^20230319.6dcf34a-1
- recommend flite to support narrator in minecraft

* Fri Feb 03 2023 seth <getchoo at tuta dot io> - 7.0^20230203.58d9ced-1
- disable tests and explicitly require cmark

* Sun Jan 15 2023 seth <getchoo at tuta dot io> - 7.0^20230115.f1247d2-1
- add 0001-find-cmark-with-pkgconfig.patch

* Fri Jan 13 2023 seth <getchoo at tuta dot io> - 7.0^20230113.3de681d-1
- add cmark as a build dep

* Tue Jan 03 2023 seth <getchoo at tuta dot io> - 7.0^20230102.4b12c85-1
- add qlogging categories

* Mon Dec 05 2022 seth <getchoo at tuta dot io> - 6.0^20221204.79d5bef-1
- revise file to better follow fedora packaging guidelines and add java 8 as a
  dependency

* Thu Nov 10 2022 seth <getchoo at tuta dot io> - 5.1-0.1.20221110.e6d057f
- add package to Amusements/Games

* Sun Nov 06 2022 seth <getchoo at tuta dot io> - 5.0-0.1.20221105.9fb80a2
- update installed files

* Thu Oct 27 2022 seth <getchoo at tuta dot io> - 5.0-0.1.20221027.610b971
- initial commit
