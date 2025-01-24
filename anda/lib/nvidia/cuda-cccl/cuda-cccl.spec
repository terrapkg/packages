%global real_name cuda_cccl

%global debug_package %{nil}
%global major_package_version 12-6

Name:           %(echo %real_name | tr '_' '-')
Epoch:          1
Version:        12.6.77
Release:        1%{?dist}
Summary:        CXX Core Compute Libraries
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-sbsa/%{real_name}-linux-sbsa-%{version}-archive.tar.xz

Requires:       cmake-filesystem
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description
CXX Core Compute Libraries.

%package devel
Summary:        CXX Core Compute Libraries development files

%description devel
CXX Core Compute Libraries development files.

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{real_name}-linux-sbsa-%{version}-archive
%endif

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}/cmake

cp -fr include/* %{buildroot}%{_includedir}/
# Conflict with rocthrust-devel in main repositories:
mv %{buildroot}%{_includedir}/thrust %{buildroot}%{_includedir}/cuda/

cp -fr lib/cmake/* %{buildroot}%{_libdir}/cmake
rm -f %{buildroot}%{_libdir}/cmake/thrust/README.md

%files devel
%license LICENSE
%doc lib/cmake/thrust/README.md
%{_includedir}/*
%{_libdir}/cmake/*

%changelog
%autochangelog

