%global tag                 ensu-v0.1.17
%global appid               io.ente.ensu
%global developer           "Ente"
%global org                 "io.ente"
%global appstream_component desktop-application

Name:           ensu
Version:        %(echo %tag | sed 's/^ensu-v//')
Release:        1%?dist
Summary:        Private, personal LLM app that runs on your device and grows with you over time
License:        AGPL-3.0-only
URL:            https://ente.com/ensu
Source0:        https://github.com/ente-io/ente/archive/refs/tags/%tag.tar.gz
Source1:        ensu.desktop
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  cmake %tauri_buildrequires

%description
%summary.

%prep
%autosetup -n ente-%tag
pushd web
npm ci
popd
cd rust/apps/ensu
%tauri_prep

%build
cd rust/apps/ensu
%npm_build -Bc
install -Dpm755 src-tauri/target/rpm/ensu -t %buildroot%_bindir
%desktop_file_install %{S:1}
install -Dpm644 src-tauri/icons/icon.png %buildroot%_hicolordir/1024x1024/apps/ensu.png
%terra_appstream

%files
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md SUPPORT.md
%license LICENSE
%_bindir/ensu
%_appsdir/ensu.desktop
%_hicolordir/*/apps/ensu.png
%_metainfodir/%appid.metainfo.xml
