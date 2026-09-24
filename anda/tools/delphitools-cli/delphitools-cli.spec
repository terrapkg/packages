Name:           delphitools-cli
Version:        0.2.0
Release:        1%{?dist}
Summary:        indie toolkit for designers — colour, image, PDF, type, calc, all in one offline CLI
URL:            https://delphi.tools/
Source0:        https://github.com/1612elphi/delphitools-cli/archive/refs/tags/v%{version}.tar.gz
SourceLicense:  0BSD
License:        %{sourcelicense} AND ((MIT OR Apache-2.0) AND NCSA) AND (Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (CC0-1.0 OR Apache-2.0) AND (BSD-3-Clause OR Apache-2.0) AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)

BuildRequires:  rust
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(openssl)
BuildRequires:  gcc-c++

Packager:       Its-J <jonah@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm 755 target/release/delphi %{buildroot}%{_bindir}/delphi
install -Dm 755 target/release/delphitools %{buildroot}%{_bindir}/delphitools
install -Dm 755 target/release/dt %{buildroot}%{_bindir}/dt
install -Dm 644 man/*.1 -t %{buildroot}%{_mandir}/man1/
%{cargo_license_online} > LICENSE.dependencies

%files
%{_bindir}/delphi
%{_bindir}/delphitools
%{_bindir}/dt
%{_mandir}/man1/delphi*.1.*
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Wed Jun 03 2026 Its-J <jonah@fyralabs.com>
- Package delphitools-cli
