%global pkg_name monoidal-containers
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

Name:           ghc-%{pkg_name}
Version:        0.6.8.0
Release:        1%{?dist}
Summary:        Containers with monoidal accumulation

%bcond tests 1

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/monoidal-containers
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-newtype-devel
BuildRequires:  ghc-semialign-devel
BuildRequires:  ghc-these-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-witherable-devel
%if %{with ghc_prof}
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-lens-prof
BuildRequires:  ghc-newtype-prof
BuildRequires:  ghc-semialign-prof
BuildRequires:  ghc-these-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-witherable-prof
%endif
# End cabal-rpm deps

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Containers with merging via monoidal accumulation. The 'Monoid' instances
provided by the 'containers' and 'unordered-containers' packages merge
structures in a left-biased manner instead of using the underlying monoidal
structure of the value.

This package wraps the types provided by these packages, but provides 'Monoid'
instances implemented in terms of the value type's 'mappend'. For instance, the
'Monoid' 'Map' instance looks like,

' instance (Ord k, Semigroup a) => Monoid (MonoidalMap k a) '.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem

%description doc
This package provides the Haskell %{pkg_name} library
documentation.
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
%doc Changelog.md


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
