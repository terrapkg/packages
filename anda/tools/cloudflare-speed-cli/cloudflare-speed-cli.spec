%define debug_package %{nil}

Name:           cloudflare-speed-cli
Version:        0.6.5
Release:        1%?dist
Summary:        CLI for internet speed test via cloudflare

License:        GPL-3.0-or-later AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND ISC AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-3-Clause AND MIT) AND (BSD-3-Clause OR Apache-2.0) AND (BSD-3-Clause OR MIT) AND BSD-3-Clause AND BSL-1.0 AND CDLA-Permissive-2.0 AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR BSD-3-Clause) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND Zlib
URL:            https://github.com/kavehtehrani/cloudflare-speed-cli
Source0:        %url/archive/refs/tags/v%version.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  mold

%description
%summary.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm 755 target/rpm/%{name} -t %{buildroot}%{_bindir}

%files
%license LICENSE LICENSE.dependencies
%doc README.md
%{_bindir}/%{name}

%changelog
* Tue Jan 13 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
