%global nimver %(curl -sSL https://nim-lang.org/channels/stable | xargs)

Name:			choosenim
Version:		0.8.9
Release:		1%?dist
Summary:		Easily install and manage multiple versions of the Nim programming language
License:		BSD-3-Clause
URL:			https://github.com/nim-lang/choosenim
Source0:        %url/archive/refs/tags/v%version.tar.gz
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	nim nim-tools git-core anda-srpm-macros

%description
choosenim installs the Nim programming language from official downloads and
sources, enabling you to easily switch between stable and development compilers.

%prep
%autosetup

%build
%nim_c src/choosenim

%install
install -Dm755 src/choosenim %buildroot%_bindir/choosenim


%files
%doc readme.md
%license LICENSE
%_bindir/choosenim

%changelog
%autochangelog
