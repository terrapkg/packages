Name:       tail-tray
Version:    0.2.32
Release:    1%{?dist}
Summary:    Tailscale tray menu and UI for the KDE Plasma Desktop
License:    GPL-3.0-or-later
URL:        https://github.com/SneWs/tail-tray
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: gettext
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qttools-devel

Requires:       tailscale
Suggests:       davfs2

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup

%conf
%cmake

%build
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_appsdir}/%{name}.desktop
%{_scalableiconsdir}/tail-tray-dark.svg
%{_scalableiconsdir}/tail-tray.svg

%changelog
* Sat May 23 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
