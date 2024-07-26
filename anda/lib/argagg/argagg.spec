%global debug_package %{nil}

Name:           argagg
Version:        0.4.7
Release:        1%{?dist}
Summary:        Simple C++ command line argument/option parser

License:        MIT
URL:            https://github.com/vietjtnguyen/argagg/
Source0:        https://github.com/vietjtnguyen/argagg/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++

%description
This is yet another C++ command line argument/option parser. It was written as
a simple and idiomatic alternative to other frameworks like getopt, Boost
program options, TCLAP, and others. The goal is to achieve the majority of
argument parsing needs in a simple manner with an easy to use API. It operates
as a single pass over all arguments, recognizing flags prefixed by - (short) or
-- (long) and aggregating them into easy to access structures with lots of
convenience functions. It defers processing types until you access them, so the
result structures end up just being pointers into the original command line
argument C-strings. argagg supports POSIX recommended argument syntax
conventions.

%package        devel
Summary:        Development files for %{name}

%description    devel
The %{name}-devel package contains the header files for developing applications
that use %{name}.

%package        doc
Summary:        Developer documentation for %{name}

%description    doc
The %{name}-doc package contains the documentation for developing applications
that use %{name}.

%prep
%setup -q

%build
# ignore doctest warnings
%cmake -DOXYGEN=ON
# enter cmake build directory
pushd redhat-linux-build
mkdir share
popd
%cmake_build -t docs


%install
%cmake_install

#ls -la redhat-linux-build/share

%files

%files devel
%{_includedir}/*

%files doc
%doc %{_datadir}/doc/%{name}

%changelog
* Fri May 26 2017 Viet The Nguyen <vietjtnguyen@gmail.com> - 0.4.6-1
- Updated version to 0.4.6

* Fri Apr 28 2017 Viet The Nguyen <vietjtnguyen@gmail.com> - 0.4.5-1
- Updated version to 0.4.5

* Tue Apr 25 2017 Viet The Nguyen <vietjtnguyen@gmail.com> - 0.4.4-1
- Updated version to 0.4.4

* Tue Apr 25 2017 Viet The Nguyen <vietjtnguyen@gmail.com> - 0.4.3-1
- Updated version to 0.4.3

* Tue Apr 25 2017 Viet The Nguyen <vietjtnguyen@gmail.com> - 0.4.2-1
- Updated version to 0.4.2

* Sun Mar 05 2017 Viet The Nguyen <vietjtnguyen@gmail.com>
- Updated description
- Remove dependence on empty root package

* Sun Feb 19 2017 Viet The Nguyen <vietjtnguyen@gmail.com>
- Disabled creation of debuginfo package

* Mon Feb 13 2017 Viet The Nguyen <vietjtnguyen@gmail.com>
- Fixed License field and doc subpackage description typo

* Sat Feb 11 2017 Viet The Nguyen <vietjtnguyen@gmail.com> - 0.2.2-1
- Updated version to 0.2.2

* Fri Feb 10 2017 Viet The Nguyen <vietjtnguyen@gmail.com> - 0.2.1-2
- Separated documentation into a separate package

* Fri Feb 10 2017 Viet The Nguyen <vietjtnguyen@gmail.com> - 0.2.1-1
- Packaged version 0.2.1

* Mon Jan 30 2017 Viet The Nguyen <vietjtnguyen@gmail.com>
- Added missing files specification for empty parent package

* Sun Jan 29 2017 Viet The Nguyen <vietjtnguyen@gmail.com>
- Initial packaging
