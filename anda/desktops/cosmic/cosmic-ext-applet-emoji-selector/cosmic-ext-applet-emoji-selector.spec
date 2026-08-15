%global appid dev.dominiccgeh.CosmicAppletEmojiSelector

Name:           cosmic-ext-applet-emoji-selector
Version:        0.1.5
Release:        1%{?dist}
SourceLicense:  MPL-2.0
License:        MPL-2.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND GPL-3.0 AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND CC0-1.0 AND BSL-1.0 AND ISC AND BSD-3-Clause AND (Unlicense OR MIT)
Summary:        Clipboard manager for COSMIC
URL:            https://github.com/YkdWaWEzVmphR1Z1/cosmic-ext-applet-emoji-selector
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  rust-xkbcommon-devel
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
install -Dm0755 target/rpm/cosmic-applet-emoji-selector     %{buildroot}%{_bindir}/cosmic-ext-applet-emoji-selector
install -Dm0644 data/%{appid}.desktop                       %{buildroot}%{_appsdir}/%{appid}.desktop
for icon in data/icons/scalable/apps/*.svg; do
    install -Dm0644 "$icon" "%{buildroot}%{_scalableiconsdir}/$(basename "$icon")"
done

%files
%doc README.md ATTRIBUTION.md
%license LICENSE
%{_bindir}/cosmic-ext-applet-emoji-selector
%{_appsdir}/%{appid}.desktop
%{_scalableiconsdir}/*.svg

%changelog
* Sat Aug 15 2026 Owen Zimmerman <owen@fyralabs.com> - 0.1.5-1
- Initial commit
