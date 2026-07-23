%global appid   io.github.DenysMb.Kontainer

Name:           kontainer
Version:        1.5.0
Release:        1%{?dist}
Summary:        A Kirigami Distrobox GUI
URL:            https://github.com/DenysMb/Kontainer
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

License:        GPL-3.0-or-later AND MIT AND CC0-1.0
BuildRequires:  cmake >= 3.20
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  kf6-kirigami-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-qqc2-desktop-style
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-kirigami-addons-devel
BuildRequires:  kf6-kirigami-addons

Requires: kf6-kirigami-addons
Requires: kf6-qqc2-desktop-style
Requires: distrobox

Packager:       Cayden Granger <caydengranger@safri.cloud>

%description
Graphical user interface for Distrobox container management.

A native KDE application for managing Distrobox containers with ease.

%prep
%autosetup -n Kontainer-%{version}

%conf
%cmake

%build
%cmake_build

%install
%cmake_install

%find_lang kontainer

%files -f kontainer.lang
%license LICENSES/
%doc README.md
%{_bindir}/kontainer
%{_appsdir}/%{appid}.desktop
%{_scalableiconsdir}/%{appid}.svg
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Fri Jun 19 2026 Cayden Granger <caydengranger@safri.cloud>
- Initial package
