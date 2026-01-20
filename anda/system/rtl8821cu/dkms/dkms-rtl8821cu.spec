%global commit 3d1fcf4bc838542ceb03b0b4e9e40600720cf6ae
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20251010
%global ver 5.12.0.4
%global modulename rtl8821cu
%global git_name 8821cu-20210916
%global debug_package %{nil}
%global _description %{expand:
Linux Driver for USB Wi-Fi Adapters that are based on the RTL8811CU, RTL8821CU, RTL8821CUH, and RTL8731AU chipsets.}

Name:          dkms-%{modulename}
Version:       %{ver}^%{commit_date}git.%{shortcommit}
Release:       2%{?dist}
Summary:       Linux Driver for USB Wi-Fi Adapters using RTL8821 chipsets
License:       GPL-2.0-only
URL:           https://github.com/morrownr/8821cu-20210916
Source0:       %{url}/archive/%{commit}.tar.gz#/%{git_name}-%{shortcommit}.tar.gz
Source1:       no-weak-modules.conf
BuildRequires: sed
BuildRequires: systemd-rpm-macros
Requires:      %{modulename}-kmod-common = %{version}
Requires:      dkms
# Required for DKMS to build the kmod
Requires:      gcc
Requires:      bc
Requires:      make
Provides:      %{modulename}-kmod
Conflicts:     akmod-%{modulename}
Packager:      Gilver E. <roachy@fyralabs.com>

%description %_description

%prep
%autosetup -n %{git_name}-%{commit}

sed -i 's/PACKAGE_VERSION=".*"/PACKAGE_VERSION="%{version}"/g' dkms.conf

# Technically this package is noarch. However it cannot be built that way due to arch dependencies for the built kmod.
%ifarch armv7hl
sed -i 's/CONFIG_PLATFORM_I386_PC = y/CONFIG_PLATFORM_I386_PC = n/g' Makefile
sed -i 's/CONFIG_PLATFORM_ARM_RPI = n/CONFIG_PLATFORM_ARM_RPI = y/g' Makefile
%elifarch aarch64
sed -i 's/CONFIG_PLATFORM_I386_PC = y/CONFIG_PLATFORM_I386_PC = n/g' Makefile
sed -i 's/CONFIG_PLATFORM_ARM_RPI = y/CONFIG_PLATFORM_ARM_RPI = n/g' Makefile
sed -i 's/CONFIG_PLATFORM_ARM64_RPI = n/CONFIG_PLATFORM_ARM64_RPI = y/g' Makefile
%endif

%build
# Hi, I'm empty.

%install
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
cp -fr core hal include os_dep platform Kconfig Makefile halmac.mk dkms-make.sh dkms.conf %{buildroot}%{_usrsrc}/%{modulename}-%{version}/

%if 0%{?fedora}
# Do not enable weak modules support in Fedora (no kABI):
install -Dpm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/dkms/%{modulename}.conf
%endif

%post
dkms add -m %{modulename} -v %{version} -q --rpm_safe_upgrade || :
# Rebuild and make available for the currently running kernel:
dkms build -m %{modulename} -v %{version} -q || :
dkms install -m %{modulename} -v %{version} -q --force || :

%preun
# Remove all versions from DKMS registry:
dkms remove -m %{modulename} -v %{version} -q --all --rpm_safe_upgrade || :

%files
%{_usrsrc}/%{modulename}-%{version}/
%if 0%{?fedora}
%{_sysconfdir}/dkms/%{modulename}.conf
%endif

%changelog
* Wed May 28 2025 Gilver E. <rockgrub@disroot.org> - 5.12.0.4^20250508git.d74134a-1
- Initial package
