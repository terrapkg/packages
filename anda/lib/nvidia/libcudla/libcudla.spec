%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-6

Name:           libcudla
Epoch:          1
Version:        12.6.77
Release:        1%{?dist}
Summary:        NVIDIA CUDA Deep Learning Accelerator (DLA) engines (Jetson Xavier and Orin)
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-aarch64/%{name}-linux-aarch64-%{version}-archive.tar.xz
Source1:        cudla.pc

%description
Low-level driver for the Deep Learning Accelerator (DLA) engine for Jetson Xavier and Orin boards.

%package devel
Summary:        Development files for CUDA Deep Learning Accelerator (DLA) engines
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
This package provides development files for the CUDA Deep Learning Accelerator (DLA) engines.

%prep
%autosetup -n %{name}-linux-aarch64-%{version}-archive

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig/

cp -fr include/* %{buildroot}%{_includedir}/
cp -fr lib/lib* %{buildroot}%{_libdir}/
cp -fr %{SOURCE1} %{buildroot}/%{_libdir}/pkgconfig/

# Set proper variables
sed -i \
    -e 's|CUDA_VERSION|%{version}|g' \
    -e 's|LIBDIR|%{_libdir}|g' \
    -e 's|INCLUDE_DIR|%{_includedir}|g' \
    %{buildroot}/%{_libdir}/pkgconfig/*.pc

%files
%license LICENSE
%{_libdir}/libcudla.so.*

%files devel
%{_includedir}/cudla.h
%{_includedir}/cudlaExternalEtbl.hpp
%{_libdir}/libcudla.so
%{_libdir}/pkgconfig/cudla.pc

%changelog
%autochangelog
