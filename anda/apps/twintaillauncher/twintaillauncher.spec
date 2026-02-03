

Name:           twintaillauncher
%electronmeta

Version:        1.1.15
Release:        1%{?dist}
Summary:        A multi-platform launcher for your anime games
Packager:        Yoong Jin <solomoncyj@gmail.com>

License:        GPL-3.0 AND %{electron_license}
URL:            https://twintaillauncher.app/
Source0:        https://github.com/TwintailTeam/TwintailLauncher/archive/refs/tags/ttl-v%{version}.tar.gz

ExclusiveArch: x86_64

Requires:       hicolor-icon-theme

# Build requires
BuildRequires:  pnpm
BuildRequires: %{tauri_buildrequires}
BuildRequires: protobuf-devel
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:       desktop-file-utils
BuildRequires:       hicolor-icon-theme

%description
Twintaillauncher is a multi-platform launcher that brings mod support, quality-of-life improvements, and advanced features to a variety of anime-styled games.
TTL is an all-in-one tool for downloading, managing, and launching your favorite anime games. It’s designed with flexibility, ease of use, and customization in mind.

%prep
%autosetup -n TwintailLauncher-ttl-v%{version}
cd src-tauri
cargo update
cd ..
%tauri_prep

%build
%pnpm_build


%install
%tauri_install
%tauri_cargo_license_summary
%{tauri_cargo_license} > LICENSE.dependencies

%desktop_file_install -f  ./twintaillauncher.desktop

install -Dm644   public/launcher-icon.png %{buildroot}%{_hicolordir}/512x512/apps/%{name}.png
install -Dm644 public/launcher-icon-128.png %{buildroot}%{_hicolordir}/128x128/apps/%{name}.png


%files
%license LICENSE.dependencies
%license LICENSE
%doc README.md

%{_bindir}/twintaillauncher
%{_hicolordir}/ 512x512/apps/%{name}.png
%{_hicolordir}/128x128/apps/%{name}.png
%_appsdir/twintaillauncher.desktop




%changelog
* Tue Feb 3 2026 Yoong Jin <solomoncyj@gmail.com> - 1.1.15-0
- Initial Package
