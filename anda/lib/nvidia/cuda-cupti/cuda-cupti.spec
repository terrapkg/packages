%global real_name cuda_cupti

%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-6

Name:           %(echo %real_name | tr '_' '-')
Epoch:          1
Version:        12.6.80
Release:        1%{?dist}
Summary:        NVIDIA CUDA Profiling Tools Interface (CUPTI) library
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-sbsa/%{real_name}-linux-sbsa-%{version}-archive.tar.xz

Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
The NVIDIA CUDA Profiling Tools Interface (CUPTI) provides performance analysis
tools with detailed information about how applications are using the GPUs in a
system.

%package devel
Summary:        Development files for NVIDIA CUDA Profiling Tools Interface (CUPTI) library
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package provides development files for the NVIDIA CUDA Profiling Tools
Interface (CUPTI) library.

%package static
Summary:        Static libraries for NVIDIA CUDA Profiling Tools Interface (CUPTI)
Requires:       %{name}-devel%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description static
This package contains static libraries for NVIDIA CUDA Profiling Tools Interface
(CUPTI).

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{real_name}-linux-sbsa-%{version}-archive
%endif

%{?ldconfig_scriptlets}

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
cp -fr include/* %{buildroot}%{_includedir}/
cp -fr lib/* %{buildroot}%{_libdir}/

%files
%license LICENSE
%{_libdir}/libcheckpoint.so
%{_libdir}/libcupti.so.*
%{_libdir}/libpcsamplingutil.so

%files devel
%doc doc/* samples/*
%{_includedir}/*
%{_libdir}/libcupti.so
%{_libdir}/libnvperf_host.so
%{_libdir}/libnvperf_target.so

%files static
%{_libdir}/libcupti_static.a
%ifarch x86_64
%{_libdir}/libnvperf_host_static.a
%endif

%changelog
%autochangelog

