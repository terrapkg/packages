Name:    unity-asset-pool
Summary: Assets and icons for Unity
Version: 0.8.24
Release: %autorelease

License:   CC-BY-SA
URL:       https://launchpad.net/unity-asset-pool
Source0:   %{url}/0.8/%{version}/+download/unity-asset-pool-%{version}.tar.gz
BuildArch: noarch

BuildRequires: binutils
BuildRequires: zstd
Requires:      adwaita-icon-theme
Requires:      hicolor-icon-theme

%description
Theme and icons for Unity.

%prep
%autosetup

%build
true

%install
mkdir -m 0755 -p %{buildroot}%{_datadir}/icons/unity-icon-theme/apps %{buildroot}%{_datadir}/icons/unity-icon-theme/places
mkdir -m 0755 -p %{buildroot}%{_datadir}/unity/themes

mkdir -m 0755 -p %{buildroot}%{_datadir}/icons/unity-icon-theme/places/svg %{buildroot}%{_datadir}/icons/unity-icon-theme/places/22
mkdir -m 0755 -p %{buildroot}%{_datadir}/icons/unity-icon-theme/places/24 %{buildroot}%{_datadir}/icons/unity-icon-theme/apps/48
mkdir -m 0755 -p %{buildroot}%{_datadir}/icons/unity-icon-theme/apps/128
mkdir -m 0755 -p %{buildroot}%{_datadir}/icons/unity-icon-theme/search/16 %{buildroot}%{_datadir}/icons/unity-icon-theme/web/48

install -m 0644 unity-icon-theme/index.theme -t %{buildroot}%{_datadir}/icons/unity-icon-theme
install -m 0644 unity-icon-theme/apps/48/workspace-switcher.png -t %{buildroot}%{_datadir}/icons/unity-icon-theme/apps/48
install -m 0644 unity-icon-theme/apps/128/* -t %{buildroot}%{_datadir}/icons/unity-icon-theme/apps/128
install -m 0644 unity-icon-theme/places/22/distributor-logo.png -t %{buildroot}%{_datadir}/icons/unity-icon-theme/places/22
install -m 0644 unity-icon-theme/places/24/distributor-logo.png -t %{buildroot}%{_datadir}/icons/unity-icon-theme/places/24
install -m 0644 unity-icon-theme/places/svg/* -t %{buildroot}%{_datadir}/icons/unity-icon-theme/places/svg
install -m 0644 unity-icon-theme/search/16/search_field.png -t %{buildroot}%{_datadir}/icons/unity-icon-theme/search/16
install -m 0644 unity-icon-theme/web/48/webapp-default-icon.png -t %{buildroot}%{_datadir}/icons/unity-icon-theme/web/48
install -m 0644 unity-icon-theme/index.theme -t %{buildroot}%{_datadir}/icons/unity-icon-theme
install -m 0644 unity-icon-theme/index.theme -t %{buildroot}%{_datadir}/icons/unity-icon-theme

install -m 0644 launcher/* -t %{buildroot}%{_datadir}/unity/themes
install -m 0644 panel/* -t %{buildroot}%{_datadir}/unity/themes

%files
%license COPYRIGHT
%dir %{_datadir}/unity/themes
%{_datadir}/unity/themes/*.png
%{_datadir}/icons/unity-icon-theme/

%changelog
%autochangelog
