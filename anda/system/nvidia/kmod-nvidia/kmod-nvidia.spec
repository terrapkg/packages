%global kmod_name nvidia

%global debug_package %{nil}

# Generate kernel symbols requirements:
%global _use_internal_dependency_generator 0

%{!?kversion: %global kversion %(uname -r)}

Name:           kmod-%{kmod_name}
Version:        575.51.02
Release:        1%{?dist}
Summary:        NVIDIA display driver kernel module
Epoch:          3
License:        NVIDIA License
URL:            http://www.nvidia.com/
ExclusiveArch:  x86_64 aarch64

Source0:        https://github.com/NVIDIA/open-gpu-kernel-modules/archive/refs/tags/%{version}.tar.gz
# Kbuild: Convert EXTRA_CFLAGS to ccflags-y (6.15+) + std=gnu17
Patch0:         nvidia-kernel-ccflags-y.patch
# https://git.almalinux.org/ngompa/nvidia-kmod-el-rpm/
Patch1:         %{name}-ldflags.patch
Patch2:         %{name}-no-hostname-whoami.patch

BuildRequires:  elfutils-libelf-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kernel-abi-stablelists
BuildRequires:  kernel-devel
BuildRequires:  kernel-rpm-macros
BuildRequires:  kmod
BuildRequires:  redhat-rpm-config

Provides:   kabi-modules = %{kversion}
Provides:   %{kmod_name}-kmod = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:   module-init-tools

%description
This package provides the proprietary NVIDIA kernel modules. It is built to
depend upon the specific ABI provided by a range of releases of the same variant
of the Linux kernel and not on any one specific build.

%prep
%autosetup -p1 -n open-gpu-kernel-modules-%{version}

echo "override %{kmod_name} * weak-updates/%{kmod_name}" > kmod-%{kmod_name}.conf

%build
export SYSSRC=%{_usrsrc}/kernels/%{kversion}
export IGNORE_XEN_PRESENCE=1
export IGNORE_PREEMPT_RT_PRESENCE=1
export IGNORE_CC_MISMATCH=1

%make_build modules

%install
export INSTALL_MOD_PATH=%{buildroot}%{_prefix}
export INSTALL_MOD_DIR=extra/%{kmod_name}

make -C %{_usrsrc}/kernels/%{kversion} -j$(nproc) modules_install M=$PWD/kernel-open

install -d %{buildroot}%{_sysconfdir}/depmod.d/
install kmod-%{kmod_name}.conf %{buildroot}%{_sysconfdir}/depmod.d/
# Remove the unrequired files.
rm -f %{buildroot}%{_prefix}/lib/modules/%{kversion}/modules.*

find %{buildroot} -type f -name '*.ko' | xargs %{__strip} --strip-debug
find %{buildroot} -type f -name '*.ko' | xargs xz

%post
if [ -e "/boot/System.map-%{kversion}" ]; then
    %{_sbindir}/depmod -aeF "/boot/System.map-%{kversion}" "%{kversion}" > /dev/null || :
fi
modules=( $(find %{_prefix}/lib/modules/%{kversion}/extra/%{kmod_name} | grep '\.ko.xz$') )
if [ -x "%{_sbindir}/weak-modules" ]; then
    printf '%s\n' "${modules[@]}" | %{_sbindir}/weak-modules --add-modules
fi

%preun
rpm -ql kmod-%{kmod_name}-%{version}-%{release}.%{_target_cpu} | grep '\.ko.xz$' > %{_var}/run/rpm-kmod-%{kmod_name}-modules

%postun
if [ -e "/boot/System.map-%{kversion}" ]; then
    %{_sbindir}/depmod -aeF "/boot/System.map-%{kversion}" "%{kversion}" > /dev/null || :
fi
modules=( $(cat /var/run/rpm-kmod-%{kmod_name}-modules) )
rm %{_var}/run/rpm-kmod-%{kmod_name}-modules
if [ -x "%{_sbindir}/weak-modules" ]; then
    printf '%s\n' "${modules[@]}" | %{_sbindir}/weak-modules --remove-modules
fi

%files
%{_prefix}/lib/modules/%{kversion}/extra/*
%config %{_sysconfdir}/depmod.d/kmod-%{kmod_name}.conf

%changelog
%autochangelog
