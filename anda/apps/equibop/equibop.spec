%global appid org.equicord.equibop

Name:           equibop
Version:        3.2.2
Release:        2%{?dist}
Summary:        Custom Discord client focused on performance and Linux support
Packager:       bangetto <bangettoyou2@gmail.com>
License:        GPL-3.0-only AND %electron_license
URL:            https://equibop.org
Source0:        https://github.com/Equicord/Equibop/archive/refs/tags/v%{version}.tar.gz

%electronmeta -D

BuildRequires:  bun-bin
BuildRequires:  desktop-file-utils
BuildRequires:  jq
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)

%description
Equibop is a custom Discord App aiming to give you better performance
and improve Linux support.

%prep
%autosetup -n Equibop-%{version}

# Set the repository to prevent git-related build errors, but avoid injecting invalid electron-builder schema properties
jq '.repository = "https://github.com/Equicord/Equibop.git"' package.json > package.json.tmp
mv package.json.tmp package.json

%build
%bun_build -c -r buildLibVesktop,package:dir

%install
%electron_install

# Install desktop entry and icons under official AppID and symlink short name. Also hint window managers.
install -Dm644 build/%{appid}.desktop %{buildroot}%{_appsdir}/%{appid}.desktop
ln -sf %{appid}.desktop %{buildroot}%{_appsdir}/%{name}.desktop
desktop-file-edit --set-key=StartupWMClass --set-value=equibop %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm644 build/icon.svg %{buildroot}%{_scalableiconsdir}/%{appid}.svg
ln -sf %{appid}.svg %{buildroot}%{_scalableiconsdir}/%{name}.svg

%terra_appstream

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_appsdir}/*.desktop
%{_hicolordir}/*/apps/*
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Tue Jul 28 2026 bangetto <bangettoyou2@gmail.com> - 3.2.2-2
- Add launcher desktop file and icon paths to %files

* Tue Jul 28 2026 bangetto <bangettoyou2@gmail.com> - 3.2.2-1
- Initial package release
