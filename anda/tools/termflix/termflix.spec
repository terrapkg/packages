Name:           termflix
Version:        0.4.2
Release:        1%?dist
Summary:        Terminal animation player with 43 procedurally generated animations, multiple render modes, and true color support

License:        MIT AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND MPL-2.0
URL:            https://github.com/paulrobello/termflix
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm 755 target/rpm/%{name} -t %{buildroot}%{_bindir}

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/%{name}

%changelog
* Thu Feb 26 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
