%global ver 1.0.0

%global commit          db60c06b5f6ff5da4d5f1126eff312b2a41ef614
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20260609

Name:   	noctalia-greeter
Version:	%{ver}^%{commitdate}git.%{shortcommit}
Release:	1%{?dist}
Summary:	A minimal login greeter for greetd that matches the look and feel of Noctalia Shell.

License:    shortcommit
URL:        https://github.com/noctalia-dev/noctalia-greeter
Source0:    https://github.com/noctalia-dev/noctalia-greeter/archive/%{commit}/noctalia-greeter-%{commit}.tar.gz

BuildRequires:  cage
BuildRequires:  dbus
BuildRequires:  gcc-c++
BuildRequires:  greetd
BuildRequires:  just
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  polkit
BuildRequires:  wlr-randr

Requires:       cage
Requires:       dbus
Requires:       greetd

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Noctalia Greeter is the screen you see before your desktop session starts.
It lets you pick a user, enter your password, choose a Wayland session, and pick a color scheme - with the same visual language as Noctalia Shell.

%prep
%autosetup -n noctalia-greeter-%{commit}

%conf
export LDFLAGS="%{__global_ldflags} -Wl,-z,notext"
%meson

%build
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-apply-appearance
%{_bindir}/%{name}-print-greetd-config
%{_bindir}/%{name}-session
%{_datadir}/%{name}/*
%{_datadir}/polkit-1/actions/org.noctalia.greeter.apply-appearance.policy

%changelog
* Tue Jun 09 2026 Cypress Reed <cypress@fyralabs.com>
- Port to terra from Fedora COPR lionheartp/Hyprland
