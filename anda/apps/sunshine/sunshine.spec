%bcond_with cuda
%bcond_with check

%global appid dev.lizardbyte.app.Sunshine
%global github_url https://github.com/LizardByte/Sunshine.git
%global commit 14ffa6fdaa53f7b51512be2b3d24f3939695403c

Name:           sunshine
Version:        2026.516.143833
Release:        1%{?dist}
License:        GPL-3.0-only AND CC0-1.0
URL:            http://app.lizardbyte.dev/Sunshine/
%dnl Patch0:         fix-test-cxxflags.patch
Summary:        Self-hosted game stream host for Moonlight
Packager:       metcya <metcya@gmail.com>

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  boost-devel
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
BuildRequires:  systemd-rpm-macros
BuildRequires:  glslc

%if %{with cuda}
BuildRequires:  cuda
%endif

%if %{with check}
BuildRequires:  desktop-file-utils
%endif

%description
Sunshine is a self-hosted game stream host for Moonlight. Offering low-latency,
cloud gaming server capabilities with support for AMD, Intel, and Nvidia GPUs
for hardware encoding. Software encoding is also available. You can connect to
Sunshine from any Moonlight client on a variety of devices. A web UI is
provided to allow configuration, and client pairing, from your favorite web
browser. Pair from the local server or any mobile device.

%prep
%git_clone %{github_url} v%{version}
%dnl %autopatch -p1

%conf
export BRANCH=master
export BUILD_VERSION=%{version}
export CLONE_URL=%{github_url}
export COMMIT=%{commit}
export TAG=v%{version}
%cmake -DSUNSHINE_ENABLE_CUDA=%{?with_cuda:ON:OFF} \
       -DSUNSHINE_ASSETS_DIR=share/%{name}

%build
%cmake_build

%install
%cmake_install

%terra_appstream

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service

%if %{with check}
%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}{,.terminal}.desktop
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-%{version}
%{_datadir}/%{name}/
%{_userunitdir}/%{name}.service
%{_udevrulesdir}/60-%{name}.rules
%{_modulesloaddir}/60-%{name}.conf
%{_scalableiconsdir}/%{name}.svg
%{_hicolordir}/scalable/status/*.svg
%{_appsdir}/*.desktop
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Sun Jan 04 2026 metcya <metcya@gmail.com> - 2025.924.154138-1
- Initial package
