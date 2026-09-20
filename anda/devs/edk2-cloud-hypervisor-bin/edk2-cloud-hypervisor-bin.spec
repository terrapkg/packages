%global release_tag vUDK2018
%global commit_date 20260918
%global shortcommit K2018

Name:           edk2-cloud-hypervisor-bin
Version:        0^%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Prebuilt EDK2 UEFI firmware for Cloud Hypervisor
License:        BSD-2-Clause-Patent
URL:            https://github.com/cloud-hypervisor/edk2
Source0:        https://github.com/cloud-hypervisor/edk2/releases/download/%{release_tag}/CLOUDHV.fd
Source1:        https://github.com/cloud-hypervisor/edk2/releases/download/%{release_tag}/CLOUDHV_EFI.fd
Source2:        https://raw.githubusercontent.com/cloud-hypervisor/edk2/%{release_tag}/License.txt
BuildArch:      noarch

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Prebuilt EDK2 UEFI firmware for Cloud Hypervisor. The firmware is built for
Cloud Hypervisor and supports UEFI boot on x86-64 guests.

%package aarch64
Summary:        AArch64 UEFI firmware for Cloud Hypervisor
Requires:       %{name} = %{evr}
BuildArch:      noarch

%description aarch64
AArch64 UEFI firmware for Cloud Hypervisor.

%prep
cp %{SOURCE2} LICENSE.txt

%build

%install
install -Dpm644 %{SOURCE0} %{buildroot}%{_datadir}/edk2/cloud-hypervisor/CLOUDHV.fd
install -Dpm644 %{SOURCE1} %{buildroot}%{_datadir}/edk2/cloud-hypervisor/CLOUDHV_EFI.fd

%files
%license LICENSE.txt
%{_datadir}/edk2/cloud-hypervisor/CLOUDHV.fd

%files aarch64
%{_datadir}/edk2/cloud-hypervisor/CLOUDHV_EFI.fd

%changelog
* Fri Sep 18 2026 Cypress Reed <cypress@fyralabs.com>
- initial commit
