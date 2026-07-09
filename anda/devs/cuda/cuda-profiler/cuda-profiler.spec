%global real_name cuda_profiler_api

%global debug_package %{nil}
%global major_package_version 13-1

Name:           cuda-profiler
Epoch:          1
Version:        13.3.27
Release:        2%{?dist}
Summary:        CUDA Profiler API
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
BuildArch:      noarch

# Different tarballs per architecture but they all contain the same headers:
Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz

Packager:       Terra Packaging Team <terra@fyralabs.com>

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
* Wed Jul 8 2026 Gilver E. <roachy@fyralabs.com> - 1:13.3.27-2
- Mass update CUDA components
