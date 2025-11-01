%global commit 315251f3e0099fc7afa7ab183880141a478f584e
%global commit_date 20250428
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           fluent-kde-theme
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Fluent design theme for KDE

License:        GPL-3.0-only
URL:            https://github.com/vinceliuice/Fluent-kde
Source0:        %url/archive/%commit/Fluent-kde-%commit.tar.gz

BuildArch:      noarch
BuildRequires:  fdupes

%description
%summary

%prep
%autosetup -n Fluent-kde-%{commit}

%build

%install
mkdir -p %{buildroot}%{_datadir}/aurorae
mkdir -p %{buildroot}%{_datadir}/color-schemes
mkdir -p %{buildroot}%{_datadir}/plasma/desktoptheme
mkdir -p %{buildroot}%{_datadir}/plasma/look-and-feel
mkdir -p %{buildroot}%{_datadir}/Kvantum
mkdir -p %{buildroot}%{_datadir}/wallpapers

# Patch install.sh to use the buildroot destination directories
sed -i "s|^[[:space:]]*AURORAE_DIR=.*|AURORAE_DIR=%{buildroot}%{_datadir}/aurorae|" install.sh
sed -i "s|^[[:space:]]*SCHEMES_DIR=.*|SCHEMES_DIR=%{buildroot}%{_datadir}/color-schemes|" install.sh
sed -i "s|^[[:space:]]*PLASMA_DIR=.*|PLASMA_DIR=%{buildroot}%{_datadir}/plasma/desktoptheme|" install.sh
sed -i "s|^[[:space:]]*LOOKFEEL_DIR=.*|LOOKFEEL_DIR=%{buildroot}%{_datadir}/plasma/look-and-feel|" install.sh
sed -i "s|^[[:space:]]*KVANTUM_DIR=.*|KVANTUM_DIR=%{buildroot}%{_datadir}/Kvantum|" install.sh
sed -i "s|^[[:space:]]*WALLPAPER_DIR=.*|WALLPAPER_DIR=%{buildroot}%{_datadir}/wallpapers|" install.sh

# Invoke the installer now that variables are patched
./install.sh

%fdupes %buildroot%_datadir

%files
%license LICENSE
%doc README.md
%{_datadir}/aurorae/Fluent*/
%{_datadir}/color-schemes/Fluent*.colors
%{_datadir}/plasma/desktoptheme/Fluent*/
%{_datadir}/plasma/look-and-feel/com.github.vinceliuice.Fluent*/
%{_datadir}/Kvantum/Fluent*/
%{_datadir}/wallpapers/Fluent*/

%changelog
%autochangelog
