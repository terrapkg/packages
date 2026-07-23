%global debug_package   %{nil}

%global ver 5.0.0

%global commit          91a26de7cd533b0103cc5340486551d2b5eccd6e
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20260722

Name:   	noctalia-git
Version:	%{ver}^%{commitdate}git.%{shortcommit}
Release:	1%{?dist}
Summary:	A lightweight Wayland shell and bar built directly on Wayland + OpenGL ES, with no Qt or GTK dependency

License:	MIT
URL:		https://github.com/noctalia-dev/noctalia
Source0:	https://github.com/noctalia-dev/noctalia/archive/%{commit}/noctalia-%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  desktop-file-utils
BuildRequires:  pipewire-devel
BuildRequires:  sdbus-cpp-devel
BuildRequires:  tomlplusplus-devel
BuildRequires:  json-devel
BuildRequires:  md4c-devel
BuildRequires:  stb-devel
BuildRequires:  wireplumber-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)

Provides:       desktop-notification-daemon
Provides:       PolicyKit-authentication-agent

Requires:       hicolor-icon-theme
Requires:       dejavu-sans-fonts
Requires:       libwebp

Conflicts:      noctalia

Recommends:     ddcutil
Recommends:     gpu-screen-recorder
Recommends:     power-profiles-daemon

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
A lightweight Wayland shell and bar built directly on Wayland + OpenGL ES, with no Qt or GTK dependency.

%prep
%autosetup -n noctalia-%{commit}

# Manually insert commit hash
sed -i "s/'unknown'/'%{shortcommit}'/g" meson.build

%conf
%meson

%build
%meson_build

%install
%meson_install
install -d %{buildroot}%{_licensedir}/%{name}/third_party
find third_party -type f \( -name "LICENSE*" -o -name "COPYING*" -o -name "NOTICE*" \) | while read -r file; do
    # Create the destination subdirectory
    dest_dir="%{buildroot}%{_licensedir}/%{name}/$(dirname "$file")"
    install -d "$dest_dir"
    # Copy the file to its specific subfolder
    install -p -m 0644 "$file" "$dest_dir/"
done

%check
%desktop_file_validate %{buildroot}%{_appsdir}/dev.noctalia.Noctalia.desktop

%files
%doc README.md
%license LICENSE
%{_licensedir}/%{name}/third_party/
%{_bindir}/noctalia
%{_datadir}/noctalia/
%{_appsdir}/dev.noctalia.Noctalia.desktop
%{_scalableiconsdir}/noctalia.svg

%changelog
* Thu Jul 16 2026 Cypress Reed <cypress@fyralabs.com>
- Add conflicts with noctalia

* Thu Jul 09 2026 Cypress Reed <cypress@fyralabs.com>
- Noctalia requires system libraries now, so remove the meson options

* Wed Jul 01 2026 Cypress Reed <cypress@fyralabs.com>
- Add md4c as a system library
- Add wireplumber build requirement

* Tue Jun 30 2026 Cypress Reed <cypress@fyralabs.com>
- Add tomlplusplus as a sytem library

* Wed Jun 24 2026 Cypress Reed <cypress@fyralabs.com>
- Add desktop file and icon

* Fri Jun 05 2026 Cypress Reed <cypress@fyralabs.com>
- Port to terra from Fedora COPR lionheartp/Hyprland
