Name:          optivorbis
Version:       0.3.2
Release:       1%{?dist}
Summary:       Library and application for lossless, format-preserving, two-pass optimization and repair of Vorbis data
SourceLicense: AGPL-3.0-or-later AND BSD-3-Clause
License:       (%{sourcelicense}) AND (Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND AGPL-3.0-or-later AND MIT AND Apache-2.0 AND (AGPL-3.0-or-later OR BSD-3-Clause) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
URL:           https://github.com/OptiVorbis/OptiVorbis
Source0:       %url/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo-rpm-macros

Provides:      OptiVorbis

Packager:      Owen Zimmerman <owen@fyralabs.com>

%description
Library and application for lossless, format-preserving,
two-pass optimization and repair of Vorbis data,
reducing its size without altering any audio information.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/optivorbis %{buildroot}%{_bindir}/optivorbis

%{cargo_license_online -a} > LICENSE.dependencies

%files
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md
%license LICENSE LICENSE.BSD-3-Clause LICENSE.dependencies
%{_bindir}/optivorbis

%changelog
* Sun Sep 20 2026 Owen Zimmerman <owen@fyralabs.com> - 0.3.2-1
- Initial commit
