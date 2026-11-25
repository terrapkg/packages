%global pkg_name rozbir
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%bcond tests 1

Name:           ghc-%{pkg_name}
Version:        0.1.0.1
Release:        1%{?dist}
Summary:        Parse, evaluate, edit and lint RPM spec files

License:        GPL-3.0-or-later
URL:            https://github.com/terrapkg/rozbir
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
%if %{with ghc_prof}
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
%endif
%if %{with tests}
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-QuickCheck-devel
%endif

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
rozbir is a pure Haskell library for RPM spec files. It parses them into a
lossless syntax tree, partially evaluates macros and conditionals without
running any shell or Lua, edits them with minimal diffs, and lints them.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{evr}
Provides:       %{name}-static%{?_isa} = %{evr}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{evr}

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
Requires:       %{name}-devel%{?_isa} = %{evr}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
%autosetup -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install


%check
%if %{with tests}
%cabal_test
%endif


%files -f %{name}.files
%license LICENSE.md


%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE.md
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Wed Nov 25 2026 Cypress Reed <cypress@fyralabs.com> - 0.1.0.0-1
- initial package
