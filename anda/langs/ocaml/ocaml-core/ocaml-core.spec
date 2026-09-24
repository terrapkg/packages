Name:           ocaml-core
Version:        0.17.2
Release:        1%{?dist}
Summary:        Core suite of libraries is an industrial strength alternative to OCaml's standard library

License:        MIT
URL:            https://github.com/janestreet/core
Source:         %{url}/archive/v%{version}/core-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-jst-config-devel
BuildRequires:  ocaml-ppx-base-devel
BuildRequires:  ocaml-ppx-jane-devel
BuildRequires:  ocaml-ppx-inline-test-devel
BuildRequires:  ocaml-ppx-sexp-message-devel
BuildRequires:  ocaml-ppx-diff-devel
BuildRequires:  ocaml-variantslib-devel
BuildRequires:  ocaml-ppx-stable-devel
BuildRequires:  ocaml-ppx-log-devel
BuildRequires:  ocaml-ppx-expect-devel
BuildRequires:  ocaml-typerep-devel
BuildRequires:  ocaml-ppx-ignore-instrumentation-devel
BuildRequires:  ocaml-ppx-assert-devel
BuildRequires:  ocaml-base-bigstring-devel
BuildRequires:  ocaml-ppx-variants-conv-devel
BuildRequires:  ocaml-ppx-typerep-conv-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
The Core suite of libraries is an industrial strength
alternative to OCaml's standard library that was
developed by Jane Street, the largest industrial user of OCaml.

This is the system-independent part of Core.
Unix-specific parts were moved to [core_unix].

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
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Tue Sep 22 2026 Owen Zimmerman <owen@fyralabs.com> - 0.17.2-1
- Initial commit
