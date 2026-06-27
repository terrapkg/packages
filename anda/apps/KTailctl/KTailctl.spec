Name:       ktailctl
Version:    0.22.0
Release:    1%{?dist}
Summary:    A GUI to monitor and manage Tailscale on your Linux desktop
License:    GPL-3.0-only
URL:        https://github.com/f-koehler/KTailctl
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  golang
BuildRequires:  json-devel
BuildRequires:  golang
BuildRequires:  kf6-breeze-icons-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-kguiaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kirigami-addons-devel
BuildRequires:  kf6-kirigami-devel
BuildRequires:  kf6-knotifications-devel
BuildRequires:  kf6-kwindowsystem-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel

Requires:       tailscale
Requires:       kf5-qqc2-desktop-style
Requires:       hicolor-icon-theme

Provides:       KTailctl

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%package static
%pkg_static_files

%prep
%autosetup -n KTailctl-%{version}
cd src/wrapper
go mod vendor

%conf
%cmake

%build
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/ktailctl
%{_libdir}/qt6/qml/org/fkoehler/KTailctl/Components/*.qml
%{_libdir}/qt6/qml/org/fkoehler/KTailctl/Components/*.version
%{_libdir}/qt6/qml/org/fkoehler/KTailctl/Components/*.qmltypes
%{_libdir}/qt6/qml/org/fkoehler/KTailctl/Components/qmldir
# Exclusive libs that the package needs to run
%{_libdir}/qt6/qml/org/fkoehler/KTailctl/Components/libktailctl_components.so
%{_libdir}/libktailctl_wrapper_logging.so
%{_appsdir}/org.fkoehler.KTailctl.desktop
%{_scalableiconsdir}/org.fkoehler.KTailctl.svg
%{_metainfodir}/org.fkoehler.KTailctl.metainfo.xml

%changelog
* Sat May 23 2026 Owen Zimmerman <owen@fyralabs.com> - 0.21.5-1
- Initial commit
