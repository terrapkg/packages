%global _major 1

Name:           libnvidia-container
Version:        1.17.5
Release:        1%?dist
Summary:        NVIDIA container runtime library
License:        BSD-3-Clause AND Apache-2.0 AND GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND GPL-2.0-only
Vendor:         NVIDIA Corporation
URL:            https://github.com/NVIDIA/%{name}
Source0:        https://github.com/NVIDIA/%{name}/archive/v%{version}.tar.gz
Patch0:         fix-revision.patch
Patch1:         fix-makefile.patch
Patch2:         fix-debug-packages.patch
BuildRequires:  bmake
BuildRequires:  elfutils-libelf-devel
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  golang
BuildRequires:  libcap-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libseccomp-devel
BuildRequires:  rpcgen

%description
The nvidia-container library provides an interface to configure containers using NVIDIA hardware.

%prep
rm -rf ./*
### Must be built this way because the Makefile expects be to in a Git directory.
git clone https://github.com/NVIDIA/%{name}.git
cd %{name}
git checkout v%{version}
%autopatch -p1

%build
cd %{name}
make distclean
%make_build REVISION=%{version} WITH_LIBELF=yes

%install
cd %{name}
make install DESTDIR=%{buildroot} REVISION=%{version} WITH_LIBELF=yes \
             LDCONFIG=/bin/true \
             prefix=%{_prefix} \
             exec_prefix=%{_exec_prefix} \
             bindir=%{_bindir} \
             libdir=%{_libdir} \
             includedir=%{_includedir} \
             docdir=%{_licensedir}

%package -n %{name}%{_major}
Summary:        NVIDIA container runtime library
Requires:       nvidia-driver >= 340.29
%description -n %{name}%{_major}
The nvidia-container library provides an interface to configure containers using NVIDIA hardware.

%post -n %{name}%{_major} -p /sbin/ldconfig
%postun -n %{name}%{_major} -p /sbin/ldconfig

%package devel
Requires:       %{name}%{_major}%{?_isa} = %{version}-%{release}
Summary:        NVIDIA container runtime library development files
Requires:       nvidia-driver >= 340.29
%description devel
This package contains the files required to compile programs with the library.

%package static
Requires:      %{name}-devel%{?_isa} = %{version}-%{release}
Summary:        NVIDIA container runtime library static library
Requires:       nvidia-driver >= 340.29
%description static
The nvidia-container library provides an interface to configure containers using NVIDIA hardware.

%package tools
Requires:       %{name}%{_major}%{?_isa} >= %{version}-%{release}
Summary:        NVIDIA container runtime library command-line tools
Requires:       nvidia-driver >= 340.29
%description tools
This package contains command-line tools that facilitate using the nvidia-container library.

%package   libseccomp2
Requires:  libseccomp2
Provides:  libseccomp.so
Conflicts: libseccomp.so
Summary:   A virtual package to provide libseccomp through libseccomp2
%description libseccomp2
This is a virtual package to satisfy the libseccomp.so dependency through a transitive dependency on libseccomp2.so.

%files -n %{name}%{_major}
%license %{_licensedir}/*
%{_libdir}/lib*.so.*

%files devel
%license %{_licensedir}/*
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files static
%license %{_licensedir}/*
%{_libdir}/lib*.a

%files tools
%license %{_licensedir}/*
%{_bindir}/*

%files libseccomp2
%license %{_licensedir}/*

%changelog
%autochangelog
