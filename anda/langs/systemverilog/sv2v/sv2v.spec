Name:           sv2v
Version:        0.0.13.1
Release:        1%{?dist}
Summary:        SystemVerilog to Verilog conversion

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/sv2v
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-cmdargs-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-githash-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  alex
BuildRequires:  happy
# End cabal-rpm deps

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
A tool for coverting SystemVerilog to Verilog. Originally forked from the
Verilog parser found at https://github.com/tomahawkins/verilog.


%prep
# Begin cabal-rpm setup:
%autosetup
# End cabal-rpm setup
for dep in base containers filepath hashable; do
  cabal-tweak-remove-upperbound $dep
done


%build
# Begin cabal-rpm build:
%ghc_bin_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_bin_install
# End cabal-rpm install


%files
# Begin cabal-rpm files:
%license LICENSE
%license NOTICE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
# End cabal-rpm files


%changelog
* Fri Nov 6 2026 Cypress Reed <cypress@fyralabs.com>
- initial package
