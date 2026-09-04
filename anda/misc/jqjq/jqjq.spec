%global commit 644d9650359eaef9d82bdd2cb146a54e891a0538
%global commit_date 20260810
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           jqjq
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        jq implementation of jq
License:        MIT
URL:            https://github.com/wader/jqjq
Source0:        %url/archive/%commit.tar.gz
Requires:       jq
BuildArch:      noarch

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
jqjq is a jq implementation in jq.

It started out researching how to write format decoders in jq for fq which
ended up involving some AST fiddling and then escalated from a joke
into a fun and educational project. But it's also a nice way to
show off jq as a very expressive, capable and neat language!

It can currently run with jq (1.8 or higher), gojq, jaq and jqjq itself.

This jqplay demo snippet can be used to play around with it.

%prep
%autosetup -n jqjq-%commit

%build

%install
install -Dm755 jqjq     %{buildroot}%{_bindir}/jqjq
install -Dm755 jqjq.jq %{buildroot}%{_libdir}/jq/jqjq.jq
sed -i 's|"$(dirname "$(realpath "${BASH_SOURCE[0]}")")"|/usr/lib/jq|g' "%{buildroot}%{_bindir}/jqjq"

%files
%{_bindir}/jqjq
%{_libdir}/jq/jqjq.jq
%doc README.md
%license LICENSE

%changelog
* Sat Aug 01 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
