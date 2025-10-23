Name:           tdf
Version:        0.4.3
Release:        1%?dist
Summary:        A tui-based PDF viewer
URL:            https://github.com/itsjunetime/tdf
Source0:        %url/archive/refs/tags/v%{version}.tar.gz
Patch0:         remove-publish.patch
License:        AGPL-3.0
BuildRequires:  cargo anda-srpm-macros cargo-rpm-macros mold fontconfig-devel mupdf glib2 libgcc clang python

Packager:       Its-J

%description
A terminal-based PDF viewer.
Designed to be performant, very responsive, and work well with even very large PDFs. Built with ratatui.

%prep
%git_clone
%patch -P0 -p1
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
# CFLAGS+=' -ffat-lto-objects'
# EXPORT=allow-dirty
%cargo_install
%cargo_license_summary_online
%{cargo_license_online -a} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE
%license 9LICENSE.dependencies
%{_bindir}/tdf

%changelog
* Wed Oct 01 2025 Its-J
- Intial Commit
