%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 13-1

Name:           libcuobjclient
Epoch:          1
Version:        1.1.0.44
Release:        1%{?dist}
Summary:        NVIDIA CUDA cuObject Client
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-x86_64/%{name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-sbsa/%{name}-linux-sbsa-%{version}-archive.tar.xz
Source3:        cuobjclient.pc

Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

Packager:       Terra Packaging Team <terra@fyralabs.com>

%description
asd

%package devel
Summary:        Development files for NVIDIA CUDA cuObject Client
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
RDMA Acceleration for S3-Compatible Object Storage.

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
%{_libdir}/libcuobjclient.so.*

%files devel
%doc README cuObjRDMADESCRprotocolformat.pdf
%{_includedir}/cuobjclient.h
%{_includedir}/cuobjtelem.h
%{_libdir}/libcuobjclient.so
%{_libdir}/pkgconfig/cuobjclient.pc

%changelog
* Wed Jul 8 2026 Gilver E. <roachy@fyralabs.com> - 1.1.0.44-1
- Initial package
