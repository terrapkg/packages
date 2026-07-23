%global appid cc.arduino.AppLab
%define debug_package %{nil}

Name:           arduino-app-lab
Version:        0.9.0
Release:        2%?dist
Summary:        A powerful visual environment for managing the Arduino UNO Q

Provides:       arduino-app-lab
URL:            https://www.arduino.cc/en/software
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-3.0-or-later AND BSD-3-Clause AND Apache-2.0 AND MIT AND ISC AND BSD-2-Clause AND 0BSD AND AGPL-3.0-or-later AND BlueOak-1.0.0 AND Python-2.0 AND CC0-1.0 AND CC-BY-SA-4.0 AND Unlicense

Source0:        https://github.com/arduino/arduino-app-lab/archive/refs/tags/al-%{version}.tar.gz
Source1:        cc.arduino.AppLab.desktop
Source2:        cc.arduino.AppLab.metainfo.xml

ExclusiveArch:  x86_64

Requires:       android-tools

BuildRequires:  desktop-file-utils
BuildRequires:  yarnpkg
BuildRequires:  wails
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  golang
BuildRequires:  wget
BuildRequires:  jq

Suggests:       arduino-flasher-cli
Suggests:       arduino-app-cli

Obsoletes:      arduino-app-lab-bin < 0.9.0-1

Packager:       Jaiden Riordan <jade@fyralabs.com>, Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n %{name}-al-%{version}
touch .env

%build
%{__yarn}
%{__yarn} install
pushd standalone-apps/app-lab-desktop/internal/board/
./download_resources.sh
popd
pushd standalone-apps/app-lab-desktop
wails build -tags webkit2_41
popd

%install
install -Dm755 standalone-apps/app-lab-desktop/build/bin/ArduinoAppLab  %{buildroot}%{_bindir}/%{name}

install -Dm644 standalone-apps/app-lab-desktop/build/appicon.png        %{buildroot}%{_hicolordir}/512x512/apps/%{appid}.png

%desktop_file_install %{S:1}

%terra_appstream -o %{S:2}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_hicolordir}/512x512/apps/%{appid}.png
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Thu Dec 25 2025 Owen Zimmerman <owen@fyralabs.com>
- Build from source, clean some stuff up, add third party licenses

* Thu Dec 25 2025 Owen Zimmerman <owen@fyralabs.com>
- Add %%check, update macros

* Thu Dec 4 2025 Jaiden Riordan <jade@fyralabs.com>
- Package arduino-app-lab-bin
