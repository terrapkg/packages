Name:           tdf
Version:        0.5.0
Release:        1%?dist
Summary:        A tui-based PDF viewer
URL:            https://github.com/itsjunetime/tdf
Source0:        %url/archive/refs/tags/v%{version}.tar.gz
License:        AGPL-3.0
BuildRequires:  cargo anda-srpm-macros cargo-rpm-macros mold fontconfig-devel mupdf glib2 libgcc clang python

Packager:       Its-J

%description
A terminal-based PDF viewer.
Designed to be performant, very responsive, and work well with even very large PDFs. Built with ratatui.

%prep
%git_clone
%cargo_prep_online
pushd ratatui-image
%cargo_prep_online
popd
pushd ratatui
%cargo_prep_online
popd

%build
%cargo_build

%install
install -Dm755 target/rpm/tdf %{buildroot}%{_bindir}/tdf
%cargo_license_summary_online
%{cargo_license_online -a} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/tdf

%changelog
* Wed Oct 22 2025 Its-J
- Intial Commit
