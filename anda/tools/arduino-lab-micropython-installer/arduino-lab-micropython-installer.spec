%define debug_package %{nil}

%ifarch x86_64
%define arch x64
%elifarch aarch64
%define arch arm64
%endif

Name:           lab-micropython-installer
Version:        1.4.0
Release:        1%?dist
License:        AGPL-3.0 AND %electron_license
Summary:        This repository hosts the entire code of the Arduino MicroPython Installer tool
URL:            https://github.com/arduino/lab-micropython-installer
Source0:        %url/archive/refs/tags/v%version.tar.gz
Source1:        micropython-installer.desktop
Packager:       Owen Zimmerman <owen@fyralabs.com>
Requires:       xdg-utils gtk3 libnotify nss libXtst xdg-utils libdrm libxcb
BuildRequires:  anda-srpm-macros pnpm nodejs-npm git-core gcc gcc-c++ make desktop-file-utils zlib-ng-compat-devel
Provides:       arduino-lab-micropython-installer

%description
MicroPython Installer for Arduino is a cross-platform tool that streamlines the process of downloading
and installing MicroPython firmware on compatible Arduino boards. It is compatible with macOS, Linux,
and Windows and is built using the Electron framework.

%prep
%autosetup -n %{name}-%{version}

%build
npm install
npm run package

%install
mkdir -p %{buildroot}%{_datadir}/micropython-installer
mkdir -p %{buildroot}%{_libdir}/micropython-installer

install -Dm755 out/MicroPython\ Installer-linux-%{arch}/micropython-installer           %{buildroot}%{_bindir}/micropython-installer
cp -r out/MicroPython\ Installer-linux-%{arch}/*                                        %{buildroot}%{_libdir}/micropython-installer
install -Dm644 assets/app-icon.png                                                      %{buildroot}%{_iconsdir}/hicolor/512x512/apps/micropython-installer.png
install -Dm644 %{SOURCE1}                                                               %{buildroot}%{_datadir}/applications/micropython-installer.desktop

%files
%doc README.md
%license LICENSE
%license MicroPython\ Installer-linux-x64/micropython-installer/LICENSE
%{_bindir}/micropython-installer
%{_libdir}/micropython-installer/
%{_iconsdir}/hicolor/512x512/apps/micropython-installer.png
%{_datadir}/applications/micropython-installer.desktop

%changelog
* Sat Dec 06 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
