Name:           ocaml-ppx-optional
Version:        0.17.0
Release:        1%{?dist}
Summary:        ppx rewriter that rewrites simple match statements with an if then else expression

License:        MIT
URL:            https://github.com/janestreet/ppx_optional
Source:         %{url}/archive/v%{version}/ppx_optional-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-ppxlib-jane-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
A ppx rewriter that rewrites simple match statements with an if then else expression.

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
