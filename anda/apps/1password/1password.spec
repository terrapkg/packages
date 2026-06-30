%global debug_package %{nil}
%global policy_owners unix-group:wheel
%global appdir %{_datadir}/1password

# Exclude private Electron libraries bundled in the app payload.
%global __provides_exclude libffmpeg.so|libvk_swiftshader.so|libvulkan.so|libEGL.so|libGLESv2.so
%global __requires_exclude libffmpeg.so|libvk_swiftshader.so|libvulkan.so|libEGL.so|libGLESv2.so

%ifarch x86_64
%global tararch x64
%elifarch aarch64
%global tararch arm64
%endif

Name:           1password
Version:        8.12.24
Release:        3%{?dist}
Summary:        Password manager and secure wallet

Packager:       Cappy Ishihara <cappy@fyralabs.com>

License:        LicenseRef-1Password-Proprietary
URL:            https://1password.com
Source0:        https://downloads.1password.com/linux/tar/stable/%{_arch}/%{name}-%{version}.%{tararch}.tar.gz
Source1:        https://downloads.1password.com/linux/tar/stable/%{_arch}/%{name}-%{version}.%{tararch}.tar.gz.sig
Source2:        1password.sysusers
ExclusiveArch:  x86_64 aarch64

BuildRequires:  desktop-file-utils
BuildRequires:  systemd-rpm-macros
Requires:       desktop-file-utils
Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       nss
Requires:       polkit
Requires:       xdg-utils
Requires(post): /usr/bin/chown
Requires(post): /usr/bin/chmod

%description
%{summary}

%prep
%autosetup -n %{name}-%{version}.%{tararch}


%build

%install
# Install icons
install -Dm0644 resources/icons/hicolor/32x32/apps/1password.png -t %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
install -Dm0644 resources/icons/hicolor/64x64/apps/1password.png -t %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
install -Dm0644 resources/icons/hicolor/256x256/apps/1password.png -t %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
install -Dm0644 resources/icons/hicolor/512x512/apps/1password.png -t %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/

sed 's|${POLICY_OWNERS}|%{policy_owners}|g' \
  com.1password.1Password.policy.tpl > com.1password.1Password.policy
install -Dm0644 com.1password.1Password.policy -t %{buildroot}%{_datadir}/polkit-1/actions/
install -Dm0644 resources/custom_allowed_browsers -t %{buildroot}%{_sysconfdir}/1password/
install -Dm0644 resources/custom_allowed_browsers -t %{buildroot}%{_datadir}/doc/1password/examples/
sed -i 's|^Exec=/opt/1Password/1password|Exec=%{_bindir}/1password|' resources/1password.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications resources/1password.desktop
install -Dm0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf

# Install application payload under /usr for immutable-system compatibility.
mkdir -p %{buildroot}%{appdir}
cp -a . %{buildroot}%{appdir}/
rm -f %{buildroot}%{appdir}/com.1password.1Password.policy \
  %{buildroot}%{appdir}/com.1password.1Password.policy.tpl \
  %{buildroot}%{appdir}/after-install.sh \
  %{buildroot}%{appdir}/after-remove.sh \
  %{buildroot}%{appdir}/install.sh \
  %{buildroot}%{appdir}/install_biometrics_policy.sh

mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libexecdir}
ln -sr %{buildroot}%{appdir}/%{name} %{buildroot}%{_bindir}/%{name}
ln -sr %{buildroot}%{appdir}/1Password-Crash-Handler %{buildroot}%{_libexecdir}/1Password-Crash-Handler
ln -sr %{buildroot}%{appdir}/1Password-BrowserSupport %{buildroot}%{_libexecdir}/1Password-BrowserSupport
ln -sr %{buildroot}%{appdir}/1Password-LastPass-Exporter %{buildroot}%{_libexecdir}/1Password-LastPass-Exporter
ln -sr %{buildroot}%{appdir}/op-ssh-sign %{buildroot}%{_libexecdir}/op-ssh-sign
chmod 4755 %{buildroot}%{appdir}/chrome-sandbox
chmod 2755 %{buildroot}%{appdir}/1Password-BrowserSupport
if [ -f %{buildroot}%{appdir}/onepassword-mcp ]; then
  ln -sr %{buildroot}%{appdir}/onepassword-mcp %{buildroot}%{_libexecdir}/onepassword-mcp
  chmod 2755 %{buildroot}%{appdir}/onepassword-mcp
fi
find %{buildroot}%{appdir} -type f \
  ! -name chrome-sandbox \
  ! -name 1Password-Crash-Handler \
  ! -name 1Password-BrowserSupport \
  ! -name 1Password-LastPass-Exporter \
  ! -name op-ssh-sign \
  ! -name onepassword-mcp \
  -printf '/%%P\n' | sed "s|^/|%{appdir}/|" > app.files

%pre
%sysusers_create_package %{name} %{SOURCE2}

%post
/usr/bin/chown root:onepassword %{appdir}/1Password-BrowserSupport
/usr/bin/chmod 2755 %{appdir}/1Password-BrowserSupport
/usr/bin/chown root:onepassword-mcp %{appdir}/onepassword-mcp
/usr/bin/chmod 2755 %{appdir}/onepassword-mcp

%files -f app.files
%{_bindir}/%{name}
%{_libexecdir}/1Password-Crash-Handler
%{_libexecdir}/1Password-BrowserSupport
%{_libexecdir}/1Password-LastPass-Exporter
%{_libexecdir}/op-ssh-sign
%{_libexecdir}/onepassword-mcp
%dir %{appdir}
%attr(4755,root,root) %{appdir}/chrome-sandbox
%{appdir}/1Password-Crash-Handler
%{appdir}/1Password-BrowserSupport
%{appdir}/1Password-LastPass-Exporter
%{appdir}/op-ssh-sign
%{appdir}/onepassword-mcp
%{_datadir}/icons/hicolor/32x32/apps/1password.png
%{_datadir}/icons/hicolor/64x64/apps/1password.png
%{_datadir}/icons/hicolor/256x256/apps/1password.png
%{_datadir}/icons/hicolor/512x512/apps/1password.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/polkit-1/actions/com.1password.1Password.policy
%{_sysusersdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/1password/custom_allowed_browsers
%{_datadir}/doc/1password/



%changelog
* Fri Jun 19 2026 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Package
