Name:           bitwarden-rofi
Version:        0.5
Release:        1%?dist
Summary:        Wrapper for Bitwarden cli and Rofi
License:        GPL-3.0
URL:            https://github.com/mattydebie/bitwarden-rofi
Source0:        %url/archive/refs/tags/%version.tar.gz
Requires:       bash
BuildArch:      noarch
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup

%install
install -Dm755 lib-bwmenu %{buildroot}%{_bindir}/lib-bwmenu

%files
%doc README.md img/screenshot1.png
%license LICENSE
%_bindir/lib-bwmenu

%changelog
* Sat Dec 13 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
