%ifarch x86_64
%define a x64
%elifarch aarch64
%define a arm64
%endif

Name:			codium
Version:		1.78.2.23132
Release:		1%{?dist}
Summary:		Code editing. Redefined.
License:		MIT
URL:			https://vscodium.com/
Source0:		https://github.com/VSCodium/vscodium/releases/download/%version/VSCodium-linux-%a-%version.tar.gz
Requires:		alsa-lib at-spi2-atk cairo cups-libs dbus-libs expat gtk3 xrandr mesa-libgbm nspr nss nss-util xdg-utils

%description
VSCodium is a new choice of tool that combines the simplicity of a code editor with what developers need for the core edit-build-debug cycle.

%prep
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
Exec=/usr/bin/codium --no-sandbox --unity-launch %F
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
install -dm755 %buildroot/opt/%name
install -dm755 %buildroot/usr/bin
install -dm755 %buildroot/usr/share/{applications,pixmaps}
cp -r * %buildroot/opt/%name
rm -rf %buildroot/opt/%name/*.desktop
ln -s /opt/%name/bin/codium %buildroot/usr/bin/codium
ln -s /opt/%name/bin/codium %buildroot/usr/bin/vscodium
install -D -m644 vscodium-bin.desktop %buildroot/usr/share/applications/codium.desktop
install -D -m644 vscodium-bin-uri-handler.desktop %buildroot/usr/share/applications/codium-uri-handler.desktop
install -D -m644 resources/app/resources/linux/code.png %buildroot/usr/share/pixmaps/vscodium.png

# Symlink shell completions
install -dm755 %buildroot/usr/share/zsh/site-functions
install -dm755 %buildroot/usr/share/bash-completion/completions
ln -s /opt/%name/resources/completions/zsh/_codium %buildroot/usr/share/zsh/site-functions
ln -s /opt/%name/resources/completions/bash/codium %buildroot/usr/share/bash-completion/completions


%files
/opt/%name
/usr/bin/codium
/usr/bin/vscodium
/usr/share/applications/codium.desktop
/usr/share/applications/codium-uri-handler.desktop
/usr/share/pixmaps/vscodium.png
/usr/share/zsh/site-functions/_codium
/usr/share/bash-completion/completions/codium

%changelog
* Sun Apr 2 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package.

