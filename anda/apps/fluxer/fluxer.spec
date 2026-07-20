%global appid app.fluxer.Fluxer

Name:           fluxer
Version:        2026.717.184203
Release:        1%{?dist}
Summary:        Fluxer is a free and open source instant messaging and VoIP platform built for friends, groups, and communities
URL:            https://fluxer.app

%electronmeta -D
%global __provides_exclude %{__provides_exclude}|libcbor\.so.*|libcrypto\.so.*|libfido2\.so.*|libudev\.so.*|libz\.so.*|libcap\.so.*

License:        AGPL-3.0-or-later AND %electron_license
Source0:        https://github.com/fluxerapp/fluxer/archive/refs/tags/%version.tar.gz
BuildRequires:  rust-packaging nodejs nodejs-npm nodejs-packaging pnpm
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libfido2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  clang-devel
BuildRequires:  pipewire-devel
Provides:       bundled(libcap)
Provides:       bundled(libcbor)
Provides:       bundled(libfido2)
Provides:       bundled(libudev)
Provides:       bundled(openssl)
Provides:       bundled(zlib)

%description
%summary.

%prep
%autosetup
%cargo_prep_online

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
mv dist-electron/*unpacked dist/
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
* Mon Jun 15 2026 madonuko <mado@fyralabs.com> - 2026.703.173023-1
- Initial package.
