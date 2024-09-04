%global nimver %(curl -sSL https://nim-lang.org/channels/stable | xargs)

Name:			choosenim
Version:		0.8.5
Release:		1%?dist
Summary:		Easily install and manage multiple versions of the Nim programming language
License:		BSD-3-Clause
URL:			https://github.com/nim-lang/choosenim
Source0:		%url/archive/refs/tags/v%version.tar.gz
Source1:		https://nim-lang.org/download/nim-%nimver-linux_x64.tar.xz
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	nim git

%description
choosenim installs the Nim programming language from official downloads and
sources, enabling you to easily switch between stable and development compilers.

%prep
%autosetup
tar xf %SOURCE1


%build
nimble setup -y
nimble c -t:-fPIE -l:-pie -d:release -t:"$CFLAGS" -l:"$LDFLAGS" src/choosenim --path:nim-%nimver/bin


%install
install -Dm755 src/choosenim %buildroot%_bindir/choosenim


%files
%doc readme.md
%license LICENSE
%_bindir/choosenim

%changelog
%autochangelog
