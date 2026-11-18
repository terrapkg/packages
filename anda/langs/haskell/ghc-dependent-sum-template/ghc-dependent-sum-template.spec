%global pkg_name dependent-sum-template
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%bcond tests 1

Name:           ghc-%{pkg_name}
Version:        0.2.0.2
Release:        1%{?dist}
Summary:        Template Haskell code to generate instances of classes in some package

License:        LicenseRef-PublicDomain
URL:            https://hackage.haskell.org/package/dependent-sum-template
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-some-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-th-abstraction-devel
BuildRequires:  ghc-constraints-extras-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-some-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-th-abstraction-prof
%endif
%if %{with tests}
BuildRequires:  ghc-some-devel
BuildRequires:  ghc-th-abstraction-devel
%endif
# End cabal-rpm deps

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Template Haskell code to generate instances of classes in some package, such as
'GEq' and 'GCompare'.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library
development files.


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
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc ChangeLog.md ReadMe.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Wed Nov 18 2026 Cypress Reed <cypress@fyralabs.com>
- initial commit
