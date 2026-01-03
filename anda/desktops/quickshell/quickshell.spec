Name:		quickshell
Version:	0.2.1
Release:	1%?dist
Summary:	Flexible QtQuick based desktop shell toolkit
License:	LGPL-3.0-only AND GPL-3.0-only
URL:		https://github.com/quickshell-mirror/quickshell
Source0:	https://github.com/quickshell-mirror/quickshell/archive/v%{version}/%{name}-%{version}.tar.gz

Packager:   Willow Reed (willow@willowidk.dev)

BuildRequires: cmake
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6ShaderTools)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-private-devel
BuildRequires: spirv-tools
BuildRequires: anda-srpm-macros
BuildRequires: breakpad-devel
BuildRequires: breakpad-static
BuildRequires: pkgconfig
BuildRequires: pkgconfig(jemalloc)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(pam)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(CLI11)

%description
Flexible QtQuick based desktop shell toolkit.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake  -GNinja \
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DDISTRIBUTOR="Fedora Terra" \
        -DDISTRIBUTOR_DEBUGINFO_AVAILABLE=YES \
        -DGIT_REVISION=%{commit} \
        -DINSTALL_QML_PREFIX=%{_lib}/qt6/qml
%cmake_build

%install
%cmake_install

%files
%license LICENSE LICENSE-GPL
%doc BUILD.md
%doc CONTRIBUTING.md
%doc README.md
%doc changelog/v%{version}.md
%{_bindir}/qs
%{_bindir}/quickshell
%{_appsdir}/org.quickshell.desktop
%{_scalableiconsdir}/org.quickshell.svg
%{_libdir}/qt6/qml/Quickshell

%changelog
* Fri Jan 02 2026 Willow Reed <willow@willowidk.dev>
- Initial commit