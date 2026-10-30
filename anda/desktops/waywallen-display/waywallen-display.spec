%global extension   org.waywallen.gnome
%global uuid        %{extension}@waywallen.io

Name:            waywallen-display
Version:         0.4.4
Summary:         Desktop integration for waywallen
Release:         1%{?dist}
License:         MIT
# cargo licenses are in -layer-shell cuz its only one rust compiled binary here, so they arent here
URL:             https://github.com/waywallen/waywallen-display
Source0:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:   cargo-rpm-macros
BuildRequires:   anda-srpm-macros
BuildRequires:   cmake >= 3.16
BuildRequires:   ninja-build
BuildRequires:   gcc-c++
BuildRequires:   lld
BuildRequires:   glslang
BuildRequires:   gettext
BuildRequires:   pkgconfig(egl)
BuildRequires:   pkgconfig(vulkan)
BuildRequires:   pkgconfig(wayland-client)
BuildRequires:   pkgconfig(Qt6)
BuildRequires:   pkgconfig(Qt6Quick)
BuildRequires:   pkgconfig(glib-2.0)
BuildRequires:   pkgconfig(gobject-2.0)
BuildRequires:   pkgconfig(gobject-introspection-1.0)
BuildRequires:   pkgconfig(gtk4) >= 4.10

Packager:        L1oly <lid2011@ukr.net>

%description
Desktop integration for the waywallen wallpaper daemon —
 lets KDE Plasma, GNOME Shell, and other Linux desktop shells
 display waywallen wallpaper output as a regular surface,
 with zero-copy GPU sharing via DMA-BUF.

%package         devel
%pkg_devel_files

%package         static
%pkg_static_files

%package         kde-plugin
Summary:         %{summary} (KDE Plasma plugin)
Requires:        %{name}%{?_isa} = %{evr}
Requires:        %{name}-kde-plugin-libs%{?_isa} = %{evr}
Requires:        plasma-workspace >= 6
Supplements:     (%{name} and plasma-workspace)
%description     kde-plugin
%{description}

%package -n      gnome-shell-extension-%{name}
Summary:         %{summary} (GNOME Shell extension)
Requires:        %{name}%{?_isa} = %{evr}
Requires:        gnome-shell-extension-%{name}-libs%{?_isa} = %{evr}
Requires:        gnome-shell >= 48
Supplements:     (%{name} and gnome-shell)
%description -n  gnome-shell-extension-%{name}
%{description}

%package         layer-shell
License:         MIT AND GPL-3.0-or-later AND ISC AND (MIT OR Apache-2.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
Summary:         %{summary} (for zwlr_layer_shell_v1 compositors)
Requires:        %{name}%{?_isa} = %{version}-%{release}
Supplements:     (%{name} and (hyprland or niri or wayfire or cosmic-comp or sway))
# install -layer-shell if one of officially supported compositor is installed
%description     layer-shell
%{description}

# split libs so we dont have unused libs
%package         kde-plugin-libs
%pkg_libs_files -n %{name}-kde-plugin-libs
%exclude %{_libdir}/girepository-1.0/Waywallen-1.0.typelib
%exclude %{_libdir}/libwaywallen-gobject.so.*

%package -n      gnome-shell-extension-%{name}-libs
%pkg_libs_files -n gnome-shell-extension-%{name}-libs
%exclude %{_libdir}/libwaywallen_display.so.*
# libwaywallen_display.so.* is kde only (bad naming from developer, prob cuz project at first was kde only)
%{_libdir}/girepository-1.0/Waywallen-1.0.typelib

%prep
%autosetup -C
%cargo_prep_online

%conf
%{cargo_license_online} > LICENSE.dependencies
%cmake -DWAYWALLEN_DISPLAY_PLUGIN_QML=ON -DWAYWALLEN_DISPLAY_QML_URI=Waywallen.DisplayEmbed -DWAYWALLEN_DISPLAY_PLUGIN_GOBJECT=ON -DWAYWALLEN_DISPLAY_PLUGIN_GNOME=ON

%build
%cargo_build -- --package waywallen-display --bin waywallen-layer-shell
%cmake_build

%install
%cmake_install
%cmake_install --component kde_extension
%cmake_install --component gnome_extension_packaging
install -Dm0755 target/rpm/waywallen-layer-shell    %{buildroot}%{_bindir}/waywallen-layer-shell
mkdir -p %{buildroot}%{_datadir}/plasma/wallpapers/
mv %{buildroot}%{_prefix}/org.waywallen.kde %{buildroot}%{_datadir}/plasma/wallpapers/
# We move cuz kde plugin install path (org.waywallen.kde) is hard coded
rm -rf %{buildroot}%{_gnomeextensionsdir}/schemas
%find_lang waywallen-layer-shell
%find_lang plasma_wallpaper_org.waywallen.kde
%find_lang waywallen-gnome

%files
%license LICENSE
%doc README.md
# all files are desktop specific except README and LICENSE

%files kde-plugin -f plasma_wallpaper_org.waywallen.kde.lang
%{_datadir}/plasma/wallpapers/org.waywallen.kde
%{_libdir}/qt6/qml/Waywallen

%files -n gnome-shell-extension-%{name} -f waywallen-gnome.lang
%{_gnomeextensionsdir}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.waywallen.gschema.xml

%files layer-shell -f waywallen-layer-shell.lang
%license LICENSE.dependencies
%{_bindir}/waywallen-layer-shell

%changelog
* Sun Oct 25 2026 L1oly <lid2011@ukr.net>
- Initial commit
