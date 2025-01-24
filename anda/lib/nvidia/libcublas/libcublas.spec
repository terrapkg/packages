%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-6

Name:           libcublas
Epoch:          1
Version:        12.6.4.1
Release:        1%{?dist}
Summary:        NVIDIA CUDA Basic Linear Algebra Subroutines (cuBLAS) libraries
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-x86_64/%{name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-sbsa/%{name}-linux-sbsa-%{version}-archive.tar.xz
Source3:        cublas.pc
Source4:        cublasLt.pc

Requires(post): ldconfig
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
The NVIDIA CUDA Basic Linear Algebra Subroutines (cuBLAS) library is a
GPU-accelerated version of the complete standard BLAS library that delivers 6x
to 17x faster performance than the latest MKL BLAS.

%package devel
Summary:        Development files for NVIDIA CUDA Basic Linear Algebra Subroutines (cuBLAS)
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
This package provides development files for the NVIDIA CUDA Basic Linear
Algebra Subroutines (cuBLAS) libraries.

%package static
Summary:        Static libraries for NVIDIA CUDA Basic Linear Algebra Subroutines (cuBLAS)
Requires:       %{name}-devel%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description static
This package contains static libraries for the NVIDIA CUDA Basic Linear Algebra
Subroutines (cuBLAS).

%prep
%ifarch x86_64
%setup -q -n %{name}-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{name}-linux-sbsa-%{version}-archive
%endif

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig/

cp -fr include/* %{buildroot}%{_includedir}/
cp -fr lib/lib* %{buildroot}%{_libdir}/
cp -fr %{SOURCE3} %{SOURCE4} %{buildroot}/%{_libdir}/pkgconfig/

# Set proper variables
sed -i \
    -e 's|CUDA_VERSION|%{version}|g' \
    -e 's|LIBDIR|%{_libdir}|g' \
    -e 's|INCLUDE_DIR|%{_includedir}|g' \
    %{buildroot}/%{_libdir}/pkgconfig/*.pc

%{?ldconfig_scriptlets}

%files
%license LICENSE
%{_libdir}/libcublas.so.*
%{_libdir}/libcublasLt.so.*
%{_libdir}/libnvblas.so.*

%files devel
%ifarch x86_64
%doc src
%endif
%{_includedir}/nvblas.h
%{_includedir}/cublasLt.h
%{_includedir}/cublas_v2.h
%{_includedir}/cublas.h
%{_includedir}/cublas_api.h
%{_includedir}/cublasXt.h
%{_libdir}/libcublas.so
%{_libdir}/libcublasLt.so
%{_libdir}/libnvblas.so
%{_libdir}/pkgconfig/cublas.pc
%{_libdir}/pkgconfig/cublasLt.pc

%files static
%{_libdir}/libcublas_static.a
%{_libdir}/libcublasLt_static.a

%changelog
%autochangelog
