%define commit 3405fd91c6e116bc0af69a8be48c95e447306b52
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%define libnbtplusplus_commit       2203af7eeb48c45398139b583615134efd8d407f
%define libnbtplusplus_shortcommit  %(c=%{libnbtplusplus_commit}; echo ${c:0:7})
%define quazip_commit               6117161af08e366c37499895b00ef62f93adc345
%define quazip_shortcommit          %(c=%{quazip_commit}; echo ${c:0:7})
%global tomlplusplus_commit         4b166b69f28e70a416a1a04a98f365d2aeb90de8
%global tomlplusplus_shortcommit    %(c=%{tomlplusplus_commit}; echo ${c:0:7})
%global filesystem_commit           cd6805e94dd5d6346be1b75a54cdc27787319dd2
%global filesystem_shortcommit      %(c=%{filesystem_commit}; echo ${c:0:7})
%bcond qt6 1

%if %{with qt6}
%define qt_version 6
%else
%define qt_version 5
%endif

Name:           prismlauncher
Version:        1.4.2.git%{shortcommit}
Release:        1%{?dist}
Summary:        Minecraft launcher with ability to manage multiple instances

#
# CC-BY-SA
# ---------------------------------------
# launcher/resources/multimc/
#
# BSD 3-clause "New" or "Revised" License
# ---------------------------------------
# application/
# libraries/LocalPeer/
# libraries/ganalytics/
#
# Boost Software License (v1.0)
# ---------------------------------------
# cmake/
#
# Expat License
# ---------------------------------------
# libraries/systeminfo/
#
# GNU Lesser General Public License (v2 or later)
# ---------------------------------------
# libraries/rainbow
#
# GNU Lesser General Public License (v2.1 or later)
# ---------------------------------------
# libraries/iconfix/
# libraries/quazip/
#
# GNU Lesser General Public License (v3 or later)
# ---------------------------------------
# libraries/libnbtplusplus/
#
# GPL (v2)
# ---------------------------------------
# libraries/pack200/
#
# ISC License
# ---------------------------------------
# libraries/hoedown/
#
# zlib/libpng license
# ---------------------------------------
# libraries/quazip/quazip/unzip.h
# libraries/quazip/quazip/zip.h
#

License:        CC-BY-SA and ASL 2.0 and BSD and Boost and LGPLv2 and LGPLv2+ and LGPLv3+ and GPLv2 and GPLv2+ and GPLv3 and ISC and zlib
URL:            https://github.com/PlaceholderMC
Source0:        https://github.com/PlaceholderMC/PrismLauncher/archive/%{commit}.tar.gz
Source1:        https://github.com/PolyMC/libnbtplusplus/archive/%{libnbtplusplus_commit}/libnbtplusplus-%{libnbtplusplus_shortcommit}.tar.gz
Source2:        https://github.com/stachenov/quazip/archive/%{quazip_commit}/quazip-%{quazip_shortcommit}.tar.gz
Source3:        https://github.com/marzer/tomlplusplus/archive/%{tomlplusplus_commit}.tar.gz#/tomlplusplus-%{tomlplusplus_shortcommit}.tar.gz
Source4:        https://github.com/gulrak/filesystem/archive/%{filesystem_commit}.tar.gz#/filesystem-%{filesystem_shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules

# TO fix our old mistakes with the naming
Provides:       prism-launcher = %{version}-%{release}

BuildRequires:  java-devel
%if %{with qt6}
BuildRequires:  %{?suse_version:lib}qt6-qtbase-devel
BuildRequires:  %{?suse_version:lib}qt6-qt5compat-devel
%else
BuildRequires:  %{?suse_version:lib}qt5-qtbase-devel
%endif

# require zlib to ensure we do not compile against zlib-ng
BuildRequires:  zlib zlib-devel
BuildRequires:  scdoc
BuildRequires:  git-core

# Needed for loading SVG Icons for Themes
%if %{with qt6}
%if 0%{?suse_version}
Requires:       libQt6Svg5
%else
Requires:       qt6-qtsvg
%endif
%else
%if 0%{?suse_version}
Requires:       libQt5Svg5
%else
Requires:       qt5-qtsvg
%endif
%endif

# Needed for a variety of Image formats fetched from the web
%if %{with qt6}
Requires:       %{?suse_version:lib}qt6-qtimageformats
%else
Requires:       %{?suse_version:lib}qt5-qtimageformats
%endif

# LWJGL uses xrandr for detection
Requires:       xrandr

