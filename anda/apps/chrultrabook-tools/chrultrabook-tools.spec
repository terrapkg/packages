%undefine __brp_mangle_shebangs

Name:           chrultrabook-tools
Version:        3.1.3
Release:        1%?dist
Summary:        User-friendly configuration utility for Chromebooks running an alternate OS
URL:            https://github.com/death7654/Chrultrabook-Tools
Source0:        %url/archive/refs/tags/%version.tar.gz
License:        GPL-3.0-only

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
install -Dm755 chrultrabook-tools-root                          %{buildroot}%{_bindir}/chrultrabook-tools-root
install -Dm644 src-tauri/linux/chrultrabook-tools.desktop       %{buildroot}%{_appsdir}chrultrabook-tools.desktop
install -Dm644 src-tauri/icons/128x128.png                      %{buildroot}%{_hicolordir}/128x128@/apps/Chrultrabook-Tools.png
install -Dm644 src-tauri/icons/128x128@2x.png                   %{buildroot}%{_hicolordir}/128x128@2x/apps/Chrultrabook-Tools.png
install -Dm644 src-tauri/icons/32x32.png                        %{buildroot}%{_hicolordir}/32x32/apps/Chrultrabook-Tools.png
install -Dm644 src-tauri/linux/com.chrultrabook.tools.policy    %{buildroot}%{_datadir}/polkit-1/actions/com.chrultrabook.tools.policy
%{tauri_cargo_license_summary}
%{tauri_cargo_license} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/chrultrabook-tools
%{_bindir}/chrultrabook-tools-root
%{_datadir}/applications/chrultrabook-tools.desktop
%{_hicolordir}/*x*/apps/Chrultrabook-Tools.png
%{_datadir}/polkit-1/actions/com.chrultrabook.tools.policy

%changelog
* Mon Jan 19 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
