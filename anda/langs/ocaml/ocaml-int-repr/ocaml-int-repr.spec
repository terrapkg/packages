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
