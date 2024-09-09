%define debug_package %nil
%global _build_id_links none

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/%{name}/.*\\.so

%ifarch x86_64
%define a x64
%elifarch aarch64
%define a arm64
%endif

Name:			codium
Version:		1.93.0.24253
Release:		1%?dist
Summary:		Code editing. Redefined.
License:		MIT
URL:			https://vscodium.com/
Source0:		https://github.com/VSCodium/vscodium/releases/download/%version/VSCodium-linux-%a-%version.tar.gz
Source1:		https://raw.githubusercontent.com/VSCodium/vscodium/%version/README.md
Source2:		https://raw.githubusercontent.com/VSCodium/vscodium/%version/LICENSE
Requires:		at-spi2-atk cairo expat gtk3 xrandr mesa-libgbm nspr nss nss-util xdg-utils
BuildRequires:	rpm_macro(fdupes)

%description
VSCodium is a new choice of tool that combines the simplicity of a code editor
with what developers need for the core edit-build-debug cycle.

%prep
mkdir stuff
cd stuff
tar xf %SOURCE0

cat <<EOF > vscodium-bin-uri-handler.desktop
[Desktop Entry]
Name=VSCodium - URL Handler
Comment=Code Editing. Redefined.
GenericName=Text Editor
Exec=/usr/bin/codium --open-url %U
Icon=vscodium
Type=Application
NoDisplay=true
StartupNotify=false
Categories=Utility;TextEditor;Development;IDE;
MimeType=x-scheme-handler/vscode;
Keywords=vscode;
EOF

cat <<EOF > vscodium-bin.desktop
[Desktop Entry]
Name=VSCodium
Comment=Code Editing. Redefined.
GenericName=Text Editor
Exec=/usr/bin/codium --no-sandbox %F
Icon=vscodium
Type=Application
StartupNotify=false
StartupWMClass=VSCodium
Categories=Utility;Development;IDE;
MimeType=text/plain;inode/directory;
Actions=new-empty-window;
Keywords=vscode;

[Desktop Action new-empty-window]
Name=New Empty Window
Exec=/usr/bin/codium --no-sandbox --new-window %F
Icon=vscodium
EOF


%build

%install
cd stuff
mkdir -p %buildroot%_datadir/doc/%name/ %buildroot%_datadir/licenses/%name
install -Dm644 %SOURCE1 %buildroot%_docdir/%name/
install -Dm644 %SOURCE2 %buildroot%_datadir/licenses/%name/
install -dm755 %buildroot%_datadir/%name
install -dm755 %buildroot%_bindir
install -dm755 %buildroot%_datadir/{applications,pixmaps}
cp -r * %buildroot%_datadir/%name
rm -rf %buildroot%_datadir/%name/*.desktop
ln -s %_datadir/%name/bin/codium %buildroot%_bindir/codium
ln -s %_datadir/%name/bin/codium %buildroot%_bindir/vscodium
install -D -m644 vscodium-bin.desktop %buildroot%_datadir/applications/codium.desktop
install -D -m644 vscodium-bin-uri-handler.desktop %buildroot%_datadir/applications/codium-uri-handler.desktop
install -D -m644 resources/app/resources/linux/code.png %buildroot%_datadir/pixmaps/vscodium.png

# Symlink shell completions
install -dm755 %buildroot%_datadir/zsh/site-functions
install -dm755 %buildroot%_datadir/bash-completion/completions
ln -s %_datadir/%name/resources/completions/zsh/_codium %buildroot%_datadir/zsh/site-functions
ln -s %_datadir/%name/resources/completions/bash/codium %buildroot%_datadir/bash-completion/completions

%fdupes %_datadir/%name/resources/app/extensions/


%files
%doc README.md
%license LICENSE
%_datadir/%name
%_bindir/codium
%_bindir/vscodium
%_datadir/applications/codium.desktop
%_datadir/applications/codium-uri-handler.desktop
%_datadir/pixmaps/vscodium.png
%_datadir/zsh/site-functions/_codium
%_datadir/bash-completion/completions/codium

%changelog
* Sat Jun 17 2023 windowsboy111 <windowsboy111@fyralabs.com> - 1.79.2.23166-2
- Use /usr/share/ instead of /opt/.
- Remove lib dependencies.

* Sun Apr 2 2023 windowsboy111 <windowsboy111@fyralabs.com> - 1.77.3.23102-1
- Initial package.

