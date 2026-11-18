%global pkg_name jsaddle-webkitgtk
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%bcond tests 1

Name:           ghc-%{pkg_name}
Version:        0.10.0.0
Release:        1%{?dist}
Summary:        Interface for JavaScript that works with GHCJS and GHC

License:        MIT
URL:            https://hackage.haskell.org/package/jsaddle-webkitgtk
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-gi-gio-devel
BuildRequires:  ghc-gi-glib-devel
BuildRequires:  ghc-gi-gtk4-devel
BuildRequires:  ghc-gi-javascriptcore6-devel
BuildRequires:  ghc-gi-webkit-devel
BuildRequires:  ghc-haskell-gi-base-devel
BuildRequires:  ghc-jsaddle-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-unix-devel
%if %{with ghc_prof}
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-gi-gio-prof
BuildRequires:  ghc-gi-glib-prof
BuildRequires:  ghc-gi-gtk4-prof
BuildRequires:  ghc-gi-javascriptcore6-prof
BuildRequires:  ghc-gi-webkit-prof
BuildRequires:  ghc-haskell-gi-base-prof
BuildRequires:  ghc-jsaddle-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-unix-prof
%endif
# End cabal-rpm deps

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Jsaddle backend hosting the app in a GTK4 window containing a WebKitGTK 6.0
WebView (gi-gtk4 / gi-webkit 6.x). The modern replacement for
jsaddle-webkit2gtk (GTK3 / webkit2gtk 4.0, which has been removed from
nixpkgs).


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


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
%doc ChangeLog.md
%{_bindir}/jsaddle-webkitgtk-demo


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
