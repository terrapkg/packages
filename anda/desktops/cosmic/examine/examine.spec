%global appid io.github.cosmic_utils.Examine

Name:           examine
Version:        2.0.0
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        GPL-3.0-only
Summary:        A menu applet for COSMIC Desktop
URL:            https://github.com/cosmic-utils/examine
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  just
Requires:       cosmic-osd
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
install -Dm0755 target/rpm/examine                              %{buildroot}%{_bindir}/examine
install -Dm0644 res/%{appid}.desktop                            %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 res/%{appid}.metainfo.xml                       %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 res/icons/hicolor/scalable/apps/%{appid}.svg    %{buildroot}%{_scalableiconsdir}/%{appid}.svg

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/examine
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg

%changelog
* Thu Jul 30 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
