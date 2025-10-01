Name:           sad
Version:        0.4.32
Release:        1%?dist
Summary:        CLI search and replace | Space Age seD
URL:            https://github.com/ms-jpq/sad
Source0:        %url/archive/refs/tags/v%{version}.tar.gz
License:        MIT
BuildRequires:  cargo anda-srpm-macros cargo-rpm-macros mold

Packager:       Its-J

%description
Basically sad is a Batch File Edit tool.
It will show you a really nice diff of proposed changes before you commit them.

%prep
%autosetup -n sad-%version
%cargo_prep_online

%build

%install
%cargo_install

%files
%doc README.md
%license LICENSE
%{_bindir}/sad

%changelog
* Tue Sep 30 2025 Its-J
- Intial Commit
