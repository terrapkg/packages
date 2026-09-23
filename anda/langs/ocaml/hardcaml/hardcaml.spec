Name:           hardcaml
Version:        0.17.1
Release:        1%?dist
Summary:        An embedded DSL for designing and simulating hardware in OCaml
URL:            https://github.com/janestreet/hardcaml/
Source0:        %{url}archive/refs/tags/v%{version}.tar.gz
License:        MIT
BuildSystem:    dune
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-base
BuildRequires:  ocaml-zarith
BuildRequires:  ocaml-stdio
BuildRequires:  ocaml-ppxlib
BuildRequires:  ocaml-ppxlib-jane-devel
BuildRequires:  ocaml-ppx-sexp-conv
ExclusiveArch:  %{ocaml_native_compiler}

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Hardcaml is an embedded DSL for designing and simulating hardware in OCaml.
Generic hardware designs are easily expressed using features such as higher
order functions, lists, maps etc. A built in simulator allows designs to be
simulated within Hardcaml. Designs are converted to either Verilog or
VHDL to interact with standard back end tooling.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{evr}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -C

%check

%files -f .ofiles
%doc README.md CONTRIBUTING.md CHANGES.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Tue Sep 22 2026 Owen Zimmerman <owen@fyralabs.com> 0.17.1-1
- Initial commit
