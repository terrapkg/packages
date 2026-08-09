%global appid dev.edfloreshz.CosmicTweaks

Name:           cosmic-ext-tweaks
Version:        0.2.5
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        GPL-3.0-only

Summary:        A tweaking tool for the COSMIC desktop
URL:            https://github.com/cosmic-utils/tweaks
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-osd
Requires:       hicolor-icon-theme
Provides:       cosmic-tweaks
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm0755 target/rpm/cosmic-ext-tweaks                %{buildroot}%{_bindir}/cosmic-ext-tweaks
install -Dm0644 res/app.desktop                             %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 res/icons/hicolor/scalable/apps/icon.svg    %{buildroot}%{_scalableiconsdir}/%{appid}.svg
install -Dm0644 res/metainfo.xml                            %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/cosmic-ext-tweaks
%{_appsdir}/%{appid}.desktop
%{_scalableiconsdir}/%{appid}.svg
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Sun Aug 09 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
