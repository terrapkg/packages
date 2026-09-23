Name:           ocaml-ppx-bin-prot
Version:        0.17.1
Release:        1%{?dist}
Summary:        Generation of bin_prot readers and writers from types

License:        MIT
URL:            https://github.com/janestreet/ppx_bin_prot
Source:         %{url}/archive/v%{version}/ppx_bin_prot-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-bin-prot-devel
BuildRequires:  ocaml-ppx-jane

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

%check

%files -f .ofiles
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Tue Sep 22 2026 Owen Zimmerman <owen@fyralabs.com> - 0.17.1-1
- Initial commit
