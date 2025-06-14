# For some reason, this package simply just doesn't have debugsource
%global _debugsource_template %{nil}
# We will enable this in F42 and later for the FFmpeg override
%bcond_with full_ffmpeg

# Optional flag for KMS support, replacing the need for a compositor backend
# This is disabled by default because it causes issues for users that use a compositor
%bcond_with kms

Name:           emulationstation-de
Version:        3.2.0
Release:        1%?dist
Summary:        ES-DE is a frontend for browsing and launching games from your multi-platform collection.
Packager:       Cappy Ishihara <cappy@fyralabs.com>
License:        MIT
URL:            https://es-de.org/
Source0:        https://gitlab.com/es-de/emulationstation-de/-/archive/v%{version}/emulationstation-de-v%{version}.tar.gz
# Backport a patch to fix a build issue with libgit2
# This patch should already be included in the next release
Patch0:         https://gitlab.com/es-de/emulationstation-de/-/commit/3510a09d83949beb765c140041332583b4e70837.patch

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
%autosetup -n emulationstation-de-v%{version} -p1


%build
# Our build environment is pretty similar to Arch's so we can use their build flags
%cmake -DAPPLICATION_UPDATER=off \
%if %{with kms}
    -DDEINIT_ON_LAUNCH=on \
%endif

%cmake_build


%install
%cmake_install

# We're going to remove the licenses directory because it's going to be installed in /usr/share/licenses
rm -rf %{buildroot}%{_datadir}/es-de/licenses %{buildroot}%{_datadir}/es-de/LICENSE

%files
%license LICENSE licenses/*
%doc README.md FAQ.md CHANGELOG.md THEMES.md USERGUIDE.md
%{_bindir}/es-de
%{_bindir}/es-pdf-convert
%{_datadir}/applications/org.es_de.frontend.desktop
%{_datadir}/es-de/resources/*
%{_datadir}/es-de/themes/*
%{_datadir}/icons/hicolor/scalable/apps/org.es_de.frontend.svg
%{_datadir}/man/man6/es-de.6.gz
%{_datadir}/metainfo/org.es_de.frontend.appdata.xml
%{_datadir}/pixmaps/org.es_de.frontend.svg




%changelog
* Sat Feb 08 2025 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Package release
