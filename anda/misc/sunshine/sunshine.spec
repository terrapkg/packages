
%global forgeurl https://github.com/LizardByte/Sunshine
Name:           sunshine
Version:        0.23.0
Release:        1%{?dist}
Summary:        Self-hosted game stream host for Moonlight. 

License:        GPL-3.0-or-later
URL:            http://app.lizardbyte.dev/Sunshine
Source0:        %{forgeurl}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  pkgconfig
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
%ifarch x86_64
BuildRequires:  intel-mediasdk-devel
%endif
BuildRequires:  libcap-devel
BuildRequires:  libcurl-devel
BuildRequires:  libdrm-devel
BuildRequires:  libevdev-devel
BuildRequires:  libnotify-devel
BuildRequires:  libva-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXtst-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  npm
BuildRequires:  numactl-devel
BuildRequires:  openssl-devel
BuildRequires:  opus-devel
BuildRequires:  pulseaudio-libs-devel

# TODO: Add CUDA support before merging PR
# blocker: nvidia-driver

%description
Sunshine is a self-hosted game stream host for Moonlight.
Offering low latency, cloud gaming server capabilities with support for AMD, Intel, and Nvidia GPUs for hardware encoding.
Software encoding is also available.
You can connect to Sunshine from any Moonlight client on a variety of devices.
A web UI is provided to allow configuration, and client pairing, from your favorite web browser.
Pair from the local server or any mobile device.

%prep
%autosetup -n Sunshine-%{version}


%build
%cmake .

%cmake_build


%install
%cmake_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Mon Apr 15 2024 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial re-packaging for Terra
