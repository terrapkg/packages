%bcond bootstrap 0
%global bootstrap_version 1.17.1

Name:          crystal
Version:       1.19.1
Release:       1%?dist
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
BuildRequires: gcc gcc-c++ make gc-devel llvm-devel
BuildRequires: pcre2-devel libyaml-devel libffi-devel
Requires:      gcc pkgconfig gc-devel
Requires:      pcre2-devel openssl-devel zlib-devel
Requires:      libyaml-devel libxml2-devel gmp-devel
Suggests:      shards

%description
Crystal is a programming language with the following goals:
- Have a syntax similar to Ruby (but compatibility with it is not a goal)
- Statically type-checked but without having to specify the type of variables or method arguments
- Be able to call C code by writing bindings to it in Crystal
- Have compile-time evaluation and generation of code, to avoid boilerplate code
- Compile to efficient native code

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
%{_datadir}/bash-completion/completions/crystal
%{_datadir}/fish/vendor_completions.d/crystal.fish
%{_mandir}/man1/crystal.1.gz

%changelog
* Mon Nov 03 2025 Carl Hörberg <carl@84codes.com> -  1.18.2-2
- Build from source, support multiple architectures.

* Sat Jun 17 2023 madonuko <mado@fyralabs.com> - 1.8.2-2
- Add devel package.

* Sat Apr 15 2023 madonuko <mado@fyralabs.com> - 1.8.0-1
- Initial package.

