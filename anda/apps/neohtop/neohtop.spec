%undefine __brp_mangle_shebangs
%global appid com.github.neohtop

Name:           neohtop
Version:        1.2.0
Release:        4%?dist
Summary:        System monitoring on steroids
SourceLicense:  MIT
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-3-Clause AND MIT) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (BSD-3-Clause OR MIT) AND BSD-3-Clause AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://abdenasser.github.io/neohtop/
Source0:        https://github.com/Abdenasser/neohtop/archive/refs/tags/v%version.tar.gz
Source1:        NeoHtop.desktop
Source2:        com.github.neohtop.metainfo.xml
Packager:       Owen Zimmerman <owen@fyralabs.com>
BuildRequires:  rust
BuildRequires:  %tauri_buildrequires
BuildRequires:  libsoup3-devel
BuildRequires:  gtk3-devel
BuildRequires:  rust-gdk-pixbuf-sys-devel
BuildRequires:  glib2-devel
BuildRequires:  openssl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  anda-srpm-macros
BuildRequires:  terra-appstream-helper

Provides:       NeoHtop

%description
%summary.

%prep
%autosetup -n neohtop-%version
%tauri_prep

%build
%npm_build -B

%install
install -Dpm755 src-tauri/target/rpm/NeoHtop %{buildroot}%{_bindir}/NeoHtop
%desktop_file_install                            %{SOURCE1}
# don't mind the numbers not matching, this is how the offical rpm installs these files
install -Dpm644 src-tauri/icons/128x128@2x.png   %{buildroot}%{_hicolordir}/256x256@2/apps/NeoHtop.png
install -Dpm644 src-tauri/icons/32x32.png        %{buildroot}%{_hicolordir}/32x32/apps/NeoHtop.png
install -Dpm644 src-tauri/icons/128x128.png      %{buildroot}%{_hicolordir}/128x128/apps/NeoHtop.png

%terra_appstream -o %{SOURCE2}

%{tauri_cargo_license} > LICENSE.dependencies

%check
%desktop_file_validate %{buildroot}%{_appsdir}/NeoHtop.desktop

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/NeoHtop
%{_appsdir}/NeoHtop.desktop
%{_hicolordir}/256x256@2/apps/NeoHtop.png
%{_hicolordir}/32x32/apps/NeoHtop.png
%{_hicolordir}/128x128/apps/NeoHtop.png
%{_metainfodir}/com.github.neohtop.metainfo.xml

%changelog
* Wed Dec 24 2025 Owen Zimmerman <owen@fyralabs.com>
- Clean up build, add %check 
* Wed Nov 19 2025 Owen Zimmerman <owen@fyralabs.com>
- Add metainfo
* Sat Feb 15 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial package
