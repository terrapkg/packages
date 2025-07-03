# Build only the akmod package and no kernel module packages:
%define buildforkernels akmod

%global debug_package %{nil}

Name:           nvidia-open-kmod
Version:        575.64.03
Release:        1%?dist
Summary:        NVIDIA display driver kernel module
Epoch:          3
License:        NVIDIA License
URL:            http://www.nvidia.com/object/unix.html
ExclusiveArch:  x86_64 aarch64

Source0:        http://download.nvidia.com/XFree86/Linux-%{_arch}/%{version}/NVIDIA-Linux-%{_arch}-%{version}.run
Requires:       nvidia-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       akmods


# Get the needed BuildRequires (in parts depending on what we build for):
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

sh %{SOURCE0} -x --target nvidia-kmod-%{version}-%{_arch}
%setup -T -D -n nvidia-kmod-%{version}-%{_arch}
%autopatch -p1

rm -f */dkms.conf

for kernel_version in %{?kernel_versions}; do
    mkdir _kmod_build_${kernel_version%%___*}
    cp -fr kernel* _kmod_build_${kernel_version%%___*}
done

%build
export MODULE_VARIANT=kernel-open
for kernel_version in %{?kernel_versions}; do
    pushd _kmod_build_${kernel_version%%___*}/
        make %{?_smp_mflags} -C ${MODULE_VARIANT} \
            KERNEL_UNAME="${kernel_version%%___*}" modules
    popd
done

%install
export MODULE_VARIANT=kernel-open
for kernel_version in %{?kernel_versions}; do
    mkdir -p %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -p -m 0755 _kmod_build_${kernel_version%%___*}/${MODULE_VARIANT}/*.ko \
        %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done
%{?akmod_install}

%changelog
%autochangelog
