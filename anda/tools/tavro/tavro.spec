%global __tavro_bin %{buildroot}%{_bindir}/tavro

Name:           tavro
Version:        0.1.0.2
Release:        1%{?dist}
Summary:        Identify SPDX licenses by their text
SourceLicense:  GPL-3.0-or-later AND CC-BY-3.0
License:        (%sourcelicense) AND BSD-2-Clause AND BSD-3-Clause AND GPL-3.0-or-later AND ISC AND MIT
URL:            https://github.com/terrapkg/tavro
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        cabal.project.freeze
Packager:       Cypress Reed <cypress@fyralabs.com>

BuildRequires:  anda-srpm-macros
BuildRequires:  cabal-install
BuildRequires:  ghc%{cabal_ghc_version}
BuildRequires:  jq
BuildRequires:  help2man

%description
tavro tells which SPDX licenses a file is, or has in it, by matching it
against the SPDX license list's templates.

%prep
%autosetup -p1
%cabal_prep_online -f %{SOURCE1}

%build
%cabal_build_online

%install
%cabal_install_bins_online
%cabal_license_online > LICENSE.dependencies
%cabal_license_preamble_online

%{buildroot}%{_bindir}/tavro --bash-completion-script %{_bindir}/tavro > tavro.bash
%{buildroot}%{_bindir}/tavro --zsh-completion-script %{_bindir}/tavro > _tavro
%{buildroot}%{_bindir}/tavro --fish-completion-script %{_bindir}/tavro > tavro.fish
install -Dpm644 tavro.bash %{buildroot}%{bash_completions_dir}/tavro
install -Dpm644 _tavro %{buildroot}%{zsh_completions_dir}/_tavro
install -Dpm644 tavro.fish %{buildroot}%{fish_completions_dir}/tavro.fish

help2man -N -n "%{summary}" %{buildroot}%{_bindir}/tavro -o tavro.1
install -Dpm644 tavro.1 %{buildroot}%{_mandir}/man1/tavro.1

%check
%{buildroot}%{_bindir}/tavro LICENSE data/LICENSE

%files
%license LICENSE data/LICENSE LICENSE.dependencies
%doc README.md CHANGELOG.md
%{_bindir}/tavro
%{_mandir}/man1/tavro.1*

%pkg_completion -Bfz

%changelog
* Fri Nov 27 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
