%global commit 1635bbd0ea044d1c3681b1843b5a0f3e878d0ed0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260504

Name:           logitech-rs50-linux-driver
Version:        1.0^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Linux kernel driver for the Logitech RS50 Direct Drive Wheel Base (USB ID 046d:c276)
License:        GPL-2.0-only
URL:            https://github.com/mescon/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Source1:        com.github.rs50.metainfo.xml
Source2:        logi-rs50-proton-setup.sh
Source3:        README.terra.md
BuildRequires:  systemd-rpm-macros
Recommends:     trueforce-sdk
Requires:       %{name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
Packager:       Luan V. <luanv.oliveira@outlook.com>
BuildArch:      noarch

%description
Linux kernel driver for the Logitech RS50 Direct Drive Wheel Base (USB ID 046d:c276).
This is a patched version of the hid-logitech-hidpp driver that adds RS50 support with force feedback (FF_CONSTANT) and exposes all G Hub settings via sysfs for runtime configuration.
Note: This driver replaces the in-kernel hid-logitech-hidpp module and continues to support all other Logitech HID++ devices (mice, keyboards, other racing wheels like the G29, G920, G923, etc.).

%package       akmod-modules
Summary:       Modules for Akmods
Requires:      %{name}-kmod = %{?epoch:%{epoch}:}%{version}
BuildArch:     noarch

%description   akmod-modules
Akmods modules for the akmod-%{name} package.

%prep
%autosetup -p1 -n %{name}-%{commit}

echo hid-logitech-hidpp > %{name}.conf
mv sdk/README.md README-SDK.md
cp %{SOURCE3} README.terra.md

%install
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/com.github.rs50.metainfo.xml

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/tools
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/Logi
ln -sr %_sharedstatedir/%{name} %{buildroot}%{_datadir}/%{name}/sdk

install -Dm755 tools/install-tf-shim.sh %{buildroot}%{_datadir}/%{name}/tools/
install -Dm755 %{SOURCE2} %{buildroot}%{_bindir}/logi-rs50-proton-setup

install -Dm644 udev/70-logitech-rs50.rules -t %{buildroot}%{_udevrulesdir}/
install -D -m644 userspace/libtrueforce/udev/99-logitech-rs50-trueforce.rules %{buildroot}%{_udevrulesdir}/70-logitech-rs50-trueforce.rules

# Akmods modules
install -Dm644 %{name}.conf -t %{buildroot}%{_modulesloaddir}

%posttrans
### Skip triggering if udevd isn't accessible
if [ -S /run/udev/control ]; then
    /usr/bin/udevadm control --reload
    /usr/bin/udevadm trigger --subsystem-match=hidraw
fi


%files
%doc README.terra.md README.md README-SDK.md CHANGELOG.md rs-wheel-hub-button-layout.png docs/*
%{_datadir}/metainfo/com.github.rs50.metainfo.xml
%{_udevrulesdir}/70-logitech-rs50.rules
%{_udevrulesdir}/70-logitech-rs50-trueforce.rules
%{_datadir}/%{name}/tools/*
%{_bindir}/logi-rs50-proton-setup
%{_datadir}/%{name}/sdk
%dir %{_sharedstatedir}/%{name}/Logi

%files akmod-modules
%{_modulesloaddir}/%{name}.conf

%changelog
* Fri May 01 2026 Luan V. <luanv.oliveira@outlook.com> - 1.0^20260430git.df7f149-2
- add logi-rs50-proton-setup script together with a readme which explains where to put the necessary files.
- and add udev rules together with a posttrans script to reload and trigger devices on install
- fix spec warnings: add Packager tag and remove autochangelog
