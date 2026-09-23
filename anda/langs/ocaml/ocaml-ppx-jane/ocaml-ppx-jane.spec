Name:           ocaml-ppx-jane
Version:        0.17.0
Release:        1%{?dist}
Summary:        ppx rewriter that inlines the reverse application operator

License:        MIT
URL:            https://github.com/janestreet/ppx_jane
Source:         %{url}/archive/v%{version}/ppx_jane-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-ppx-fields-conv-devel
BuildRequires:  ocaml-ppx-custom-printf-devel
BuildRequires:  ocaml-ppx-ignore-instrumentation-devel
BuildRequires:  ocaml-ppx-variants-conv-devel
BuildRequires:  ocaml-ppx-string-conv-devel
BuildRequires:  ocaml-ppx-stable-devel
BuildRequires:  ocaml-ppx-typerep-conv-devel

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
