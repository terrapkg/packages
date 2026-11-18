%global pkg_name generic-lens
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

# ghc-inspection-testing doesn't exist (yet)
%bcond tests 0

Name:           ghc-%{pkg_name}
Version:        2.2.2.0
Release:        1%{?dist}
Summary:        Generically derive traversals, lenses and prisms

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/generic-lens
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-generic-lens-core-devel
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-text-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-generic-lens-core-prof
BuildRequires:  ghc-profunctors-prof
BuildRequires:  ghc-text-prof
%endif
# End cabal-rpm deps
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-inspection-testing-devel
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-doctest-devel
%endif

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
This library uses GHC.Generics to derive efficient optics (traversals, lenses
and prisms) for algebraic data types in a type-directed way, with a focus on
good type inference and error messages when possible.

The library exposes a van Laarhoven interface. For an alternative interface,
supporting an opaque optic type, see
'<https://hackage.haskell.org/package/generic-optics generic-optics>'.


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
cp -bp %{SOURCE1} %{pkg_name}.cabal
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
%doc ChangeLog.md examples


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
