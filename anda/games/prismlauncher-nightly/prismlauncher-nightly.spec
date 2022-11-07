%global fancy_name PrismLauncher
%global real_name prismlauncher
%global repo https://github.com/%{fancy_name}/%{fancy_name}

%global commit 126bbd67f7bdeb26905520a068d8dc1968f2659c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global filesystem_commit cd6805e94dd5d6346be1b75a54cdc27787319dd2
%global libnbtplusplus_commit 2203af7eeb48c45398139b583615134efd8d407f
%global quazip_commit 6117161af08e366c37499895b00ef62f93adc345
%global tomlplusplus_commit 4b166b69f28e70a416a1a04a98f365d2aeb90de8

%global commit_date %(date '+%Y%m%d')
%global git_rel .%{commit_date}.%{shortcommit}

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

%global build_platform unknown

%if 0%{?suse_version}
%global build_platform openSUSE
%endif

%if 0%{?fedora}
%global build_platform Fedora
%endif

%if 0%{?rhel_version}
%global build_platform RedHat
%endif

%if 0%{?centos_version}
%global build_platform CentOS
%endif

%if %{with qt6}
Name:           prismlauncher-nightly
%else
Name:           prismlauncher-qt5-nightly
%endif
Version:        5.1
Release:        0.1%{?git_rel}%{?dist}
Summary:        Minecraft launcher with ability to manage multiple instances
License:        GPL-3.0-only
URL:            https://prismlauncher.org/
Source0:        %{repo}/archive/%{commit}/%{fancy_name}-%{shortcommit}.tar.gz
Source1:        https://github.com/PrismLauncher/libnbtplusplus/archive/%{libnbtplusplus_commit}/libnbtplusplus-%{libnbtplusplus_commit}.tar.gz
Source2:        https://github.com/stachenov/quazip/archive/%{quazip_commit}/quazip-%{quazip_commit}.tar.gz
Source3:        https://github.com/marzer/tomlplusplus/archive/%{tomlplusplus_commit}/tomlplusplus-%{tomlplusplus_commit}.tar.gz
Source4:        https://github.com/gulrak/filesystem/archive/%{filesystem_commit}/filesystem-%{filesystem_commit}.tar.gz

BuildRequires:  cmake >= 3.15
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  java-devel

%if 0%{?suse_version}
BuildRequires:  appstream-glib
%else
BuildRequires:	libappstream-glib
%endif

BuildRequires:  desktop-file-utils
BuildRequires:  cmake(Qt%{qt_version}Concurrent) >= %{min_qt_version}
BuildRequires:  cmake(Qt%{qt_version}Core) >= %{min_qt_version}
BuildRequires:  cmake(Qt%{qt_version}Gui) >= %{min_qt_version}
BuildRequires:  cmake(Qt%{qt_version}Network) >= %{min_qt_version}
BuildRequires:  cmake(Qt%{qt_version}Test) >= %{min_qt_version}
BuildRequires:  cmake(Qt%{qt_version}Widgets) >= %{min_qt_version}
BuildRequires:  cmake(Qt%{qt_version}Xml) >= %{min_qt_version}

%if %{with qt6}
BuildRequires:  cmake(Qt6Core5Compat)
%endif

BuildRequires:  pkgconfig(scdoc)
BuildRequires:  zlib-devel

# Prism Launcher requires QuaZip >= 1.3
%if 0%{?suse_version} >= 1550
BuildRequires:  cmake(QuaZip-Qt%{qt_version})
%endif

%if 0%{?suse_version}
Requires:       %{!?with_qt6:lib}qt%{qt_version}-%{!?with_qt6:qt}imageformats
Requires:       libQt%{qt_version}Svg%{qt_version}
%else
Requires:       qt%{qt_version}-qtimageformats
Requires:       qt%{qt_version}-qtsvg
%endif

Recommends:     java-openjdk-headless
# xrandr needed for LWJGL [2.9.2, 3) https://github.com/LWJGL/lwjgl/issues/128
Recommends:     xrandr

# Prism supports enabling gamemode
%if 0%{?suse_version}
Recommends:     gamemoded
%else
Recommends:     gamemode
%endif

Conflicts:     %{real_name}
Conflicts:     %{real_name}-qt5
%if %{with qt6}
Conflicts:     %{real_name}-qt5-nightly
%else
Conflicts:     %{real_name}-nightly
%endif

%description
A custom launcher for Minecraft that allows you to easily manage
multiple installations of Minecraft at once (Fork of MultiMC)


%prep
%autosetup -n %{fancy_name}-%{commit}

tar -xvf %{SOURCE1} -C libraries
tar -xvf %{SOURCE2} -C libraries
tar -xvf %{SOURCE3} -C libraries
tar -xvf %{SOURCE4} -C libraries
rmdir libraries/{quazip/,libnbtplusplus}
mv -f libraries/quazip-%{quazip_commit} libraries/quazip
mv -f libraries/libnbtplusplus-%{libnbtplusplus_commit} libraries/libnbtplusplus
mv -f libraries/tomlplusplus-%{tomlplusplus_commit}/* libraries/tomlplusplus
mv -f libraries/filesystem-%{filesystem_commit}/* libraries/filesystem

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

%cmake_build

%install
%cmake_install

%if 0%{?suse_version} > 1500 || 0%{?fedora} > 35
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/metainfo/org.prismlauncher.PrismLauncher.metainfo.xml
%endif

%check
%ctest
desktop-file-validate %{buildroot}%{_datadir}/applications/org.prismlauncher.PrismLauncher.desktop

%files
%doc README.md
%license LICENSE COPYING.md
%dir %{_datadir}/%{real_name}
%{_bindir}/prismlauncher
%{_datadir}/%{real_name}/NewLaunch.jar
%{_datadir}/%{real_name}/JavaCheck.jar
%{_datadir}/applications/org.prismlauncher.PrismLauncher.desktop
%{_datadir}/metainfo/org.prismlauncher.PrismLauncher.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/org.prismlauncher.PrismLauncher.svg
%{_datadir}/mime/packages/modrinth-mrpack-mime.xml
%{_mandir}/man?/prismlauncher.*


%changelog
* Sun Nov 06 2022 seth <getchoo at tuta dot io> - 5.0-0.1.20221105.9fb80a2
- update installed files

* Thu Oct 27 2022 seth <getchoo at tuta dot io> - 5.0-0.1.20221027.610b971
- initial commit
