Name:          shards
Version:       0.20.0
Release:       1%?dist
Summary:       Dependency manager for the Crystal language 
License:       Apache-2.0
Packager:      Carl Hörberg <carl@84codes.com>
URL:           https://crystal-lang.org/
Source0:       https://github.com/crystal-lang/shards/archive/refs/tags/v%version.tar.gz
BuildRequires: crystal make
BuildRequires: gcc gc-devel libyaml-devel pcre-devel
Suggests:      git make
Supplements:   crystal

%description
Shards is a dependency manager for the Crystal programming language. It allows you to easily manage and install external libraries (called "shards") that your Crystal projects depend on.

%prep
%setup -q

%build
%make_build release=1 FLAGS="--link-flags=\"%{build_ldflags}\""

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/shards
%{_mandir}/man1/shards.1.gz
%{_mandir}/man5/shard.yml.5.gz

%changelog
* Mon Nov 03 2025 Carl Hörberg <carl@84codes.com> - 0.19.1-1
- Initial package
