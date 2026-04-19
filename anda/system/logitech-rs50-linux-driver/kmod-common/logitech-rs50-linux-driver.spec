%global commit 7249eef3280912ad8b9166441596d9d14f696fb6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260419

Name:           logitech-rs50-linux-driver
Version:        1.0^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Linux kernel driver for the Logitech RS50 Direct Drive Wheel Base (USB ID 046d:c276)
License:        GPL-2.0-only
URL:            https://github.com/mescon/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Source1:        com.github.rs50.metainfo.xml
BuildRequires:  systemd-rpm-macros
Requires:       %{name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
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

%install
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/com.github.rs50.metainfo.xml

# Akmods modules
install -Dm644 %{name}.conf -t %{buildroot}%{_modulesloaddir}


%files
%doc README.md rs-wheel-hub-button-layout.png docs/*
%{_datadir}/metainfo/com.github.rs50.metainfo.xml

%files akmod-modules
%{_modulesloaddir}/%{name}.conf

%changelog
%autochangelog
