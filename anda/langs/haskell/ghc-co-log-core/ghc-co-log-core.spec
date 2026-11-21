%global pkg_name co-log-core
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%bcond tests 1

Name:           ghc-%{pkg_name}
Version:        0.3.2.7
Release:        1%{?dist}
Summary:        Composable Contravariant Comonadic Logging Library

License:        MPL-2.0
URL:            https://hackage.haskell.org/package/co-log-core
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
%endif
# End cabal-rpm deps
%if %{with tests}
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-doctest-devel
%endif

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
This package provides core types and functions to work with the 'LogAction'
data type which is both simple and powerful.

' __newtype__ LogAction m msg = LogAction { unLogAction :: msg -> m () } '

The ideas behind this package are described in the following blog post:

* [co-log: Composable Contravariant Combinatorial Comonadic Configurable
Convenient Logging](https://kowainik.github.io/posts/2018-09-25-co-log)

See the following packages for different implementations based on
'co-log-core':

* [co-log](http://hackage.haskell.org/package/co-log): taggless final
implementations. *
[co-log-polysemy](http://hackage.haskell.org/package/co-log-polysemy):
extensible effects implementation based on 'polysemy'.


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
%doc CHANGELOG.md README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Fri Nov 20 2026 Cypress Reed <cypress@fyralabs.com>
- initial package
