%global appid cc.arduino.AppLab

Name:           arduino-app-lab-bin
Version:        0.2.4
Release:        1%{?dist}
Summary:        A powerful visual environment for managing the Arduino UNO Q

URL:            https://www.arduino.cc/en/software
License:        GPL-3.0

Source0:        https://downloads.arduino.cc/AppLab/Stable/ArduinoAppLab_%{version}_Linux_x86-64.tar.gz
Source1:        https://downloads.arduino.cc/AppLab/Stable/source-app-lab-%{version}.zip
Source2:        cc.arduino.AppLab.desktop
Source3:        cc.arduino.AppLab.metainfo.xml

ExclusiveArch:  x86_64

Requires:       android-tools

BuildRequires:  terra-appstream-helper

Suggests:       arduino-flasher-cli

Packager:       Jaiden Riordan <jade@fyralabs.com>

%description
%summary.

%prep
tar -xvf %{_sourcedir}/ArduinoAppLab_%{version}_Linux_x86-64.tar.gz
unzip %{_sourcedir}/source-app-lab-%{version}.zip

%install
install -dm755 %{buildroot}%{_bindir}
install -p -m755 ArduinoAppLab_%{version}_Linux_x86-64/arduino-app-lab %{buildroot}%{_bindir}/%{name}

install -dm755 %{buildroot}%{_datadir}/pixmaps/
install -p -m644 source-app-lab/ui-packages/images/assets/round-arduino-logo.svg %{buildroot}%{_datadir}/pixmaps/cc.arduino.AppLab.svg

install -dm755 %{buildroot}%{_datadir}/applications/
install -p -m644 %{SOURCE2} %{buildroot}%{_datadir}/applications/cc.arduino.AppLab.desktop

%terra_appstream -o %{SOURCE3}

%files 
%{_bindir}/%{name}
%{_datadir}/pixmaps/cc.arduino.AppLab.svg
%{_datadir}/applications/cc.arduino.AppLab.desktop
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Thu Dec 4 2025 Jaiden Riordan  <jade@fyralabs.com>
- Package arduino-app-lab-bin