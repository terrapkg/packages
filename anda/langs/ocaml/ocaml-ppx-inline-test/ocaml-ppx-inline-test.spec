Name:           ocaml-ppx-inline-test
Version:        0.17.1
Release:        1%{?dist}
Summary:        Syntax extension for writing in-line tests in ocaml code

License:        MIT
URL:            https://github.com/janestreet/ppx_inline_test
Source:         %{url}/archive/v%{version}/ppx_inline_test-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-time-now-devel

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
# Disable check due to known bootstrapping error with this package

%files -f .ofiles
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Tue Sep 22 2026 Owen Zimmerman <owen@fyralabs.com> - 0.17.1-1
- Initial commit
