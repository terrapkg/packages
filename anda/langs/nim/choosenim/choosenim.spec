Name:			choosenim
Version:		0.8.5
Release:		1%?dist
Summary:		Easily install and manage multiple versions of the Nim programming language
License:		BSD-3-Clause
URL:			https://github.com/dom96/choosenim
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildRequires:	nim git

%description
choosenim installs the Nim programming language from official downloads and
sources, enabling you to easily switch between stable and development compilers.

%prep
%autosetup

%build
nimble setup -y
nim c -t:-fPIE -l:-pie -d:release -t:"$CFLAGS" -l:"$LDFLAGS" src/choosenim

%install
install -Dm755 src/choosenim %buildroot%_bindir/choosenim


%files
%doc readme.md
%license LICENSE
%_bindir/choosenim

%changelog
%autochangelog
