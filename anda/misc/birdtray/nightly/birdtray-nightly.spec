%global commit bcceec6a1a56fa7acd19e1b6a93f430b5a566537
%global commit_date 20260803
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global ver 1.11.4

Name:                  	birdtray-nightly
Version:                %{ver}^%{commit_date}git.%{shortcommit}
Release:                1%{?dist}
Summary:                Mail system tray notification icon for Thunderbird (nightly)

License:                GPL-3.0-or-later
URL:                    https://github.com/gyunaev/birdtray
Source0:                %{url}/archive/%{commit}/birdtray-%{commit}.tar.gz

BuildRequires:          cmake-rpm-macros
BuildRequires:          gcc-c++
BuildRequires:          cmake(Qt5Core)
BuildRequires:          cmake(Qt5Svg)
BuildRequires:          cmake(Qt5X11Extras)
BuildSystem:            cmake
BuildOption(conf):      -DCMAKE_POLICY_VERSION_MINIMUM=3.5
Packager:		Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/birdtray
%{_appsdir}/com.ulduzsoft.Birdtray.desktop
%{_hicolordir}/*x*/apps/com.ulduzsoft.Birdtray.png
%{_scalableiconsdir}/com.ulduzsoft.Birdtray.svg
%{_metainfodir}/com.ulduzsoft.Birdtray.appdata.xml

%changelog
* Thu Aug 27 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit

