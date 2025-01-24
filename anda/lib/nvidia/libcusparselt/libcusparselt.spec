%global         debug_package %{nil}
%global         __strip /bin/true
%global         _missing_build_ids_terminate_build 0
%global         _build_id_links none

Name:           libcusparselt
Version:        0.6.3.2
Release:        1%?dist
Summary:        CUDA Library for Sparse Matrix-Matrix Multiplication
License:        NVIDIA License
URL:            https://docs.nvidia.com/cuda/cusparselt/index.html
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cusparselt/redist/libcusparse_lt/linux-x86_64/libcusparse_lt-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cusparselt/redist/libcusparse_lt/linux-sbsa/libcusparse_lt-linux-sbsa-%{version}-archive.tar.xz

Conflicts:      %{name}0 < %{?epoch:%{epoch}:}%{version}-%{release}

%description
NVIDIA cuSPARSELt is a high-performance CUDA library dedicated to general
matrix-matrix operations in which at least one operand is a sparse matrix.

The cuSPARSELt APIs allow flexibility in the algorithm/operation selection,
epilogue, and matrix characteristics, including memory layout, alignment, and
data types.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       cuda-devel%{?_isa}
Conflicts:      %{name}-devel < %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use cuSPARSELt.

%package        static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    static
Static libraries for cuSPARSELt.

%prep
%ifarch x86_64
%setup -q -n libcusparse_lt-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n libcusparse_lt-linux-sbsa-%{version}-archive
%endif

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_libdir}/
cp -a lib/libcusparseLt.so* %{buildroot}%{_libdir}/
chmod 755 %{buildroot}%{_libdir}/*.so*
install -p -m0644 lib/libcusparseLt_static.a %{buildroot}%{_libdir}/

mkdir -p %{buildroot}%{_includedir}/
install -p -m0644 include/cusparseLt.h %{buildroot}%{_includedir}/

%{?ldconfig_scriptlets}

%files
%license LICENSE
%{_libdir}/libcusparseLt.so.*

%files devel
%{_includedir}/cusparseLt.h
%{_libdir}/libcusparseLt.so

%files static
%{_libdir}/libcusparseLt_static.a

%changelog
%autochangelog
