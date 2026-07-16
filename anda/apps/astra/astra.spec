%global appid dev.astramusic.astra
%global ver v0.6.1-beta

Name:           astra
%electronmeta -D
Version:        %(echo %ver | sed 's/-/~/;s/^v//')
Release:        1%?dist
Summary:        A desktop music player for people who still have a music library
License:        GPL-3.0-only AND %electron_license
URL:            https://astramusic.dev
Source0:        https://github.com/Boof2015/astra/archive/refs/tags/%ver.tar.gz
BuildRequires:  nodejs-npm nodejs-packaging

%description
Audiophile music player with gapless playback, parametric EQ, AutoEQ import, and real-time DSP visualizers.

%prep
%autosetup -n %name-%(echo %ver | sed 's/^v//')

%build
%npm_build -BV -M production
%__nodejs ./scripts/build/writeAppBuildMetadata.cjs

%install
%electron_install -I -D

%terra_appstream

%files
%license LICENSE
%doc README.md
%_bindir/%name
%_libdir/%name
%_appsdir/%name.desktop
%_metainfodir/%appid.metainfo.xml
%_hicolordir/*/apps/%name.png

%changelog
* Sat Jun 28 2026 madonuko <madonuko@outlook.com> - 0.6.1~beta
- Initial package.
