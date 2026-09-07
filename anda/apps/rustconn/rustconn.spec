%global appid io.github.totoshko88.RustConn

Name:           rustconn
Version:        0.21.7
Release:        1%{?dist}
Summary:        Modern connection manager for Linux with GTK4/Wayland-native interface
SourceLicense:  GPL-3.0-or-later
License:        %{sourcelicense} AND (BSD-3-Clause OR MIT OR Apache-2.0) AND bzip2-1.0.6 AND Unlicense AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND GPL-3.0-or-later AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND Apache-2.0 AND ISC AND (BSD-3-Clause OR Apache-2.0) AND (CC0-1.0 OR MIT-0) AND ISC AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
URL:            https://github.com/totoshko88/RustConn
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(javascriptcoregtk-6.0)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  desktop-file-utils

%description
RustConn is a cross-platform connection orchestrator with a
GTK4/libadwaita interface. It brings SSH, RDP, VNC, SPICE,
MOSH, Telnet, Serial, Kubernetes, and Zero Trust connections
under one roof — with embedded Rust clients where possible
and seamless integration with external tools where needed.
Runs on Linux (GTK4/libadwaita), macOS, FreeBSD, and Windows via WSLg.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/rustconn                                              %{buildroot}%{_bindir}/rustconn
install -Dm755 target/rpm/rustconn-cli                                          %{buildroot}%{_bindir}/rustconn-cli
install -Dm644 rustconn/assets/%{appid}.metainfo.xml                            %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm644 rustconn/assets/icons/hicolor/256x256/apps/%{appid}.png          %{buildroot}%{_hicolordir}/256x256/apps/%{appid}.png
install -Dm644 rustconn/assets/icons/hicolor/128x128/apps/%{appid}.png          %{buildroot}%{_hicolordir}/128x128/apps/%{appid}.png
install -Dm644 rustconn/assets/icons/hicolor/scalable/apps/%{appid}.svg         %{buildroot}%{_scalableiconsdir}/%{appid}.svg
install -Dm644 rustconn/assets/icons/hicolor/scalable/apps/%{appid}-tray.svg    %{buildroot}%{_scalableiconsdir}/%{appid}-tray.svg
install -Dm644 rustconn/assets/io.github.totoshko88.RustConn-vv.xml             %{buildroot}%{_datadir}/mime/packages/%{appid}-vv.xml
%desktop_file_install rustconn/assets/%{appid}.desktop

%terra_appstream

%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%find_lang rustconn

%files -f rustconn.lang
%license LICENSE
%license LICENSE.dependencies
%doc README.md docs/*
%{_bindir}/rustconn
%{_bindir}/rustconn-cli
%{_metainfodir}/%{appid}.metainfo.xml
%{_appsdir}/%{appid}.desktop
%{_hicolordir}/128x128/apps/%{appid}.png
%{_hicolordir}/256x256/apps/%{appid}.png
%{_scalableiconsdir}/%{appid}.svg
%{_scalableiconsdir}/%{appid}-tray.svg
%{_datadir}/mime/packages/%{appid}-vv.xml

%changelog
* Sun Sep 06 2026 Owen Zimmerman <owen@fyralabs.com> - 0.21.7-1
- Initial commit
