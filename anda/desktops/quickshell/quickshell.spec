Name:		quickshell
Version:	0.2.1
Release:	5
Summary:	Flexible QtQuick based desktop shell toolkit
License:	LGPL-3.0-only AND GPL-3.0-only
URL:		https://github.com/quickshell-mirror/quickshell
Source0:	https://github.com/quickshell-mirror/quickshell/archive/v%{version}/%{name}-%{version}.tar.gz

Packager:   Willow Reed (willow@willowidk.dev)

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-qtdeclarative-private-devel
BuildRequires: qt6-qtshadertools-devel
BuildRequires: qt6-qtwayland-devel
BuildRequires: spirv-tools
BuildRequires: pkgconfig
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(pam)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(CLI11)

%description
Flexible QtQuick based desktop shell toolkit

%package i3
Summary:	i3 integration for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	i3
Supplements:	(%{name} and i3)

%description i3
i3 integration for %{name}

%package wayland
Summary:	Wayland integration for %{name}
Requires:	%{name} = %{version}-%{release}
Supplements:	(%{name} and libwayland-client)

%description wayland
Wayland integration for %{name}

%package x11
Summary:	X11 integration for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	x11-server
Supplements:	(%{name} and xorg-x11-server-Xorg)

%description x11
X11 integration for %{name}

%package greetd
Summary:	GreetD integration for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	greetd
Supplements:	(%{name} and greetd)

%description greetd
GreetD integration for %{name}

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -DENABLE_CRASH_REPORTER=OFF -DUSE_BREAKPAD=OFF -DWITH_BREAKPAD=OFF -DINSTALL_QMLDIR="%{_qt6_qmldir}" -DINSTALL_QML_PREFIX="%{_qt6_qmldir}"
%cmake_build

%install
%cmake_install

%files
%license LICENSE LICENSE-GPL
%{_bindir}/qs
%{_bindir}/quickshell
%{_datadir}/applications/org.quickshell.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.quickshell.svg
%dir %{_qt6_qmldir}/Quickshell
%{_qt6_qmldir}/Quickshell/Bluetooth
%{_qt6_qmldir}/Quickshell/DBusMenu
%{_qt6_qmldir}/Quickshell/Io
%dir %{_qt6_qmldir}/Quickshell/Services
%{_qt6_qmldir}/Quickshell/Services/Mpris
%{_qt6_qmldir}/Quickshell/Services/Notifications
%{_qt6_qmldir}/Quickshell/Services/Pam
%{_qt6_qmldir}/Quickshell/Services/Pipewire
%{_qt6_qmldir}/Quickshell/Services/SystemTray
%{_qt6_qmldir}/Quickshell/Services/UPower
%{_qt6_qmldir}/Quickshell/Widgets
%{_qt6_qmldir}/Quickshell/_Window
%{_qt6_qmldir}/Quickshell/qmldir
%{_qt6_qmldir}/Quickshell/quickshell-core.qmltypes

%files i3
%{_qt6_qmldir}/Quickshell/I3

%files wayland
%{_qt6_qmldir}/Quickshell/Wayland

%files x11
%{_qt6_qmldir}/Quickshell/X11

%files greetd
%{_qt6_qmldir}/Quickshell/Services/Greetd

%changelog
* Fri Jan 02 2026 Willow Reed <willow@willowidk.dev>
- Initial commit