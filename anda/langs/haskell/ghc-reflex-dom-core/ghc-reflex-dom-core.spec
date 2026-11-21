%global pkg_name reflex-dom-core
%global commit e57a114c5121b8fecf9eece3ee196d28120e908a
%global commit_date 20261111
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 0.9.0.0
%global pkgver %{pkg_name}-%{ver}
%global cabal_configure_options -f-hydration-tests -f-gc-tests
%{?haskell_setup}

Name:           ghc-%{pkg_name}
Version:        %{ver}^%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Functional Reactive Web Apps with Reflex

License:        BSD-3-Clause
URL:            https://github.com/reflex-frp/reflex-dom
Source0:        https://github.com/ghcjs/reflex-dom/archive/%{commit}/reflex-dom-%{commit}.tar.gz

BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bifunctors-devel
BuildRequires:  ghc-bimap-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-commutative-semigroups-devel
BuildRequires:  ghc-constraints-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-dependent-map-devel
BuildRequires:  ghc-dependent-sum-devel
BuildRequires:  ghc-dependent-sum-template-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-exception-transformers-devel
BuildRequires:  ghc-ghcjs-dom-devel
BuildRequires:  ghc-jsaddle-devel
BuildRequires:  ghc-keycode-devel
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-ref-tf-devel
BuildRequires:  ghc-reflex-devel
BuildRequires:  ghc-semialign-devel
BuildRequires:  ghc-semigroups-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-these-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-zenc-devel
%if %{with ghc_prof}
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bifunctors-prof
BuildRequires:  ghc-bimap-prof
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-commutative-semigroups-prof
BuildRequires:  ghc-constraints-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-contravariant-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-dependent-map-prof
BuildRequires:  ghc-dependent-sum-prof
BuildRequires:  ghc-dependent-sum-template-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-exception-transformers-prof
BuildRequires:  ghc-ghcjs-dom-prof
BuildRequires:  ghc-jsaddle-prof
BuildRequires:  ghc-keycode-prof
BuildRequires:  ghc-lens-prof
BuildRequires:  ghc-monad-control-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-ref-tf-prof
BuildRequires:  ghc-reflex-prof
BuildRequires:  ghc-semialign-prof
BuildRequires:  ghc-semigroups-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-these-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-zenc-prof
%endif

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Reflex-DOM is a functional reactive web framework based on the Reflex FRP
engine. It builds HTML and other Document Object Model (DOM) data with a pure
functional interface, so web applications need no callbacks or side effects.

This is a snapshot of the ghcjs/reflex-dom port to ghcjs-dom 0.10, which is
what Leksah builds against.


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
%autosetup -n reflex-dom-%{commit}/%{pkg_name}


%build
%ghc_lib_build %{pkg_name} %{ver}


%install
%ghc_lib_install %{pkg_name} %{ver}


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc ChangeLog.md


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
