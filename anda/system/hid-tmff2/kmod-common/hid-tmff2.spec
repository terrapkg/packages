%global commit 8187920ed261c7024826f8204cc7bea45153a3da
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260310
%global ver 0.83

%global tminit_commit 8c4547288a6c182ed4ff131e36f710f11a76c4a9
%global tminit_shortcommit %(c=%{tminit_commit}; echo ${c:0:7})

Name:           hid-tmff2
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        2%{?dist}
Summary:        Thrustmaster Force Feedback driver common files
License:        GPL-2.0-only
URL:            https://github.com/Kimplul/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Source1:        https://github.com/Kimplul/hid-tminit/archive/%{tminit_commit}.tar.gz#/hid-tminit-%{tminit_shortcommit}.tar.gz
Requires:       %{name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
BuildArch:      noarch

%description
Linux kernel module for Thrustmaster T300RS, T248 and (experimental) TX, T128,
T598, T-GT II and TS-XW wheels. This package contains common files shared
between the akmod and dkms variants.

%package       akmod-modules
Summary:       Modules for Akmods
Requires:      akmod-%{name}
BuildArch:     noarch

%description   akmod-modules
Akmods modules for the akmod-%{name} package.

%prep
%autosetup -p1 -n %{name}-%{commit}

# Extract module names from Kbuild for modules-load.d
echo hid-tmff-new > %{name}.conf
echo hid-tminit >> %{name}.conf

%install
# UDev rules:
install -Dpm644 udev/99-thrustmaster.rules -t %{buildroot}%{_udevrulesdir}/

# Akmods modules
install -Dm644 %{name}.conf -t %{buildroot}%{_modulesloaddir}

%files
%license LICENSE
%doc README.md
%{_udevrulesdir}/99-thrustmaster.rules

%files akmod-modules
%{_modulesloaddir}/%{name}.conf

%changelog
* Thu Apr 02 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package
