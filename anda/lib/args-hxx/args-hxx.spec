%define debug_package %nil

Name:		args-hxx
Version:	6.5.0
Release:	1%{?dist}
Summary:	A simple header-only C++ argument parser library
License:	MIT
URL:		https://github.com/Taywee/args
Source0:	%url/archive/refs/tags/%version.tar.gz
BuildRequires:	make doxygen gcc-c++ cmake

%description
A simple header-only C++ argument parser library. Supposed to be flexible and
powerful, and attempts to be compatible with the functionality of the Python
standard argparse library (though not necessarily the API).


%package doc
Summary:	Documentations for args-hxx

%description doc
%summary.


%prep
%autosetup -n args-%version

%conf
%cmake

%build
%cmake_build
%__make doc/man

%install
%cmake_install
make installman DESTDIR=%buildroot%_prefix

%files
%_includedir/args.hxx
%{_datadir}/cmake/args/args-*.cmake
%{_datadir}/pkgconfig/args.pc

%files doc
%_mandir/man3/args*
%_mandir/man3/conanfile_ArgsConan.3.gz
%_mandir/man3/md_CONTRIBUTING.3.gz


%changelog
%autochangelog
