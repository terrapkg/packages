Name:           ocaml-typerep
Version:        0.17.1
Release:        1%{?dist}
Summary:        OCaml library for runtime types

License:        MIT
URL:            https://github.com/janestreet/typerep
Source:         %{url}/archive/v%{version}/typerep-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-base

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
%doc CONTRIBUTING.md

%files devel -f .ofiles-devel

%changelog
* Tue Sep 22 2026 Owen Zimmerman <owen@fyralabs.com> - 0.17.1-1
- Initial commit
