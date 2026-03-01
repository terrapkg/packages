%global uuid vicinae@dagimg-dot.netlify.app

Name:           gnome-shell-extension-vicinae
Version:        1.5.3
Release:        2%{?dist}
License:        MIT
URL:            https://github.com/dagimg-dot/vicinae-gnome-extension
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
Summary:        Companion GNOME extension for Vicinae launcher
Packager:       metcya <metcya@gmail.com>

BuildArch:      noarch

BuildRequires:  bun-bin glib2-devel
Requires:       (gnome-shell >= 48~ with gnome-shell < 50~)
Requires:       vicinae
Recommends:     gnome-extensions-app
Provides:       gnome-shell-extension-vicinae-gnome-extension

%description
Companion GNOME extension for Vicinae launcher with clipboard monitoring,
window management APIs, and paste-to-active-window capabilities.

%prep
%autosetup -n vicinae-gnome-extension-%{version}

%build
%{__bun} i && %{__bun} run build

%install
mkdir -p %{buildroot}%{_gnomeextensionsdir}
cp -a src/ %{buildroot}%{_gnomeextensionsdir}/

%files
%license LICENSE
%doc README.md DEVELOPMENT.md
%{_gnomeextensionsdir}/

%changelog
* Sat Dec 27 2025 metcya <metcya@gmail.com> - 1.5.3-1
- Package
