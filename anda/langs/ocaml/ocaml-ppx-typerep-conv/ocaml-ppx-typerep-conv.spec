Name:           ocaml-ppx-typerep-conv
Version:        0.17.1
Release:        1%{?dist}
Summary:        Automatic generation of runtime types from type definitions

License:        MIT
URL:            https://github.com/janestreet/ppx_typerep_conv
Source:         %{url}/archive/v%{version}/ppx_typerep_conv-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-cold-devel
BuildRequires:  ocaml-ppx-compare-devel
BuildRequires:  ocaml-ppx-enumerate-devel
BuildRequires:  ocaml-ppx-globalize-devel
BuildRequires:  ocaml-ppx-hash-devel
BuildRequires:  ocaml-ppx-sexp-conv-devel
BuildRequires:  ocaml-ppx-stable-witness-devel
BuildRequires:  ocaml-ppx-variants-conv-devel
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-typerep-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Automatic generation of runtime types from type definitions.

This syntax extension defines the type-conv generator [@@deriving typerep],
which creates a (runtime) value (called typerep_of_$typename) representing
the type definition (see typerep for more information). It is intended to
be the main creator of values of type Typerep.t.

This generator supports mostly core types, not all fancy types like union
of polymorphic variants.

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
%doc README.md

%files devel -f .ofiles-devel

%changelog
* Tue Sep 22 2026 Owen Zimmerman <owen@fyralabs.com> - 0.17.1-1
- Initial commit
