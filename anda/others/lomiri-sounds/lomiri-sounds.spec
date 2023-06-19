%global forgeurl https://gitlab.com/ubports/development/core/lomiri-sounds
%global commit 4e71c32b2181ae00feb09818c304a7e8e4574fed
%forgemeta

Name:       lomiri-sounds
Summary:    Ring-tones and notification tones included with Ubuntu Touch
Version:    22.02
Release:    %autorelease
License:    CC-BY-SA-3.0 AND CC-BY-4.0 AND CC0-1.0 AND CC-BY-3.0
URL:        https://gitlab.com/ubports/development/core/lomiri-sounds
Source0:    %{url}/-/archive/%commit/lomiri-sounds-%commit.tar.gz
BuildArch: noarch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++

%description
Lomiri sounds contains the ringtones and notification tones recommended for the Lomiri stack.

%prep
%autosetup -n %{name}-%commit

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md 
%license debian/copyright
%{_datadir}/pkgconfig/lomiri-sounds.pc
%dir %{_datadir}/sounds/lomiri
%{_datadir}/sounds/lomiri/camera/
%{_datadir}/sounds/lomiri/notifications/
%{_datadir}/sounds/lomiri/ringtones/

%changelog
%autochangelog
