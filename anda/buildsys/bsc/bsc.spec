%define debug_package %{nil}
%global __provides_exclude_from ^%{_libdir}/bsc/SAT/.*
%global __requires_exclude libstp\\.so\\.1|libyices\\.so\\.2\\.6

Name:           bsc
Version:        2026.01
Release:        1%{?dist}
Summary:        Bluespec Compiler (BSC)

License:        BSD-3-Clause AND BSD-2-Clause AND MIT AND LGPL-2.0-or-later AND AND BSL-1.0
URL:            https://github.com/B-Lang-org/bsc
Source:         %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  ghc
BuildRequires:  ghc-regex-compat-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-old-time-devel
BuildRequires:  ghc-split-devel
BuildRequires:  gperf
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  zlib-ng-compat-devel
BuildRequires:  tcl-devel

# For check
BuildRequires:  binutils
BuildRequires:  iverilog

Provides:       bundled(stp)
Provides:       bundled(yices)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Compiler, simulator, and tools for the Bluespec Hardware Description Language.
Bluespec is a single language for digital electronic hardware designs that
comes in two syntactic flavors, which are interchangeable:

    Bluespec SystemVerilog (BSV)
    Bluespec Haskell (BH, or "Bluespec Classic")

Bluespec is a high-level hardware description language. It has a variety of
advanced features including a powerful type system that can prevent errors prior
to synthesis time, and its most distinguishing feature, Guarded Atomic Actions,
allow you to define hardware components in a modular manner based on their
invariants, and let the compiler pick a scheduler.

%prep
%git_clone %{url} %{version}

%build
%make_build install-src GHCJOBS=%{_smp_build_ncpus}

%install
mkdir -p %{buildroot}%{_datadir}/bsc/
mkdir -p %{buildroot}%{_bindir}
cp -r inst/ %{buildroot}%{_datadir}/bsc/

# https://github.com/B-Lang-org/bsc/blob/main/INSTALL.md#overview
# Note this is symlinking the wrapper scripts, not the ELFs
%{__ln_s} -f %{_datadir}/bsc/inst/bin/bsc %{buildroot}%{_bindir}/bsc
%{__ln_s} -f %{_datadir}/bsc/inst/bin/bluetcl %{buildroot}%{_bindir}/bluetcl

# Patch wrapper scripts to use correct paths
for wrapper in %{buildroot}%{_datadir}/bsc/inst/bin/bsc %{buildroot}%{_datadir}/bsc/inst/bin/bluetcl; do
    sed -i 's|BLUESPECDIR="$(cd ${BINDIR}/../lib; echo $PWD)"|BLUESPECDIR="%{_datadir}/bsc/inst/lib"|' $wrapper
    sed -i 's|BLUESPECEXEC=${BINDIR}/core/${SCRIPTNAME}|BLUESPECEXEC="%{_datadir}/bsc/inst/bin/core/${SCRIPTNAME}"|' $wrapper
done

%check
%{make_build} check-smoke

%files
%doc README.md DEVELOP.md
%license COPYING LICENSES/
%{_bindir}/bsc
%{_bindir}/bluetcl
%{_datadir}/bsc/*

%changelog
* Fri Apr 24 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
