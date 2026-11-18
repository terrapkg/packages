%global pkg_name lsp-types
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

# hspec-golden isn't packaged
%bcond tests 0

Name:           ghc-%{pkg_name}
Version:        2.3.0.1
Release:        1%{?dist}
Summary:        Haskell library for the Microsoft Language Server Protocol, data types

License:        MIT
URL:            https://hackage.haskell.org/package/lsp-types
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-generic-arbitrary-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-indexed-traversable-devel
BuildRequires:  ghc-indexed-traversable-instances-devel
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-mod-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-prettyprinter-devel
BuildRequires:  ghc-quickcheck-instances-devel
BuildRequires:  ghc-regex-devel
BuildRequires:  ghc-row-types-devel
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-some-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-witherable-devel
%if %{with ghc_prof}
BuildRequires:  ghc-Diff-prof
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-dlist-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-file-embed-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-generic-arbitrary-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-indexed-traversable-prof
BuildRequires:  ghc-indexed-traversable-instances-prof
BuildRequires:  ghc-lens-prof
BuildRequires:  ghc-mod-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-prettyprinter-prof
BuildRequires:  ghc-quickcheck-instances-prof
BuildRequires:  ghc-regex-prof
BuildRequires:  ghc-row-types-prof
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-some-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-witherable-prof
%endif
# End cabal-rpm deps
%if %{with tests}
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-golden-devel
%endif

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
An implementation of the types to allow language implementors to support the
Language Server Protocol for their specific language.


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
%{_bindir}/generator


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
