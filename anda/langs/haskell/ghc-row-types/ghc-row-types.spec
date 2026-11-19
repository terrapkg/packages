%global pkg_name row-types
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%bcond tests 1

Name:           ghc-%{pkg_name}
Version:        1.0.1.2
Release:        1%{?dist}
Summary:        Open Records and Variants

License:        MIT
URL:            https://hackage.haskell.org/package/row-types
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-constraints-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-generic-lens-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-unordered-containers-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-constraints-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-generic-lens-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-profunctors-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-unordered-containers-prof
%endif
# End cabal-rpm deps

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
This package uses closed type families and type literals to implement open
records and variants. The core is based off of the
<https://hackage.haskell.org/package/CTRex CTRex> package, but it also includes
polymorphic variants and a number of additional functions. That said, it is not
a proper superset of CTRex as it specifically forbids records from having more
than one element of the same label.


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
%doc CHANGELOG.md README.md examples


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
