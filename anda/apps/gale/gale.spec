%undefine __brp_mangle_shebangs

%global appid com.kesomannen.gale

Name:           gale
Version:        1.22.0
Release:        1%{?dist}
Summary:        A modern mod manager for Thunderstore
Packager:       Jan200101 <sentrycraft123@gmail.com>

License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) or ((MIT OR Apache-2.0) AND NCSA) or ((MIT OR Apache-2.0) AND Unicode-3.0) or (0BSD OR MIT OR Apache-2.0) or (Apache-2.0) or (Apache-2.0 AND ISC) or (Apache-2.0 AND MIT) or (Apache-2.0 OR BSL-1.0) or (Apache-2.0 OR ISC OR MIT) or (Apache-2.0 OR MIT) or (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) or (BSD-2-Clause) or (BSD-2-Clause OR Apache-2.0 OR MIT) or (BSD-3-Clause) or (BSD-3-Clause AND MIT) or (BSD-3-Clause OR Apache-2.0) or (BSD-3-Clause OR MIT) or (BSD-3-Clause OR MIT OR Apache-2.0) or (BSL-1.0) or (CC0-1.0 OR Apache-2.0) or (CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception) or (CC0-1.0 OR MIT-0 OR Apache-2.0) or (CDLA-Permissive-2.0) or (GPL-3.0) or (ISC) or (ISC AND (Apache-2.0 OR ISC)) or (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) or (LGPL-2.1) or (MIT) or (MIT OR Apache-2.0) or (MIT OR Apache-2.0 OR LGPL-2.1-or-later) or (MIT OR Apache-2.0 OR Zlib) or (MIT OR Zlib OR Apache-2.0) or (MPL-2.0) or (Unicode-3.0) or (Unlicense OR MIT) or (Zlib) or (Zlib OR Apache-2.0 OR MIT)
SourceLicense:  GPL-3.0-only
URL:            https://github.com/Kesomannen/gale
Source0:        %{url}/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
Source1:        gale.desktop

BuildRequires:  pnpm
BuildRequires:  tauri %{tauri_buildrequires -a}
BuildRequires:  desktop-file-utils
BuildRequires:  terra-appstream-helper
BuildRequires:  ImageMagick

%description
A powerful mod manager for Thunderstore, built with Svelte and Tauri.

%prep
%autosetup -n %{name}-%{version}
%tauri_prep

%build
%{__pnpm} install --frozen-lockfile
%tauri_build

%install
%tauri_install

%desktop_file_install %{SOURCE1}

%terra_appstream

for size in 16 24 32 48 64 128 256; do
    mkdir -p "%{buildroot}/%{_hicolordir}/${size}x${size}/apps"

    magick \
        "src-tauri/icons/icon.png" \
        -thumbnail ${size}x${size} \
        -alpha on \
        -background none \
        -flatten \
        "%{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps/gale.png"
done

%tauri_cargo_license_summary
%{tauri_cargo_license} > LICENSE.dependencies

# Remove the cargo registry files that get installed when building online
rm -rf %{buildroot}%{_datadir}/cargo/registry

%check
%desktop_file_validate %{buildroot}%{_appsdir}/gale.desktop

%files
%license LICENSE.md
%doc README.md
%doc CHANGELOG.md
%{_bindir}/gale
%{_appsdir}/gale.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_hicolordir}/*/apps/gale.png

%changelog
* Sat Aug 22 2026 Jan200101 <sentrycraft123@gmail.com> - 1.21.0-1
- initial package

