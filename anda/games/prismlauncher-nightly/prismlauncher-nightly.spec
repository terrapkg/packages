%global real_name prismlauncher

%global commit d95625ed88c30a58da050abff538a4b7f7157622
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global libnbtplusplus_commit 2203af7eeb48c45398139b583615134efd8d407f
%global quazip_commit 6117161af08e366c37499895b00ef62f93adc345
%global tomlplusplus_commit 0a90913abf9390b9e08ab6d3b40ac11634553f38

%global commit_date %(date '+%Y%m%d')
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

%global build_platform unknown

%if 0%{?fedora}
%global build_platform Fedora
%endif

%if 0%{?rhel}
%global build_platform RedHat
%endif

%if 0%{?centos}
%global build_platform CentOS
%endif

Name:             prismlauncher-nightly
Version:          6.0^%{snapshot_info}
Release:          1%{?dist}
Summary:          Minecraft launcher with ability to manage multiple instances
License:          GPL-3.0-only
Group:            Amusements/Games
URL:              https://prismlauncher.org/
Source0:          https://github.com/PrismLauncher/PrismLauncher/archive/%{commit}/%{real_name}-%{shortcommit}.tar.gz
Source1:          https://github.com/PrismLauncher/libnbtplusplus/archive/%{libnbtplusplus_commit}/libnbtplusplus-%{libnbtplusplus_commit}.tar.gz
Source2:          https://github.com/stachenov/quazip/archive/%{quazip_commit}/quazip-%{quazip_commit}.tar.gz
Source3:          https://github.com/marzer/tomlplusplus/archive/%{tomlplusplus_commit}/tomlplusplus-%{tomlplusplus_commit}.tar.gz

BuildRequires:    cmake >= 3.15
BuildRequires:    extra-cmake-modules
BuildRequires:    gcc-c++
BuildRequires:    java-devel >= 17
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

BuildRequires:    pkgconfig(scdoc)
BuildRequires:    pkgconfig(zlib)

Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

Requires:         qt%{qt_version}-qtimageformats
Requires:         qt%{qt_version}-qtsvg
Requires:         javapackages-filesystem
Requires:         java-headless >= 17
Requires:         java-1.8.0-openjdk-headless

# xrandr needed for LWJGL [2.9.2, 3) https://github.com/LWJGL/lwjgl/issues/128
Recommends:       xrandr
# Prism supports enabling gamemode
Suggests:         gamemode

Conflicts:        prismlauncher
Conflicts:        prismlauncher-qt5


%description
A custom launcher for Minecraft that allows you to easily manage
multiple installations of Minecraft at once (Fork of MultiMC)


%prep
%autosetup -n PrismLauncher-%{commit}

tar -xzf %{SOURCE1} -C libraries
tar -xvf %{SOURCE2} -C libraries
tar -xvf %{SOURCE3} -C libraries

rmdir libraries/{libnbtplusplus,quazip,tomlplusplus}/
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

%cmake_build


%install
%cmake_install


%check
%ctest

%if 0%{?fedora} > 35
appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/org.prismlauncher.PrismLauncher.metainfo.xml
%endif

desktop-file-validate %{buildroot}%{_datadir}/applications/org.prismlauncher.PrismLauncher.desktop


%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/bin/touch --no-create %{_datadir}/mime/packages &>/dev/null || :


%postun
/usr/bin/update-desktop-database &> /dev/null || :

if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
		/usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :


%files
%doc README.md
%license LICENSE COPYING.md
%dir %{_datadir}/%{real_name}
%{_bindir}/prismlauncher
%{_datadir}/%{real_name}/NewLaunch.jar
%{_datadir}/%{real_name}/JavaCheck.jar
%{_datadir}/applications/org.prismlauncher.PrismLauncher.desktop
%{_metainfodir}/org.prismlauncher.PrismLauncher.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/org.prismlauncher.PrismLauncher.svg
%{_datadir}/mime/packages/modrinth-mrpack-mime.xml
%{_mandir}/man?/prismlauncher.*


%changelog
* Mon Dec 05 2022 seth <getchoo at tuta dot io> - 6.0^20221204.79d5bef-1
- revise file to better follow fedora packaging guidelines and add java 8 as a
  dependency

* Thu Nov 10 2022 seth <getchoo at tuta dot io> - 5.1-0.1.20221110.e6d057f
- add package to Amusements/Games

* Sun Nov 06 2022 seth <getchoo at tuta dot io> - 5.0-0.1.20221105.9fb80a2
- update installed files

* Thu Oct 27 2022 seth <getchoo at tuta dot io> - 5.0-0.1.20221027.610b971
- initial commit
