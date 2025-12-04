Name:           arduino-app-lab-bin
Version:        0.2.4
Release:        1%{?dist}
Summary:        A powerful visual environment for managing the Arduino UNO Q

URL:            https://www.arduino.cc/en/software
License:        GPL-3.0

Source0:        https://downloads.arduino.cc/AppLab/Stable/ArduinoAppLab_%{version}_Linux_x86-64.tar.gz
Source1:        https://downloads.arduino.cc/AppLab/Stable/source-app-lab-${version}.zip
Source2:        cc.arduino.AppLab.desktop

ExclusiveArch:  x86_64

Requires:       android-tools
Suggests:       arduino-flasher-cli #arduino-app-cli

Packager:       Jaiden Riordan <jade@fyralabs.com>

%description
%summary.

%prep
%autosetup -n ArduinoAppLab_%{version}_Linux_x86_64
%autosetup -n source-app-lab-${version}

%build

%install
install -dm755 %{buildroot}ArduinoAppLab_%{version}_Linux_x86_64/arduino-app-lab
cp -a * %{buildroot}%{_bindir}/%{name}/

install -dm755 %{buildroot}source-app-lab-0.2.4/source-app-lab/ui-packages/images/assets/round-arduino-logo.svg
cp -a * %{buildroot}%{_datadir}/pixmaps/round-arduino-logo.svg

%changelog
* Thu Dec 4 2025 Jaiden Riordan  <jade@fyralabs.com>
- Package arduino-app-lab-bin

