%bcond_without cuda

Name:           sunshine
Version:        2025.924.154138
Release:        1%{?dist}
License:        GPL-3.0-Only
URL:            http://app.lizardbyte.dev/Sunshine/
Patch0:         fix-test-cxxflags.patch
Summary:        Self-hosted game stream host for Moonlight
Packager:       metcya <metcya@gmail.com>

BuildRequires:  anda-srpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(pkg-config)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(miniupnpc)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(numa)
BuildRequires:  doxygen
BuildRequires:  nodejs-npm

%if %{with cuda}
BuildRequires:  cuda
%endif

%description
Sunshine is a self-hosted game stream host for Moonlight. Offering low-latency,
cloud gaming server capabilities with support for AMD, Intel, and Nvidia GPUs
for hardware encoding. Software encoding is also available. You can connect to
Sunshine from any Moonlight client on a variety of devices. A web UI is
provided to allow configuration, and client pairing, from your favorite web
browser. Pair from the local server or any mobile device.

%prep
%git_clone https://github.com/LizardByte/Sunshine.git v%{version}
%autopatch -p1

%build
%cmake -DSUNSHINE_ENABLE_CUDA=%{?with_cuda:ON:OFF}
%cmake_build

%install
%cmake_install

%files

%changelog
* Sun Jan 04 2026 metcya <metcya@gmail.com> - 2025.924.154138-1
- Initial package 

