Name:          mdBook
Version:       0.4.52
Release:       1%?dist
Summary:       Create a book from markdown files
License:       MPL-2.0
URL:           https://github.com/rust-lang/mdBook
Source0:       %url/archive/refs/tags/v%{version}.tar.gz

BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros
BuildRequires: gcc
BuildRequires: cargo
BuildRequires: mold

Packager:      Owen Zimmerman <owen@fyralabs.com>

Provides:      mdbook

%description
mdBook is a utility to create modern online books from Markdown files.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install
%{cargo_license_online -a} > LICENSE.dependencies

%files
%doc README.md CONTRIBUTING.md CHANGELOG.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/mdbook

%changelog
* Mon Sep 01 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
