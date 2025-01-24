%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-6

Name:           libnvfatbin
Epoch:          1
Version:        12.6.77
Release:        1%{?dist}
Summary:        CUDA Fatbin Creator API
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-x86_64/%{name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{name}/linux-sbsa/%{name}-linux-sbsa-%{version}-archive.tar.xz
Source3:        nvfatbin.pc

Requires(post): ldconfig
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
The Fatbin Creator APIs are a set of APIs which can be used at runtime to
combine multiple CUDA objects into one CUDA fat binary (fatbin).

The functionality in this library is similar to the fatbinary offline tool in
the CUDA toolkit, with the following advantages:

 - Support for runtime fatbin creation.
 - The clients get fine grain control and can specify separate options for each
   fatbinary.
 - Supports direct input from memory, rather than requiring inputs be written to
   files.

%package devel
Summary:        Development files for CUDA Fatbin Creator API
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
This package provides development files for the CUDA Fatbin Creator API.

%package static
Summary:        Static libraries for CUDA Fatbin Creator API.
Requires:       %{name}-devel%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description static
This package contains static libraries for CUDA Fatbin Creator API.

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

%{?ldconfig_scriptlets}

%files
%license LICENSE
%{_libdir}/libnvfatbin.so.*

%files devel
%{_includedir}/nvFatbin.h
%{_libdir}/libnvfatbin.so
%{_libdir}/pkgconfig/nvfatbin.pc

%files static
%{_libdir}/libnvfatbin_static.a

%changelog
%autochangelog

