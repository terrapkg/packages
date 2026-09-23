Name:           ocaml-int-repr
Version:        0.17.0
Release:        1%{?dist}
Summary:        Integers of various widths

License:        MIT
URL:            https://github.com/janestreet/int_repr
Source:         %{url}/archive/v%{version}/int_repr-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-ppx-jane-devel
BuildRequires:  ocaml-ppx-stable-devel
BuildRequires:  ocaml-base-quickcheck-devel
BuildRequires:  ocaml-ppx-log-devel
BuildRequires:  ocaml-ppx-expect-devel
BuildRequires:  ocaml-ppx-ignore-instrumentation-devel
BuildRequires:  ocaml-ppx-variants-conv-devel
BuildRequires:  ocaml-ppx-typerep-conv-devel
BuildRequires:  ocaml-ppx-tydi-devel
BuildRequires:  ocaml-ppx-string-conv-devel
BuildRequires:  ocaml-ppx-stable-witness-devel
BuildRequires:  ocaml-ppx-sexp-value-devel
BuildRequires:  ocaml-ppx-pipebang-devel
BuildRequires:  ocaml-ppx-optional-devel
BuildRequires:  ocaml-ppx-module-timer-devel
BuildRequires:  ocaml-ppx-let-devel
BuildRequires:  ocaml-ppx-fixed-literal-devel
BuildRequires:  ocaml-ppx-fields-conv-devel
BuildRequires:  ocaml-ppx-disable-unused-warnings-devel
BuildRequires:  ocaml-ppx-custom-printf-devel
BuildRequires:  ocaml-ppx-bin-prot-devel
BuildRequires:  ocaml-ppx-assert-devel
BuildRequires:  ocaml-bin-prot-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

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
