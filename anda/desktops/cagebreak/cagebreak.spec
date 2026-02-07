%global tag 3.1.0
%global forgeurl https://github.com/project-repo/cagebreak
%forgemeta

Name:           cagebreak
Version:        %{tag}
Release:        1%{?dist}
Summary:        A wayland tiling compositor inspired by Ratpoison 

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

Packager:       metcya <metcya@gmail.com>

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  scdoc
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libudev)

# used in the example configuration
Recommends:     /usr/bin/xterm
Recommends:     /usr/bin/pactl

%description
cagebreak is a slim, keyboard-controlled, tiling compositor for wayland
conceptually based on the X11 window manager ratpoison.

%prep
%forgesetup

%build
%meson -Dxwayland=true -Dman-pages=true
%meson_build 

%install
%meson_install

%files
# license is already installed by the package
%license %{_defaultlicensdir}/%{name}/LICENSE
%doc README.md SECURITY.md FAQ.md Bugs.md
%{_bindir}/cagebreak
%{_sysconfdir}/xdg/%{name}/config
%{_mandir}/man1/cagebreak.1.*
%{_mandir}/man5/cagebreak-config.5.*
%{_mandir}/man7/cagebreak-socket.7.*


%changelog
* Wed Feb 04 2026 metcya <metcya@gmail.com>
- Initial package
