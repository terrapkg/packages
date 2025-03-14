%global commit aeb27e6d98f7b22b3672701af6171612254a4d0c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250313
%global ver 0.3
%global _dracutconfdir %{_prefix}/lib/dracut/dracut.conf.d
%global firmware_hash 48084d9fa53b9bb04358f3bb127b7495dc8f7bb0b3ca1437bd24ef2b6eabdf66

Name:           xone
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        1%?dist
Summary:        Linux kernel driver for Xbox One and Xbox Series X|S accessories common files
License:        GPL-2.0-or-later
URL:            https://github.com/dlundqvist/xone
Source0:        %{url}/archive/%{commit}.tar.gz#/xone-%{shortcommit}.tar.gz
Source1:        modules.conf
### Windows driver and firmware file:
Source2:        http://download.windowsupdate.com/c/msdownload/update/driver/drvs/2017/07/1cd6a87c-623f-4407-a52d-c31be49e925c_e19f60808bdcbfbd3c3df6be3e71ffc52e43261e.cab
### Microsoft TOU copy:
Source3:        https://www.microsoft.com/en-us/legal/terms-of-use
BuildRequires:  cabextract
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires:       wireless-regdb
Requires:       %{name}-firmware = 1.0.46.1
Requires:       (akmod-%{name} = %{?epoch:%{epoch}:}%{version} or dkms-%{name} = %{?epoch:%{epoch}:}%{version})
Requires(post): dracut
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
Obsoletes:      %{name}-kmod-common < %{?epoch:%{epoch}:}%{version}-2%{?dist}
Conflicts:      xow <= 0.5
Obsoletes:      xow <= 0.5
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
Version:         1.0.46.1
Summary:         Firmware for the XBox One controller dongle
License:         Proprietary
Requires:        wireless-regdb
BuildArch:       noarch

%description     firmware
Proprietary firmware for XBox controller dongles.
 
%prep
%autosetup -p1 -n %{name}-%{commit}
/usr/bin/cp %{SOURCE3} .
/usr/bin/sed -nE '/^BUILT_MODULE_NAME/{s@^.+"(.+)"@\1@; s|-|_|g; p}' dkms.conf > %{name}.conf

# Firmware:
cabextract -F FW_ACC_00U.bin %{SOURCE2}
echo %{firmware_hash} FW_ACC_00U.bin | sha256sum -c

%install
# xone-gip-headset module should have the snd-pcm and snd-seq modules be preloaded or it will give errors on boot due to injecting late.
# It still loads afterwards, but this error is easily fixable by just loading the modules in the initramfs.
install -Dpm644 %{SOURCE1} %{buildroot}%{_dracutconfdir}/60-%{name}-snd.conf

# Blacklist:
install -Dpm644 install/modprobe.conf %{buildroot}%{_modprobedir}/60-%{name}.conf

# Firmware:
install -Dpm644 FW_ACC_00U.bin %{buildroot}%{_prefix}/lib/firmware/xow_dongle.bin

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

%post
/usr/bin/dracut -f

%postun
/usr/bin/dracut -f

%post firmware
echo "The firmware for the wireless dongle is subject to Microsoft's Terms of Use:"
echo 'https://www.microsoft.com/en-us/legal/terms-of-use'

%changelog
* Thu Feb 27 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
