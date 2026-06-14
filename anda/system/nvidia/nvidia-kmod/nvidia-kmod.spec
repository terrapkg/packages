%global debug_package %{nil}

# Build only the akmod package and no kernel module packages:
%define buildforkernels akmod

# Build flags should be inherited from the kernel!
%undefine _auto_set_build_flags

Name:           nvidia-kmod
Version:        610.43.02
Release:        1%{?dist}
Summary:        NVIDIA display driver kernel module
Epoch:          3
License:        NVIDIA License
URL:            http://www.nvidia.com/object/unix.html
Source0:        https://download.nvidia.com/XFree86/NVIDIA-kernel-module-source/NVIDIA-kernel-module-source-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  kmodtool
Requires:       nvidia-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       akmods
Provides:       akmod-nvidia-open = %{?epoch:%{epoch}:}%{version}
Obsoletes:      akmod-nvidia-open < %{?epoch:%{epoch}:}%{version}
Conflicts:      dkms-nvidia
Conflicts:      nvidia-kmod-580xx
ExclusiveArch:  x86_64 aarch64
Packager:       Terra Packaging Team <terra@fyralabs.com>

# kmodtool does its magic here:
%{expand:%(kmodtool --target %{_target_cpu} --repo terrapkg.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
The NVidia %{version} display driver kernel module for kernel %{kversion}.

%prep
# Error out if there was something wrong with kmodtool:
%{?kmodtool_check}
# Print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu}  --repo terrapkg.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -c

pushd NVIDIA-kernel-module-source-%{version}
%autopatch -p1
popd

rm -f NVIDIA-kernel-module-source-%{version}/dkms.conf

for kernel_version in %{?kernel_versions}; do
    cp -fr NVIDIA-kernel-module-source-%{version} _kmod_build_${kernel_version%%___*}
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
* Mon Apr 13 2026 Gilver E. <roachy@fyralabs.com> - 3:595.58.03-3
- Update patches for DSC functionality
- Update spec for Terra packaging team
