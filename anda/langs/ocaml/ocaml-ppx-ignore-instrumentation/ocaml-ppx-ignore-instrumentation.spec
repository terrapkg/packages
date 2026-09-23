Name:           ocaml-ppx-ignore-instrumentation
Version:        0.17.0
Release:        1%{?dist}
Summary:        Ignore Jane Street specific instrumentation extensions from internal PPXs or compiler features not yet upstreamed

License:        MIT
URL:            https://github.com/janestreet/ppx_ignore_instrumentation
Source:         %{url}/archive/v%{version}/ppx_ignore_instrumentation-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-cold-devel
BuildRequires:  ocaml-ppx-compare-devel
BuildRequires:  ocaml-ppx-enumerate-devel
BuildRequires:  ocaml-ppx-globalize-devel
BuildRequires:  ocaml-ppx-hash-devel
BuildRequires:  ocaml-ppx-sexp-conv-devel
BuildRequires:  ocaml-ppxlib-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{evr}
Requires:       ocaml-ppx-cold-devel%{?_isa}
Requires:       ocaml-ppx-compare-devel%{?_isa}
Requires:       ocaml-ppx-enumerate-devel%{?_isa}
Requires:       ocaml-ppx-globalize-devel%{?_isa}
Requires:       ocaml-ppx-hash-devel%{?_isa}
Requires:       ocaml-ppx-sexp-conv-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -C

%files -f .ofiles
%license LICENSE.md
%doc README.md

%files devel -f .ofiles-devel

%changelog
* Tue Sep 22 2026 Owen Zimmerman <owen@fyralabs.com> - 0.17.0-1
- Initial commit
