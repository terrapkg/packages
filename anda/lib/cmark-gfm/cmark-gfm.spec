Name:           cmark-gfm
Version:        0.29.0.gfm.13
Release:        2%{?dist}
License:        BSD-2-Clause AND MIT
URL:            https://github.com/github/cmark-gfm
Source:         %{url}/archive/refs/tags/%{version}.tar.gz
Patch0:         fix-cmake-dir.patch
Summary:        GitHub's fork of cmark, a CommonMark parsing and rendering library and program in C
Packager:       metcya <metcya@gmail.com>

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
cmark-gfm is an extended version of the C reference implementation of
CommonMark, a rationalized version of Markdown syntax with a spec. This
repository adds GitHub Flavored Markdown extensions to the upstream
implementation, as defined in the spec.

%package libs
Summary:        Library files for %{name}
%pkg_libs_files

%description libs
Library files for %{name}.

%package static
Summary:        Static library files for %{name}
%pkg_static_files

%description static
Static library files for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs = %{evr}
%pkg_devel_files

%description devel
Development files for %{name}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man3/%{name}.3.*

%files devel
%{_libdir}/cmake/cmark-gfm/
%{_libdir}/cmake-gfm-extensions/

%changelog
* Thu Dec 25 2025 metcya <metcya@gmail.com> - 0.29.0.gfm.13-2
- Fix cmake install directories

* Wed Dec 24 2025 metcya <metcya@gmail.com> - 0.29.0.gfm.13-1
- Package cmark-gfm
