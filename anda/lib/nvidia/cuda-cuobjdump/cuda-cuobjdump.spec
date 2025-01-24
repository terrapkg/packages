%global real_name cuda_cuobjdump

%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-6

Name:           %(echo %real_name | tr '_' '-')
Epoch:          1
Version:        12.6.77
Release:        1%{?dist}
Summary:        Utility to extract information from CUDA binary files
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-sbsa/%{real_name}-linux-sbsa-%{version}-archive.tar.xz

Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
cuobjdump extracts information from CUDA binary files (both standalone and those
embedded in host binaries) and presents them in human readable format. The
output of cuobjdump includes CUDA assembly code for each kernel, CUDA ELF
section headers, string tables, relocators and other CUDA specific sections. It
also extracts embedded ptx text from host binaries.

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{real_name}-linux-sbsa-%{version}-archive
%endif

%install
install -m 0755 -p -D bin/cuobjdump %{buildroot}%{_bindir}/cuobjdump

%files
%license LICENSE
%{_bindir}/cuobjdump

%changelog
%autochangelog

