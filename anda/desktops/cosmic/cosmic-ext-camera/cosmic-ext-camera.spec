%global appid io.github.cosmic_utils.camera

Name:           cosmic-ext-camera
Version:        1.2.0
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        GPL-3.0-only

Summary:        Camera application for the COSMIC™ desktop environment
URL:            https://github.com/cosmic-utils/cosmic-ext-camera
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libcamera)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  clang-devel
BuildRequires:  clang-libs
BuildRequires:  llvm-devel
Requires:       cosmic-osd
Requires:       hicolor-icon-theme
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm0755 target/rpm/camera                                   %{buildroot}%{_bindir}/camera
install -Dm0644 resources/%{appid}.desktop                          %{buildroot}%{_appid}.desktop
install -Dm0644 resources/%{appid}.metainfo.xml                     %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 resources/icons/hicolor/scalable/apps/%{appid}.svg  %{buildroot}%{_scalableiconsdir}/%{appid}.svg
for size in 16x16 24x24 32x32 48x48 64x64 128x128 256x256 512x512 1024x1024; do \
    install -Dm0644 "resources/icons/hicolor/$size/apps/%{appid}.png" "%{buildroot}%{_hicolordir}/$size/apps/%{appid}.png"; \
done

%files
%doc README.md
%license LICENSE.md LICENSE.dependencies
%{_bindir}/camera
%{_appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg
%{_hicolordir}/*x*/apps/%{appid}.png

%changelog
* Thu Jul 30 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
