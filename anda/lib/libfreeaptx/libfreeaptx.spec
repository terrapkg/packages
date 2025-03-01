%global commit c176b7de9c2017d0fc1877659cea3bb6c330aafa
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20210809

Name:       libfreeaptx
Version:    0.1.1.%{commit_date}git%{shortcommit}
Release:    1%{?dist}
Summary:    Free implementation of Audio Processing Technology codec (aptX)
License:    LGPLv2+
URL:        https://github.com/iamthehorker/libfreeaptx
Source0:    %{url}/archive/%{commit}/libfreeaptx-%{commit}.tar.gz
BuildRequires:  gcc
BuildRequires:  make

%description
This is an Open Source implementation of Audio Processing Technology codec
(aptX). This codec is mainly used in Bluetooth A2DP profile.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package tools
Summary:    %{name} encoder and decoder utilities
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description tools
The %{name}-tools package contains command line encoder and decoder utilities.

%prep
%autosetup -n libfreeaptx-%{commit} -p1

%build
%make_build LDFLAGS="%{build_ldflags}" "CFLAGS=%{build_cflags}"

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_lib}

%files
%license COPYING
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.0.1.1

%files devel
%{_includedir}/freeaptx.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%doc README
%{_bindir}/freeaptxenc
%{_bindir}/freeaptxdec

%changelog
%autochangelog
