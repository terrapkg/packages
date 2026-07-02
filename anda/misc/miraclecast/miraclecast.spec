%global commit 0b7f1f1f6586dc65ff480f3cda5c2170a70aa020
%global commit_date 20260310
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global ver 1.0

Name:               miraclecast
Version:            %{ver}^%{commit_date}git.%{shortcommit}
Release:            1%{?dist}
Summary:            Connect external monitors to your system via Wifi-Display specification also known as Miracast
License:            LGPL-2.1-or-later AND GPL-2.0-only
URL:                https://github.com/albfan/miraclecast
Source0:            %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Packager:           Owen Zimmerman <owen@fyralabs.com>
BuildRequires:      gcc
BuildRequires:      gcc-c++
BuildRequires:      cmake
BuildRequires:      pkgconfig(libsystemd)
BuildRequires:      pkgconfig(glib-2.0)
BuildRequires:      readline-devel
BuildSystem:        cmake
BuildOption(conf):  -DCMAKE_POSITION_INDEPENDENT_CODE=ON
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

%description
The MiracleCast project provides software to connect
external monitors to your system via Wi-Fi. It is compatible
to the Wifi-Display specification also known as Miracast.
MiracleCast implements the Display-Source as well as Display-Sink side.

%pkg_completion -B miracle-sinkctl miracle-wifictl miracle-wifid

%files
%license COPYING LICENSE_gdhcp LICENSE_htable LICENSE_lgpl
%doc README.md
%config %{_sysconfdir}/dbus-1/system.d/org.freedesktop.miracle.conf
%{_bindir}/gstplayer
%{_bindir}/miracle-dhcp
%{_bindir}/miracle-gst
%{_bindir}/miracle-sinkctl
%{_bindir}/miracle-uibcctl
%{_bindir}/miracle-wifictl
%{_bindir}/miracle-wifid
%{_bindir}/uibc-viewer

%changelog
* Mon Jun 29 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
