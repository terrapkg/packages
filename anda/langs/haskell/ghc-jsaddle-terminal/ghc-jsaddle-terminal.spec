%global pkg_name jsaddle-terminal
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%bcond tests 1

Name:           ghc-%{pkg_name}
Version:        0.1.0.0
Release:        1%{?dist}
Summary:        Run jsaddle apps in a tmux pane, tunnelling over stdin/stdout

License:        MIT
URL:            https://hackage.haskell.org/package/jsaddle-terminal
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-jsaddle-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-unix-devel
%if %{with ghc_prof}
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-jsaddle-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-unix-prof
%endif
# End cabal-rpm deps

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
A jsaddle transport for executables that run inside a tmux pane. When a
watching IDE (leksah) answers the handshake, jsaddle Batch/Results JSON is
tunnelled over the process's own stdin/stdout — framed as OSC 5799 escape
sequences on stdout (delivered to the IDE via tmux control-mode %output) and
RS-prefixed lines on stdin (injected via tmux send-keys -H) — and the UI
renders in an iframe hosted by the IDE. No sockets are opened on the app's
machine, so it works over ssh-reached tmux servers too. When nobody answers the
handshake there is nothing to tunnel to, so the runner reports that on stderr
and stops (an earlier version fell back to serving the app over jsaddle-warp;
that has been removed).


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
