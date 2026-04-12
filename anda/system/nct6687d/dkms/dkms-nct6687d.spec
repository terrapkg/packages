%global commit cedda8bff09a4083e07414fb80fdc3901e7ab544
%global debug_package %{nil}
%global modulename nct6687d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260411

Name:           dkms-%{modulename}
Version:        1.0^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Linux kernel driver for the NCT6687D hardware monitoring chip
License:        GPL-2.0-or-later
URL:            https://github.com/Fred78290/%{modulename}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Patch0:         dkms-version.patch
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Conflicts:      akmod-%{modulename}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
BuildArch:      x86_64
Provides:       %{modulename}-kmod

%description
Linux kernel driver for the NCT6687D hardware monitoring chip.
This kernel module permit to recognize the chipset Nuvoton NCT6687-R in lm-sensors package. This sensor is present on some B550 motherboard such as MSI or ASUS.
The implementation is minimalist and was done by reverse coding of Windows 10 source code from LibreHardwareMonitor

%package       akmod-modules
Summary:       Modules for Akmods
Requires:      akmod-%{name}
BuildArch:     noarch

%description   akmod-modules
Akmods modules for the akmod-%{name} package.

%prep
%autosetup -p1 -n %{modulename}-%{commit}
sed -i -e 's/__VERSION_STRING/%{version}/g' dkms.conf

%install
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}
cp -fr ./ %{buildroot}%{_usrsrc}/%{modulename}-%{version}/

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
* Sat Apr 11 2026 Luan Oliveira <luanv.oliveira@outlook.com> - 1.0^20260411git.cedda8b-1
- Initial package
