%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-6

Name:           libnpp
Epoch:          1
Version:        12.3.1.54
Release:        1%{?dist}
Summary:        NVIDIA Performance Primitives libraries
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-x86_64/%{name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-sbsa/%{name}-linux-sbsa-%{version}-archive.tar.xz

Source10:       nppc.pc
Source11:       nppial.pc
Source12:       nppicc.pc
Source13:       nppicom.pc
Source14:       nppidei.pc
Source15:       nppif.pc
Source16:       nppig.pc
Source17:       nppim.pc
Source18:       nppi.pc
Source19:       nppist.pc
Source20:       nppisu.pc
Source21:       nppitc.pc
Source22:       npps.pc

Requires(post): ldconfig
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
The NVIDIA Performance Primitives library (NPP) is a collection of
GPU-accelerated image, video, and signal processing functions that deliver 5x
to 10x faster performance than comparable CPU-only implementations. Using NPP,
developers can take advantage of over 1900 image processing and approx 600
signal processing primitives to achieve significant improvements in application
performance in a matter of hours.

%package devel
Summary:        Development files for NVIDIA Performance Primitives libraries.
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
This package provides development files for the NVIDIA Performance Primitives
libraries.

%package static
Summary:        Static libraries for NVIDIA Performance Primitives
Requires:       %{name}-devel%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description static
This package contains static libraries for NVIDIA Performance Primitives
libraries.

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
cp -fr %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} \
    %{SOURCE16} %{SOURCE17} %{SOURCE18} %{SOURCE19} %{SOURCE20} %{SOURCE21} \
    %{SOURCE22} %{buildroot}/%{_libdir}/pkgconfig/

# Set proper variables
sed -i \
    -e 's|CUDA_VERSION|%{version}|g' \
    -e 's|LIBDIR|%{_libdir}|g' \
    -e 's|INCLUDE_DIR|%{_includedir}|g' \
    %{buildroot}/%{_libdir}/pkgconfig/*.pc

%{?ldconfig_scriptlets}

%files
%license LICENSE
%{_libdir}/libnppc.so.*
%{_libdir}/libnppial.so.*
%{_libdir}/libnppicc.so.*
%{_libdir}/libnppidei.so.*
%{_libdir}/libnppif.so.*
%{_libdir}/libnppig.so.*
%{_libdir}/libnppim.so.*
%{_libdir}/libnppist.so.*
%{_libdir}/libnppisu.so.*
%{_libdir}/libnppitc.so.*
%{_libdir}/libnpps.so.*

%files devel
%{_includedir}/nppcore.h
%{_includedir}/nppdefs.h
%{_includedir}/npp.h
%{_includedir}/nppi_arithmetic_and_logical_operations.h
%{_includedir}/nppi_color_conversion.h
%{_includedir}/nppi_data_exchange_and_initialization.h
%{_includedir}/nppi_filtering_functions.h
%{_includedir}/nppi_geometry_transforms.h
%{_includedir}/nppi.h
%{_includedir}/nppi_linear_transforms.h
%{_includedir}/nppi_morphological_operations.h
%{_includedir}/nppi_statistics_functions.h
%{_includedir}/nppi_support_functions.h
%{_includedir}/nppi_threshold_and_compare_operations.h
%{_includedir}/npps_arithmetic_and_logical_operations.h
%{_includedir}/npps_conversion_functions.h
%{_includedir}/npps_filtering_functions.h
%{_includedir}/npps.h
%{_includedir}/npps_initialization.h
%{_includedir}/npps_statistics_functions.h
%{_includedir}/npps_support_functions.h
%{_libdir}/libnppc.so
%{_libdir}/libnppial.so
%{_libdir}/libnppicc.so
%{_libdir}/libnppidei.so
%{_libdir}/libnppif.so
%{_libdir}/libnppig.so
%{_libdir}/libnppim.so
%{_libdir}/libnppist.so
%{_libdir}/libnppisu.so
%{_libdir}/libnppitc.so
%{_libdir}/libnpps.so
%{_libdir}/pkgconfig/npp*.pc

%files static
%{_libdir}/libnppc_static.a
%{_libdir}/libnppial_static.a
%{_libdir}/libnppicc_static.a
%{_libdir}/libnppidei_static.a
%{_libdir}/libnppif_static.a
%{_libdir}/libnppig_static.a
%{_libdir}/libnppim_static.a
%{_libdir}/libnppist_static.a
%{_libdir}/libnppisu_static.a
%{_libdir}/libnppitc_static.a
%{_libdir}/libnpps_static.a
%changelog
%autochangelog