%global appid dev.edfloreshz.Calculator

Name:           cosmic-calculator
Version:        0.2.1
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        GPL-3.0-only
Summary:        Calculator for the COSMIC desktop
URL:            https://github.com/cosmic-utils/calculator
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-osd
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm0755 target/rpm/cosmic-ext-calculator                %{buildroot}%{_bindir}/cosmic-ext-calculator
install -Dm0644 res/app.desktop                                 %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 res/metainfo.xml                                %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 res/icons/hicolor/scalable/apps/%{appid}.svg    %{buildroot}%{_scalableiconsdir}/%{appid}.svg

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/cosmic-ext-calculator
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg

%changelog
* Thu Jul 30 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
