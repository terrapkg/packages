Name:           arnis
Version:        3.1.0
Release:        1%{?dist}
Summary:        Generate any location from the real world in  Minecraft with a high level of detail
URL:            https://github.com/louis-e/arnis
Source0:        %{url}/archive/refs/tags/v3.1.0.tar.gz
License:        Apache-2.0 AND LGPL-2.1-or-later
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(javascriptcoregtk-4.1)
%dnl Requires:       runtime deps here
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
