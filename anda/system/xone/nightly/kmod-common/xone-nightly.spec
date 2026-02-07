%global commit 10d12acb50e84145b7b5aef978695851040c05a4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260206
%global ver 0.5.5
%global modulename xone
%global _dracutconfdir %{_prefix}/lib/dracut/dracut.conf.d
%global firmware_hash0 080ce4091e53a4ef3e5fe29939f51fd91f46d6a88be6d67eb6e99a5723b3a223
%global firmware_hash1 48084d9fa53b9bb04358f3bb127b7495dc8f7bb0b3ca1437bd24ef2b6eabdf66
%global firmware_hash2 0023a7bae02974834500c665a281e25b1ba52c9226c84989f9084fa5ce591d9b
%global firmware_hash3 e2710daf81e7b36d35985348f68a81d18bc537a2b0c508ffdfde6ac3eae1bad7

Name:           xone-nightly
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        1%?dist
%if 0%{?fedora} <= 43 || 0%{?rhel} <= 10
Epoch:          1
%endif
Summary:        Linux kernel driver for Xbox One and Xbox Series X|S accessories common files
License:        GPL-2.0-or-later
URL:            https://github.com/dlundqvist/xone
Source0:        %{url}/archive/%{commit}.tar.gz#/xone-%{shortcommit}.tar.gz
Source1:        modules.conf
Source2:        https://catalog.s.download.windowsupdate.com/d/msdownload/update/driver/drvs/2017/03/2ea9591b-f751-442c-80ce-8f4692cdc67b_6b555a3a288153cf04aec6e03cba360afe2fce34.cab
Source3:        https://catalog.s.download.windowsupdate.com/c/msdownload/update/driver/drvs/2017/07/1cd6a87c-623f-4407-a52d-c31be49e925c_e19f60808bdcbfbd3c3df6be3e71ffc52e43261e.cab
Source4:        https://catalog.s.download.windowsupdate.com/c/msdownload/update/driver/drvs/2017/06/1dbd7cb4-53bc-4857-a5b0-5955c8acaf71_9081931e7d664429a93ffda0db41b7545b7ac257.cab
Source5:        https://catalog.s.download.windowsupdate.com/d/msdownload/update/driver/drvs/2017/08/aeff215c-3bc4-4d36-a3ea-e14bfa8fa9d2_e58550c4f74a27e51e5cb6868b10ff633fa77164.cab
### Microsoft TOU copy:
Source6:        https://www.microsoft.com/en-us/legal/terms-of-use
BuildRequires:  cabextract
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires:       wireless-regdb
Requires:       %{name}-firmware = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-kmod = %{?epoch:%{epoch}:}%{version}
Requires(post): dracut
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
Conflicts:      %{modulename}
Conflicts:      xow <= 0.5
Obsoletes:      xow <= 0.5
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

%description
Linux kernel driver for Xbox One and Xbox Series X|S accessories common files.

%package        akmod-modules
Summary:        Modules for Akmods
Requires:       akmod-%{name}
BuildArch:      noarch

%description    akmod-modules
Akmods modules for the akmod-%{name} package.

%package         firmware
Summary:         Firmware for the XBox One controller dongle
License:         Proprietary
Requires:        wireless-regdb
BuildArch:       noarch

%description     firmware
Proprietary firmware for XBox controller dongles.
 
%prep
%autosetup -p1 -n %{modulename}-%{commit}
/usr/bin/sed -nE '/^BUILT_MODULE_NAME/{s@^.+"(.+)"@\1@; s|-|_|g; p}' dkms.conf > %{modulename}.conf

### Firmware:
# Some of the .bin files have the same name so put them in subdirs
mkdir firm{0..4}

pushd firm0
cabextract -F FW_ACC_00U.bin %{SOURCE2}
echo %{firmware_hash0} FW_ACC_00U.bin | sha256sum -c
popd

pushd firm1
cabextract -F FW_ACC_00U.bin %{SOURCE3}
echo %{firmware_hash1} FW_ACC_00U.bin | sha256sum -c
popd

pushd firm2
cabextract -F FW_ACC_CL.bin %{SOURCE4}
echo %{firmware_hash2} FW_ACC_CL.bin | sha256sum -c
popd

pushd firm3
cabextract -F FW_ACC_BR.bin %{SOURCE5}
echo %{firmware_hash3} FW_ACC_BR.bin | sha256sum -c
popd

%install
# xone-gip-headset module should have the snd-pcm and snd-seq modules be preloaded or it will give errors on boot due to injecting late.
# It still loads afterwards, but this error is easily fixable by just loading the modules in the initramfs.
install -Dpm644 %{SOURCE1} %{buildroot}%{_dracutconfdir}/60-%{modulename}-snd.conf

# Blacklist:
install -Dpm644 install/modprobe.conf %{buildroot}%{_modprobedir}/60-%{modulename}.conf

# Firmware:
install -Dpm644 firm0/FW_ACC_00U.bin %{buildroot}%{_prefix}/lib/firmware/xone_dongle_02e6.bin
install -Dpm644 firm1/FW_ACC_00U.bin %{buildroot}%{_prefix}/lib/firmware/xone_dongle_02fe.bin
install -Dpm644 firm2/FW_ACC_CL.bin %{buildroot}%{_prefix}/lib/firmware/xone_dongle_02f9.bin
install -Dpm644 firm3/FW_ACC_BR.bin %{buildroot}%{_prefix}/lib/firmware/xone_dongle_091e.bin

# Akmods modules
install -Dm644 %{modulename}.conf -t %{buildroot}%{_modulesloaddir}

# TOU file
/usr/bin/cp %{SOURCE6} .

%files
%license LICENSE
%doc README.md
%{_modprobedir}/60-%{modulename}.conf
%{_dracutconfdir}/60-%{modulename}-snd.conf

%files akmod-modules
%{_modulesloaddir}/%{modulename}.conf

%files firmware
%license terms-of-use
%{_prefix}/lib/firmware/xone_dongle_02e6.bin
%{_prefix}/lib/firmware/xone_dongle_02fe.bin
%{_prefix}/lib/firmware/xone_dongle_02f9.bin
%{_prefix}/lib/firmware/xone_dongle_091e.bin

%postun
/usr/bin/dracut -f || :

%post firmware
echo "The firmware for the wireless dongle is subject to Microsoft's Terms of Use:"
echo 'https://www.microsoft.com/en-us/legal/terms-of-use'

%changelog
* Wed Dec 10 2025 Gilver E. <rockgrub@disroot.org> - 0.3.4^20250718git.778dbc9-2
- Added new firmware files
* Thu Apr 17 2025 Gilver E. <rockgrub@disroot.org> - 0.3^20250418git.ecdd59e-2
- Added additional firmware needed for dongle pairing on some controllers
* Thu Feb 27 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
