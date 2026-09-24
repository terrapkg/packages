Name:           ocaml-ppx-stable
Version:        0.17.1
Release:        1%{?dist}
Summary:        ppx extension for easier implementation of conversion functions

License:        MIT
URL:            https://github.com/janestreet/ppx_stable
Source:         %{url}/archive/v%{version}/ppx_stable-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0
BuildRequires:  ocaml-base-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
A ppx extension for easier implementation of
conversion functions between almost identical types.

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