# Minecraft <  1.17
Recommends:     java-1.8.0-openjdk
# Minecraft >= 1.17
Recommends:     java-17-openjdk
# Prism supports enabling gamemode
Recommends:     gamemode

%description
Prism Launcher is a free, open source launcher for Minecraft. It allows you to have
multiple, separate instances of Minecraft (each with their own mods, texture
packs, saves, etc) and helps you manage them and their associated options with
a simple interface.


%prep
%autosetup -p1 -n PrismLauncher-%{commit}

tar -xvf %{SOURCE1} -C libraries
tar -xvf %{SOURCE2} -C libraries
tar -xvf %{SOURCE3} -C libraries
tar -xvf %{SOURCE4} -C libraries
rmdir libraries/{quazip/,libnbtplusplus}
mv -f libraries/quazip-%{quazip_commit} libraries/quazip
mv -f libraries/libnbtplusplus-%{libnbtplusplus_commit} libraries/libnbtplusplus
mv -f libraries/tomlplusplus-%{tomlplusplus_commit}/* libraries/tomlplusplus
mv -f libraries/filesystem-%{filesystem_commit}/* libraries/filesystem

%build
%if %{with qt6}
%cmake_qt6 \
	-DLauncher_FORCE_BUNDLED_LIBS:BOOL=ON \
	-DLauncher_QT_VERSION_MAJOR="6" \
%else
%cmake \
	-DLauncher_FORCE_BUNDLED_LIBS:BOOL=ON \
	-DLauncher_QT_VERSION_MAJOR="5" \
%endif

%cmake_build

%install
%cmake_install


%check
# skip tests on systems that aren't officially supported
%if ! 0%{?suse_version}
%ctest
desktop-file-validate %{buildroot}%{_datadir}/applications/org.prismlauncher.PrismLauncher.desktop
%endif


%files
%license COPYING.md
%{_bindir}/prismlauncher
%{_datadir}/icons/hicolor/scalable/apps/org.prismlauncher.PrismLauncher.svg
%{_datadir}/applications/org.prismlauncher.PrismLauncher.desktop
%{_datadir}/metainfo/org.prismlauncher.PrismLauncher.metainfo.xml
%{_datadir}/jars/NewLaunch.jar
%{_datadir}/jars/JavaCheck.jar
%{_mandir}/man6/prismlauncher.6*
#%%config %%{_sysconfdir}/ld.so.conf.d/*


%changelog
* Tue Oct 18 2022 seth <getchoo at tuta dot io> - 1.4.2.git3405fd9-1
- merge with terrapkg and bump commit

* Tue Oct 18 2022 seth <getchoo at tuta dot io> - 1.4.2.git2b7b9a2-1
- bump commit

* Tue Oct 18 2022 seth <getchoo at tuta dot io> - 1.4.2.git3773f2e-2
- fix desktop file path

* Tue Oct 18 2022 seth <getchoo at tuta dot io> - 1.4.2.git3773f2e-1
- add new curseforge api key

* Tue Oct 18 2022 seth <getchoo at tuta dot io> - 1.4.2.gitafaef4e-3
- bump commit and add rebrand

* Tue Oct 18 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 1.4.2.git981e9cf-4
- Update provides and obsoletes

* Tue Oct 18 2022 seth <getchoo at tuta dot io> - 1.4.2.git981e9cf-3
- start using qt6

* Tue Oct 18 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 1.4.2-1
- Repackaged as Prism Launcher

* Thu Sep 08 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.4.2-1
- Update to 1.4.2

* Fri Jul 29 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Sat Jul 23 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.4.0-2
- Recommend gamemode

* Sat Jul 23 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.4.0-1
- Update to 1.4.0

* Wed Jun 15 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.3.2-2
- Fixing OpenSuse Tumbleweed compilation

* Sun Jun 12 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.3.2-1
- Update to 1.3.2

* Mon May 30 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Mon May 23 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Sat May 14 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Mon Apr 25 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.2.1-2
- Correct dependencies for openSUSE

* Wed Apr 20 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Tue Apr 19 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Tue Apr 19 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.1.1-3
- Correct dependencies for openSuse

* Wed Apr 06 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.1.1-2
- Add missing dependencies

* Mon Mar 28 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Wed Mar 16 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Mon Jan 24 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.0.5-2
- remove explicit dependencies, correct dependencies to work on OpenSuse

* Sun Jan 09 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.0.5-1
- Update to 1.0.5

* Sun Jan 09 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.0.4-2
- rework spec

* Fri Jan 7 2022 getchoo <getchoo at tuta dot io> - 1.0.4-1
- Initial polymc spec
