%global pkg_name tasty-discover
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%bcond tests 1

Name:           ghc-%{pkg_name}
Version:        5.0.2
Release:        1%{?dist}
Summary:        Test discovery for the tasty framework

License:        MIT
URL:            https://hackage.haskell.org/package/tasty-discover
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-tasty-devel
%if %{with ghc_prof}
BuildRequires:  ghc-Glob-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-tasty-prof
%endif
# End cabal-rpm deps
%if %{with tests}
BuildRequires: ghc-bytestring-devel
BuildRequires: ghc-tasty-golden-devel
BuildRequires: ghc-hedgehog-devel
BuildRequires: ghc-hspec-devel
BuildRequires: ghc-hspec-core-devel
BuildRequires: ghc-tasty-devel
BuildRequires: ghc-tasty-hedgehog-devel
BuildRequires: ghc-tasty-hspec-devel
BuildRequires: ghc-tasty-hunit-devel
BuildRequires: ghc-tasty-quickcheck-devel
BuildRequires: ghc-tasty-smallcheck-devel
%endif

Packager:      Cypress Reed <cypress@fyralabs.com>

%description
Automatic test discovery and runner for the tasty framework. Prefix your test
case names and tasty-discover will discover, collect and run them. All popular
test libraries are covered. Configure once and then just write your tests.
Avoid forgetting to add test modules to your Cabal/Hpack files. Tasty
ingredients are included along with various configuration options for different
use cases. Please see the `README.md` below for how to get started.


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
%if %{with tests}
sed -i -E 's/^(common +tasty-quickcheck.*>= *[0-9.]+) *&& *< *[0-9.]+/\1/' %{pkg_name}.cabal
%endif


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
%doc CHANGELOG.md README.md
%{_bindir}/%{pkg_name}


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
