Name:           ocaml-uopt
Version:        0.17.0
Release:        1%{?dist}
Summary:        Provides an unboxed option type

License:        MIT
URL:            https://github.com/janestreet/uopt
Source:         %{url}/archive/v%{version}/uopt-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-ppx-jane-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Uopt_base provides an unboxed option type, for use in
high-performance systems which avoid allocation. It has
several downsides as compared to [option], and is
not recommended for use in general-purpose software.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{evr}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -C

%files -f .ofiles
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Tue Sep 22 2026 Owen Zimmerman <owen@fyralabs.com> - 0.17.0-1
- Initial commit
