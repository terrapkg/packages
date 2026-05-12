%global commit cedda8bff09a4083e07414fb80fdc3901e7ab544
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260411

Name:           nct6687d
Version:        1.0^%{commitdate}git.%{shortcommit}
Release:        2%{?dist}
Summary:        Linux kernel driver for the NCT6687D hardware monitoring chip
License:        GPL-2.0-or-later
URL:            https://github.com/Fred78290/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Source1:        com.github.nct6687d.metainfo.xml
BuildRequires:  systemd-rpm-macros
BuildRequires:  anda-srpm-macros
Requires:       %{name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
Obsoletes:      %{name}-akmods-modules < %{evr}
BuildArch:      noarch

%description
Linux kernel driver for the NCT6687D hardware monitoring chip.
This kernel module permit to recognize the chipset Nuvoton NCT6687-R in lm-sensors package. This sensor is present on some B550 motherboard such as MSI or ASUS.
The implementation is minimalist and was done by reverse coding of Windows 10 source code from LibreHardwareMonitor

%prep
%autosetup -p1 -n %{name}-%{commit}

echo nct6687 > %{name}.conf
echo "blacklist nct6683" > nct6683_blacklist.conf

%install
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/com.github.nct6687d.metainfo.xml

# Akmods modules
install -Dm 0644 %{name}.conf -t %{buildroot}%{_modulesloaddir}
install -Dm 0644 nct6683_blacklist.conf -t %{buildroot}%{_modprobedir}

%files
%license LICENSE
%doc README.md images/* TESTING_RESULTS.md
%{_modprobedir}/nct6683_blacklist.conf
%{_datadir}/metainfo/com.github.nct6687d.metainfo.xml
%{_modulesloaddir}/%{name}.conf

%changelog
* Wed May 06 2026 Luan Oliveira <luanv.oliveira@outlook.com> - 1.0^20260411git.cedda8b-2
- fix module load file
* Sat Apr 11 2026 Luan Oliveira <luanv.oliveira@outlook.com> - 1.0^20260411git.cedda8b-1
- Initial package
