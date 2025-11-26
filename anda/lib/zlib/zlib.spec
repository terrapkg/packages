Name:           zlib
Version:        1.3.1
Release:        1%?dist
License:        Zlib
URL:            https://zlib.net
Source:         https://github.com/madler/zlib/archive/v%{version}.tar.gz
Summary:        A massively spiffy yet delicately unobtrusive compression library
Conflicts:      zlib-ng

BuildRequires:  cmake gcc

%description
%summary.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and headers for developing applications that use %{name}.

%package static
Summary:    Static library files for %{name}
Requires:   %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static library files for %{name}

%prep
%autosetup
%cmake -DLIBDIR=lib64 .

%build
%cmake_build

%install
%cmake_install 
ls -lah %{_libdir}

%files
%license LICENSE
%doc README FAQ INDEX ChangeLog
%{_libdir}/libz.so.*
%{_libdir}/libz.so.%{version}

%files devel
%{_includedir}/*.h
%{_libdir}/libz.so
%{_datadir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{name}.3.*

%files static
%{_libdir}/libz.a

%changelog
* Wed Nov 26 2025 metcya <metcya@gmail.com>
- package zlib
