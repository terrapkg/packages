# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global choice choice-0.2.4.2
%global thenv th-env-0.1.1
%global cabalsyntax Cabal-syntax-3.14.2.0

%global subpkgs %{choice} %{thenv} %{cabalsyntax}

Name:           fourmolu
Version:        0.19.0.1
Release:        1%{?dist}
Summary:        A formatter for Haskell source code

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/fourmolu
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{choice}/%{choice}.tar.gz
Source2:        https://hackage.haskell.org/package/%{thenv}/%{thenv}.tar.gz
Source3:        https://hackage.haskell.org/package/%{cabalsyntax}/%{cabalsyntax}.tar.gz
Source4:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}.cabal#/%{name}-%{version}.cabal

BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-MemoTrie-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-ghc-lib-parser-devel
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-terminal-size-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-unliftio-devel
BuildRequires:  ghc-yaml-devel
# th-env
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-th-compat-devel
# Cabal-syntax
BuildRequires:  alex
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  help2man

Provides:       bundled(ghc-choice) = 0.2.4.2
Provides:       bundled(ghc-th-env) = 0.1.1
Provides:       bundled(ghc-Cabal-syntax) = 3.14.2.0

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Fourmolu is a formatter for Haskell source code. It is a fork of Ormolu that
allows configuring its formatting style.

%pkg_completion -Bfz

%prep
%setup -q -a1 -a2 -a3
cp -p %{SOURCE4} %{name}.cabal

%build
%ghc_libs_build -P -H %{subpkgs}
%ghc_bin_build

%install
%ghc_bin_install

mkdir -p %{buildroot}{%{bash_completions_dir},%{fish_completions_dir},%{zsh_completions_dir}}
%{buildroot}%{_bindir}/%{name} --bash-completion-script %{name} | sed s/filenames/default/ > %{buildroot}%{bash_completions_dir}/%{name}
%{buildroot}%{_bindir}/%{name} --fish-completion-script %{name} > %{buildroot}%{fish_completions_dir}/%{name}.fish
%{buildroot}%{_bindir}/%{name} --zsh-completion-script %{name} | sed s/filenames/default/ > %{buildroot}%{zsh_completions_dir}/_%{name}

mkdir -p %{buildroot}%{_mandir}/man1/
help2man --no-info %{buildroot}%{_bindir}/%{name} > %{buildroot}%{_mandir}/man1/%{name}.1

rm -r %{buildroot}%{ghclibdir}/lib

mkdir -p licenses/{th-env,Cabal-syntax}
cp -p %{thenv}/LICENSE licenses/th-env
cp -p %{cabalsyntax}/LICENSE licenses/Cabal-syntax

%files
%license LICENSE.md licenses/{th-env,Cabal-syntax}
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Nov 18 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
