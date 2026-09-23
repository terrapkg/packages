Name:           ocaml-base-bigstring
Version:        0.17.0
Release:        1%{?dist}
Summary:        String type based on [Bigarray], for use in I/O and C-bindings

License:        MIT
URL:            https://github.com/janestreet/base_bigstring
Source:         %{url}/archive/v%{version}/base_bigstring-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-jst-config-devel
BuildRequires:  ocaml-int-repr
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
