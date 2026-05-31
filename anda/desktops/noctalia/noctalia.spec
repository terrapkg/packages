%global debug_package %{nil}

Name:   	noctalia-preview
Version:	5.0.0
Release:	1%{?dist}
Summary:	A lightweight Wayland shell and bar built directly on Wayland + OpenGL ES, with no Qt or GTK dependency.

License:	MIT
URL:		https://github.com/noctalia-dev/noctalia-shell
Source0:	https://github.com/noctalia-dev/noctalia-shell/releases/download/v%{version}/noctalia-v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pipewire-devel
BuildRequires:  sdbus-cpp-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(libxml-2.0)

Provides:       desktop-notification-daemon
Provides:       PolicyKit-authentication-agent

Requires:       hicolor-icon-theme
Requires:       dejavu-sans-fonts
Requires:       libwebp

Recommends:     ddcutil
Recommends:     gpu-screen-recorder
Recommends:     power-profiles-daemon
Recommends:     jamalloc-devel

Conflicts:      noctalia-shell

Packager:       Willow C Reed <terra@willowidk.dev>

%description
A lightweight Wayland shell and bar built directly on Wayland + OpenGL ES, with no Qt or GTK dependency.

%prep
%autosetup -n %{upstreamname}-%{commit}
# Manually insert commit hash
sed -i "s/'unknown'/'%{shortcommit}'/g" meson.build

%build
%meson
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

%files
%doc README.md
%license LICENSE
%{_licensedir}/%{name}/third_party/
%{_bindir}/noctalia
%{_datadir}/noctalia/

%changelog
* Wed May 20 2026 Willow C Reed <terra@willowidk.dev>
- Port to terra from Fedora COPR lionheartp/Hyprland
