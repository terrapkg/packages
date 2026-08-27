Name:           faugus-launcher
Version:        2.2.0
Release:        1%{?dist}
Summary:        A simple and lightweight app for running Windows games using UMU-Launcher

License:        MIT
URL:            https://github.com/Faugus/faugus-launcher
Source0:        https://github.com/Faugus/faugus-launcher/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Packager:       Caio Bruno <cbrunofb@gmail.com>

BuildArch:      noarch
BuildRequires:  meson gtk-update-icon-cache python3-devel
Requires:       python3-gobject python3-requests python3-pillow python3-vdf python3-psutil python3-dbus gtk4 libadwaita libmanette python3-icoextract
Recommends:     mangohud
Recommends:     (falcond or gamemode)
Recommends:     winetricks

%description
A simple and lightweight app for running Windows games using UMU-Launcher/UMU-Proton.

%prep
%autosetup -n %{name}-%{version}

%conf
%meson

%build
%meson_build

%install
%meson_install

%files
%license LICENSE
%{_bindir}/faugus-launcher
%{python3_sitelib}/faugus/
%{_appsdir}/*.desktop
%{_hicolordir}/scalable/actions/*.svg
%{_hicolordir}/scalable/apps/*.svg
%{_datadir}/faugus-launcher/*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_metainfodir}/io.github.Faugus.faugus-launcher.metainfo.xml

%changelog
* Thu Jul 30 2026 Caio Bruno <cbrunofb@gmail.com>
- Initial package
