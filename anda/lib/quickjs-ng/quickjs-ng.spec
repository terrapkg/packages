Name:           quickjs-ng
Version:        0.11.0
Release:        1%?dist
License:        MIT
Summary:        A mighty JavaScript engine
URL:            https://github.com/quickjs-ng/quickjs
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
Provides:       qjs
Provides:       qjsc

BuildRequires:  gcc
BuildRequires:  cmake

Requires:       %{name}-libs%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
QuickJS is a small and embeddable JavaScript engine. It aims to support the
latest ECMAScript specification. This project is a fork of the original QuickJS
project by Fabrice Bellard and Charlie Gordon, after it went dormant, with the
intent of reigniting its development.

%package libs
%pkg_libs_files

%package devel
Requires:   %{name}-libs%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%pkg_devel_files

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

%files devel
%{_libdir}/cmake/quickjs/*.cmake

%files examples
%{_docdir}/quickjs/examples/*

%changelog
* Sun Dec 07 2025 metcya <metcya@gmail.com> - 0.11.0
- Package quickjs-ng
