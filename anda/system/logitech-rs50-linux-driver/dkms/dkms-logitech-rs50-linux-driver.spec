%global commit 09a7f6306b1caa744bc3794620e3a932297fe79e
%global debug_package %{nil}
%global modulename logitech-rs50-linux-driver
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260806

Name:           dkms-%{modulename}
Version:        1.0^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Linux kernel driver for the Logitech RS50 Direct Drive Wheel Base (USB ID 046d:c276)
License:        GPL-2.0-only
URL:            https://github.com/mescon/%{modulename}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Source1:        dkms.conf
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Conflicts:      akmod-%{modulename}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
BuildArch:      x86_64
Provides:       %{modulename}-kmod
Packager:       Luan V. <luanv.oliveira@outlook.com>

%description
Linux kernel driver for the Logitech RS50 Direct Drive Wheel Base (USB ID 046d:c276).
This is a patched version of the hid-logitech-hidpp driver that adds RS50 support with force feedback (FF_CONSTANT) and exposes all G Hub settings via sysfs for runtime configuration.
Note: This driver replaces the in-kernel hid-logitech-hidpp module and continues to support all other Logitech HID++ devices (mice, keyboards, other racing wheels like the G29, G920, G923, etc.).

%package       akmod-modules
Summary:       Modules for Akmods
Requires:      akmod-%{name}
BuildArch:     noarch

%description   akmod-modules
Akmods modules for the akmod-%{name} package.

%prep
%autosetup -p1 -n logitech-trueforce-linux-driver-%{commit}
pushd mainline
mkdir build
cp %{SOURCE1} ./dkms.conf
sed -i -e 's/__VERSION_STRING/%{version}/g' dkms.conf
popd

%install
mkdir -p %{buildroot}%{_usrsrc}/logitech-trueforce-linux-driver-%{version}
cp -fr ./mainline/* %{buildroot}%{_usrsrc}/logitech-trueforce-linux-driver-%{version}/

%post
dkms add -m logitech-trueforce-linux-driver -v %{version} -q --rpm_safe_upgrade || :
# Rebuild and make available for the currently running kernel:
dkms build -m logitech-trueforce-linux-driver -v %{version} -q || :
dkms install -m logitech-trueforce-linux-driver -v %{version} -q --force || :

%preun
dkms remove -m logitech-trueforce-linux-driver -v %{version} -q --all --rpm_safe_upgrade || :

%files
%{_usrsrc}/logitech-trueforce-linux-driver-%{version}

%changelog
* Sun May 03 2026 Luan V. <luanv.oliveira@outlook.com> - 1.0^20260502git.7296717-2
- ship our own dkms.conf, allowing full cleanup on uninstall
* Fri May 01 2026 Luan V. <luanv.oliveira@outlook.com> - 1.0^20260430git.df7f149-2
- fix build due to upstream changes
- resolve spec warnings: add Packager tag, remove autochangelog
