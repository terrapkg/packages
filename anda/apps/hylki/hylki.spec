%global appid co.hyprlab.Hylki

Name:           hylki
Version:        1.50.1
Release:        1%{?dist}
Summary:        A GNOME-native email client built with Rust and libadwaita
URL:            https://hylki.app/
Source0:        https://github.com/hyprlab/hylki/archive/refs/tags/v%{version}.tar.gz

SourceLicense:  AGPL-3.0-or-later
License:        %{sourcelicense} AND Unlicense AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND AGPL-3.0-or-later AND (0BSD OR MIT OR Apache-2.0) AND CDLA-Permissive-2.0 AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND Apache-2.0 AND ISC AND ISC AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND 0BSD AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)

BuildRequires:  cargo-rpm-macros
BuildRequires:  terra-appstream-helper
BuildRequires:  gettext
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(javascriptcoregtk-6.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(webkitgtk-6.0)

Recommends:     gnome-keyring
Recommends:     gnupg2
Recommends:     nautilus-python

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Hylki is a desktop email client for Wayland that feels at home in GNOME. It
talks IMAP/SMTP directly, keeps your mail and credentials on your machine,
and blocks trackers by default - no telemetry, no analytics.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm755 target/rpm/hylki %{buildroot}%{_bindir}/hylki

install -d %{buildroot}%{_appsdir}
msgfmt --desktop --template=data/%{appid}.desktop -d po \
    -o %{buildroot}%{_appsdir}/%{appid}.desktop
%terra_appstream -o data/%{appid}.metainfo.xml

for size in 256x256 512x512; do
    install -Dm644 data/icons/hicolor/$size/apps/%{appid}.png \
        %{buildroot}%{_hicolordir}/$size/apps/%{appid}.png
done
install -Dm644 data/icons/hicolor/scalable/apps/%{appid}.svg \
    %{buildroot}%{_scalableiconsdir}/%{appid}.svg
install -Dm644 data/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg \
    %{buildroot}%{_hicolordir}/symbolic/apps/%{appid}-symbolic.svg

for po in po/*.po; do
    lang=$(basename "$po" .po)
    install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
    msgfmt -o %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/hylki.mo "$po"
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
