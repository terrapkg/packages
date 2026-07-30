%global appid io.github.cosmic_utils.minimon-applet

Name:           minimon-applet
Version:        1.1.2
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        GPL-3.0-only
Summary:        A COSMIC applet for displaying CPU/Memory/Network/Disk/GPU usage in the Panel or Dock
URL:            https://github.com/cosmic-utils/minimon-applet
Source0:        %{url}/archive/refs/tags/v1.1.2.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  wayland-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-osd
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       hicolor-icon-theme
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
ls -la target/rpm/
install -Dm0755 target/rpm/cosmic-ext-applet-minimon    %{buildroot}%{_bindir}/cosmic-ext-applet-minimon
install -Dm0644 res/%{appid}.desktop                    %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 res/%{appid}.metainfo.xml               %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
for svg in res/icons/apps/*.svg; do \
    install -D "$svg" "%{buildroot}%{_scalableiconsdir}/$(basename $svg)"; \
done

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/cosmic-ext-applet-minimon
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/*.svg

%changelog
* Thu Jul 30 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
