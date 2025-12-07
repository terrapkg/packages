%global commit 58f2fda7184fbde95033f492f7c54990552ef86f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250831

Name:           zenergy
Version:        1.0^%{commitdate}git.%{shortcommit}
Release:        1%?dist
Summary:        Exposes the energy counters that are reported via the Running Average Power Limit (RAPL) Model-specific Registers (MSRs) via the hardware monitor (HWMON) sysfs interface.
License:        GPL-2.0
URL:            https://github.com/BoukeHaarsma23/zenergy
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Source1:        com.github.zenergy.metainfo.xml
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires:       (akmod-%{name} = %{?epoch:%{epoch}:}%{version} or dkms-%{name} = %{?epoch:%{epoch}:}%{version})
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
BuildArch:      noarch
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
%autosetup -p1 -n %{name}-%{commit}

# Zenergy has no concrete version, but upstream says "1.0" in their documentation
/usr/bin/sed -nE 's/@VERSION@/%{version}/g' dkms.conf > %{name}.conf

%install
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/com.github.zenergy.metainfo.xml

# Akmods modules
install -Dm644 %{name}.conf -t %{buildroot}%{_modulesloaddir}


%files
%license LICENSE
%doc README.md
%{_datadir}/metainfo/com.github.zenergy.metainfo.xml

%files akmod-modules
%{_modulesloaddir}/%{name}.conf

%changelog
%autochangelog