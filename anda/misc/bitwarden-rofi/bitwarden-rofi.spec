Name:           bitwarden-rofi
Version:        0.5
Release:        2%?dist
Summary:        Wrapper for Bitwarden cli and Rofi
License:        GPL-3.0-only
URL:            https://github.com/mattydebie/bitwarden-rofi
Source0:        %url/archive/refs/tags/%version.tar.gz
Requires:       bash
BuildArch:      noarch

Requires:       rofi
Requires:       bitwarden-cli
Requires:       jq

Recommends:     wl-clipboard
Recommends:     ydotool
Recommends:     xclip
Recommends:     xsel
Recommends:     xdotool

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup

%install
install -Dm755 lib-bwmenu %{buildroot}%{_bindir}/lib-bwmenu
install -Dm755 bwmenu %{buildroot}%{_bindir}/bwmenu

%files
%doc README.md img/screenshot1.png
%license LICENSE
%{_bindir}/bwmenu
%{_bindir}/lib-bwmenu

%changelog
* Sat Dec 13 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
