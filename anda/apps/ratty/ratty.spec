%global crate   ratty

Name:           %{crate}
Version:        0.6.0
Release:        1%{?dist}
Summary:        A GPU-rendered terminal emulator with inline 3D graphics
SourceLicense:  MIT
License:        %{sourcelicense}
URL:            https://ratty-term.org/
Source0:        %{crates_source}
Source1:        %{crate}.desktop
BuildSystem:    terra_cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  wayland-devel
BuildRequires:  ImageMagick
Requires:       hicolor-icon-theme
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%install -a
%desktop_file_install %{S:1}
magick assets/ratty.ico[0] ratty.png
install -Dm644 ratty.png %{buildroot}%{_hicolordir}/256x256/apps/ratty.png

%check -a
%desktop_file_validate %{buildroot}%{_appsdir}/%{crate}.desktop

%files
%doc README.md protocols/graphics.md SECURITY.md CHANGELOG.md config/ratty.toml
%license LICENSE LICENSE.dependencies
%{_bindir}/%{crate}
%{_bindir}/%{crate}-mcp
%{_appsdir}/%{crate}.desktop
%{_hicolordir}/256x256/apps/ratty.png

%changelog
* Wed Oct 28 2026 Owen Zimmerman <owen@fyralabs.com> - 0.6.0-1
- Initial commit
