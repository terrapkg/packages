Name:           ocaml-ppx-log
Version:        0.17.0
Release:        1%{?dist}
Summary:        Extension nodes for lazily rendering log messages

License:        MIT
URL:            https://github.com/janestreet/ppx_log
Source:         %{url}/archive/v%{version}/ppx_log-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-ppx-expect-devel
BuildRequires:  ocaml-ppx-fields-conv-devel
BuildRequires:  ocaml-ppx-sexp-value-devel
BuildRequires:  ocaml-ppx-sexp-message-devel
BuildRequires:  ocaml-ppx-variants-conv-devel
BuildRequires:  ocaml-ppx-let-devel
BuildRequires:  ocaml-ppx-string-devel

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
* Tue Sep 22 2026 Owen Zimmerman <owen@fyralabs.com> - 0.17.0-1
- Initial commit
