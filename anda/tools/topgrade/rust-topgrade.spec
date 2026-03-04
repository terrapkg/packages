%global __brp_mangle_shebangs %{nil}
%global crate topgrade

Name:           rust-topgrade
# renovate: datasource=github-releases depName=topgrade-rs/topgrade
Version:        16.9.0
Release:        1%?dist
Summary:        Upgrade all the things

SourceLicense:  GPL-3.0-or-later
License:        ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND GPL-3.0 AND GPL-3.0-only AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://crates.io/crates/topgrade
Source:         %crates_source
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          topgrade-fix-metadata-auto.diff

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rpm_macro(cargo_install)
BuildRequires:  anda-srpm-macros mold

%global _description %{expand:
Keeping your system up to date usually involves invoking multiple package managers.
This results in big, non-portable shell one-liners saved in your shell.
To remedy this, Topgrade detects which tools you use and
runs the appropriate commands to update them.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc BREAKINGCHANGES.md
%doc CHANGELOG.md
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%doc RELEASE_PROCEDURE.md
%doc SECURITY.md
%{_bindir}/topgrade

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

%build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install

%changelog
* Tue Jul 02 2024 Andrey Brusnik <dev@shdwchn.io> - 15.0.0-1
- chore(topgrade): Bump to 15.0.0

* Tue Jun 18 2024 Andrey Brusnik <dev@shdwchn.io> - 14.0.1-1
- feat: Added topgrade package
