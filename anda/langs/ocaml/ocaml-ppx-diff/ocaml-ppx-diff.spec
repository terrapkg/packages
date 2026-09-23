Name:           ocaml-ppx-diff
Version:        0.17.1
Release:        1%{?dist}
Summary:        PPX rewriter that generates the implementation of [Ldiffable.S]

License:        MIT
URL:            https://github.com/janestreet/ppx_diff
Source:         %{url}/archive/v%{version}/ppx_diff-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
A PPX rewriter that generates the implementation of
[Ldiffable.S]. Generates diffs and update functions for OCaml types.

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
* Tue Sep 22 2026 Owen Zimmerman <owen@fyralabs.com> - 0.17.1-1
- Initial commit
