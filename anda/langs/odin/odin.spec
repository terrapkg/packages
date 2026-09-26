%global ver dev-2026-09
%global sanitized_ver %(echo %{ver} | sed 's/^dev-//;s/-/./')

%global __requires_exclude_from ^%{_libexecdir}/Odin/vendor/.*$

Name:           odin
Version:        %{sanitized_ver}
Release:        1%{?dist}
Summary:        Odin Programming Language
URL:            odin-lang.org
Source0:        https://github.com/odin-lang/Odin/archive/refs/tags/%{ver}.tar.gz
License:        Zlib
BuildRequires:  llvm-devel(major) = 22
BuildRequires:  clang
Requires:       clang
Provides:       Odin
Provides:       odin-lang
Provides:       Odin-lang

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Odin is a general-purpose programming language with distinct
typing, built for high performance, modern systems, and built-in
data-oriented data types. The Odin Programming Language,
the C alternative for the joy of programming.

%prep
%autosetup -n Odin-%{ver}
find . -name '*.dll' -delete

%build
export CC=clang
export CXX=clang++
export LLVM_CONFIG=/usr/bin/llvm-config-22
./build_odin.sh

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libexecdir}/Odin
cp -a odin base core vendor %{buildroot}%{_libexecdir}/Odin
%{__ln_s} ../libexec/Odin/odin %{buildroot}%{_bindir}/odin-lang
%{__ln_s} ../libexec/Odin/odin %{buildroot}%{_bindir}/odin

%files
%doc README.md
%license LICENSE
%{_bindir}/odin-lang
%{_bindir}/odin
%{_libexecdir}/Odin

%changelog
* Thu Sep 24 2026 ammix <maxim@ammix.dev>
- Add base collection
- Fix version sed
- Pin llvm22
- Require clang

* Thu Jul 23 2026 Owen Zimmerman <owen@fyralabs.com>
- Fix sanitized_ver sed script

* Thu Jul 09 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
