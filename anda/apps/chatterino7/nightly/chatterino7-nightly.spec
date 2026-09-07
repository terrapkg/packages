%global appid com.chatterino.chatterino
%global appstream_component desktop-application
%global name_pretty Chatterino7

%global ver 7.5.5
%global commit 5a77ec758b7f02af47cac92d3ed92d5947ffad33
%global shortcommit %{sub %{commit} 1 7}
%global commit_date 20260903

Name:           chatterino7-nightly
Version:        %{ver}^%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Twitch chat client with 7TV subscriber features

License:        MIT AND BSD-3-Clause AND BSL-1.0 AND LicenseRef-fourtf-chatterino-sound-license
URL:            https://github.com/SevenTV/chatterino7
Source0:        %{url}/archive/%{commit}/chatterino7-%{commit}.tar.gz

Packager:       ammix <maxim@ammix.dev>

BuildRequires:  anda-srpm-macros
BuildRequires:  terra-appstream-helper
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  desktop-file-utils
BuildRequires:  boost-devel
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6NetworkPrivate)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WidgetsPrivate)
BuildRequires:  cmake(RapidJSON)
BuildRequires:  miniaudio-devel
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(openssl)

Requires:       hicolor-icon-theme
Requires:       qt6-qtimageformats
Requires:       kf6-kimageformats

Conflicts:      chatterino
Conflicts:      chatterino7

%description
Chatterino7 is a fork of Chatterino 2 with 7TV name paints, personal emotes,
animated profile avatars and higher-resolution emotes.

%prep
%git_clone %{url} %{commit}

%conf
%cmake -G Ninja \
    -DUSE_SYSTEM_MINIAUDIO=ON \
    -DCHATTERINO_NO_AVIF_PLUGIN=ON \
    -DCHATTERINO_UPDATER=OFF \
    -DCHATTERINO_NIGHTLY_BUILD=ON \
    -DSKIP_JSON_GENERATION=ON

%build
%cmake_build

%install
%cmake_install
%terra_appstream

%check
%desktop_file_validate %{buildroot}%{_appsdir}/com.chatterino.chatterino.desktop

%files
%license LICENSE LICENSES
%license resources/licenses lib/sol2/LICENSE.txt
%doc README.md CHANGELOG.c7.md
%{_bindir}/chatterino
%{_appsdir}/com.chatterino.chatterino.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_hicolordir}/256x256/apps/com.chatterino.chatterino.png

%changelog
* Sun Sep 06 2026 ammix <maxim@ammix.dev>
- Initial package
