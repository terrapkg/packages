%global real_name cuda_cuxxfilt

%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 13-1

Name:           %(echo %real_name | tr '_' '-')
Epoch:          1
Version:        13.3.29
Release:        2%{?dist}
Summary:        CUDA cuxxfilt (demangler)
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-sbsa/%{real_name}-linux-sbsa-%{version}-archive.tar.xz

Packager:       Terra Packaging Team <terra@fyralabs.com>

%description
CUDA cuxxfilt (demangler).

%package devel
Summary:        CUDA cuxxfilt (demangler)
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
CUDA cuxxfilt (demangler).

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{real_name}-linux-sbsa-%{version}-archive
%endif

%install
install -m 0755 -p -D bin/cu++filt %{buildroot}%{_bindir}/cu++filt
install -m 0644 -p -D include/nv_decode.h %{buildroot}%{_includedir}/nv_decode.h
install -m 0644 -p -D lib/libcufilt.a %{buildroot}%{_libdir}/libcufilt.a

%files devel
%license LICENSE
%{_bindir}/cu++filt
%{_includedir}/nv_decode.h
%{_libdir}/libcufilt.a

%changelog
* Wed Jul 8 2026 Gilver E. <roachy@fyralabs.com> - 1:13.3.29-2
- Mass update CUDA components
