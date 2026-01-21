%undefine __brp_mangle_shebangs

Name:           chrultrabook-tools
Version:        3.1.3
Release:        1%?dist
Summary:        User-friendly configuration utility for Chromebooks running an alternate OS
URL:            https://github.com/death7654/Chrultrabook-Tools
Source0:        %url/archive/refs/tags/%version.tar.gz
License:        GPL-3.0-only AND MPL-2.0 AND MIT-0 AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND (CC0-1.0 OR Apache-2.0) AND BSL-1.0 AND BlueOak-1.0.0 AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-2-Clause AND ISC AND MIT AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND NCSA AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT) AND (Apache-2.0/MIT) AND CDLA-Permissive-2.0 AND (MIT OR Zlib OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND Unlicense

BuildRequires:  cargo
BuildRequires:  glib2
BuildRequires:  glib2-devel
BuildRequires:  gtk3
BuildRequires:  gtk3-devel
BuildRequires:  javascriptcoregtk4.1
BuildRequires:  javascriptcoregtk4.1-devel
BuildRequires:  libsoup3
BuildRequires:  libsoup3-devel
BuildRequires:  libappindicator-gtk3
BuildRequires:  libappindicator-devel
BuildRequires:  gstreamer1
BuildRequires:  gstreamer1-devel
BuildRequires:  patchelf
BuildRequires:  libstdc++-static
BuildRequires:  libxdo-devel
BuildRequires:  anda-srpm-macros
BuildRequires:  rustc
BuildRequires:  %{tauri_buildrequires -a}
# This may seem weird, but https://github.com/nodejs/node/issues/51752#issuecomment-2970163641
BuildRequires:  nodejs-full-i18n

Requires:       chromium-ectool
Requires:       coreboot-utils-cbmem
Requires:       libayatana-appindicator-gtk3
Requires:       libayatana-ido-gtk3
Requires:       libayatana-indicator-gtk3

Packager:       Owen Zimmerman owen@fyralabs.com

%description
%summary.

%prep
%autosetup -n Chrultrabook-Tools-%version
%tauri_prep

%build
%npm_build -r build -B

%install
%tauri_install
install -Dm755 src-tauri/linux/chrultrabook-tools-root          %{buildroot}%{_bindir}/chrultrabook-tools-root
install -Dm644 src-tauri/linux/chrultrabook-tools.desktop %{buildroot}%{_appsdir}/chrultrabook-tools.desktop
install -Dm644 src-tauri/icons/128x128.png                      %{buildroot}%{_hicolordir}/128x128@/apps/Chrultrabook-Tools.png
install -Dm644 src-tauri/icons/128x128@2x.png                   %{buildroot}%{_hicolordir}/128x128@2x/apps/Chrultrabook-Tools.png
install -Dm644 src-tauri/icons/32x32.png                        %{buildroot}%{_hicolordir}/32x32/apps/Chrultrabook-Tools.png
install -Dm644 src-tauri/linux/com.chrultrabook.tools.policy    %{buildroot}%{_datadir}/polkit-1/actions/com.chrultrabook.tools.policy
%{tauri_cargo_license} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/chrultrabook-tools
%{_bindir}/chrultrabook-tools-root
%{_appsdir}/chrultrabook-tools.desktop
%{_hicolordir}/*x*/apps/Chrultrabook-Tools.png
%{_datadir}/polkit-1/actions/com.chrultrabook.tools.policy

%changelog
* Mon Jan 19 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
