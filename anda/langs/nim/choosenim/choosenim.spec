%global nimver %(curl -sSL https://nim-lang.org/channels/stable | xargs)

Name:			choosenim
Version:		0.8.9
Release:		1%?dist
Summary:		Easily install and manage multiple versions of the Nim programming language
License:		BSD-3-Clause
URL:			https://github.com/nim-lang/choosenim
Source1:		https://nim-lang.org/download/nim-%nimver-linux_x64.tar.xz
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	nim git curl tar anda-srpm-macros

%description
choosenim installs the Nim programming language from official downloads and
sources, enabling you to easily switch between stable and development compilers.

%prep
%git_clone %url v%version
tar -xvJf %SOURCE1

%build
NIMPATH=`pwd`/nim-%nimver/bin
PATH=$PATH:$NIMPATH
# compile choosenim
ls -lah
nimble install --path=$NIMPATH -y
%nim_c --path:$NIMPATH
#nimble build --path:$NIMPATH -d:release

%install
install -Dm755 src/choosenim %buildroot%_bindir/choosenim


%files
%doc readme.md
%license LICENSE
%_bindir/choosenim

%changelog
%autochangelog
