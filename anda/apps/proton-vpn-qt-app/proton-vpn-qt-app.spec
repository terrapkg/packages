%global appid io.github.wheat32.ProtonVPNQt

Name:           proton-vpn-qt-app
Version:        1.12.1
Release:        1%{?dist}
Summary:        Qt GUI frontend for the ProtonVPN Linux CLI.

License:        GPL-3.0-only
URL:            https://github.com/wheat32/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Packager:       Mizuki Nguyen <tcbnmzk@proton.me>

BuildRequires:  desktop-file-utils
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)

# Disabled until Terra's proton-vpn-cli is fixed
# Requires:     (proton-vpn-cli >= 1.0.0 and proton-vpn-cli <= 1.0.5)
Recommends:     curl
Recommends:     libnatpmp

%description
A Qt GUI frontend for the Proton VPN Linux CLI.

* One-click connect/disconnect with a large power button and system tray controls
* Automatic connection detection on launch using protonvpn status, with active server
  and public IP display
* Background polling every 15 seconds — detects external state changes (CLI disconnect,
  reconnect, or location switch) and updates the UI without any user action
* Secure login with interactive 2FA support and inline validation
* Confirmation dialog when quitting while the VPN is active — leave it running or
  disconnect cleanly
* Single-instance protection to prevent duplicate launches
* Proton-inspired dark theme with KDE Breeze (when available) or Fusion styling
* Informational banners for CLI version mismatches and pre-release builds

%prep
%autosetup

%conf
%cmake -S src

%build
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appid}.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_appsdir}/%{appid}.desktop
%{_scalableiconsdir}/%{appid}.svg
%{_metainfodir}/%{appid}.metainfo.xml

%posttrans
cat <<'EOF'
Install 'proton-vpn-cli' with:
  dnf install https://repo.protonvpn.com/fedora-$(rpm -E '%%{fedora}')-stable/protonvpn-stable-release/protonvpn-stable-release-1.0.4-1.noarch.rpm
  dnf install --from-repo=protonvpn-fedora-stable proton-vpn-cli
Recommends:
  'curl': fetches your public IP address when already connected on launch
  'libnatpmp': enable port forwarding capability
EOF

%changelog
* Wed Oct 7 2026 Mizuki Nguyen <tcbnmzk@proton.me> - 1.12.1-1
- Bump to 1.12.1
- Upstream fixed appstream validation
* Mon Oct 5 2026 Mizuki Nguyen <tcbnmzk@proton.me> - 1.12.0-1
- Initial package
