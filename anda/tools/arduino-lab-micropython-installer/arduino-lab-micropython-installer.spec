
Name:           lab-micropython-installer
%electronmeta
Version:        1.4.0
Release:        1%?dist
License:        AGPL-3.0 AND %electron_license
Summary:        This repository hosts the entire code of the Arduino MicroPython Installer tool
URL:            https://github.com/arduino/lab-micropython-installer
Source0:        %url/archive/refs/tags/v%version.tar.gz
Source1:        micropython-installer.desktop
Packager:       Owen Zimmerman <owen@fyralabs.com>
Requires:       libdrm libxcb
BuildRequires:  anda-srpm-macros
BuildRequires:  pnpm
Provides:       arduino-lab-micropython-installer
%description
MicroPython Installer for Arduino is a cross-platform tool that streamlines the process of downloading
and installing MicroPython firmware on compatible Arduino boards. It is compatible with macOS, Linux,
and Windows and is built using the Electron framework.

%prep
%autosetup -n %{name}-%{version}

%build
%npm_build -r package

%install
%electron_install -i micropython-installer -s micropython-installer -d micropython-installer -b micropython-installer
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/micropython-installer.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/micropython-installer
%{_libdir}/micropython-installer/
%{_hicolordir}/512x512/apps/micropython-installer.png
%{_appsdir}/micropython-installer.desktop

%changelog
* Sat Dec 06 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
