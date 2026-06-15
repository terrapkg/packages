%global appid app.fluxer.Fluxer
%global commit ee1f27fe1a372b5291aead8042944afd706bf5db
%global shortcommit %{sub %commit 1 7}
%global commit_date 20260409

Name:           fluxer-nightly
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        Fluxer is a free and open source instant messaging and VoIP platform built for friends, groups, and communities
URL:            https://fluxer.app

%electronmeta -D

License:        AGPL-3.0-or-later AND %electron_license
Source0:        https://github.com/fluxerapp/fluxer/archive/%{commit}/fluxer-%{commit}.tar.gz
BuildRequires:  rust-packaging nodejs nodejs-npm nodejs-packaging pnpm

%description
%summary.

%prep
%autosetup -n fluxer-%commit

%build
pushd fluxer_desktop
export BUILD_CHANNEL=stable
export NODE_ENV=production
if ! grep entry electron-builder.config.cjs; then
    sed '/desktop:/,/}/{/desktop:/a entry:{
    /\}/a },
    }' -i electron-builder.config.cjs
fi
ln -sf electron-builder.config.cjs electron-builder.js
%pnpm_build -F -r set-channel,build
popd

%install
pushd fluxer_desktop
mv dist-electron/linux-unpacked dist/
%electron_install -b fluxer_desktop -i app.fluxer.Fluxer -s fluxer -I packaging/linux/%appid.svg

%desktop_file_install -k Exec,Icon -v fluxer,%appid -u %U packaging/linux/%appid.desktop
install -Dm644 packaging/linux/%appid.svg %{buildroot}%{_scalableiconsdir}/%appid.svg

%terra_appstream packaging/linux/%appid.metainfo.xml

%files
%doc README.md
%license LICENSE
%_bindir/fluxer
%_libdir/%name
%_appsdir/%appid.desktop
%_scalableiconsdir/%appid.svg
%_metainfodir/%appid.metainfo.xml

%changelog
* Mon Jun 15 2026 madonuko <mado@fyralabs.com> - 0~20260409git.ee1f27f-1
- Initial package.
