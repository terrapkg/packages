%global _description %{expand:
Automatically patches Garry's Mod's internal Chromium Embedded Framework to:

- Bring CEF up to date
- Fix GMod missing menu/launch issues on macOS and Linux
- Enable Proprietary Video/Audio codec, like H.264 (MP4) and AAC, support
- Enable Widevine support (but no VMP)
- Enable Software WebGL
- Enable partial GPU acceleration}
%global git_name GModPatchTool
%undefine __brp_mangle_shebangs

Name:          gmodpatchtool
Version:       20251102
Release:       1%{?dist}
SourceLicense: GPL-3.0-only
License:       ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 AND ISC) AND (Apache-2.0 AND MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR GPL-2.0-only) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (BSD-3-Clause AND MIT) AND (BSD-3-Clause OR MIT) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSL-1.0 AND CC0-1.0 AND (CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND GPL-3.0-only AND ISC AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR CC0-1.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT) AND bzip2-1.0.6
Summary:       Automatic Patching/Updating of GMod CEF. Fixes macOS/Linux launch issues.
URL:           https://solsticegamestudios.com/fixmedia
Source0:       https://github.com/solsticegamestudios/%{git_name}/archive/refs/tags/%{version}.tar.gz
BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros
BuildRequires: git-lfs
BuildRequires: mold
Provides:      %{git_name}
Packager:      Gilver E. <roachy@fyralabs.com>

%description %_description

%prep
%git_clone https://github.com/solsticegamestudios/%{git_name}.git %{version}
git-lfs checkout
%cargo_prep_online

%build
%cargo_build

%install
find target/rpm \
    -maxdepth 1 -type f -executable ! -name '*.so' \
    -exec install -Dm755 -t %{buildroot}%{_bindir} {} +
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE.txt
%license LICENSE.dependencies
%{_bindir}/%{name}

%changelog
* Tue Feb 24 2026 Gilver E. <roachy@fyralabs.com>
- Initial package
