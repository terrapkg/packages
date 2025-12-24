Name:           chrultrabook-tools
Version:        3.1.2
Release:        1%?dist
Summary:        User-friendly configuration utility for Chromebooks running an alternate OS
URL:            https://github.com/death7654/Chrultrabook-Tools
Source0:        %url/archive/refs/tags/%version.tar.gz
License:        GPLv3

BuildRequires:  rust
BuildRequires:  nodejs-npm
BuildRequires:  cargo
BuildRequires:  glib2
BuildRequires:  glib2-devel
BuildRequires:  gtk3
BuildRequires:  gtk3-devel
BuildRequires:  javascriptcoregtk4.1
BuildRequires:  javascriptcoregtk4.1-devel
BuildRequires:  libsoup3
BuildRequires:  libsoup3-devel
BuildRequires:  webkit2gtk4.1
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  libappindicator
BuildRequires:  libappindicator-gtk3
BuildRequires:  libappindicator-devel
BuildRequires:  libappindicator-gtk3-devel
BuildRequires:  gstreamer1
BuildRequires:  gstreamer1-devel
BuildRequires:  patchelf
BuildRequires:  libstdc++-static
BuildRequires:  librsvg2-devel
BuildRequires:  libxdo-devel
BuildRequires:  anda-srpm-macros

BuildRequires: nodejs
BuildRequires: npm
BuildRequires: cargo
BuildRequires: rustc
BuildRequires: pkgconfig
BuildRequires: webkit2gtk3-devel
BuildRequires: openssl-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make

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

%build
npm install --save-dev @angular/cli
npm install
npm run tauri build # --bundles rpm

%install
install -Dm755 Chrultrabook-Tools %{buildroot}%{_bindir}/chrultrabook-tools

%files
%doc README.md
%license LICENSE
%_bindir/chrultrabook-tools
%{_datadir}/applications/chrultrabook-tools.desktop
%{_datadir}/icons/hicolor/128x128/apps/Chrultrabook-Tools.png
%{_datadir}/icons/hicolor/256x256@2/apps/Chrultrabook-Tools.png
%{_datadir}/icons/hicolor/32x32/apps/Chrultrabook-Tools.png

%changelog
* Mon Jun 23 2025 Owen Zimmerman owen@fyralabs.com
- Initial Package
