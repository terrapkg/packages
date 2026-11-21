%global pkg_name ghcjs-dom-jsaddle
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%bcond tests 1

Name:           ghc-%{pkg_name}
Version:        0.10.0.0
Release:        1%{?dist}
Summary:        DOM library that supports both GHCJS and GHC using jsaddle

License:        MIT
URL:            https://hackage.haskell.org/package/ghcjs-dom-jsaddle
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-jsaddle-dom-devel
# End cabal-rpm deps

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Document Object Model (DOM) functions that work with GHCJS, but can also be
used with GHC and a Browser.


%package devel
Summary:        Haskell %{pkg_name} library development files
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif

%description devel
This package provides the Haskell %{pkg_name} library development
files.


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build_without_haddock
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install -m
mv %{buildroot}%{_ghcdocdir}{,-devel}
# End cabal-rpm install

%check
%if %{with tests}
%cabal_test
%endif

%files devel -f %{name}-devel.files
%license LICENSE


%changelog
* Wed Nov 18 2026 Cypress Reed <cypress@fyralabs.com>
- initial package
