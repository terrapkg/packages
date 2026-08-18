%global         appid org.srb2.SRB2Kart
%global         appstream_component desktop-application

%global         asset_dir %{_datadir}/games/SRB2Kart

Summary:        A kart racing mod based on the 3D Sonic the Hedgehog fangame Sonic Robo Blast 2, based on a modified version of Doom Legacy.
Name:           srb2kart
Version:        1.6
Release:        1%{?dist}
Packager:       Jan200101 <sentrycraft123@gmail.com>

License:        GPL-2.0-only
URL:            https://mb.srb2.org/addons/srb2kart.2435/
Source0:        https://github.com/STJr/Kart-Public/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/STJr/Kart-Public/releases/download/v%{version}/AssetsLinuxOnly.zip#/%{name}-%{version}-assets.zip
Source2:        srb2kart.desktop
Source3:        %{appid}.metainfo.xml

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGLU-devel
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  game-music-emu-devel
BuildRequires:  libupnp-devel
BuildRequires:  libcurl-devel
BuildRequires:  unzip
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  terra-appstream-helper

Requires:       %{name}-data = %{evr}

%description
A kart racing mod based on the 3D Sonic the Hedgehog fangame Sonic Robo Blast 2, based on a modified version of Doom Legacy.

%package data
Summary:        game data for %{name}
BuildArch:      noarch

%description data
%{summary}.

%prep
%autosetup -n Kart-Public-%{version}

mkdir -p assets/installer
cd assets/installer
unzip %{SOURCE1}

%conf
%cmake \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    -DCMAKE_C_STANDARD=99 \
    -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo

%build
%cmake_build

%install
install -Dm755 %{__cmake_builddir}/bin/srb2kart \
               %{buildroot}/%{_bindir}/srb2kart
install -Dm644 src/sdl/SDL_icon.xpm \
               %{buildroot}%{_datadir}/pixmaps/srb2kart.xpm

%desktop_file_install %{SOURCE2}
%terra_appstream -o %{SOURCE3}

# assets
mkdir -p %{buildroot}%{asset_dir}/
cp -pr assets/installer/* %{buildroot}%{asset_dir}/

%check
%desktop_file_validate %{buildroot}%{_appsdir}/srb2kart.desktop

%files
%license LICENSE
%doc README.md
%doc doc
%{_bindir}/srb2kart
%{_datadir}/pixmaps/srb2kart.xpm
%{_appsdir}/srb2kart.desktop
%{_metainfodir}/%{appid}.metainfo.xml

%files data
%{asset_dir}/

%changelog
* Wed Aug 12 2026 Jan200101 <sentrycraft123@gmail.com> - 1.6-1
- initial package
