%global appid net.blockbench.Blockbench

Name:           blockbench
Version:        5.1.6
Release:        1%{?dist}
Summary:        Low-poly 3D modeling and animation software

%electronmeta -D

License:        GPL-3.0-only AND %{electron_license}
URL:            https://www.blockbench.net/
Source0:        https://github.com/JannisX11/blockbench/archive/refs/tags/v%{version}.tar.gz
Source1:        blockbench.desktop
Source2:        %{appid}.metainfo.xml

BuildRequires:  nodejs
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  terra-appstream-helper
BuildRequires:  appstream

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Blockbench is a low-poly 3D model editor with pixel art textures. Models can be
exported into standardized formats for use in games, rendering, and 3D printing.

%prep
%autosetup -n %{name}-%{version}

%build
%npm_build -r build-electron
%__npm exec electron-builder -- --linux dir --publish=never

%install
mkdir -p dist
mv dist-electron/*-unpacked dist/linux-unpacked
%electron_install -i %{name} -s %{name} -b %{name} -I icon.png
%desktop_file_install %{SOURCE1}
%terra_appstream -o %{SOURCE2}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/blockbench.desktop
appstreamcli validate --no-net %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml

%files
%license LICENSE.MD
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_appsdir}/blockbench.desktop
%{_hicolordir}/*/apps/%{name}.*
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Wed Sep 16 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
