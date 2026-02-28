%global real_name libnvvm

%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 13-0

Name:           %(echo %real_name | tr '_' '-')
Version:        13.1.115
Release:        1%?dist
Summary:        CUDA NVVM
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-sbsa/%{real_name}-linux-sbsa-%{version}-archive.tar.xz

Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}
 
%description
NVVM IR is a compiler IR (intermediate representation) based on the LLVM IR.
The NVVM IR is designed to represent GPU compute kernels (for example, CUDA
kernels). High-level language front-ends, like the CUDA C compiler front-end,
can generate NVVM IR. The NVVM compiler (which is based on LLVM) generates PTX
code from NVVM IR.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
Files for development with %{name} and LLVM IR bytecode.

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{real_name}-linux-sbsa-%{version}-archive
%endif

%install
install -p -m 0755 -D nvvm/bin/cicc %{buildroot}%{_bindir}/cicc
install -p -m 0644 -D nvvm/include/nvvm.h %{buildroot}%{_includedir}/nvvm.h
install -p -m 0644 -D nvvm/libdevice/libdevice.10.bc %{buildroot}%{_datadir}/libdevice/libdevice.10.bc
# CMake expects the nvvm/libdevice in the same prefix as bin/cicc:
ln -sf share %{buildroot}%{_prefix}/nvvm

mkdir -p %{buildroot}%{_libdir}
cp -fr nvvm/lib64/* %{buildroot}%{_libdir}/

%files
%license LICENSE
%{_libdir}/libnvvm.so.*

%files devel
%{_bindir}/cicc
%{_datadir}/libdevice
%{_includedir}/nvvm.h
%{_libdir}/libnvvm.so
%{_prefix}/nvvm

%changelog
%autochangelog
