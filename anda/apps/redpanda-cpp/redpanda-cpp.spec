%global appid   RedPandaIDE
%global srcname RedPanda-CPP
# Upstream hasn't defined reverse-DNS notation yet, though a candidate is net.royqh.RedPandaIDE

Name:           redpanda-cpp
Version:        3.5
Release:        1%{?dist}
Summary:        Fast, lightweight, open-source and cross platform C++ IDE
License:        GPL-3.0-or-later
URL:            https://github.com/royqh1979/RedPanda-CPP
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Packager:       Mizuki Nguyen <acertaindrizzle@proton.me>

BuildRequires:  desktop-file-utils
BuildRequires:  libubsan
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Xml)

Requires:       gcc gcc-c++ astyle
Requires:       glibc-static libstdc++-static libasan
Requires:       qt6-qtbase qt6-qtsvg

%description
A lightweight but powerful C/C++ IDE

Red Panda C++ (Old name Red Panda Dev-C++ 7) is a full featured C/C++ IDE.
It's the succesor of Red Panda Dev-C++ 6, which is developed by Delphi 7 and
can only running under Windows.

%prep
%autosetup -n %{srcname}-%{version}

%conf
%cmake -S . -DLUA_ADDON=ON

%build
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appid}.desktop

%files
/usr/bin/RedPandaIDE
/usr/libexec/RedPandaCPP/*
/usr/share/RedPandaCPP/*
/usr/share/doc/RedPandaCPP/*
/usr/share/applications/RedPandaIDE.desktop
/usr/share/icons/hicolor/scalable/apps/redpandaide.svg
/usr/share/mime/packages/redpandaide.xml

%changelog
* Wed Nov 11 2026 Mizuki Nguyen <acertaindrizzle@proton.me> - 3.5-1
- Initial package

