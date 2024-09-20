%global csrc_commit 561b417c65791cd8356b5f73620914ceff845d10
%global commit 755307be61e4ee7b32c8354b2c303d04bdfc3a3e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 2.1.99
%global commit_date 20240920
%global debug_package %nil

Name:			nim-nightly
Version:		%ver^%commit_date.%shortcommit
Release:		1%?dist
Summary:		Imperative, multi-paradigm, compiled programming language
License:		MIT and BSD
URL:			https://nim-lang.org
Source0:		https://github.com/nim-lang/Nim/archive/%commit.tar.gz
Source1:		nim.1
Source2:		nimgrep.1
Source3:		nimble.1
Source4:		nimsuggest.1
BuildRequires:	gcc mold git gcc-c++ nodejs openssl-devel pkgconfig(bash-completion) gc-devel pcre pcre-devel
Requires:		redhat-rpm-config gcc
Conflicts:		choosenim
# somehow wrong name and never noticed
Provides:		nim-nightly = %version-%release
Obsoletes:		nim-nighlty < 2.1.1^20240404.9e1b170-2


%description
Nim is a compiled, garbage-collected systems programming language with a
design that focuses on efficiency, expressiveness, and elegance (in that
order of priority).


%package tools
Summary:	Tools for Nim programming language
Provides:	nim-nightly-tools = %version-%release
Obsoletes:	nim-nighlty-tools < 2.1.1^20240404.9e1b170-2

%description tools
Nim is a compiled, garbage-collected systems programming language with a
design that focuses on efficiency, expressiveness, and elegance (in that
order of priority).

This package provides various tools, which help Nim programmers.


%ifarch x86_64
%package doc
Summary:	Documentation for Nim programming language
BuildArch:	noarch
Provides:	nim-nightly-doc = %version-%release
Obsoletes:	nim-nighlty-doc < 2.1.1^20240404.9e1b170-2
%description doc
Nim is a compiled, garbage-collected systems programming language with a
design that focuses on efficiency, expressiveness, and elegance (in that
order of priority).

This package provides documentation and reference manual for the language
and its standard library.
%endif


%prep
%autosetup -n Nim-%commit
# hack
cp /usr/bin/mold /usr/bin/ld


%build
export CFLAGS="${CFLAGS} -Ofast"
export CXXFLAGS="${CXXFLAGS} -Ofast"
export FFLAGS="${FFLAGS} -Ofast"
export FCFLAGS="${FCFLAGS} -Ofast"

export PATH="$(pwd):$(pwd)/bin:${PATH}"

. ci/funs.sh
nimBuildCsourcesIfNeeded CFLAGS="${CFLAGS} -Ic_code -w -O3 -fno-strict-aliasing -fPIE" LDFLAGS="-ldl -lm -lrt -pie"

nim c --noNimblePath --skipUserCfg --skipParentCfg --hints:off -d:danger koch.nim
koch boot -d:release -d:nimStrictMode --lib:lib

%ifarch x86_64
koch docs &
%endif
(cd lib; nim c --app:lib -d:danger -d:createNimRtl -t:-fPIE -l:-pie nimrtl.nim) &
koch tools --skipUserCfg --skipParentCfg --hints:off -d:release -t:-fPIE -l:-pie &
nim c -d:danger -t:-fPIE -l:-pie nimsuggest/nimsuggest.nim &
wait

%ifarch x86_64
sed -i '/<link.*fonts.googleapis.com/d' doc/html/*.html
%endif


%install
export PATH="$(pwd):$(pwd)/bin:${PATH}"

# --main:compiler/nim.nim
mold -run bin/nim cc -d:nimCallDepthLimit=10000 -r tools/niminst/niminst --var:version=%ver --var:mingw=none scripts compiler/installer.ini

sh ./install.sh %buildroot/usr/bin

mkdir -p %buildroot/%_bindir %buildroot/%_datadir/bash-completion/completions %buildroot/usr/lib/nim %buildroot%_datadir
install -Dpm755 bin/nim{grep,suggest,pretty} %buildroot/%_bindir
install -Dpm644 tools/nim.bash-completion %buildroot/%_datadir/bash-completion/completions/nim
install -Dpm644 dist/nimble/nimble.bash-completion %buildroot/%_datadir/bash-completion/completions/nimble
install -Dpm644 -t%buildroot/%_mandir/man1 %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4
mv %buildroot%_bindir/nim %buildroot%_datadir/
ln -s %_datadir/nim/bin/nim %buildroot%_bindir/nim

%ifarch x86_64
mkdir -p %buildroot/%_docdir/%name/html || true
cp -a doc/html/*.html %buildroot/%_docdir/%name/html/ || true
cp tools/dochack/dochack.js %buildroot/%_docdir/%name/ || true
%endif

cp -r lib/* %buildroot%_prefix/lib/nim/
cp -a compiler %buildroot%_prefix/lib/nim/
install -Dm644 nim.nimble %buildroot%_prefix/lib/nim/compiler
install -Dm644 config/* -t %buildroot/etc/nim
install -d %buildroot%_includedir || true
cp -a %buildroot%_prefix/lib/nim/lib/*.h %buildroot%_includedir || true
ln -s %_prefix/lib/nim %buildroot%_prefix/lib/nim/lib || true
rm -rf %buildroot/nim || true
rm %buildroot%_bindir/*.bat || true


%files
%license copying.txt dist/nimble/license.txt
%doc doc/readme.txt
%_bindir/nim{,ble}
%_mandir/man1/nim{,ble}.1*
%_datadir/bash-completion/completions/nim{,ble}
%_datadir/nim/
%_prefix/lib/nim/
%_sysconfdir/nim/

%files tools
%license copying.txt
%_bindir/nim{grep,suggest,pretty}
%_mandir/man1/nim{grep,suggest}.1*

%ifarch x86_64
%files doc
%doc %_docdir/%name
%endif

%changelog
%autochangelog
