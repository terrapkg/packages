# We will enable this in F42 and later for the FFmpeg override
%bcond_with full_ffmpeg
Name:           emulationstation-de
Version:        3.1.1
Release:        1%{?dist}
Summary:        ES-DE is a frontend for browsing and launching games from your multi-platform collection.


License:        MIT
URL:            https://es-de.org/
Source0:        https://gitlab.com/es-de/emulationstation-de/-/archive/v%{version}/emulationstation-de-v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  clang-tools-extra
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  harfbuzz-devel
BuildRequires:  libicu-devel
BuildRequires:  libasan
BuildRequires:  rpm-build
BuildRequires:  SDL2-devel
%if %{with full_ffmpeg}
BuildRequires:  ffmpeg-devel
%else
BuildRequires:  ffmpeg-free-devel
%endif
BuildRequires:  freeimage-devel
BuildRequires:  freetype-devel
BuildRequires:  libgit2-devel
BuildRequires:  curl-devel
BuildRequires:  pugixml-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  poppler-cpp-devel

Provides:       es-de = %{version}-%{release}

%description
ES-DE (EmulationStation Desktop Edition) is a frontend for browsing and launching games from your multi-platform collection.

The goal of this project is to make a high quality frontend that is easy to use, requires minimal setup and configuration, looks nice, and is available across a wide range of operating systems.
It comes preconfigured for use with a large selection of emulators, game engines, game managers and gaming services. It can also run locally installed games and applications. It's fully customizable, so you can easily expand it with support for additional systems and applications.

%prep
%autosetup -n emulationstation-de-v%{version}


%build
%cmake -DAPPLICATION_UPDATER=off 
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md FAQ.md CHANGELOG.md THEMES.md USERGUIDE.md
%{_bindir}/es-de
%{_bindir}/es-pdf-convert
%{_datadir}/applications/org.es_de.frontend.desktop
%{_datadir}/es-de/licenses/*
%{_datadir}/es-de/resources/*
%{_datadir}/es-de/themes/*
%{_datadir}/es-de/LICENSE
%{_datadir}/icons/hicolor/scalable/apps/org.es_de.frontend.svg
%{_datadir}/man/man6/es-de.6.gz
%{_datadir}/metainfo/org.es_de.frontend.appdata.xml
%{_datadir}/pixmaps/org.es_de.frontend.svg




%changelog
* Sat Feb 08 2025 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Package release
