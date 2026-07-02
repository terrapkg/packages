%global csrc_commit 561b417c65791cd8356b5f73620914ceff845d10
%global commit fa4f9c9759fbb9c82021745425c76bc886d8c805
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 2.3.1
%global commit_date 20260702
%global debug_package %nil

Name:			nim-nightly
Version:		%ver^%commit_date.%shortcommit
Release:		1%{?dist}
Summary:		Imperative, multi-paradigm, compiled programming language
License:		MIT and BSD
URL:			https://nim-lang.org
Source0:		https://github.com/nim-lang/Nim/archive/%commit.tar.gz
BuildRequires:	gcc mold git gcc-c++ nodejs openssl-devel pkgconfig(bash-completion) gc-devel help2man
Requires:		redhat-rpm-config gcc
Conflicts:		choosenim
# somehow wrong name and never noticed
Obsoletes:		nim-nighlty < 2.1.1^20240404.9e1b170-2
Conflicts:		nim
Recommends:		nim-nightly-tools nimble


%description
Nim is a compiled, garbage-collected systems programming language with a
design that focuses on efficiency, expressiveness, and elegance (in that
order of priority).


%package tools
Summary:	Tools for Nim programming language
Provides:	nim-nightly-tools = %version-%release
Obsoletes:	nim-nighlty-tools < 2.1.1^20240404.9e1b170-2
Conflicts:	nim-tools

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

%pkg_completion -Bz nim nimble
%pkg_completion -Bn nimgrep
%pkg_completion -Bn nimpretty
%pkg_completion -Bn nimsuggest

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
./koch docs --skipUserCfg --skipParentCfg --hints:off &
%endif
(cd lib; nim c --app:lib -d:danger -d:createNimRtl -t:-fPIE -l:-pie nimrtl.nim) &
koch tools --skipUserCfg --skipParentCfg --hints:off -d:release -t:-fPIE -l:-pie &
wait

# generate install.sh
./koch distrohelper

%install
export PATH="$(pwd):$(pwd)/bin:${PATH}"

# --main:compiler/nim.nim
mold -run bin/nim cc -d:nimCallDepthLimit=10000 -r tools/niminst/niminst --var:version=%ver --var:mingw=none scripts compiler/installer.ini

sh ./install.sh %buildroot/usr/bin

# generate man pages
h2m_args=(
  --section=1
  --no-info
  --version-string=%version
)
help2man --name='Nim Language Compiler' "${h2m_args[@]}" -o nim.1 ./bin/nim
help2man --name='Nimsuggest' "${h2m_args[@]}" -o nimsuggest.1 ./bin/nimsuggest
#help2man --name='Nimgrep' "${h2m_args[@]}" -o nimgrep.1 ./bin/nimgrep
help2man --name='Nimpretty' "${h2m_args[@]}" -o nimpretty.1 ./bin/nimpretty
help2man --name='Nim Package Installer' "${h2m_args[@]}" -o nimble.1 ./bin/nimble
help2man --name='Atlas' "${h2m_args[@]}" -o atlas.1 ./bin/atlas

mkdir -p %buildroot/%_bindir %buildroot/%_datadir/bash-completion/completions %buildroot/usr/lib/nim %buildroot%_datadir
install -Dpm755 bin/nim{grep,suggest,pretty} bin/atlas %buildroot/%_bindir
install -Dpm644 tools/nim.bash-completion %buildroot%bash_completions_dir/nim
install -Dpm644 tools/nim.zsh-completion %buildroot%zsh_completions_dir/_nim
for comp in {tools,dist/nimble}/*.bash-completion; do
  install -Dm 644 ${comp} "%buildroot%bash_completions_dir/$(basename "${comp/.bash-completion}")"
done
for comp in {tools,dist/nimble}/*.zsh-completion; do
  install -Dm 644 ${comp} "%buildroot%zsh_completions_dir/_$(basename "${comp/.zsh-completion}")"
done
install -Dpm644 -t%buildroot/%_mandir/man1 *.1
mv %buildroot%_bindir/nim %buildroot%_datadir/
ln -s %_datadir/nim/bin/nim %buildroot%_bindir/nim

%ifarch x86_64
mkdir -p %buildroot/%_docdir/%name/html || true
cp -a doc/html/*.html %buildroot/%_docdir/%name/html/ || true
find "%buildroot%_docdir/%name" -name '*.idx' -delete

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

cp -r dist %buildroot%_prefix/lib/nim/
# cannot use `ln` here, possibly a nim bug
cp -r %buildroot%_prefix/lib/nim/dist %buildroot%_datadir/nim/


%files
%license copying.txt dist/nimble/license.txt
%doc doc/readme.txt
%_bindir/nim
%_mandir/man1/nim{,ble}.1.*
%_datadir/nim/
%_prefix/lib/nim/
%_sysconfdir/nim/

%files tools
%license copying.txt
%_bindir/atlas
%_bindir/nim{grep,suggest,pretty}
%_mandir/man1/{atlas,nimsuggest,nimpretty}.1*

%ifarch x86_64
%files doc
%doc %_docdir/%name
%endif

%changelog
* Wed May 27 2026 madonuko <mado@fyralabs.com> - 2.3.1^20260522.561b417
- more manfiles
- no more nimgrep manfile (cannot generate)
- no longer dep on pcre
