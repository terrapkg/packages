%global debug_package %{nil}

Name:           sticky
Version:        1.24
Release:        1%{?dist}
Summary:        A sticky notes app for the Linux desktop

License:        GPL-2.0
URL:            https://github.com/linuxmint/sticky
Source0:        %{url}/archive/%{version}.tar.gz
Patch0:         remove-meson-postinstall-script.patch
Patch1:         point-executable-to-sitepackages-directory.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  meson
BuildRequires:  gettext-devel

Requires:       python3
Requires:       glib2
Requires:       gspell
Requires:       gtk3
Requires:       python3-gobject-base
Requires:       python3-xapp
Requires:       xapps

Packager:       sadlerm <sad_lerm@hotmail.com>

%description
Sticky is a note-taking app for the Linux desktop that simulates traditional "sticky note" style stationery on your desktop. Some of its features include basic text formatting (bold, italics, monospaced, etc.), spell-checking, a tray icon for controlling note visibility, color notes, manual and automatic backups, and a manager to organize your notes into groups.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{python3_sitelib}
mv -v %{buildroot}%{_prefix}/lib/%{name} %{buildroot}%{python3_sitelib}/%{name}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.x.%{name}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}*.svg
%{_datadir}/icons/hicolor/scalable/status/%{name}*.svg
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/%{name}/*
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_datadir}/dbus-1/services/org.x.%{name}.service
%{python3_sitelib}/%{name}/*.py
%{python3_sitelib}/%{name}/__pycache__/*.pyc

%changelog
* Thu Jan 16 2025 sadlerm4 <sad_lerm@hotmail.com>
- Initial package
