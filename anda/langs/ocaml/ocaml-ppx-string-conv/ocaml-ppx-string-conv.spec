Name:           ocaml-ppx-string-conv
Version:        0.17.0
Release:        1%{?dist}
Summary:        A ppx to help derive of_string and to_string

License:        MIT
URL:            https://github.com/janestreet/ppx_string_conv
Source:         %{url}/archive/v%{version}/ppx_string_conv-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-capitalization-devel
BuildRequires:  ocaml-ppx-let-devel
BuildRequires:  ocaml-ppx-string-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
ppx_string_conv is a ppx to help derive of_string
and to_string, primarily for variant types.

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
