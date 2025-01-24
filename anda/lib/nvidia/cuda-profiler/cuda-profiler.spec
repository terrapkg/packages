%global real_name cuda_profiler_api

%global debug_package %{nil}
%global major_package_version 12-6

Name:           cuda-profiler
Epoch:          1
Version:        12.6.77
Release:        1%?dist
Summary:        CUDA Profiler API
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 ppc64le aarch64 %{ix86}

# Different tarballs per architecture but they all contain the same headers:
Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz

%description
NVIDIA CUDA API for profiling.

%package devel
Summary:        Development files for CUDA Profiler API
Conflicts:      %{real_name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
This package provides development files for the CUDA Profiler API.

%prep
%autosetup -n %{real_name}-linux-x86_64-%{version}-archive

%install
mkdir -p %{buildroot}%{_includedir}
cp -f include/* %{buildroot}%{_includedir}/

%files devel
%license LICENSE
%{_includedir}/*

%changelog
%autochangelog
