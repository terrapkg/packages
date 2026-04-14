# Build only the akmod package and no kernel module packages:
%define buildforkernels akmod
%global modulename nvidia-580xx

%global debug_package %{nil}

Name:           %{modulename}-kmod
Version:        580.142
Release:        3%{?dist}
Summary:        NVIDIA display driver kernel module
Epoch:          3
License:        NVIDIA License
URL:            http://www.nvidia.com/object/unix.html
Source0:        http://download.nvidia.com/XFree86/Linux-%{_arch}/%{version}/NVIDIA-Linux-%{_arch}-%{version}.run
Patch0:         0001-Enable-atomic-kernel-modesetting-by-default.patch
BuildRequires:  kmodtool
Requires:       nvidia-580xx-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       akmods
Provides:       akmod-nvidia-580 = %{evr}
Provides:       nvidia-580-kmod = %{?epoch:%{epoch}:}%{version}
Conflicts:      dkms-nvidia-580xx
Conflicts:      nvidia-kmod
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
kmodtool  --target %{_target_cpu}  --repo terrapkg.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

sh %{SOURCE0} -x --target %{real_name}-%{version}-%{_arch}
%setup -T -D -n %{real_name}-%{version}-%{_arch}

pushd kernel-open
%autopatch -p1
popd

rm -f */dkms.conf

for kernel_version in %{?kernel_versions}; do
    mkdir _kmod_build_${kernel_version%%___*}
    cp -fr Kbuild Makefile common conftest.sh *.mk nvidia* _kmod_build_${kernel_version%%___*}/
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
    install -p -m 0755 _kmod_build_${kernel_version%%___*}/*.ko \
        %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done
%{?akmod_install}

%changelog
* Mon Apr 13 2026 Gilver E. <roachy@fyralabs.com> - 3:580.142-3
- Update spec for Terra packaging team
