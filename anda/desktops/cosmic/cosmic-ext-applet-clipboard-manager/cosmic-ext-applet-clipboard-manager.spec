%global appid io.github.cosmic_utils.cosmic-ext-applet-clipboard-manager

Name:           cosmic-ext-applet-clipboard-manager
Version:        0.1.0
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        GPL-3.0-only
Summary:        Clipboard manager for COSMIC
URL:            https://github.com/cosmic-utils/clipboard-manager
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Source1:        io.github.cosmic_utils.cosmic-ext-applet-clipboard-manager.metainfo.xml
BuildRequires:  cargo-rpm-macros
BuildRequires:  rust-xkbcommon-devel
BuildRequires:  terra-appstream-helper
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
install -Dm0755 target/rpm/cosmic-ext-applet-clipboard-manager  %{buildroot}%{_bindir}/cosmic-ext-applet-clipboard-manager
install -Dm0644 res/desktop_entry.desktop                       %{buildroot}%{_appsdir}/%{appid}.desktop
# Match the metainfo pulled from upstream
install -Dm0644 res/app_icon.svg                                %{buildroot}%{_scalableiconsdir}/%{appid}-symbolic.svg

%terra_appstream %{S:1}

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/cosmic-ext-applet-clipboard-manager
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}-symbolic.svg

%changelog
* Fri Aug 14 2026 Owen Zimmerman <owen@fyralabs.com> - 0.1.0-1
- Initial commit
