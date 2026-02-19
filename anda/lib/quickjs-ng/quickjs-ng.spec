%global _distro_extra_cflags -Wno-discarded-qualifiers -Wno-maybe-uninitialized

Name:           quickjs-ng
Version:        0.12.1
Release:        1%?dist
License:        MIT
Summary:        A mighty JavaScript engine
URL:            https://github.com/quickjs-ng/quickjs
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:       Metcya <metcya@gmail.com>
Provides:       qjs
Provides:       qjsc

BuildRequires:  gcc
BuildRequires:  cmake

Requires:       %{name}-libs%{_isa} = %evr

%description
QuickJS is a small and embeddable JavaScript engine. It aims to support the
latest ECMAScript specification. This project is a fork of the original QuickJS
project by Fabrice Bellard and Charlie Gordon, after it went dormant, with the
intent of reigniting its development.

%package libs
%pkg_libs_files

%files libs
%license LICENSE

%package devel
Requires:   %{name}-libs%{_isa} = %evr
%pkg_devel_files

%files devel
%{_libdir}/cmake/quickjs/*.cmake


%package examples
Summary:    Example files for %{name}

%description examples
Example files for %{name}

%prep
%autosetup -p1 -n quickjs-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_docdir}/quickjs/LICENSE

%files
%doc README.md
%license LICENSE
%{_bindir}/qjs
%{_bindir}/qjsc

%files examples
%license LICENSE
%{_docdir}/quickjs/examples/*

%changelog
* Sun Dec 07 2025 metcya <metcya@gmail.com> - 0.11.0
- Package quickjs-ng
