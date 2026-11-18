%global pkg_name mod
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

# quickcheck-classes and quickcheck-classes-base aren't packaged (yet)
%bcond tests 0

Name:           ghc-%{pkg_name}
Version:        0.2.2.0
Release:        1%{?dist}
Summary:        Fast type-safe modular arithmetic

License:        MIT
URL:            https://hackage.haskell.org/package/mod
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-ghc-bignum-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-semirings-devel
BuildRequires:  ghc-vector-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-ghc-bignum-prof
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-semirings-prof
BuildRequires:  ghc-vector-prof
%endif
# End cabal-rpm deps
%if %{with tests}
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-quickcheck-classes-devel
BuildRequires:  ghc-quickcheck-classes-base-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-vector-devel
%endif

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
<https://en.wikipedia.org/wiki/Modular_arithmetic Modular arithmetic>,
promoting moduli to the type level, with an emphasis on performance.
Originally part of the <https://hackage.haskell.org/package/arithmoi arithmoi>
package.


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
%doc README.md changelog.md


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
