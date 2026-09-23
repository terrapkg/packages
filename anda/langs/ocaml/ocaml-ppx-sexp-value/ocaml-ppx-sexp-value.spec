Name:           ocaml-ppx-sexp-value
Version:        0.17.0
Release:        1%{?dist}
Summary:        installs a ppx-jane executable

License:        MIT
URL:            https://github.com/janestreet/ppx_sexp_value
Source:         %{url}/archive/v%{version}/ppx_sexp_value-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-ppx-sexp-conv-devel
BuildRequires:  ocaml-ppx-here-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
This package installs a ppx-jane executable,
which is a ppx driver including all standard Jane Street ppx rewriters.

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
