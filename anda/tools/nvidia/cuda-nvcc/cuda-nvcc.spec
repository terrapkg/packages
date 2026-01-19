%global real_name cuda_nvcc

%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 13-0

Name:           %(echo %real_name | tr '_' '-')
Epoch:          1
Version:        13.1.115
Release:        1%?dist
Summary:        CUDA Compiler (NVCC)
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-sbsa/%{real_name}-linux-sbsa-%{version}-archive.tar.xz
Source3:        nvcc.profile

Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

# CUDA 13.0 does not support GCC 16+:
%if 0%{?fedora} >= 44
Requires:       cuda-gcc
%else
# But it supports GCC 14, so obsolete the wrapper in case of an upgrade:
Obsoletes:      cuda-gcc
Provides:       cuda-gcc
%endif

Requires:       cuda-crt
Requires:       cuda-cudart-devel
Requires:       libnvptxcompiler-devel
Requires:       libnvvm-devel

%description
The compilation trajectory involves several splitting, compilation,
preprocessing, and merging steps for each CUDA source file. It is the purpose of
nvcc, the CUDA compiler driver, to hide the intricate details of CUDA
compilation from developers. It accepts a range of conventional compiler
options, such as for defining macros and include/library paths, and for steering
the compilation process. All non-CUDA compilation steps are forwarded to a C++
host compiler that is supported by nvcc, and nvcc translates its options to
appropriate host compiler command line options.

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{real_name}-linux-sbsa-%{version}-archive
%endif

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_includedir}

cp -fr bin/* %{buildroot}%{_bindir}/
cp -fr include/* %{buildroot}%{_includedir}/

cp -f %{SOURCE3} %{buildroot}%{_bindir}/

# Set proper variables
sed -i \
    -e 's|PREFIX|%{_prefix}|g' \
    -e 's|BINDIR|%{_bindir}|g' \
    -e 's|LIBDIR|%{_libdir}|g' \
    -e 's|INCLUDE_DIR|%{_includedir}|g' \
    %{buildroot}/%{_bindir}/nvcc.profile

%files
%license LICENSE
%{_bindir}/__nvcc_device_query
%{_bindir}/bin2c
%dir %{_bindir}/crt/
%{_bindir}/crt/link.stub
%{_bindir}/crt/prelink.stub
%{_bindir}/cudafe++
%{_bindir}/fatbinary
%{_bindir}/nvcc
%{_bindir}/nvcc.profile
%{_bindir}/nvlink
%{_bindir}/ptxas
%{_includedir}/fatbinary_section.h

%changelog
%autochangelog
