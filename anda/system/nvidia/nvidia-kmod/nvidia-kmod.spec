%global debug_package %{nil}

# Build only the akmod package and no kernel module packages:
%define buildforkernels akmod

# Build flags should be inherited from the kernel!
%undefine _auto_set_build_flags

Name:           nvidia-kmod
Version:        590.48.01
Release:        3%?dist
Summary:        NVIDIA display driver kernel module
Epoch:          3
License:        NVIDIA License
URL:            http://www.nvidia.com/object/unix.html
ExclusiveArch:  x86_64 aarch64

Source0:        https://github.com/NVIDIA/open-gpu-kernel-modules/archive/%{version}/open-gpu-kernel-modules-%{version}.tar.gz
Requires:       nvidia-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       akmods
Provides:       akmod-nvidia-open = %{?epoch:%{epoch}:}%{version}
Obsoletes:      akmod-nvidia-open < %{?epoch:%{epoch}:}%{version}


BuildRequires:  gcc-c++
BuildRequires:  kmodtool

# kmodtool does its magic here:
%{expand:%(kmodtool --target %{_target_cpu} --repo terra.fyralabs.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
The NVidia %{version} display driver kernel module for kernel %{kversion}.

%prep
# Error out if there was something wrong with kmodtool:
%{?kmodtool_check}
# Print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu}  --repo terra.fyralabs.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -p1 -c

rm -f open-gpu-kernel-modules-%{version}/dkms.conf

for kernel_version in %{?kernel_versions}; do
    cp -fr open-gpu-kernel-modules-%{version} _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
    pushd _kmod_build_${kernel_version%%___*}/
        make %{?_smp_mflags} KERNEL_UNAME="${kernel_version%%___*}" modules
    popd
done

%install
for kernel_version in %{?kernel_versions}; do
    mkdir -p %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -p -m 0755 _kmod_build_${kernel_version%%___*}/kernel-open/*.ko \
        %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done
%{?akmod_install}

%changelog
%autochangelog
