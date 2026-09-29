Name:           ocaml-ppx-fixed-literal
Version:        0.17.0
Release:        1%{?dist}
Summary:        A ppx rewriter that rewrites fixed point literal of the form 1.0v to conversion functions currently in scope

License:        MIT
URL:            https://github.com/janestreet/ppx_fixed_literal
Source:         %{url}/archive/v%{version}/ppx_fixed_literal-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-base-devel

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
