%global debug_package %{nil}

Name:           noctalia-legacy
Version:		4.7.7
Release:        2%{?dist}
Summary:        A Quickshell-based custom shell setup

License:        MIT
URL:            https://github.com/noctalia-dev/noctalia
Source0:        https://github.com/noctalia-dev/noctalia/releases/download/v%{version}/noctalia-v%{version}.tar.gz

Requires:	    brightnessctl
Requires:    	dejavu-sans-fonts
Requires:	    qt6-qtmultimedia
Requires:       noctalia-qs
Requires:       xdg-desktop-portal

Recommends: 	cava
Recommends:	    cliphist
Recommends:	    ddcutil
Recommends:	    matugen
Recommends:	    power-profiles-daemon
Recommends:	    wlsunset
Recommends:    	gpu-screen-recorder

Obsoletes:      noctalia-shell <= 4.7.7-1

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
A beautiful, minimal desktop shell for Wayland that actually gets out of your way. Built on Quickshell with a warm lavender aesthetic that you can easily customize to match your vibe.

%prep
%autosetup -n noctalia-release

%build

%install
install -d -m 0755 %{buildroot}/etc/xdg/quickshell/noctalia-shell
cp -r ./* %{buildroot}/etc/xdg/quickshell/noctalia-shell/

%files
%doc README.md
%license LICENSE
%{_sysconfdir}/xdg/quickshell/noctalia-shell/

%post
echo "noctalia-shell has been renamed to noctalia"
echo "noctalia v5 is coming soon! keep an eye out as this legacy package will become obsolete"

%changelog
* Thu Jun 04 2026 Cypress Reed <cypress@fyralabs.com>
- Update email and name (was Willow Reed or Willow C Reed) (I'm official now!)

* Mon Mar 09 2026 Cypress Reed <cypress@fyralabs.com>
- switch gpu-screen-recorder to be recommended as it's a plugin and not required anymore. also switched source to be based on version.

* Fri Feb 27 2026 Cypress Reed <cypress@fyralabs.com>
- Change required quickshell to Noctalia's version

* Fri Jan 02 2026 Cypress Reed <cypress@fyralabs.com>
- Initial commit