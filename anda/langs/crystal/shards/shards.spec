Name:          shards
Version:       0.20.0
Release:       3%?dist
Summary:       Dependency manager for the Crystal language 
License:       Apache-2.0
Packager:      Carl Hörberg <carl@84codes.com>
URL:           https://crystal-lang.org/
Source0:       https://github.com/crystal-lang/shards/archive/refs/tags/v%version.tar.gz
BuildRequires: crystal make
BuildRequires: libyaml-devel
Recommends:    git make
Supplements:   crystal

%description
Shards is a dependency manager for the Crystal programming language. It allows you to easily manage and install external libraries (called "shards") that your Crystal projects depend on.

%prep
%autosetup

%build
%make_build release=1 FLAGS="--link-flags=\"%{build_ldflags}\""

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/shards
%{_mandir}/man1/shards.1.gz
%{_mandir}/man5/shard.yml.5.gz

%changelog
* Thu Sep 24 2026 Carl Hörberg <carl@84codes.com> - 0.20.0-3
- Make git/make recommended instead of suggested, since shards needs them to do useful work
- Drop BuildRequires already pulled in by crystal

* Mon Nov 03 2025 Carl Hörberg <carl@84codes.com> - 0.19.1-1
- Initial package
