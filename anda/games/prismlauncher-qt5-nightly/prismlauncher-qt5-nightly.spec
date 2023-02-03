%global real_name prismlauncher

%global commit 58d9ceda4bf4c78d62d4ed4ee4242147dda9d910
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global libnbtplusplus_commit 2203af7eeb48c45398139b583615134efd8d407f
%global quazip_commit 6117161af08e366c37499895b00ef62f93adc345
%global tomlplusplus_commit 0a90913abf9390b9e08ab6d3b40ac11634553f38

%global commit_date %(date '+%Y%m%d')
%global snapshot_info %{commit_date}.%{shortcommit}

%bcond_with qt6

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

Name:             prismlauncher-qt5-nightly
Version:          7.0^%{snapshot_info}
Release:          1%{?dist}
Summary:          Minecraft launcher with ability to manage multiple instances
License:          GPL-3.0-only
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

BuildRequires:    pkgconfig(libcmark)
# https://bugzilla.redhat.com/show_bug.cgi?id=2166815
BuildRequires:    cmark
BuildRequires:    pkgconfig(scdoc)
BuildRequires:    pkgconfig(zlib)

Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

Requires:         qt%{qt_version}-qtimageformats
Requires:         qt%{qt_version}-qtsvg
Requires:         javapackages-filesystem
Requires:         java >= 17
Requires:         java-1.8.0-openjdk

# xrandr needed for LWJGL [2.9.2, 3) https://github.com/LWJGL/lwjgl/issues/128
Recommends:       xrandr
# Prism supports enabling gamemode
Suggests:         gamemode

Conflicts:        prismlauncher
Conflicts:        prismlauncher-qt5
Conflicts:        primslauncher-nightly


%description
A custom launcher for Minecraft that allows you to easily manage
multiple installations of Minecraft at once (Fork of MultiMC)


%prep
%autosetup -p1 -n PrismLauncher-%{commit}

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
  -DBUILD_TESTING=OFF

%cmake_build


%install
%cmake_install


%check
## disabled due to inconsistent results in copr builds that are not reproducible locally
# %ctest

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
%{_datadir}/qlogging-categories%{qt_version}/prismlauncher.categories
%{_mandir}/man?/prismlauncher.*


%changelog
* Fri Feb 03 2023 seth flynn <getchoo at tuta dot io> - 7.0^20230203.58d9ced-1
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
