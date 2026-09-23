Name:           ocaml-splittable-random
Version:        0.17.0
Release:        1%{?dist}
Summary:        PRNG that can be split into independent streams

License:        MIT
URL:            https://github.com/janestreet/splittable_random
Source:         %{url}/archive/v%{version}/splittable_random-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-ppx-fields-conv-devel
BuildRequires:  ocaml-ppx-assert-devel
BuildRequires:  ocaml-ppx-bench-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

A splittable pseudo-random number generator (SPRNG)
functions like a PRNG in that it can be used as a stream
of random values; it can also be "split" to produce a
second, independent stream of random values.

This library implements a splittable pseudo-random number
generator that sacrifices cryptographic-quality
randomness in favor of performance.

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
