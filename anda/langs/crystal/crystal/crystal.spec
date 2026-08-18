%bcond bootstrap 0
%global bootstrap_version 1.17.1

Name:          crystal
Version:       1.21.0
Release:       1%{?dist}
Summary:       A general-purpose, object-oriented programming language
License:       Apache-2.0
Packager:      Carl Hörberg <carl@84codes.com>
URL:           https://crystal-lang.org/
Source0:       https://github.com/crystal-lang/crystal/archive/%version.tar.gz
%if %{with bootstrap}
Source1:       https://dev.alpinelinux.org/archive/crystal/crystal-%{bootstrap_version}-%{_arch}-alpine-linux-musl.tar.gz
%else
BuildRequires: crystal
%endif
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: gc-devel
BuildRequires: llvm-devel
BuildRequires: rubygem-asciidoctor
BuildRequires: pcre2-devel
BuildRequires: libyaml-devel
BuildRequires: libffi-devel
Requires:      gcc
Requires:      pkgconfig
Requires:      gc-devel
Requires:      pcre2-devel
Requires:      openssl-devel
Requires:      zlib-ng-devel
Requires:      libyaml-devel
Requires:      libxml2-devel
Requires:      gmp-devel
Suggests:      shards

%description
Crystal is a programming language with the following goals:
- Have a syntax similar to Ruby (but compatibility with it is not a goal)
- Statically type-checked but without having to specify the type of variables or method arguments
- Be able to call C code by writing bindings to it in Crystal
- Have compile-time evaluation and generation of code, to avoid boilerplate code
- Compile to efficient native code

%pkg_completion -Bf

%prep
%setup -q
%if %{with bootstrap}
%setup -q -b 1
%endif

%build
%if %{with bootstrap}
# Use bootstrap crystal binary
export PATH="%{_builddir}/crystal-%{bootstrap_version}-%{_arch}-alpine-linux-musl/bin:$PATH"
%endif
%make_build release=1 interpreter=1 LDFLAGS="%{build_ldflags}" CRYSTAL_CONFIG_LIBRARY_PATH=%{_libdir}/crystal

%install
%make_install PREFIX=%{_prefix}

%files
%license %{_datadir}/licenses/crystal/LICENSE
%{_bindir}/crystal
%{_datadir}/crystal
%{_datadir}/zsh/site-functions/_crystal
%{_mandir}/man1/crystal.1.gz
%{_mandir}/man1/crystal-build.1.gz
%{_mandir}/man1/crystal-docs.1.gz
%{_mandir}/man1/crystal-env.1.gz
%{_mandir}/man1/crystal-eval.1.gz
%{_mandir}/man1/crystal-init.1.gz
%{_mandir}/man1/crystal-play.1.gz
%{_mandir}/man1/crystal-run.1.gz
%{_mandir}/man1/crystal-spec.1.gz
%{_mandir}/man1/crystal-tool-dependencies.1.gz
%{_mandir}/man1/crystal-tool-format.1.gz
%{_mandir}/man1/crystal-tool-macro_code_coverage.1.gz
%{_mandir}/man1/crystal-tool-unreachable.1.gz

%changelog
* Thu Jul 16 2026 Owen Zimmerman <owen@fyralabs.com> - 1.21.0-1 
- Update for 1.21.0, use %%pkg_completions

* Mon Nov 03 2025 Carl Hörberg <carl@84codes.com> -  1.18.2-2
- Build from source, support multiple architectures.

* Sat Jun 17 2023 madonuko <mado@fyralabs.com> - 1.8.2-2
- Add devel package.

* Sat Apr 15 2023 madonuko <mado@fyralabs.com> - 1.8.0-1
- Initial package.

