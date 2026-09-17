Name:           elm
Version:        0.19.2
Release:        1%?dist
Summary:        A delightful language for reliable webapps
URL:            https://elm-lang.org
Source0:        https://github.com/elm/compiler/archive/refs/tags/%{version}.tar.gz
Patch0:         0001-elm-wl-pprint.patch
License:        BSD-3-Clause

BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-HTTP-devel
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-edit-distance-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-filelock-devel
BuildRequires:  ghc-haskeline-devel
BuildRequires:  ghc-snap-server-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-zip-archive-devel
BuildRequires:  ghc-language-glsl-devel
BuildRequires:  ghc-ansi-wl-pprint-devel

Packager:       Jamie Murphy <hello@itsjamie.dev>

%description
%summary.

%prep
%autosetup -p1 -n compiler-%{version}

%build
%ghc_bin_build

%install
%ghc_bin_install

%files
%{_bindir}/elm
%license LICENSE
%doc README.md

%changelog
* Sun Aug 16 2026 Jamie Murphy <hello@itsjamie.dev> - 0.19.2-1
- Initial Commit
