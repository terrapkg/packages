%global __brp_mangle_shebangs %{nil}
%global crate topgrade

Name:           topgrade
# renovate: datasource=github-releases depName=topgrade-rs/topgrade
Version:        16.0.3
Release:        1%?dist
Summary:        Upgrade all the things

SourceLicense:  GPL-3.0-or-later
License:        ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND GPL-3.0 AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT)
URL:            https://github.com/topgrade-rs/%{name}
Source:         %crates_source
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          topgrade-fix-metadata-auto.diff

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rpm_macro(cargo_install)
BuildRequires:  anda-srpm-macros mold

%description
Keeping your system up to date usually involves invoking multiple package managers.
This results in big, non-portable shell one-liners saved in your shell.
To remedy this, Topgrade detects which tools you use and
runs the appropriate commands to update them.

%global _description %{expand:
Upgrade all the things.}

%package     -n rust-%name-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-%name-devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files       -n rust-%name-devel
%dnl %license %{crate_instdir}/LICENSE
%dnl %doc %{crate_instdir}/BREAKINGCHANGES.md
%dnl %doc %{crate_instdir}/CODE_OF_CONDUCT.md
%dnl %doc %{crate_instdir}/CONTRIBUTING.md
%dnl %doc %{crate_instdir}/README.md
%dnl %doc %{crate_instdir}/RELEASE_PROCEDURE.md
%dnl %doc %{crate_instdir}/SECURITY.md
%{crate_instdir}/

%package     -n rust-%{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-%{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n rust-%{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n rust-%{name}+self-update-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-%{name}+self-update-devel %{_description}

This package contains library source intended for building other packages which
use the "self-update" feature of the "%{crate}" crate.

%files       -n rust-%{name}+self-update-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n rust-%{name}+self_update_crate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-%{name}+self_update_crate-devel %{_description}

This package contains library source intended for building other packages which
use the "self_update_crate" feature of the "%{crate}" crate.

%files       -n rust-%{name}+self_update_crate-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{name}-%{version} -p1
%cargo_prep_online

%build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install

%files
%license LICENSE LICENSE.dependencies
%doc BREAKINGCHANGES.md README.md
%{_bindir}/%{name}

%changelog
* Tue Jul 02 2024 Andrey Brusnik <dev@shdwchn.io> - 15.0.0-1
- chore(topgrade): Bump to 15.0.0

* Tue Jun 18 2024 Andrey Brusnik <dev@shdwchn.io> - 14.0.1-1
- feat: Added topgrade package
