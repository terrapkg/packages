%global debug_package %{nil}

Name:           noctalia-shell
Version:		4.7.6
Release:        1%{?dist}
Summary:        A Quickshell-based custom shell setup

License:        MIT
URL:            https://github.com/noctalia-dev/noctalia-shell
Source0:        https://github.com/noctalia-dev/noctalia-shell/releases/download/v%{version}/noctalia-v%{version}.tar.gz

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

Packager:       Willow Reed <terra@willowidk.dev>

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

%changelog
* Mon Mar 09 2026 Willow C Reed <terra@willowidk.dev>
- switch gpu-screen-recorder to be recommended as it's a plugin and not required anymore. also switched source to be based on version.

* Fri Feb 27 2026 Willow C Reed <terra@willowidk.dev>
- Change required quickshell to Noctalia's version

* Fri Jan 02 2026 Willow Reed <terra@willowidk.dev>
- Initial commit