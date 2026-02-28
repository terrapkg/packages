%global real_name cuda_sandbox_dev

%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 13-0

Name:           cuda-sandbox
Epoch:          1
Version:        13.1.115
Release:        1%?dist
Summary:        CUDA nvsandboxutils
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-sbsa/%{real_name}-linux-sbsa-%{version}-archive.tar.xz

Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
A C-based API for monitoring and managing various states of the NVIDIA GPU
devices. It provides a direct access to the queries and commands exposed via
nvidia-smi. The runtime version of NVML ships with the NVIDIA display driver.

Each new version of NVML is backwards compatible and is intended to be a
platform for building 3rd party applications.

%package devel
Summary:        Development files for the CUDA nvsandboxutils library
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
This package provides development files for the CUDA nvsandboxutils library.

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{real_name}-linux-sbsa-%{version}-archive
%endif

%install
mkdir -p %{buildroot}%{_includedir}

cp -fr include/* %{buildroot}%{_includedir}/
install -p -m 0644 -D lib/stubs/libnvidia-sandboxutils_loader.a %{buildroot}%{_libdir}/libnvidia-sandboxutils_loader.a

%files devel
%license LICENSE
%{_includedir}/nvsandboxutils_loader.h
%{_includedir}/nvsandboxutils.h
%{_libdir}/libnvidia-sandboxutils_loader.a

%changelog
%autochangelog
