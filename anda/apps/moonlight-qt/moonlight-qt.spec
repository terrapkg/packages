%global appid com.moonlight_stream.Moonlight
%global _qt6_cxxflags -fpermissive

Name:           moonlight-qt
Version:        6.1.0
Release:        1%{?dist}
Summary:        GameStream client for PCs

License:        GPL-3.0-only AND CC-1.0
URL:            https://github.com/moonlight-stream/moonlight-qt
Source0:        %{url}/releases/download/v%{version}/MoonlightSrc-%{version}.tar.gz

Packager:       Olivia <git@olivia.sh>

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  qt6-rpm-macros
BuildRequires:  openssl-devel 
BuildRequires:  SDL2-devel 
BuildRequires:  SDL2_ttf-devel 
BuildRequires:  ffmpeg-free-devel 
BuildRequires:  libva-devel 
BuildRequires:  libvdpau-devel 
BuildRequires:  opus-devel 
BuildRequires:  pulseaudio-libs-devel 
BuildRequires:  alsa-lib-devel 
BuildRequires:  libdrm-devel 
BuildRequires:  qt6-qtsvg-devel 
BuildRequires:  qt6-qtdeclarative-devel 
BuildRequires:  libplacebo-devel 

%description
Moonlight PC is an open source PC client for NVIDIA GameStream and Sunshine.

%prep
%autosetup -c %{name}-%{version}

%conf
# evil
echo $CFLAGS
echo $CXXFLAGS
%qmake_qt6 PREFIX=%{buildroot}%{_prefix}

%build
%make_build

%install
%make_install
mv %{buildroot}%{_metainfodir}/%{appid}.{appdata,metainfo}.xml
%terra_appstream

%files
%license LICENSE
%doc README.md
%{_bindir}/moonlight
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/moonlight.svg

%changelog
* Sat Sep 05 2026 Olivia <git@olivia.sh>
- Initial package
