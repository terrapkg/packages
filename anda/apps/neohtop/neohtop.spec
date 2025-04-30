%global __brp_mangle_shebangs %{nil}

Name:           neohtop
Version:        1.1.2
Release:        1%?dist
Summary:        System monitoring on steroids
License:        MIT
URL:            https://github.com/Abdenasser/neohtop
Source0:        %url/archive/refs/tags/v%version.tar.gz
Source1:        NeoHtop.desktop
Packager:       Owen Zimmerman <owen@fyralabs.com>
BuildRequires:  rust
BuildRequires:  nodejs-npm
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  javascriptcoregtk4.1-devel
BuildRequires:  libsoup3-devel
BuildRequires:  gtk3-devel
BuildRequires:  rust-gdk-pixbuf-sys-devel
BuildRequires:  glib2-devel
BuildRequires:  openssl-devel

%description
%summary.

%prep
%autosetup -n neohtop-%version

%build
npm install
npm run tauri build

%install
install -Dpm755 src-tauri/target/release/NeoHtop %buildroot%_bindir/NeoHtop
install -Dpm644 %{SOURCE1} %buildroot%{_datadir}/applications/NeoHtop.desktop
# don't mind the numbers not matching, this is how the offical rpm installs these files
install -Dpm644 src-tauri/icons/128x128@2x.png %buildroot%{_iconsdir}/hicolor/256x256@2/apps/NeoHtop.png
install -Dpm644 src-tauri/icons/32x32.png %buildroot%{_iconsdir}/hicolor/32x32/apps/NeoHtop.png
install -Dpm644 src-tauri/icons/128x128.png %buildroot%{_iconsdir}/hicolor/128x128/apps/NeoHtop.png

%files
%doc README.md
%license LICENSE
%_bindir/NeoHtop
%{_datadir}/applications/NeoHtop.desktop
%{_iconsdir}/hicolor/256x256@2/apps/NeoHtop.png
%{_iconsdir}/hicolor/32x32/apps/NeoHtop.png
%{_iconsdir}/hicolor/128x128/apps/NeoHtop.png

%changelog
* Sat Feb 15 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial package
