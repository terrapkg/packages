%global buildforkernels akmod
%global debug_package %{nil}
%global modulename openrazer

Name:           %{modulename}-kmod
Version:        3.12.4
Release:        1%{?dist}
Summary:        Kernel modules (kmod) for Razer devices
License:        GPL-2.0-or-later
URL:            https://openrazer.github.io
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>
Source0:        https://github.com/openrazer/openrazer/releases/download/v%{version}/%{modulename}-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  kmodtool
BuildRequires:  elfutils-libelf-devel
Requires:       akmods
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       kernel-devel
Conflicts:      dkms-%{modulename}
Conflicts:      openrazer-kernel-modules-dkms

%{expand:%(kmodtool --target %{_target_cpu} --repo terrapkg.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Kernel drivers for Razer devices, providing the razerkbd, razermouse,
razerkraken and razeraccessory modules used by the OpenRazer daemon.

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool --target %{_target_cpu} --repo terrapkg.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -p1 -n %{modulename}-%{version}

for kernel_version in %{?kernel_versions}; do
    cp -a driver _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
    %make_build -C "${kernel_version##*___}" M=${PWD}/_kmod_build_${kernel_version%%___*} modules
done

%install
for kernel_version in %{?kernel_versions}; do
    mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -D -m 755 _kmod_build_${kernel_version%%___*}/*.ko \
        %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/*.ko
done
%{?akmod_install}

%changelog
* Mon Aug 31 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 3.12.4-1
- Initial package
