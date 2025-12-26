Name:       webapp-manager
Version:    master.lmde7
Release:    1%?dist
Summary:    Web Application Manager
License:    GPL-3.0-or-later
URL:        https://github.com/linuxmint/webapp-manager
Source:     %{url}/archive/refs/tags/%{version}.tar.gz
BuildArch:  noarch

Requires:   python3-beautifulsoup4
Requires:   python3-configobj
Requires:   python3-gobject
Requires:   python3-pillow
Requires:   python3-setproctitle
Requires:   python3-tldextract
Requires:   xapps

BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  python3-devel

Packager:       metcya <metcya@gmail.com>

%description
Launch websites as if they were apps.

%prep
%autosetup -n %{name}-%{version}

%build
%make_build buildmo

%install
mkdir -p %{buildroot}%{_datadir}/locale
cp -r usr/share/locale/* %{buildroot}%{_datadir}/locale
install -Dm 755 usr/bin/%{name} -t %{buildroot}%{_bindir}
install -Dm 755 usr/lib/%{name}/*.py -t %{buildroot}%{_libdir}/%{name}/
install -Dm 644 usr/share/applications/%{name}.desktop -t %{buildroot}%{_datadir}/applications
install -Dm 644 usr/share/desktop-directories/webapps-webapps.directory -t %{buildroot}%{_datadir}/desktop-directories/webapps-webapps.directory
install -Dm 644 usr/share/glib-2.0/schemas/org.x.%{name}.gschema.xml -t %{buildroot}%{_datadir}/glib-2.0/schemas
install -Dm 644 usr/share/icons/hicolor/scalable/apps/webapp-manager.svg -t %{buildroot}%{_scalableiconsdir}
install -Dm 644 usr/share/icons/hicolor/scalable/categories/applications-webapps.svg -t %{buildroot}%{_hicolordir}/scalable/categories
install -Dm 644 usr/share/%{name}/*.ui -t %{buildroot}%{_datadir}/%{name}
install -Dm 644 usr/share/%{name}/firefox/userChrome-with-navbar.css -t %{buildroot}%{_datadir}/%{name}/firefox
install -Dm 644 usr/share/%{name}/firefox/profile/{places.sqlite,search.json.mozlz4,user.js} -t %{buildroot}%{_datadir}/%{name}/firefox/profile
install -Dm 644 usr/share/%{name}/firefox/profile/chrome/userChrome.css -t %{buildroot}%{_datadir}/%{name}/firefox/profile/chrome
install -Dm 644 etc/xdg/menus/applications-merged/webapps.menu -t %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}/*.py
%{_appsdir}/%{name}.desktop
%{_datadir}/desktop-directories/webapps-webapps.directory
%{_datadir}/glib-2.0/schemas/org.x.%{name}.gschema.xml
%{_scalableiconsdir}/%{name}.svg
%{_hicolordir}/scalable/categories/applications-webapps.svg
%{_datadir}/%{name}/
%{_sysconfdir}/xdg/menus/applications-merged/webapps.menu

%dnl %find_lang does not work because the upstream Makefile does not place them in the right spot.
%{_datadir}/locale/*/*/webapp-manager.mo

%changelog
* Mon Dec 22 2025 Owen Zimmerman <owen@fyralabs.com>
- Build fixes

* Fri Dec 19 2025 metcya <metcya@gmail.com>
- Port to Terra
