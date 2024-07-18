%global csrc_commit 561b417c65791cd8356b5f73620914ceff845d10
%global debug_package %{nil}

Name:			nim
Version:		2.0.10
Release:		1%?dist
Summary:		Imperative, multi-paradigm, compiled programming language
License:		MIT and BSD
URL:			https://nim-lang.org
Source0:		https://nim-lang.org/download/nim-%{version}-linux_x64.tar.xz
Source1:		nim.1
Source2:		nimgrep.1
Source3:		nimble.1
Source4:		nimsuggest.1
BuildRequires:	gcc mold git gcc-c++ nodejs openssl-devel pkgconfig(bash-completion) gc-devel pcre-devel
Requires:		gcc


%description
Nim is a compiled, garbage-collected systems programming language with a
design that focuses on efficiency, expressiveness, and elegance (in that
order of priority).


%package tools
Summary:	Tools for Nim programming language
%description tools
Nim is a compiled, garbage-collected systems programming language with a
design that focuses on efficiency, expressiveness, and elegance (in that
order of priority).

This package provides various tools, which help Nim programmers.

%ifarch x86_64
%package doc
Summary:	Documentation for Nim programming language
BuildArch:	noarch
%description doc
Nim is a compiled, garbage-collected systems programming language with a
design that focuses on efficiency, expressiveness, and elegance (in that
order of priority).

This package provides documentation and reference manual for the language
and its standard library.
%endif


%prep
%autosetup -n nim-%{version}


%build
export CFLAGS="${CFLAGS} -Ofast"
export CXXFLAGS="${CXXFLAGS} -Ofast"
export FFLAGS="${FFLAGS} -Ofast"
export FCFLAGS="${FCFLAGS} -Ofast"

export PATH="$(pwd):$(pwd)/bin:${PATH}"

mold -run nim c -d:danger koch.nim
mold -run koch boot -d:useLinenoise -t:-fPIE -l:-pie -d:release -d:nativeStacktrace -d:useGnuReadline

%ifarch x86_64
mold -run koch docs &
%endif
(cd lib && nim c --app:lib -d:createNimRtl -d:release nimrtl.nim) &
mold -run koch tools -t:-fPIE -l:-pie &
mold -run nim c -t:-fPIE -l:-pie -d:release nimsuggest/nimsuggest.nim &
wait

%ifarch x86_64
sed -i '/<link.*fonts.googleapis.com/d' doc/html/*.html
%endif


%install
export PATH="$(pwd):$(pwd)/bin:${PATH}"
sh install.sh %{buildroot}usr/bin

mkdir -p %buildroot{%_bindir,%_prefix/lib/nim}
install -Dp -m755 bin/nim{,ble,grep,suggest,pretty} %buildroot/%_bindir
install -Dp -m644 dist/nimble/nimble.bash-completion %{buildroot}%{bashcompdir}/nimble
install -Dp -m644 -t%{buildroot}%{_mandir}/man1 %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4
# completions
for comp in tools/*.bash-completion; do
	install -Dm644 $comp %bashcompdir/$(basename "${comp/.bash-completion}")
done
for comp in tools/*.zsh-completion; do
	install -Dm644 $comp %zshcompdir/_$(basename "${comp/.zsh-completion}")
done

%ifarch x86_64
mkdir -p %buildroot%_docdir/%name/html
cp -a doc/html/*.html %buildroot%_docdir/%name/html/
cp tools/dochack/dochack.js %{buildroot}%{_docdir}/%{name}/
ln -s %_datadir/nim/doc %buildroot%_prefix/lib/nim/doc
%endif

cp -a lib %buildroot%_prefix/lib/
mv %buildroot%_prefix/lib/{lib,nim}
cp -a compiler %buildroot%_prefix/lib/nim
install -Dm644 nim.nimble %buildroot%_prefix/lib/nim/compiler
install -m755 lib/libnimrtl.so %buildroot%_prefix/lib/libnimrtl.so  # compiler needs
install -Dm644 config/* -t %buildroot/etc/nim
install -Dm755 bin/* -t %buildroot%_bindir
install -d %buildroot%_includedir
cp -a %buildroot%_prefix/lib/nim/lib/*.h %buildroot%_includedir
ln -s %_prefix/lib/nim %buildroot%_prefix/lib/nim/lib  # compiler needs lib from here
ln -s %_prefix/lib/nim/system.nim %_prefix/lib/system.nim  # nimsuggest bug
rm -rf %buildroot/nim || true
rm %buildroot%_bindir/*.bat || true


%files
%license copying.txt dist/nimble/license.txt
%doc doc/readme.txt
/etc/nim/
%_bindir/atlas
%_bindir/nim_dbg
%_bindir/nim-gdb
%_bindir/testament
%_prefix/lib/nim/
%_prefix/lib/libnimrtl.so
%{_bindir}/nim{,ble}
%{_mandir}/man1/nim{,ble}.1*
%_includedir/cycle.h
%_includedir/nimbase.h

%files tools
%license copying.txt
%_prefix/lib/nim/
%{_bindir}/nim{grep,suggest,pretty}
%{_mandir}/man1/nim{grep,suggest}.1*

%ifarch x86_64
%files doc
%doc %{_docdir}/nim
%endif

%changelog
%autochangelog
