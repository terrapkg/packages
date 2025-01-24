%global real_name cuda_nvdisasm

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
nvdisasm extracts information from standalone cubin files and presents them in
human readable format. The output of nvdisasm includes CUDA assembly code for
each kernel, listing of ELF data sections and other CUDA specific sections.
Output style and options are controlled through nvdisasm command-line options.
nvdisasm also does control flow analysis to annotate jump/branch targets and
makes the output easier to read.

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{real_name}-linux-sbsa-%{version}-archive
%endif

%install
install -m 0755 -p -D bin/nvdisasm %{buildroot}%{_bindir}/nvdisasm

%files
%license LICENSE
%{_bindir}/nvdisasm

%changelog
%autochangelog

