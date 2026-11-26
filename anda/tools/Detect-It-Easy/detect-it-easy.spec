%global appid io.github.horsicq.detect-it-easy

Name:          detect-it-easy
Version:       4.0.0
Release:       1%{?dist}
Summary:       Program for determining types of files for Windows, Linux and MacOS
License:       MIT
URL:           https://ntinfo.biz/#detect-it-easydie
Source0:       https://github.com/horsicq/DIE-engine/archive/refs/tags/%{version}.tar.gz
BuildRequires: anda-srpm-macros
BuildRequires: cmake
BuildRequires: cmake-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: git-core
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Svg)
Requires:      hicolor-icon-theme
Packager:      Gilver E. <roachy@fyralabs.com>

%description
Detect It Easy (DiE) is a cross-platform tool for file identification and static inspection,
used by malware analysts, cybersecurity experts, and reverse engineers.

It combines native format parsers with an extensible DiE-JS analysis layer,
supporting both compact signatures and multi-stage static analysis across Windows, Linux, and MacOS.

%prep
%git_clone https://github.com/horsicq/DIE-engine.git %{version}

%conf
%cmake

%build
%cmake_build

%install
%cmake_install

%files
%license %{buildroot}%{_defaultdocdir}/DetectItEasy/detect-it-easy/LICENSE
%doc %{buildroot}%{_defaultdocdir}/DetectItEasy/detect-it-easy/README.md
%{_prefix}/lib/die/
%{_libdir}/die/
%{_appsdir}/die.desktop
%{_hicolordir}/16x16/apps/%{appid}.png
%{_hicolordir}/20x10/apps/%{appid}.png
%{_hicolordir}/24x24/apps/%{appid}.png
%{_hicolordir}/32x32/apps/%{appid}.png
%{_hicolordir}/48x48/apps/%{appid}.png
%{_hicolordir}/256x256/apps/%{appid}.png
%{_metainfodir}/%{appid}.metainfo.xml
