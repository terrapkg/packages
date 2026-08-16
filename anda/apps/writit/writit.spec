Name:           writit
Version:        1.0.0
Release:        1%{?dist}
Summary:        Fast, free and open-source notes
URL:            https://github.com/iamnotmega/writit
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
License:        GPL-3.0-or-later
Packager:       NotMega <iamnotmega@proton.me>

BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  openssl-devel
BuildRequires:  curl
BuildRequires:  wget
BuildRequires:  file
BuildRequires:  libappindicator-gtk3-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libxdo-devel
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  nodejs
BuildRequires:  npm

%description
%{summary}.

%prep
%autosetup -n writit-%{version}

%build
npm install
npm run tauri build

%files
%doc README.md
%license LICENSE
%{_bindir}/writit
%{_appsdir}/applications/writit.desktop
%{_hicolordir}/icons/hicolor/*/apps/writit.png

%install
# Create required directories
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_appsdir}
install -d %{buildroot}%{_hicolordir}/icons/hicolor/{32x32,64x64,128x128,128x128@2}/apps

# Install built binary and desktop entry
install -m 0755 src-tauri/target/release/writit %{buildroot}%{_bindir}/writit

# Create desktop entry
cat <<EOF > %{buildroot}%{_appsdir}/writit.desktop
[Desktop Entry]
Name=Writit
Comment=Fast, free and open-source notes
Exec=writit
Icon=writit
Terminal=false
Type=Application
Categories=Utility;
EOF

# Install icons
install -m 0644 src-tauri/icons/32x32.png %{_hicolordir}/32x32/apps/writit.png
install -m 0644 src-tauri/icons/64x64.png %{_hicolordir}/64x64/apps/writit.png
install -m 0644 src-tauri/icons/128x128.png %{_hicolordir}/128x128/apps/writit.png
install -m 0644 src-tauri/icons/128x128@2x.png %{_hicolordir}/128x128@2/apps/writit.png

%check
%desktop_file_validate %{buildroot}%{_appsdir}/writit.desktop

%changelog
* Sun Aug 16 2026 NotMega <iamnotmega@proton.me> - 1.0.0-1
- Initial commit