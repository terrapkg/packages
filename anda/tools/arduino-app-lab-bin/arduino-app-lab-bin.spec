%global appid cc.arduino.AppLab

Name:           arduino-app-lab-bin
Version:        0.8.0
Release:        1%?dist
Summary:        A powerful visual environment for managing the Arduino UNO Q

Provides:       arduino-app-lab
URL:            https://www.arduino.cc/en/software
License:        GPL-3.0-or-later

Source0:        https://downloads.arduino.cc/AppLab/Stable/ArduinoAppLab_%{version}_Linux_x86-64.tar.gz
Source1:        https://github.com/arduino/arduino-app-lab/archive/refs/tags/al-%{version}.zip
Source2:        cc.arduino.AppLab.desktop
Source3:        cc.arduino.AppLab.metainfo.xml

ExclusiveArch:  x86_64

Requires:       android-tools

BuildRequires:  terra-appstream-helper desktop-file-utils

Suggests:       arduino-flasher-cli arduino-app-cli

Packager:       Jaiden Riordan <jade@fyralabs.com>

%description
%summary.

%prep
tar -xvf %{_sourcedir}/ArduinoAppLab_%{version}_Linux_x86-64.tar.gz
unzip %{_sourcedir}/al-%{version}.zip

%install
install -dm755 %{buildroot}%{_bindir}
install -p -m755 ArduinoAppLab_%{version}_Linux_x86-64/arduino-app-lab %{buildroot}%{_bindir}/%{name}

install -dm755 %{buildroot}%{_scalableiconsdir}/
install -p -m644 arduino-app-lab-al-%{version}/ui-packages/images/assets/round-arduino-logo.svg %{buildroot}%{_scalableiconsdir}/cc.arduino.AppLab.svg

install -dm755 %{buildroot}%{_appsdir}/
install -p -m644 %{SOURCE2} %{buildroot}%{_appsdir}/%{appid}.desktop

cp arduino-app-lab-al-%{version}/LICENSE -t .

%terra_appstream -o %{SOURCE3}

%check
desktop-file-validate %{buildroot}%{_appsdir}/%{appid}.desktop

%files
%license LICENSE
%{_bindir}/%{name}
%{_scalableiconsdir}/%{appid}.svg
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Wed Jul 1 2026 Jaiden Riordan <jade@fyralabs.com>
- Source changes
* Thu Dec 25 2025 Owen Zimmerman <owen@fyralabs.com>
- Add %check, update macros
* Thu Dec 4 2025 Jaiden Riordan <jade@fyralabs.com>
- Package arduino-app-lab-bin
