%global commit 0bb95d961664c7a0ac180f849fa16fe7da71922d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260425

Name:           ryzen_smu
Version:        0.1.7^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Linux kernel driver that exposes access to the SMU (System Management Unit) for certain AMD Ryzen processors
License:        GPL-2.0-only
URL:            https://github.com/amkillam/ryzen_smu
Source:         %{url}/archive/%{commit}.tar.gz
BuildRequires:  systemd-rpm-macros
Requires:       %{name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
BuildArch:      noarch
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>

%description
Ryzen SMU is a Linux kernel driver that exposes access to the SMU (System
Management Unit) for certain AMD Ryzen processors. It allows reading and writing
SMU mailbox commands and exposes the power metrics (PM) table via sysfs.
Use at your own risk.

%package       akmod-modules
Summary:       Modules for Akmods
Requires:      %{name}-kmod = %{?epoch:%{epoch}:}%{version}
BuildArch:     noarch

%description   akmod-modules
Akmods modules for the akmod-%{name} package.

%prep
%autosetup -p1 -n %{name}-%{commit}

# Autoload the module on boot
echo %{name} > %{name}.conf

# Akmods modules
install -Dm644 %{name}.conf -t %{buildroot}%{_modulesloaddir}

%files
%license LICENSE
%doc README.md

%files akmod-modules
%{_modulesloaddir}/%{name}.conf

%changelog
* Thu Jun 04 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package release
