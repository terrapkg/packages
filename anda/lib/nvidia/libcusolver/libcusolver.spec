%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-8

Name:           libcusolver
Epoch:          2
Version:        11.7.2.55
Release:        1%{?dist}
Summary:        NVIDIA cuSOLVER library
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-x86_64/%{name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-sbsa/%{name}-linux-sbsa-%{version}-archive.tar.xz
Source3:        cusolver.pc

Requires:       libgomp%{_isa}
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
The NVIDIA cuSOLVER library provides a collection of dense and sparse direct
solvers which deliver significant acceleration for Computer Vision, CFD,
Computational Chemistry, and Linear Optimization applications.

%package devel
Summary:        Development files for NVIDIA cuSOLVER library
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
This package provides development files for the NVIDIA cuSOLVER library.

%package static
Summary:        Static libraries for NVIDIA cuSOLVER
Requires:       %{name}-devel%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description static
This package contains static libraries for NVIDIA cuSOLVER.

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
cp -fr %{SOURCE3} %{buildroot}/%{_libdir}/pkgconfig/

# Set proper variables
sed -i \
    -e 's|CUDA_VERSION|%{version}|g' \
    -e 's|LIBDIR|%{_libdir}|g' \
    -e 's|INCLUDE_DIR|%{_includedir}|g' \
    %{buildroot}/%{_libdir}/pkgconfig/*.pc

%files
%license LICENSE
%{_libdir}/libcusolver.so.*
%{_libdir}/libcusolverMg.so.*

%files devel
%{_includedir}/cusolver_common.h
%{_includedir}/cusolverDn.h
%{_includedir}/cusolverMg.h
%{_includedir}/cusolverRf.h
%{_includedir}/cusolverSp.h
%{_includedir}/cusolverSp_LOWLEVEL_PREVIEW.h
%{_libdir}/libcusolver.so
%{_libdir}/libcusolverMg.so
%{_libdir}/libcusolver_lapack_static.a
%{_libdir}/libcusolver_metis_static.a
%{_libdir}/libmetis_static.a
%{_libdir}/pkgconfig/cusolver.pc

%files static
%{_libdir}/libcusolver_static.a

%changelog
* Fri Feb 07 2025 Simone Caronni <negativo17@gmail.com> - 2:11.7.2.55-1
- Update to 11.7.2.55.

* Fri Dec 13 2024 Simone Caronni <negativo17@gmail.com> - 2:11.7.1.2-1
- Update to 11.7.1.2.

* Thu Sep 19 2024 Simone Caronni <negativo17@gmail.com> - 2:11.6.4.69-1
- Update to 11.6.4.69.

* Thu Jul 11 2024 Simone Caronni <negativo17@gmail.com> - 2:11.6.3.83-1
- Update to 11.6.3.83.

* Tue Mar 12 2024 Simone Caronni <negativo17@gmail.com> - 2:11.6.0.99-1
- Update to 11.6.0.99.
- Drop ppc64le.

* Tue Nov 28 2023 Simone Caronni <negativo17@gmail.com> - 2:11.5.4.101-1
- Update to 11.5.4.101.

* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 2:11.5.2.141-1
- Update to 11.5.2.141.

* Tue Jul 11 2023 Simone Caronni <negativo17@gmail.com> - 2:11.5.0.53-1
- Update to 11.5.0.53.

* Thu Jun 08 2023 Simone Caronni <negativo17@gmail.com> - 2:11.4.5.107-1
- Update to 11.4.5.107.

* Tue Apr 11 2023 Simone Caronni <negativo17@gmail.com> - 2:11.4.4.55-1
- Update to 11.4.4.55.

* Sat Feb 25 2023 Simone Caronni <negativo17@gmail.com> - 2:11.4.3.1-1
- Update to 11.4.3.1.

* Tue Dec 13 2022 Simone Caronni <negativo17@gmail.com> - 2:11.4.2.57-1
- Update to 11.4.2.57.

* Fri Nov 11 2022 Simone Caronni <negativo17@gmail.com> - 2:11.4.1.48-1
- Update to 11.4.1.48.
- Use aarch64 archive in place of sbsa.

* Sun Sep 04 2022 Simone Caronni <negativo17@gmail.com> - 2:11.4.0.1-1
- Update to 11.4.0.1.

* Thu Jun 23 2022 Simone Caronni <negativo17@gmail.com> - 2:11.3.5.50-1
- Update to 11.3.5.50.

* Thu Mar 31 2022 Simone Caronni <negativo17@gmail.com> - 2:11.3.4.124-1
- Update to 11.3.4.124 (CUDA 11.6.2).

* Tue Mar 08 2022 Simone Caronni <negativo17@gmail.com> - 2:11.3.3.112-1
- Update to 11.3.3.112 (CUDA 11.6.1).

* Wed Jan 26 2022 Simone Caronni <negativo17@gmail.com> - 2:11.3.2.55-1
- First build with the new tarball components.

