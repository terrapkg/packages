%global         appid io.github.novum.vkquake
%global         appstream_component desktop-application

Summary:        Vulkan Quake port based on QuakeSpasm
Name:           vkquake
Version:        1.35.0
Release:        1%{?dist}
Packager:       Jan200101 <sentrycraft123@gmail.com>

License:        GPL-2.0-only
URL:            https://github.com/Novum/vkQuake
Source0:        https://github.com/Novum/vkQuake/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glslang
BuildRequires:  spirv-tools
BuildRequires:  SDL3-devel
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  desktop-file-utils

Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup -n vkQuake-%{version}

%conf
%meson \
    -Duse_codec_mp3=enabled \
    -Duse_codec_flac=enabled \
    -Duse_codec_vorbis=enabled \
    -Duse_codec_opus=enabled \
    -Dmp3_lib=mad \
    -Dvorbis_lib=vorbis \
    -Duse_sdl3=enabled \
    -Ddo_userdirs=enabled

%build
%meson_build

%install
install -Dm755 \
    %{_vpath_builddir}/vkquake \
   %{buildroot}/%{_bindir}/vkquake

%desktop_file_install Misc/vkquake.desktop

%terra_appstream

for size in 256 512; do
    install -Dm644 \
        "Misc/vkQuake_${size}.png" \
        "%{buildroot}/%{_hicolordir}/${size}x${size}/apps/vkquake.png"
done

%check
%desktop_file_validate %{buildroot}%{_appsdir}/vkquake.desktop

%files
%license LICENSE.txt
%doc readme.md
%{_bindir}/vkquake
%{_appsdir}/vkquake.desktop
%{_hicolordir}/*/apps/vkquake.png
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Tue Aug 25 2026 Jan200101 <sentrycraft123@gmail.com> - 1.35.0-1
- Initial package
