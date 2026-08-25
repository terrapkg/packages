%global commit 58e0adb55a67fb0862fd2cc77e999013c4843222
%global commit_date 20260825
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           porffor-nightly
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        An ahead-of-time JavaScript compiler
License:        MIT
URL:            https://porffor.dev/
Source0:		    https://github.com/CanadaHonk/porffor/archive/%commit/porffor-%commit.tar.gz
Packager:       madonuko <mado@fyralabs.com>
Provides:       porffor = %evr
Provides:       porf = %evr
BuildRequires:  clang mold compiler-rt llvm
BuildRequires:  nodejs

%description
Porffor is a 100% AOT compiled JS engine/runtime. There is nothing interpreted or compiled just-in-time. Porffor compiles JS to C (with an IR inbetween).

%prep
%autosetup -n porffor-%commit

%build
node selfhosted/build.mjs
./porf c --compress-data selfhosted/bundle.js -o selfhosted/stage1.c

clang -O0 -fuse-ld=mold -fno-sanitize=undefined -w \
  -fprofile-instr-generate=release.profraw \
  selfhosted/stage1.c -o pgo-porf -lm
./pgo-porf c selfhosted/bundle.js -o selfhosted/stage2.c
llvm-profdata merge -o release.profdata release.profraw

clang %build_cflags -fuse-ld=mold \
  -fprofile-instr-use=release.profdata \
  -mllvm -force-attribute=porf_strict_eq:noinline \
  selfhosted/stage1.c -o porf -lm

%install
install -Dpm755 porf -t %buildroot%_bindir

%files
%doc README.md
%license LICENSE
%_bindir/porf

%changelog
* Tue Aug 18 2026 madonuko <mado@fyralabs.com> - 0~20260812git.747d551-1
- Initial package
