%global goipath github.com/kairos-io/kairos-lab
Version:        0.1.5

%gometa -f

Name:           kairos-lab
Release:        1%{?dist}
Summary:        CLI for running Kairos virtual machines locally
License:        Apache-2.0
URL:            https://github.com/kairos-io/kairos-lab
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  go-rpm-macros
BuildRequires:  go-srpm-macros
Requires:       dnsmasq
Requires:       iproute
Requires:       qemu

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Kairos Lab is a command-line tool for creating and managing local Kairos
virtual machines using QEMU.

%prep
%autosetup

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/%{name} ./cmd/%{name}

%install
install -Dm0755 %{gobuilddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Mon Sep 21 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
