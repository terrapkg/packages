%global commit df7f1494f3bd584b8650304be7a37eca4bb49aa5
%global debug_package %{nil}
%global modulename logitech-rs50-linux-driver
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260430

Name:           dkms-%{modulename}
Version:        1.0^%{commitdate}git.%{shortcommit}
Release:        2%{?dist}
Summary:        Linux kernel driver for the Logitech RS50 Direct Drive Wheel Base (USB ID 046d:c276)
License:        GPL-2.0-only
URL:            https://github.com/mescon/%{modulename}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Patch0:         fix-dkms-conf.patch
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
%autosetup -p1 -n %{modulename}-%{commit}
pushd mainline
mkdir build
sed -i -e 's/__VERSION_STRING/%{version}/g' dkms.conf
popd

%install
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}
cp -fr ./mainline/* %{buildroot}%{_usrsrc}/%{modulename}-%{version}/

%post
dkms add -m %{modulename} -v %{version} -q --rpm_safe_upgrade || :
# Rebuild and make available for the currently running kernel:
dkms build -m %{modulename} -v %{version} -q || :
dkms install -m %{modulename} -v %{version} -q --force || :

%preun
dkms remove -m %{modulename} -v %{version} -q --all --rpm_safe_upgrade || :

%files
%{_usrsrc}/%{modulename}-%{version}


%changelog
* Fri May 01 2026 Luan V. <luanv.oliveira@outlook.com> - 1.0^20260430git.df7f149-2
- fix build due to upstream changes
- resolve spec warnings: add Packager tag, remove autochangelog
