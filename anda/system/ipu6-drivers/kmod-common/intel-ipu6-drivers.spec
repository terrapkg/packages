%global debug_package %{nil}
%global ipu6_commit e89983c628d046b2f77af3b6678cc49c2dd58332
%global ipu6_commitdate 20250521
%global ipu6_shortcommit %(c=%{ipu6_commit}; echo ${c:0:7})
%global usbio_commit 4fb690c6d15a81c492954636c2db396cb700a119
%global usbio_commitdate 20241210
%global usbio_shortcommit %(c=%{usbio_commit}; echo ${c:0:7})
# Actual "release" version, currently unused as the release versions are back and forth on if on if they use 1.0.0 or 1.0.1
# Use this if they ever stop doing that I guess
%global ver 1.0.1

Name:           intel-ipu6-drivers
Summary:        Common files for Intel IPU6 drivers
Version:        0^%{ipu6_commitdate}git.%{ipu6_shortcommit}
Release:        1%?dist
License:        GPL-2.0-or-later
URL:            https://github.com/intel/ipu6-drivers
Source0:        https://github.com/intel/ipu6-drivers/archive/%{ipu6_commit}/ipu6-drivers-%{ipu6_shortcommit}.tar.gz
Source1:        https://github.com/intel/usbio-drivers/archive/%{usbio_commit}/usbio-drivers-%{usbio_shortcommit}.tar.gz
Requires:       ipu6-camera-bins
Requires:       (intel-ipu6-kmod = %{?epoch:%{epoch}:}%{version} or dkms-intel-ipu6 = %{?epoch:%{epoch}:}%{version})
Provides:       intel-ipu6-kmod-common = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch:      noarch
Packager:       Gilver E. <rockgrub@disroot.org>

%description
Common files for the Intel IPU6 camera drivers.

%prep
%setup -q -c -a 1

%build

%install
install -Dpm644 usbio-drivers-%{usbio_commit}/LICENSE.txt -t %{buildroot}%{_defaultlicensedir}/%{name}/usbio-drivers/
install -Dpm644 usbio-drivers-%{usbio_commit}/{CODE_OF_CONDUCT.md,README.md,SECURITY.md,security.md} -t %{buildroot}%{_defaultdocdir}/%{name}/usbio-drivers/

%files
%license ipu6-drivers-%{ipu6_commit}/LICENSE
%doc ipu6-drivers-%{ipu6_commit}/README.md
%doc ipu6-drivers-%{ipu6_commit}/SECURITY.md
%{_defaultdocdir}/%{name}/usbio-drivers
%{_defaultlicensedir}/%{name}/usbio-drivers

%changelog
* Thu Apr 24 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
