%global pkg_name patch
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

# hedgehog isn't packaged
%bcond tests 0

Name:           ghc-%{pkg_name}
Version:        0.0.8.4
Release:        1%{?dist}
Summary:        Data structures for describing changes to other data structures

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/patch
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-commutative-semigroups-devel
BuildRequires:  ghc-constraints-extras-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-dependent-map-devel
BuildRequires:  ghc-dependent-sum-devel
BuildRequires:  ghc-indexed-traversable-devel
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-monoidal-containers-devel
BuildRequires:  ghc-semialign-devel
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-these-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-witherable-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-commutative-semigroups-prof
BuildRequires:  ghc-constraints-extras-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-dependent-map-prof
BuildRequires:  ghc-dependent-sum-prof
BuildRequires:  ghc-indexed-traversable-prof
BuildRequires:  ghc-lens-prof
BuildRequires:  ghc-monoidal-containers-prof
BuildRequires:  ghc-semialign-prof
BuildRequires:  ghc-semigroupoids-prof
BuildRequires:  ghc-these-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-witherable-prof
%endif
# End cabal-rpm deps
%if %{with tests}
BuildRequires:  ghc-hedgehog-devel
BuildRequires:  ghc-HUnit-devel
%endif

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Data structures for describing changes to other data structures.

In this library, a patch is something which can be applied, analogous to a
function, and which distinguishes returning the argument it was provided from
returning something else.


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
