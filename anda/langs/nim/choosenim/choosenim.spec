Name:			choosenim
Version:		0.8.4
Release:		1%{?dist}
Summary:		Easily install and manage multiple versions of the Nim programming language
License:		BSD-3-Clause
URL:			https://github.com/dom96/choosenim
BuildRequires:	nim git

%description
choosenim installs the Nim programming language from official downloads and
sources, enabling you to easily switch between stable and development compilers.

%prep
git clone https://github.com/dom96/choosenim .
git checkout v%version

%build
nimble setup -y
nim c -t:-fPIE -l:-pie -d:release src/choosenim

%install
install -Dm755 src/choosenim %buildroot%_bindir/choosenim


%files
%doc readme.md
%license LICENSE
%_bindir/choosenim

%changelog
%autochangelog
