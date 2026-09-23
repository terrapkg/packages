Name:           ocaml-ppx-sexp-message
Version:        0.17.0
Release:        1%{?dist}
Summary:        installs a ppx-jane executable

License:        MIT
URL:            https://github.com/janestreet/ppx_sexp_message
Source:         %{url}/archive/v%{version}/ppx_sexp_message-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0
BuildRequires:  ocaml-ppx-sexp-conv-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
The aim of ppx_sexp_message is to ease the creation of s-expressions in OCaml.
This is mainly motivated by writing error and debugging messages,
where one needs to construct a s-expression based on various
element of the context such as function arguments.

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
