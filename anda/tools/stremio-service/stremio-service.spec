Name:          stremio-service
Version:       0.1.15
Release:       2%?dist
Summary:       Lets you run Stremio server in the background
License:       GPL-2.0-only AND MPL-2.0 AND (Apache-2.0 OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (Unlicense OR MIT) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND CC0-1.0 AND ISC AND MIT AND (BSD-3-Clause OR MIT OR Apache-2.0) AND Apache-2.0 AND MIT AND (Apache-2.0 OR BSL-1.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
URL:           https://github.com/Stremio/stremio-service
Source0:       %url/archive/refs/tags/v%{version}.tar.gz
BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros
BuildRequires: gcc
BuildRequires: cargo
BuildRequires: pkgconfig(gdk-3.0)
BuildRequires: pkgconfig(atk)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: rust-gdk-pixbuf-devel
Requires:      libayatana-appindicator-gtk3
Requires:      gdk-pixbuf2
Requires:      glibc
Requires:      cairo
Requires:      gtk3
Requires:      glib2
# Build fails without this, all deps are listed above.
AutoReqProv:   0

Packager:      Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build -f bundled

%install
mkdir -p %{buildroot}%{_datadir}/stremio-service

# This is weird but the file going into _bindir is a wrapper script for what is going into _datadir, upstream does this.
# Also, yes all of these file permissions are correct.
install -Dm755 resources/stremio-service                    %{buildroot}%{_bindir}/stremio-service
install -Dm755 target/release/stremio-service               %{buildroot}%{_datadir}/stremio-service/stremio-service

install -Dm755 resources/bin/linux/stremio-runtime          %{buildroot}%{_datadir}/stremio-service/stremio-runtime
install -Dm755 resources/bin/linux/ffmpeg                   %{buildroot}%{_datadir}/stremio-service/ffmpeg
install -Dm755 resources/bin/linux/ffprobe                  %{buildroot}%{_datadir}/stremio-service/ffprobe
install -Dm755 resources/bin/linux/server.js                %{buildroot}%{_datadir}/stremio-service/server.js

install -Dm644 resources/com.stremio.service.desktop        %{buildroot}%{_appsdir}/com.stremio.service.desktop
install -Dm644 resources/com.stremio.service.metainfo.xml   %{buildroot}%{_metainfodir}/com.stremio.service.metainfo.xml
install -Dm644 resources/com.stremio.service.svg            %{buildroot}%{_scalableiconsdir}/com.stremio.service.svg
%{cargo_license_summary_online} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE.md
%license LICENSE.dependencies
%{_bindir}/stremio-service
%{_datadir}/stremio-service/stremio-service
%{_datadir}/stremio-service/stremio-runtime
%{_datadir}/stremio-service/ffmpeg
%{_datadir}/stremio-service/ffprobe
%{_datadir}/stremio-service/server.js
%{_appsdir}/com.stremio.service.desktop
%{_scalableiconsdir}/com.stremio.service.svg
%{_metainfodir}/com.stremio.service.metainfo.xml

%changelog
* Sun Feb 01 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
