%global pkg_name dependent-sum
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

Name:           ghc-%{pkg_name}
Version:        0.7.2.0
Release:        1%{?dist}
Summary:        Dependent sum type

%bcond tests 1

License:        LicenseRef-PublicDomain
URL:            https://hackage.haskell.org/package/dependent-sum
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-constraints-extras-devel
BuildRequires:  ghc-some-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-constraints-extras-prof
BuildRequires:  ghc-some-prof
%endif
# End cabal-rpm deps

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
A dependent sum is a generalization of a particular way of thinking about the
'Either' type. 'Either a b' can be thought of as a 2-tuple '(tag, value)',
where the value of the tag determines the type of the value. In particular,
either 'tag = Left' and 'value :: a' or 'tag = Right' and 'value :: b'.

This package allows you to define your own dependent sum types by using your
own "tag" types.


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
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc ChangeLog.md examples


%if %{with haddock}
%files doc -f %{name}-doc.files
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Wed Nov 18 2026 Cypress Reed <cypress@fyralabs.com>
- initial package
