Name:           ocaml-base-quickcheck
Version:        0.17.1
Release:        1%{?dist}
Summary:        provides randomized testing in the style of Haskell's Quickcheck library

License:        MIT
URL:            https://github.com/janestreet/base_quickcheck
Source:         %{url}/archive/v%{version}/base_quickcheck-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-ppxlib-jane-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
provides randomized testing in the style of Haskell's Quickcheck
library, with support for built-in types as well as types provided by Base.

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
