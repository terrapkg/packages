%define debug_package %{nil}

Name:           cliamp
Version:        1.62.0
Release:        1%{?dist}
Summary:        A retro terminal music player inspired by Winamp

License:        MIT
URL:            https://cliamp.stream
Source0:        https://github.com/bjarneo/cliamp/archive/refs/tags/v%{version}.tar.gz

Packager:       Caio Bruno <cbrunofb@gmail.com>

BuildRequires:  golang gcc alsa-lib-devel libvorbis-devel flac-devel desktop-file-utils
Recommends:     ffmpeg yt-dlp pipewire-alsa

%description
cliamp is a retro terminal (TUI) music player inspired by Winamp that plays
local files, HTTP streams, podcasts, and content from YouTube, SoundCloud,
Spotify, Navidrome, Plex, Jellyfin and more, with a spectrum visualizer,
parametric EQ, and a Lua plugin system.

%prep
%autosetup -n cliamp-%{version}
sed -i 's/^Name=cliamp$/Name=Cliamp/' cliamp.desktop

%build
export CGO_ENABLED=1
go build -trimpath -buildmode=pie -ldflags "-s -w -X main.version=%{version}" -o cliamp .

%install
install -Dpm755 cliamp        %{buildroot}%{_bindir}/cliamp
install -Dpm644 cliamp.desktop %{buildroot}%{_appsdir}/cliamp.desktop
install -Dpm644 Cliamp.png     %{buildroot}%{_hicolordir}/512x512/apps/cliamp.png

%check
desktop-file-validate %{buildroot}%{_appsdir}/cliamp.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/cliamp
%{_appsdir}/cliamp.desktop
%{_hicolordir}/512x512/apps/cliamp.png

%changelog
* Fri Jul 31 2026 Caio Bruno <cbrunofb@gmail.com> - 1.62.0-1
- Initial package
