%global pkg_name kmonad

Name:           %{pkg_name}
Version:        0.4.4
Release:        1%?dist
Summary:        An advanced keyboard manager

License:        MIT
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros

BuildRequires:  ghc-base-prof
BuildRequires:  ghc-cereal-prof
BuildRequires:  ghc-lens-prof
BuildRequires:  ghc-megaparsec-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rio-prof
BuildRequires:  ghc-unliftio-devel

BuildRequires:  systemd-rpm-macros

Packager:       sadlerm <sad_lerm@hotmail.com>

%description
The Onion of Keyboard Management Tools, available on GNU/Linux, Windows, and MacOS!


%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package contains the Haskell %{name} library.


%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Requires:       ghc-compiler = %{ghc_version}
Requires:       ghc-%{name} = %{version}-%{release}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.


%package -n ghc-%{name}-prof
Summary:        Haskell %{name} profiling library
Requires:       ghc-%{name}-devel = %{version}-%{release}
Supplements:    (ghc-%{name}-devel and ghc-prof)

%description -n ghc-%{name}-prof
This package provides the Haskell %{name} profiling library.


%prep
%autosetup

%build
%ghc_lib_build

%install
%ghc_lib_install
install -Dm644 startup/kmonad@.service -t %{buildroot}%{_unitdir}


%files
%license LICENSE
%doc README.md
%doc doc/faq.md doc/quick-reference.md
%{_bindir}/%{name}
%{_unitdir}/%{name}@.service


%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENSE


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc CONTRIBUTING.md
%doc doc/module_structure.md


%files -n ghc-%{name}-prof -f ghc-%{name}-prof.files



%changelog
* Fri Jan 17 2025 sadlerm <sad_lerm@hotmail.com>
- Initial package
