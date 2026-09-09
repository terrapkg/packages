%undefine __brp_mangle_shebangs

Name:           arnis
Version:        3.2.0
Release:        1%{?dist}
Summary:        Generate any location from the real world in  Minecraft with a high level of detail
URL:            https://github.com/louis-e/arnis
Source0:        %{url}/archive/refs/tags/v3.1.0.tar.gz
SourceLicense:	Apache-2.0 AND LGPL-2.1-or-later
License:        %{sourcelicense} AND (ISC AND (Apache-2.0 OR ISC)) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND ((MIT OR Apache-2.0) AND NCSA) AND (Apache-2.0 OR ISC OR MIT) AND Apache-2.0 AND MIT AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND CDLA-Permissive-2.0 AND BSD-2-Clause AND Zlib AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND MIT AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (CC0-1.0 OR Apache-2.0) AND Apache-2.0 AND ISC AND (BSD-3-Clause OR Apache-2.0) AND BSD-3-Clause AND MIT AND ISC AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(javascriptcoregtk-4.1)
BuildRequires:	pkgconfig(webkit2gtk-4.1)
BuildRequires:	desktop-file-utils
Packager:       Emmett Zimmerman <miniipadfun@icloud.com>

%description
Arnis creates complex and accurate Minecraft Java Edition (1.17+)
and Bedrock Edition worlds that reflect real-world
geography, topography, and architecture.

This free and open source project is designed to handle large-scale geographic
data from the real world and generate detailed Minecraft worlds. The algorithm
processes geospatial data from OpenStreetMap as well as elevation data to
create an accurate Minecraft representation of terrain and architecture.
Generate your hometown, big cities, and natural landscapes with ease!

%prep
%autosetup -n arnis-%{version}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/arnis         %{buildroot}%{_bindir}/arnis
install -Dm644 src/gui/arnis.desktop    %{buildroot}%{_appsdir}/arnis.desktop
install -Dm644 assets/icons/icon.png    %{buildroot}%{_hicolordir}/512x512/apps/arnis.png

%desktop_file_edit -k Icon -v arnis -f %{buildroot}%{_appsdir}/arnis.desktop

%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/arnis
%{_appsdir}/arnis.desktop
%{_hicolordir}/512x512/apps/arnis.png

%changelog
* Sun Aug 23 2026 Emmett Zimmerman <miniipadfun@icloud.com> - 3.1.0-1
- Initial commit
