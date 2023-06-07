%global csrc_commit 561b417c65791cd8356b5f73620914ceff845d10
%global commit fcc383d89994241f1b73fe4f85ef38528c135e2e
%global ver 1.9.3
%global debug_package %{nil}

Name:			nim-nighlty
Version:		%ver^%commit
Release:		1%?dist
Summary:		Imperative, multi-paradigm, compiled programming language
License:		MIT and BSD
URL:			https://nim-lang.org
Source0:		https://github.com/nim-lang/Nim/archive/%commit.tar.gz
Source1:		nim.1
Source2:		nimgrep.1
Source3:		nimble.1
Source4:		nimsuggest.1
BuildRequires:	gcc mold git gcc-c++ nodejs openssl-devel pkgconfig(bash-completion) gc-devel
Requires:		redhat-rpm-config gcc
Conflicts:		choosenim


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


%package doc
Summary:	Documentation for Nim programming language
BuildArch:	noarch
%description doc
Nim is a compiled, garbage-collected systems programming language with a
design that focuses on efficiency, expressiveness, and elegance (in that
order of priority).

This package provides documentation and reference manual for the language
and its standard library.

%prep
%autosetup -n nim

%build
export CFLAGS="${CFLAGS} -Ofast"
export CXXFLAGS="${CXXFLAGS} -Ofast"
export FFLAGS="${FFLAGS} -Ofast"
export FCFLAGS="${FCFLAGS} -Ofast"

export PATH="$(pwd):$(pwd)/bin:${PATH}"

mold -run nim c -d:danger koch.nim
mold -run koch boot -d:useLinenoise

mold -run koch docs &
(cd lib; mold -run nim c --app:lib -d:danger -d:createNimRtl nimrtl.nim) &
mold -run koch tools -d:release &
mold -run nim c -d:danger nimsuggest/nimsuggest.nim &
wait

sed -i '/<link.*fonts.googleapis.com/d' doc/html/*.html


%install
sh install.sh %{buildroot}usr/bin

mkdir -p %{buildroot}/%{_bindir} 
install -Dp -m755 bin/nim{,ble,grep,suggest,pretty} %{buildroot}/%{_bindir}
install -Dp -m644 tools/nim.bash-completion %{buildroot}%{bashcompdir}/nim
install -Dp -m644 dist/nimble/nimble.bash-completion %{buildroot}%{bashcompdir}/nimble
install -Dp -m644 -t%{buildroot}%{_mandir}/man1 %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4

mkdir -p %{buildroot}%{_docdir}/%{name}/html
cp -a doc/html/*.html %{buildroot}%{_docdir}/%{name}/html/
mkdir -p %{buildroot}%{_docdir}/%{name}/html/
cp tools/dochack/dochack.js %{buildroot}%{_docdir}/%{name}/

%check
# export PATH=$PATH:$(realpath ./bin)
# for cat in manyloc gc threads nimble-all lib io async rodfiles debugger examples dll flags
# do
#   ./koch tests --pedantic category $cat -d:nimCoroutines || (echo "$cat test category failed" && exit 1)
# done

%files
%license copying.txt dist/nimble/license.txt
%doc doc/readme.txt
%{_bindir}/nim{,ble}
%{_mandir}/man1/nim{,ble}.1*

%files tools
%license copying.txt
%{_bindir}/nim{grep,suggest,pretty}
%{_mandir}/man1/nim{grep,suggest}.1*

%%files doc
%doc %{_docdir}/nim


%changelog
* Mon Jan 9 2023 windowsboy111 <windowsboy111@fyralabs.com> - 0.8.4
- Initial Package.
