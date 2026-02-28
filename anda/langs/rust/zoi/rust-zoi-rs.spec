%define __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

%global crate zoi-rs
%global crate_version 1.7.0

Name:           rust-zoi-rs
Version:        %(echo %crate_version | sed 's/-/~/g')
Release:        1%?dist
Summary:        Universal Package Manager & Environment Setup Tool
SourceLicense:  Apache-2.0
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 AND ISC) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CDLA-Permissive-2.0 AND ISC AND LGPL-2.0-or-later AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND MPL-2.0+ AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib
URL:            https://crates.io/crates/zoi-rs
Source:         %{crates_source %{crate} %{crate_version}}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          zoi-rs-fix-metadata-auto.diff
BuildRequires:  cargo
BuildRequires:  gcc-c++
BuildRequires:  rpm_macro(cargo_install)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(lib)
BuildRequires:  perl(Time::Piece)
Packager:       madonuko <mado@fyralabs.com>

%global _description %{expand:
Universal Package Manager & Environment Setup Tool.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 AND ISC) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CDLA-Permissive-2.0 AND ISC AND LGPL-2.0-or-later AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND MPL-2.0+ AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib
# LICENSE.dependencies contains a full license breakdown
Provides:       zoi = %evr
Requires:       git

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc CODE_OF_CONDUCT.md
%doc PACKAGING.md
%doc README.md
%doc RELEASE.md
%doc SECURITY.md
%{_bindir}/zoi

%pkg_completion -Befz zoi -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CODE_OF_CONDUCT.md
%doc %{crate_instdir}/PACKAGING.md
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/RELEASE.md
%doc %{crate_instdir}/SECURITY.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{crate_version}
%cargo_prep_online

%build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install

# skip powershell
"%buildroot%_bindir/zoi" generate-completions bash | install -Dm644 /dev/stdin %buildroot%bash_completions_dir/zoi
"%buildroot%_bindir/zoi" generate-completions elvish | install -Dm644 /dev/stdin %buildroot%elvish_completions_dir/zoi.elv
"%buildroot%_bindir/zoi" generate-completions fish | install -Dm644 /dev/stdin %buildroot%fish_completions_dir/zoi.fish
"%buildroot%_bindir/zoi" generate-completions zsh | install -Dm644 /dev/stdin %buildroot%zsh_completions_dir/_zoi
