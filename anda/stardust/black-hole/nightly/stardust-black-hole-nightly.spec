%global commit 5abca9d613fac7861803319b3191061b2d8ce067
%global commit_date 20251130
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-black-hole-nightly
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        Spatial storage for Stardust XR
URL:            https://github.com/StardustXR/black-hole
Source0:        %url/archive/%commit/black-hole-%commit.tar.gz
License:        MIT
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold

Provides:       black-hole-nightly stardust-black-hole-nightly
Conflicts:      stardust-xr-black-hole
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n black-hole-%commit
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
export STARDUST_RES_PREFIXES=%_datadir
%cargo_install
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

mkdir -p %buildroot%_datadir
cp -r res/* %buildroot%_datadir/

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%_bindir/black-hole
%_datadir/black_hole/

%changelog
* Sun Jan 11 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit (port from stable)
