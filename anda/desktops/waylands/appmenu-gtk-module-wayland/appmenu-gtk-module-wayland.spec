%define debug_package %{nil}

Name:           appmenu-gtk-module-wayland
License:        LGPL-3.0-or-later
Summary:        GTK global menu on Plasma Wayland
Version:        26.08.03
Release:        1%{?dist}
URL:            https://github.com/guiodic/appmenu-gtk-module-wayland
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake
BuildRequires:  cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%install -a
install -Dm644 redhat-linux-build/libappmenu-gtk-module-wayland.so      %{buildroot}%{_libdir}/gtk-3.0/modules/libappmenu-gtk-module-wayland.so
install -Dm755 appmenu-gtk-module-wayland.sh                            %{buildroot}%{_sysconfdir}/profile.d/appmenu-gtk-module-wayland.sh

%files
%{_libdir}/gtk-3.0/modules/libappmenu-gtk-module-wayland.so
%{_sysconfdir}/profile.d/appmenu-gtk-module-wayland.sh

%changelog
* Tue Oct 27 2026 Owen Zimmerman <owen@fyralabs.com> - 26.08.03-1
- Initial commit
