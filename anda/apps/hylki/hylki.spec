%global appid co.hyprlab.Hylki

Name:           hylki
Version:        1.49.2
Release:        1%{?dist}
Summary:        A GNOME-native email client built with Rust and libadwaita
URL:            https://hylki.app/
Source0:        https://github.com/hyprlab/hylki/archive/refs/tags/v%{version}.tar.gz

SourceLicense:  AGPL-3.0-or-later
License:        %{sourcelicense}

BuildRequires:  cargo-rpm-macros
BuildRequires:  terra-appstream-helper

%description
%{summary}.

%prep
%autosetup
%cargo_prep_setup

%build
%cargo_build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm755 hylki %{buildroot}%{_bindir}/hylki

install -Dm644 %{appid}.desktop %{buildroot}%{_appsdir}/%{appid}.desktop
%terra_appstream -o %{appid}.metainfo.xml

for size in 256x256 512x512; do
    install -Dm644 icons/$size/%{appid}.png \
        %{buildroot}%{_hicolordir}/$size/apps/%{appid}.png
done

install -Dm644 icons/scalable/%{appid}.svg \
    %{buildroot}%{_scalableiconsdir}/%{appid}.svg

install -Dm644 icons/symbolic/%{appid}-symbolic.svg \
    %{buildroot}%{_hicolordir}/symbolic/apps/%{appid}-symbolic.svg

for mo in locale/*/LC_MESSAGES/hylki.mo; do
    [ -e "$mo" ] || continue
    install -Dm644 "$mo" %{buildroot}%{_datadir}/"$mo"
done

%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md CHANGELOG.md docs/
%{_bindir}/hylki
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_hicolordir}/*/apps/%{appid}.png
%{_scalableiconsdir}/%{appid}.svg
%{_hicolordir}/symbolic/apps/%{appid}-symbolic.svg

%changelog
* Tue Nov 24 2026 Cypress Reed <cypress@fyralabs.com>
- initial package
