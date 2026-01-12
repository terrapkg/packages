%global real_name libnvptxcompiler

%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 13-0

Name:           %{real_name}-devel
Epoch:          1
Version:        13.1.115
Release:        1%?dist
Summary:        CUDA nvptxcompiler
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-sbsa/%{real_name}-linux-sbsa-%{version}-archive.tar.xz

Conflicts:      %{real_name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}
 
%description
Compiler IR for CUDA applications.

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{real_name}-linux-sbsa-%{version}-archive
%endif

%install
install -p -m 0755 -D lib/libnvptxcompiler_static.a %{buildroot}%{_libdir}/libnvptxcompiler_static.a
install -p -m 0644 -D include/nvPTXCompiler.h %{buildroot}%{_includedir}/nvPTXCompiler.h

%files
%license LICENSE
%{_libdir}/libnvptxcompiler_static.a
%{_includedir}/nvPTXCompiler.h

%changelog
%autochangelog
