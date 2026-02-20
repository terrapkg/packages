%global commit0 b09c9f62fb6d8b839e0e87e6f0ce53b7dbf9b3c5
%global date 20260220
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global upstream_name nvidia-vaapi-driver

%ifarch %ix86
%global build_cflags %{__build_flags_lang_c} %{?_distro_extra_cflags} -Wno-error=format=
%endif

Name:           libva-nvidia-driver
Epoch:          1
Version:        0.0.15%{!?tag:^%{date}git%{shortcommit0}}
Release:        1%?dist
Summary:        VA-API user mode driver for Nvidia GPUs
License:        MIT
URL:            https://github.com/elFarto/%{upstream_name}

%if "%{?shortcommit0}"
Source0:        %{url}/archive/%{commit0}/%{upstream_name}-%{commit0}.tar.gz#/%{upstream_name}-%{shortcommit0}.tar.gz
%else
Source0:        %{url}/archive/v%{version}/%{upstream_name}-%{version}.tar.gz
%endif

BuildRequires:  gcc
BuildRequires:  meson >= 0.58.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(ffnvcodec) >= 11.1.5.1
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  pkgconfig(gstreamer-codecparsers-1.0)
%endif
BuildRequires:  pkgconfig(libdrm) >= 2.4.60
BuildRequires:  pkgconfig(libva) >= 1.8.0

Conflicts:      libva-vdpau-driver%{?_isa}
Obsoletes:      %{upstream_name} < 0.0.10-3
Provides:       %{upstream_name} = %{version}-%{release}
# Alternative name that better describes the API involved
Provides:       nvdec-vaapi-driver = %{version}-%{release}

Requires:       mesa-filesystem
%if 0%{?fedora}
%ifarch x86_64
Requires:       (%{name}(x86-32) = %{?epoch:%{epoch}:}%{version}-%{release} if steam(x86-32))
%endif
%endif

%description
This is a VA-API implementation that uses NVDEC as a backend. This
implementation is specifically designed to be used by Firefox for accelerated
decode of web content, and may not operate correctly in other applications.

%prep
%if "%{?shortcommit0}"
%autosetup -p1 -n %{upstream_name}-%{commit0}
%else
%autosetup -p1 -n %{upstream_name}-%{version}
%endif

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_libdir}/dri/nvidia_drv_video.so

%changelog
%autochangelog
