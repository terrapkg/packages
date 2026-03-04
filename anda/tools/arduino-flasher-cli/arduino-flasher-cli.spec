%global goipath         github.com/arduino/arduino-flasher-cli
Version:                0.5.0

%gometa -f

%global common_description %{expand:
CLI tool to flash UNO Q boards with the latest Arduino Linux image.}

%global golicenses      LICENSE license_header.tpl
%global godocs          README.md

Name:           arduino-flasher-cli
Release:        1%?dist
Summary:        CLI tool to flash UNO Q boards with the latest Arduino Linux image
License:        GPL-3.0-only
URL:            %{gourl}
Source0:        %{gosource}
Source1:        https://raw.githubusercontent.com/arduino/arduino-flasher-cli/refs/heads/main/README.md
BuildRequires:  anda-srpm-macros qdl
ExclusiveArch:  x86_64

%description %{common_description}

%gopkg

%prep
%goprep

%build
mkdir -p updater/artifacts/resources_linux_amd64
cp %{_bindir}/qdl updater/artifacts/resources_linux_amd64/qdl
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/arduino-cli %{goipath}

%install
cp %{S:1} README.md
install -Dm755 %{gobuilddir}/bin/arduino-cli -t %buildroot%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/arduino-cli

%changelog
* Fri Nov 14 2025 Jaiden Riordan <jade@fyralabs.com>
- Package Arduino Flasher :3
