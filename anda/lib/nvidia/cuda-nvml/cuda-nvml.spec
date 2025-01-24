%global real_name cuda_nvml_dev

%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-6

Name:           cuda-nvml
Epoch:          1
Version:        12.6.77
Release:        1%{?dist}
Summary:        NVIDIA Management library (NVML)
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-sbsa/%{real_name}-linux-sbsa-%{version}-archive.tar.xz
Source3:        nvidia-ml.pc

Requires(post): ldconfig
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
A C-based API for monitoring and managing various states of the NVIDIA GPU
devices. It provides a direct access to the queries and commands exposed via
nvidia-smi. The runtime version of NVML ships with the NVIDIA display driver.

Each new version of NVML is backwards compatible and is intended to be a
platform for building 3rd party applications.

%package devel
Summary:        Development files for the NVIDIA Management library (NVML)
# Unversioned as it is provided by the driver's NVML library
Requires:       %{name}%{_isa}
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
This package provides development files for the NVIDIA Management library
(NVML). Main libraries are provided by the driver package.

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{real_name}-linux-sbsa-%{version}-archive
%endif

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig/

cp -fr include/* %{buildroot}%{_includedir}/
cp -fr %{SOURCE3} %{buildroot}/%{_libdir}/pkgconfig/

# Libraries in the driver package
ln -sf libnvidia-ml.so.1 %{buildroot}%{_libdir}/libnvidia-ml.so

# Set proper variables
sed -i \
    -e 's|CUDA_VERSION|%{version}|g' \
    -e 's|LIBDIR|%{_libdir}|g' \
    -e 's|INCLUDE_DIR|%{_includedir}|g' \
    %{buildroot}/%{_libdir}/pkgconfig/*.pc

%{?ldconfig_scriptlets}

%files devel
%license LICENSE
%doc nvml/example
%{_includedir}/nvml.h
%{_libdir}/libnvidia-ml.so
%{_libdir}/pkgconfig/nvidia-ml.pc

%changelog
%autochangelog
