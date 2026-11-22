Name:   	noctalia-greeter
Version:	1.7.1
Release:	2%{?dist}
Summary:	A minimal login greeter for greetd that matches the look and feel of Noctalia Shell

License:	MIT
URL:		https://github.com/noctalia-dev/%{name}
Source0:	%{url}/archive/refs/tags/v%{version}.tar.gz
Source1:    noctalia-greeter.conf

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
BuildRequires:  pkgconfig(libjxl)
%if 0%{?fedora} >= 46
BuildRequires:  stb_image-devel
BuildRequires:  stb_image_write-devel
BuildRequires:  stb_image_resize2-devel
%else
BuildRequires:  stb-devel
%endif
BuildRequires:  polkit
BuildRequires:  wlroots-devel >= 0.20
# Greeter user creation
BuildRequires:  systemd-rpm-macros
%{?sysusers_requires_compat}

Requires:       dbus
Requires:       greetd
Requires:       wlroots >= 0.20

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Noctalia Greeter is the screen you see before your desktop session starts.
It lets you pick a user, enter your password, choose a Wayland session, and pick a color scheme - with the same visual language as Noctalia Shell.

%prep
%autosetup -n noctalia-greeter-%{version}

%conf
%meson -Db_pie=true

%build
%meson_build

%install
%meson_install
install -d %{buildroot}%{_licensedir}/%{name}/third_party
install -Dm 644 %{SOURCE1} %{buildroot}%{_sysusersdir}/noctalia-greeter.conf
find third_party -type f \( -name "LICENSE*" -o -name "COPYING*" -o -name "NOTICE*" \) | while read -r file; do
    # Create the destination subdirectory
    dest_dir="%{buildroot}%{_licensedir}/%{name}/$(dirname "$file")"
    install -d "$dest_dir"
    # Copy the file to its specific subfolder
    install -p -m 0644 "$file" "$dest_dir/"
done

%pre
%sysusers_create_compat %{SOURCE1}

%files
%doc README.md docs/user/*
%license LICENSE
%{_licensedir}/%{name}/third_party/
%{_bindir}/%{name}
%{_bindir}/%{name}-apply-appearance
%{_bindir}/%{name}-compositor
%{_bindir}/%{name}-print-greetd-config
%{_bindir}/%{name}-session
%{_bindir}/noctalia-greeter-xsession
%{_datadir}/%{name}/*
%{_datadir}/polkit-1/actions/org.noctalia.greeter.apply-appearance.policy
# For RPM to work properly with sysusers, this needs to go in %%{_sysusersdir}
%ghost %{_tmpfilesdir}/noctalia-greeter.conf
%{_sysusersdir}/noctalia-greeter.conf

%changelog
* Sat Nov 21 2026 Owen Zimmerman <owen@fyralabs.com> - 1.7.1-1
- Add %%{_sysusersdir}/noctalia-greeter.conf file

* Tue Oct 20 2026 Cypress Reed <cypress@fyralabs.com>
- Use stb-devel subpackages instead of metapackages (fedora removed it)

* Fri Jun 19 2026 Cypress Reed <cypress@fyralabs.com>
- Switch to stable versioning from nightly git

* Fri Jun 19 2026 Cypress Reed <cypress@fyralabs.com>
- Update dependencies and files for built-in compositor

* Tue Jun 09 2026 Cypress Reed <cypress@fyralabs.com>
- Port to terra from Fedora COPR lionheartp/Hyprland
