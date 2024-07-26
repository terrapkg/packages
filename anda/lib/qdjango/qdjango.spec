Name:       qdjango
Version:    0.6.2
Release:    %autorelease
Summary:    A web framework written in C++ and built on top of the Qt library
License:    LGPLv2
URL:        https://github.com/jlaine/qdjango
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz
Patch0:     https://sources.debian.org/data/main/q/qdjango/0.6.2-3.3/debian/patches/disable_hash_tests.patch
Patch1:     https://sources.debian.org/data/main/q/qdjango/0.6.2-3.3/debian/patches/fix_gcc6_ftbfs.patch

BuildRequires: qt5-rpm-macros
BuildRequires: qt5-qtbase-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: doxygen


%description
QDjango is a web framework written in C++ and built on top of the Qt library.
Where possible, it tries to follow django's API, hence its name.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documenation for %{name}
BuildArch: noarch

%description doc
The %{name}-doc contains documentation for %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%qmake_qt5 PREFIX=%{_exec_prefix} LIBDIR=%{_lib}
%make_build
%make_build docs

%install
%make_install INSTALL_ROOT=%{buildroot}
# Aren't needed and already ran plus contain rpaths in every single file underneath
rm -rf %{buildroot}%{_prefix}/tests

%files
%doc README.md
%license LICENSE.LGPL
%{_libdir}/libqdjango-db.so.*
%{_libdir}/libqdjango-http.so.*

%files devel
%dir %{_includedir}/qdjango
%dir %{_includedir}/qdjango/db
%{_includedir}/qdjango/db/*.h
%dir %{_includedir}/qdjango/http
%{_includedir}/qdjango/http/*.h
%{_libdir}/libqdjango-db.so
%{_libdir}/libqdjango-http.so
%{_libdir}/pkgconfig/qdjango-db.pc
%{_libdir}/pkgconfig/qdjango-http.pc

%files doc
%dir %{_docdir}/qdjango
%{_docdir}/qdjango/html/

%changelog
%autochangelog
