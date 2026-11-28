%global pkg_name reflex
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

# these-lens isn't packaged
%bcond tests 0

Name:           ghc-%{pkg_name}
Version:        0.9.4.1
Release:        1%{?dist}
Summary:        Higher-order Functional Reactive Programming

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/reflex
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-MemoTrie-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bifunctors-devel
BuildRequires:  ghc-commutative-semigroups-devel
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-constraints-devel
BuildRequires:  ghc-constraints-extras-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-dependent-map-devel
BuildRequires:  ghc-dependent-sum-devel
BuildRequires:  ghc-exception-transformers-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-haskell-src-exts-devel
BuildRequires:  ghc-haskell-src-meta-devel
BuildRequires:  ghc-mmorph-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-monoidal-containers-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-patch-devel
BuildRequires:  ghc-prim-uniq-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-ref-tf-devel
BuildRequires:  ghc-reflection-devel
BuildRequires:  ghc-semialign-devel
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-these-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unbounded-delays-devel
BuildRequires:  ghc-witherable-devel
%if %{with ghc_prof}
BuildRequires:  ghc-MemoTrie-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bifunctors-prof
BuildRequires:  ghc-commutative-semigroups-prof
BuildRequires:  ghc-comonad-prof
BuildRequires:  ghc-constraints-prof
BuildRequires:  ghc-constraints-extras-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-dependent-map-prof
BuildRequires:  ghc-dependent-sum-prof
BuildRequires:  ghc-exception-transformers-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-haskell-src-exts-prof
BuildRequires:  ghc-haskell-src-meta-prof
BuildRequires:  ghc-mmorph-prof
BuildRequires:  ghc-monad-control-prof
BuildRequires:  ghc-monoidal-containers-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-patch-prof
BuildRequires:  ghc-prim-uniq-prof
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-profunctors-prof
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-ref-tf-prof
BuildRequires:  ghc-reflection-prof
BuildRequires:  ghc-semialign-prof
BuildRequires:  ghc-semigroupoids-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-syb-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-these-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unbounded-delays-prof
BuildRequires:  ghc-witherable-prof
%endif
# End cabal-rpm deps
%if %{with tests}
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-these-lens-devel
BuildRequires:  ghc-hspec-devel
%endif

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Interactive programs without callbacks or side-effects. Functional Reactive
Programming (FRP) uses composable events and time-varying values to describe
interactive systems as pure functions. Just like other pure functional code,
functional reactive code is easier to get right on the first try, maintain, and
reuse.

Reflex is a fully-deterministic, higher-order Functional Reactive Programming
interface and an engine that efficiently implements that interface.

<https://reflex-frp.org>.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem

%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install

%check
%if %{with tests}
%cabal_test
%endif

%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc ChangeLog.md README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Wed Nov 18 2026 Cypress Reed <cypress@fyralabs.com>
- initial package
