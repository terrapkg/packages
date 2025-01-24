%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-6

Name:           libcufft
Epoch:          2
Version:        11.3.0.4
Release:        1%{?dist}
Summary:        NVIDIA CUDA Fast Fourier Transform library (cuFFT) libraries
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-x86_64/%{name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-sbsa/%{name}-linux-sbsa-%{version}-archive.tar.xz
Source3:        cufft.pc
Source4:        cufftw.pc

Requires(post): ldconfig
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}
# Drop in 11.7:
Provides:       cuda-cufft = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      cuda-cufft < %{?epoch:%{epoch}:}%{version}-%{release}

%description
The NVIDIA CUDA Fast Fourier Transform libraries (cuFFT) provide a simple
interface for computing FFTs up to 10x faster.  By using hundreds of processor
cores inside NVIDIA GPUs, cuFFT delivers the floating‐point performance of a
GPU without having to develop your own custom GPU FFT implementation.

%package devel
Summary:        Development files for CUDA Fast Fourier Transform library (cuFFT)
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}
# Drop in 11.7:
Provides:       cuda-cufft-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      cuda-cufft-devel < %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package provides development files for the NVIDIA CUDA Fast Fourier
Transform library (cuFFT) libraries.

%package static
Summary:        Static libraries for CUDA Fast Fourier Transform library (cuFFT)
Requires:       %{name}-devel%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# Drop in 11.7:
Provides:       cuda-cufft-static = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      cuda-cufft-static < %{?epoch:%{epoch}:}%{version}-%{release}

%description static
This package contains static libraries for CUDA Fast Fourier Transform library
(cuFFT).

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
%{_libdir}/libcufft.so.*
%{_libdir}/libcufftw.so.*

%files devel
%{_includedir}/cudalibxt.h
%{_includedir}/cufft.h
%{_includedir}/cufftw.h
%{_includedir}/cufftXt.h
%{_libdir}/libcufft.so
%{_libdir}/libcufftw.so
%{_libdir}/pkgconfig/cufft.pc
%{_libdir}/pkgconfig/cufftw.pc

%files static
%{_libdir}/libcufft_static.a
%{_libdir}/libcufft_static_nocallback.a
%{_libdir}/libcufftw_static.a

%changelog
%autochangelog

