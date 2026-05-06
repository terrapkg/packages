Name:          mdBook
Version:       0.5.2
Release:       1%?dist
Summary:       Create a book from markdown files
License:       MPL-2.0 AND MIT AND (Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND ISC AND (MIT OR Zlib OR Apache-2.0) AND Unicode-3.0 AND (Apache-2.0 OR BSL-1.0) AND (MIT AND BSD-3-Clause)
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
%cargo_license_summary_online
%{cargo_license_online -a} > LICENSE.dependencies

%files
%doc README.md CONTRIBUTING.md CHANGELOG.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/mdbook

%changelog
* Mon Sep 01 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
