%global commit 53be9986dea776eb4c2804d4e342cbd3a3cf06fc
%global commit_date 20240716
%global shortcommit %{sub %{commit} 1 7}

Name:           blackbox-terminal
Version:        0.15.0~^%{commit_date}.%{shortcommit}
Release:        1%{?dist}
Summary:        A beautiful GTK 4 terminal

License:        GPL-3.0
URL:            https://gitlab.gnome.org/raggesilver/blackbox
Source0:        %{url}/-/archive/%{commit}/blackbox-%{commit}.tar.gz
# Patch modified from upstream Fedora for terra use to rename executable to blackbox-terminal to avoid conflict with blackbox wm
Patch0:         0001-Rename-executable-to-blackbox-terminal.patch

BuildRequires:  vala meson gettext
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(pqmarble)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  desktop-file-utils

%description
An elegant and customizable terminal for GNOME.

%prep
%autosetup -n blackbox-%{commit} -p1

%build
%meson -Dblackbox_is_flatpak=false
%meson_build

%install
%meson_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.raggesilver.BlackBox.desktop
# don't validate appstream data because terra doesn't use it currently anyway
# appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.raggesilver.BlackBox.metainfo.xml

%files
%doc README.md CHANGELOG.md
%license COPYING
%{_bindir}/blackbox-terminal
%{_datadir}/applications/com.raggesilver.BlackBox.desktop
%{_datadir}/metainfo/com.raggesilver.BlackBox.metainfo.xml
%{_datadir}/blackbox/
%{_datadir}/glib-2.0/schemas/com.raggesilver.BlackBox.gschema.xml
%{_datadir}/icons/hicolor/scalable/actions/com.raggesilver.BlackBox-fullscreen-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/com.raggesilver.BlackBox-show-headerbar-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/external-link-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/settings-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/com.raggesilver.BlackBox.svg
%{_datadir}/locale/*/LC_MESSAGES/blackbox.mo


%changelog
* Sun Oct 23 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
