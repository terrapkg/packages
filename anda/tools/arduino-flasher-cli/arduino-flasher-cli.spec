%global goipath         github.com/arduino/arduino-flasher-cli
Version:                0.5.1

%gometa -f

%global common_description %{expand:
CLI tool to flash UNO Q boards with the latest Arduino Linux image.}

%global golicenses      LICENSE license_header.tpl
%global godocs          README.md

%ifarch x86_64
%global arch amd64
%elifarch aarch64
%global arch arm64
%endif

Name:           arduino-flasher-cli
Release:        1%{?dist}
Summary:        CLI tool to flash UNO Q boards with the latest Arduino Linux image
License:        GPL-3.0-or-later
URL:            %{gourl}
Source0:        %{gosource}
Source1:        https://raw.githubusercontent.com/arduino/arduino-flasher-cli/refs/heads/main/README.md
BuildRequires:  qdl
%description %{common_description}

%gopkg

%prep
%goprep

%build
mkdir -p internal/updater/artifacts/resources_linux_%{arch}
cp %{_bindir}/qdl internal/updater/artifacts/resources_linux_%{arch}/qdl
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/cmd/arduino-flasher-cli %{goipath}/cmd/arduino-flasher-cli

%install
cp %{S:1} README.md
ls -laH %{gobuilddir}/cmd/
install -Dm755 %{gobuilddir}/cmd/arduino-flasher-cli -t %buildroot%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/arduino-flasher-cli

%changelog
* Fri Nov 14 2025 Jaiden Riordan <jade@fyralabs.com>
- Package Arduino Flasher :3
