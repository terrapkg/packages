%global buildforkernels akmod
%global debug_package %{nil}
%global prjname zenpower3

# There will probably not be an update script for this package, since this kernel module
# is kind of dead, I will update them manually when needed.
%global commit 138fa0637b46a0b0a087f2ba4e9146d2f9ba2475
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: %{prjname}
Version: 0.2.0^2.git%{shortcommit}
Release: 1%{?dist}
Summary: AMD Ryzen SMU driver for lm_sensors, up to Zen 3
Packager: Cappy Ishihara <cappy@fyralabs.com>

License: GPLv2
URL: https://gitlab.com/shdwchn10/%{prjname}
Source0: https://gitlab.com/shdwchn10/%{prjname}/-/archive/%{commit}/%{prjname}-%{commit}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: kmodtool

# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --repo %{repo} --kmodname %{prjname} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null | sed '/global with_rhel_kabi/d') }

%description
Zenpower3 is a Linux kernel driver for reading temperature, voltage(SVI2), current(SVI2) and power(SVI2) for AMD Zen family CPUs, now with Zen 3 support!

This package contains the kmod module for %{prjname}.


%prep
%setup -q -n %{prjname}-%{commit}

# Error out if there was something wrong with kmodtool.
%{?kmodtool_check}

# Print kmodtool output for debugging purposes:
kmodtool --target %{_target_cpu} --repo %{repo} --kmodname %{prjname} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null | sed '/global with_rhel_kabi/d'

mkdir src
cp -a Makefile zenpower.c src/

for kernel_version in %{?kernel_versions} ; do
    cp -a src _kmod_build_${kernel_version%%___*}
done

echo %{version} > VERSION


%build
for kernel_version in %{?kernel_versions} ; do
    make V=1 %{?_smp_mflags} -C ${kernel_version##*___} M=${PWD}/_kmod_build_${kernel_version%%___*} modules
done


%install
for kernel_version in %{?kernel_versions}; do
    mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -Dpm 0755 _kmod_build_${kernel_version%%___*}/*.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/*.ko
done
%{?akmod_install}


%changelog
* Sun Dec 29 2024 Cappy Ishihara <cappy@cappuchino.xyz> - 0.2.0^2.gitc176fdb-1
- Repackaged for Terra

* Mon Dec 23 2024 Andrey Brusnik <dev@shdwchn.io> - 0.2.0^2.gitc176fdb-4
- fix: Actually fix building with custom kernels on EL

* Thu Dec 19 2024 Andrey Brusnik <dev@shdwchn.io> - 0.2.0^2.gitc176fdb-3
- fix: Update broken link to mirror
- fix: Rollback to akmod on EL so module will work with custom kernels

* Sat Sep 28 2024 Andrey Brusnik <dev@shdwchn.io> - 0.2.0^1.gitc176fdb0d5-2
- fix: Build kmod instead of akmod for EL

* Tue Nov 07 2023 Andrey Brusnik <dev@shdwchn.io> - 0.2.0^1.gitc176fdb0d5-1
- Initial package
