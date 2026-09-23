Name:           ocaml-ppx-disable-unused-warnings
Version:        0.17.0
Release:        1%{?dist}
Summary:        disables the many OCaml compiler warnings having to do with something being used

License:        MIT
URL:            https://github.com/janestreet/ppx_disable_unused_warnings
Source:         %{url}/archive/v%{version}/ppx_disable_unnused_warnings-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-base-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
The @disable_unused_warnings annotation disables the many
OCaml compiler warnings having to do with something being
used (variable, constructor, declaration, open, rec keyword, etc.).

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
