%define __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           zoi.prod.beta
Version:        4.3.7
Release:        1%?dist
Summary:        Universal Package Manager & Environment Setup Tool
SourceLicense:  Apache-2.0
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 AND ISC) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CDLA-Permissive-2.0 AND ISC AND LGPL-2.0-or-later AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND MPL-2.0+ AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib
URL:            https://gitlab.com/Zillowe/Zillwen/Zusty/Zoi
Source0:        https://gitlab.com/Zillowe/Zillwen/Zusty/Zoi/-/archive/Prod-Beta-%version/Zoi-Prod-Beta-%version.tar.gz
BuildRequires:  cargo
BuildRequires:  rpm_macro(cargo_install)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
Provides:       zoi = %version
Packager:       madonuko <mado@fyralabs.com>
Requires:       git

%description
Zoi is a universal package manager and environment setup tool, designed to simplify package management and environment configuration across multiple operating systems.

%pkg_completion -befz zoi

%prep
%autosetup -n Zoi-Prod-Beta-%version
%cargo_prep_online

%build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install

# skip powershell
"%buildroot%_bindir/zoi" generate-completions bash | install -Dm644 /dev/stdin %bash_completions_dir/zoi.bash
"%buildroot%_bindir/zoi" generate-completions elvish | install -Dm644 /dev/stdin %elvish_completions_dir/zoi.elv
"%buildroot%_bindir/zoi" generate-completions fish | install -Dm644 /dev/stdin %fish_completions_dir/zoi.fish
"%buildroot%_bindir/zoi" generate-completions zsh | install -Dm644 /dev/stdin %zsh_completions_dir/_zoi

%files
%doc README.md
%license LICENSE
%_bindir/zoi
