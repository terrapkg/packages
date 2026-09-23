Name:           ocaml-ppx-tydi
Version:        0.17.1
Release:        1%{?dist}
Summary:        Provides a ppx for [let%%tydi]

License:        MIT
URL:            https://github.com/janestreet/ppx_tydi
Source:         %{url}/archive/v%{version}/ppx_tydi-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Provides a ppx for [let%%tydi]: type-directed [let] bindings.
In [let%%tydi a = b in ...], [a]'s type is inferred from [b]
rather than the other way around. This is convenient for
record patterns whose fields are not in scope.

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
