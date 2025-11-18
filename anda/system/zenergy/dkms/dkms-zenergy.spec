%global commit 58f2fda7184fbde95033f492f7c54990552ef86f
%global debug_package %{nil}
%global modulename zenergy
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250831

Name:           dkms-%{modulename}
Version:        1.0^%{commitdate}git.%{shortcommit}
Release:        1%?dist
Summary:        Exposes the energy counters that are reported via the Running Average Power Limit (RAPL) Model-specific Registers (MSRs) via the hardware monitor (HWMON) sysfs interface.
License:        GPL-2.0
URL:            https://github.com/BoukeHaarsma23/zenergy
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
BuildArch:      x86_64
Requires:       dkms
Requires:       help2man
Conflicts:      akmod-%{modulename}
Packager:       Cappy Ishihara <cappy@fyralabs.com>

%description
Based on AMD_ENERGY driver, but with some jiffies added so non-root users can read it safely.
Exposes the energy counters that are reported via the Running Average Power Limit (RAPL) Model-specific Registers (MSRs)
via the hardware monitor (HWMON) sysfs interface.


%package       akmod-modules
Summary:       Modules for Akmods
Requires:      akmod-%{name}
BuildArch:     noarch

%description   akmod-modules
Akmods modules for the akmod-%{name} package.
 
%prep
%autosetup -p1 -n %{modulename}-%{commit}
# Zenergy has no concrete version, but upstream says "1.0" in their documentation
/usr/bin/sed -i 's/@VERSION@/%{version}/g' dkms.conf

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
%autochangelog
