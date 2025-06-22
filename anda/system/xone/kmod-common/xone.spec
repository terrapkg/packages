%global commit a9505894818dd6d164cab80c3e6acdc113454348
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250622
%global ver 0.3.1
%global _dracutconfdir %{_prefix}/lib/dracut/dracut.conf.d
%global firmware_hash0 48084d9fa53b9bb04358f3bb127b7495dc8f7bb0b3ca1437bd24ef2b6eabdf66
%global firmware_hash1 080ce4091e53a4ef3e5fe29939f51fd91f46d6a88be6d67eb6e99a5723b3a223

Name:           xone
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
### Windows drivers and firmware files:
Source2:        http://download.windowsupdate.com/c/msdownload/update/driver/drvs/2017/07/1cd6a87c-623f-4407-a52d-c31be49e925c_e19f60808bdcbfbd3c3df6be3e71ffc52e43261e.cab
Source3:        https://catalog.s.download.windowsupdate.com/d/msdownload/update/driver/drvs/2015/12/20810869_8ce2975a7fbaa06bcfb0d8762a6275a1cf7c1dd3.cab
### Microsoft TOU copy:
Source4:        https://www.microsoft.com/en-us/legal/terms-of-use
BuildRequires:  cabextract
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires:       wireless-regdb
Requires:       %{name}-firmware = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       (akmod-%{name} = %{?epoch:%{epoch}:}%{version} or dkms-%{name} = %{?epoch:%{epoch}:}%{version})
Requires(post): dracut
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
Conflicts:      xow <= 0.5
Obsoletes:      xow <= 0.5
%if 0%{?fedora} <= 43 || 0%{?rhel} <= 10
Conflicts:      %{name} < %{?epoch:%{epoch}:}0.3^20250419git.c682b0c
Obsoletes:      %{name} < %{?epoch:%{epoch}:}0.3^20250419git.c682b0c
%endif
BuildArch:      noarch
Packager:       Gilver E. <rockgrub@disroot.org>

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
%if 0%{?fedora} <= 43 || 0%{?rhel} <= 10
Obsoletes:      %{name}-firmware < %{?epoch:%{epoch}:}0.3^20250419git.c682b0c
%endif
BuildArch:       noarch

%description     firmware
Proprietary firmware for XBox controller dongles.
 
%prep
%autosetup -p1 -n %{name}-%{commit}
/usr/bin/cp %{SOURCE4} .
/usr/bin/sed -nE '/^BUILT_MODULE_NAME/{s@^.+"(.+)"@\1@; s|-|_|g; p}' dkms.conf > %{name}.conf

### Firmware:
# The .bin files have the same name so put them in subdirs
mkdir firm{0..1}

pushd firm0
cabextract -F FW_ACC_00U.bin %{SOURCE2}
echo %{firmware_hash0} FW_ACC_00U.bin | sha256sum -c
popd

pushd firm1
cabextract -F FW_ACC_00U.bin %{SOURCE3}
echo %{firmware_hash1} FW_ACC_00U.bin | sha256sum -c
popd

%install
# xone-gip-headset module should have the snd-pcm and snd-seq modules be preloaded or it will give errors on boot due to injecting late.
# It still loads afterwards, but this error is easily fixable by just loading the modules in the initramfs.
install -Dpm644 %{SOURCE1} %{buildroot}%{_dracutconfdir}/60-%{name}-snd.conf

# Blacklist:
install -Dpm644 install/modprobe.conf %{buildroot}%{_modprobedir}/60-%{name}.conf

# Firmware:
install -Dpm644 firm0/FW_ACC_00U.bin %{buildroot}%{_prefix}/lib/firmware/xow_dongle.bin
install -Dpm644 firm1/FW_ACC_00U.bin %{buildroot}%{_prefix}/lib/firmware/xow_dongle_045e_02e6.bin

# Akmods modules
install -Dm644 %{name}.conf -t %{buildroot}%{_modulesloaddir}

%files
%license LICENSE
%doc README.md
%{_modprobedir}/60-%{name}.conf
%{_dracutconfdir}/60-%{name}-snd.conf

%files akmod-modules
%{_modulesloaddir}/%{name}.conf

%files firmware
%license terms-of-use
%{_prefix}/lib/firmware/xow_dongle.bin
%{_prefix}/lib/firmware/xow_dongle_045e_02e6.bin

%post
/usr/bin/dracut -f

%postun
/usr/bin/dracut -f

%post firmware
echo "The firmware for the wireless dongle is subject to Microsoft's Terms of Use:"
echo 'https://www.microsoft.com/en-us/legal/terms-of-use'

%changelog
* Thu Apr 17 2025 Gilver E. <rockgrub@disroot.org> - 0.3^20250418git.ecdd59e-2%{?dist}
- Added additional firmware needed for dongle pairing on some controllers
* Thu Feb 27 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
