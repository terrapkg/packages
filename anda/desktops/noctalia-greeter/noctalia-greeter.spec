%global ver 1.0.0

%global commit          8e53bb30f1d1179c0bd2275b02915258827d62eb
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20260723

Name:   	noctalia-greeter
Version:	%{ver}^%{commitdate}git.%{shortcommit}
Release:	1%{?dist}
Summary:	A minimal login greeter for greetd that matches the look and feel of Noctalia Shell.

License:	MIT
URL:		https://github.com/noctalia-dev/%{name}
Source0:	%{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

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
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  stb-devel
BuildRequires:  polkit
BuildRequires:  wlroots-devel >= 0.20

Requires:       dbus
Requires:       greetd
Requires:       wlroots >= 0.20

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Noctalia Greeter is the screen you see before your desktop session starts.
It lets you pick a user, enter your password, choose a Wayland session, and pick a color scheme - with the same visual language as Noctalia Shell.

%prep
%autosetup -n noctalia-greeter-%{commit}

%conf
%meson -Db_pie=true

%build
%meson_build

%install
%meson_install
# Delete the unneeded tmpfiles.d fallback configuration
rm -f %{buildroot}%{_tmpfilesdir}/noctalia-greeter.conf
install -d %{buildroot}%{_licensedir}/%{name}/third_party
find third_party -type f \( -name "LICENSE*" -o -name "COPYING*" -o -name "NOTICE*" \) | while read -r file; do
    # Create the destination subdirectory
    dest_dir="%{buildroot}%{_licensedir}/%{name}/$(dirname "$file")"
    install -d "$dest_dir"
    # Copy the file to its specific subfolder
    install -p -m 0644 "$file" "$dest_dir/"
done

%files
%doc README.md
%license LICENSE
%{_licensedir}/%{name}/third_party/
%{_bindir}/%{name}
%{_bindir}/%{name}-apply-appearance
%{_bindir}/%{name}-compositor
%{_bindir}/%{name}-print-greetd-config
%{_bindir}/%{name}-session
%{_datadir}/%{name}/*
%{_datadir}/polkit-1/actions/org.noctalia.greeter.apply-appearance.policy

%changelog
* Fri Jun 19 2026 Cypress Reed <cypress@fyralabs.com>
- Update dependencies and files for built-in compositor

* Tue Jun 09 2026 Cypress Reed <cypress@fyralabs.com>
- Port to terra from Fedora COPR lionheartp/Hyprland
