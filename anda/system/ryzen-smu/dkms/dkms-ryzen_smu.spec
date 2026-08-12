%global commit 1be4fb1cd9d60b5ddefc2a4201a898766a731400
%global debug_package %{nil}
%global modulename ryzen_smu
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260626

Name:           dkms-%{modulename}
Version:        0.1.7^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Linux kernel driver that exposes access to the SMU (System Management Unit) for certain AMD Ryzen processors
License:        GPL-2.0-only
URL:            https://github.com/amkillam/ryzen_smu
Source:         %{url}/archive/%{commit}.tar.gz
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
BuildArch:      x86_64
Requires:       dkms
Conflicts:      akmod-%{modulename}
Provides:       %{modulename}-kmod
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>

%description
Ryzen SMU is a Linux kernel driver that exposes access to the SMU (System
Management Unit) for certain AMD Ryzen processors. It allows reading and writing
SMU mailbox commands and exposes the power metrics (PM) table via sysfs.
Use at your own risk.

%package       akmod-modules
Summary:       Modules for Akmods
Requires:      akmod-%{name}
BuildArch:     noarch

%description   akmod-modules
Akmods modules for the akmod-%{name} package.

%prep
%autosetup -p1 -n %{modulename}-%{commit}
/usr/bin/sed -i -e 's/@VERSION@/%{version}/g' -e 's/@CFLGS@//g' dkms.conf
# Fix bad python3 shebangs
find . -name '*.py' -exec /usr/bin/sed -i '1s|^#![[:space:]]*/bin/python$|#!/usr/bin/python3|' {} +

%install
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}
cp -fr ./ %{buildroot}%{_usrsrc}/%{modulename}-%{version}/

%post
dkms add -m %{modulename} -v %{version} -q --rpm_safe_upgrade || :
# Rebuild and make available for the currently running kernel:
dkms build -m %{modulename} -v %{version} -q || :
dkms install -m %{modulename} -v %{version} -q --force || :

%files
%{_usrsrc}/%{modulename}-%{version}
%license LICENSE
%doc README.md

%changelog
* Thu Jun 04 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package release
