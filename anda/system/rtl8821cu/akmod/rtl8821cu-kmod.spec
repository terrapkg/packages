%global commit 3d1fcf4bc838542ceb03b0b4e9e40600720cf6ae
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20251010
%global ver 5.12.0.4
%global modulename rtl8821cu
%global git_name 8821cu-20210916
%define buildforkernels akmod
%global debug_package %{nil}
%global _description %{expand:
Linux Driver for USB Wi-Fi Adapters that are based on the RTL8811CU, RTL8821CU, RTL8821CUH, and RTL8731AU chipsets.}

Name:          %{modulename}-kmod
Version:       %{ver}^%{commit_date}git.%{shortcommit}
Release:       3%{?dist}
Summary:       Linux Driver for USB Wi-Fi Adapters using RTL8821 chipsets
License:       GPL-2.0-only
URL:           https://github.com/morrownr/8821cu-20210916
Source0:       %{url}/archive/%{commit}.tar.gz#/%{git_name}-%{shortcommit}.tar.gz
BuildRequires: kmodtool
BuildRequires: systemd-rpm-macros
Requires:      %{modulename}-kmod-common = %{version}
Requires:      akmods
Conflicts:     dkms-%{modulename}
Packager:      Gilver E. <roachy@fyralabs.com>

%{expand:%(kmodtool --target %{_target_cpu} --repo terra.fyralabs.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description %_description

%prep
%{?kmodtool_check}
kmodtool  --target %{_target_cpu}  --repo terra.fyralabs.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -n %{git_name}-%{commit}

%ifarch armv7hl
sed -i 's/CONFIG_PLATFORM_I386_PC = y/CONFIG_PLATFORM_I386_PC = n/g' Makefile
sed -i 's/CONFIG_PLATFORM_ARM_RPI = n/CONFIG_PLATFORM_ARM_RPI = y/g' Makefile
%elifarch aarch64
sed -i 's/CONFIG_PLATFORM_I386_PC = y/CONFIG_PLATFORM_I386_PC = n/g' Makefile
sed -i 's/CONFIG_PLATFORM_ARM_RPI = y/CONFIG_PLATFORM_ARM_RPI = n/g' Makefile
sed -i 's/CONFIG_PLATFORM_ARM64_RPI = n/CONFIG_PLATFORM_ARM64_RPI = y/g' Makefile
%endif

for kernel_version in %{?kernel_versions}; do
    mkdir _kmod_build_${kernel_version%%___*}
    cp -fr core hal include os_dep platform Kconfig Makefile halmac.mk _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
    pushd _kmod_build_${kernel_version%%___*}/
        %make_build -C "${kernel_version##*___}" M=$(pwd) VERSION="v%{version}" modules
    popd
done

%install
for kernel_version in %{?kernel_versions}; do
    mkdir -p %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -p -m 0755 _kmod_build_${kernel_version%%___*}/*.ko \
        %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done
%{?akmod_install}

%changelog
* Wed May 28 2025 Gilver E. <rockgrub@disroot.org> - 5.12.0.4^20250508git.d74134a-1
- Initial package
