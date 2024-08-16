%global appname io.elementary.appcenter

Name:           elementary-appcenter
Summary:        Software Center from elementary
Version:        8.0.0
Release:        1%?dist
License:        GPL-3.0

Provides:       appcenter = %{version}-%{release}
Obsoletes:      appcenter < 7.2.1-2

URL:            https://github.com/elementary/appcenter
Source0:        %url/archive/%{version}/appcenter-%{version}.tar.gz

Patch0:         pr2099.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  appstream-vala

BuildRequires:  pkgconfig(appstream) >= 0.10.0
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(packagekit-glib2)
BuildRequires:  pkgconfig(polkit-gobject-1)

Requires:       PackageKit
Requires:       hicolor-icon-theme

%description
AppCenter is a native Gtk+ app store built on AppStream and Packagekit.


%package        gnome-shell-search-provider
Summary:        Software Center from elementary (gnome-shell search provider)

Provides:       appcenter-gnome-shell-search-provider = %{version}-%{release}
Obsoletes:      appcenter-gnome-shell-search-provider < 7.2.1-2

BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Requires:       gnome-shell

Supplements:    (%{name} and gnome-shell)

%description    gnome-shell-search-provider
AppCenter is a native Gtk+ app store built on AppStream and Packagekit.

This package contains the gnome-shell search provider.


%prep
%autosetup -p1 -n appcenter-%version


%build
%meson -Dpayments=false -Dcurated=false -Dhide_upstream_distro_apps=false
%meson_build


%install
%meson_install

%find_lang %{appname}

# remove empty hidden apps file
rm -r %{buildroot}/%{_sysconfdir}/%{appname}/appcenter.hiddenapps

# create autostart entry symlink
mkdir -p %{buildroot}/%{_sysconfdir}/xdg/autostart/

ln -s %{_datadir}/applications/%{appname}-daemon.desktop \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}-daemon.desktop


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}*.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%dir %{_sysconfdir}/%{appname}
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}-daemon.desktop

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}*.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}{,-symbolic}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/polkit-1/actions/%{appname}.policy


%files gnome-shell-search-provider
%{_datadir}/gnome-shell/search-providers/%{appname}.search-provider.ini


%changelog
* Tue Jun 07 2022 Fabio Valentini <decathorpe@gmail.com> - 3.10.0-1
- Update to version 3.10.0.

* Tue Dec 14 2021 Fabio Valentini <decathorpe@gmail.com> - 3.9.1-1
- Update to version 3.9.1.

* Wed Nov 24 2021 Fabio Valentini <decathorpe@gmail.com> - 3.9.0-1
- Update to version 3.9.0.

* Sat Oct 30 2021 Fabio Valentini <decathorpe@gmail.com> - 3.8.2-1
- Update to version 3.8.2.

* Wed Oct 27 2021 Fabio Valentini <decathorpe@gmail.com> - 3.8.1-1
- Update to version 3.8.1.

* Tue Sep 28 2021 Fabio Valentini <decathorpe@gmail.com> - 3.8.0-1
- Update to version 3.8.0.

* Fri Sep 17 2021 Fabio Valentini <decathorpe@gmail.com> - 3.7.1-3
- Mark flatpak sources in the UI.

* Fri Sep 17 2021 Fabio Valentini <decathorpe@gmail.com> - 3.7.1-2
- Hard-code Fedora instead of ubuntu repository names.

* Tue Aug 31 2021 Fabio Valentini <decathorpe@gmail.com> - 3.7.1-1
- Update to version 3.7.1.

* Fri Aug 27 2021 Fabio Valentini <decathorpe@gmail.com> - 3.7.0-1
- Update to version 3.7.0.

* Tue Aug 17 2021 Fabio Valentini <decathorpe@gmail.com> - 3.6.3-1
- Update to version 3.6.3.

* Wed Aug 11 2021 Fabio Valentini <decathorpe@gmail.com> - 3.6.2-1
- Update to version 3.6.2.

* Thu Aug 05 2021 Fabio Valentini <decathorpe@gmail.com> - 3.6.1-1
- Update to version 3.6.1.

* Fri Jul 16 2021 Fabio Valentini <decathorpe@gmail.com> - 3.6.0-1
- Update to version 3.6.0.

* Fri Oct 09 2020 Fabio Valentini <decathorpe@gmail.com> - 3.5.1-1
- Update to version 3.5.1.

* Wed Oct 07 2020 Fabio Valentini <decathorpe@gmail.com> - 3.5.0-1
- Update to version 3.5.0.

* Fri Aug 07 2020 Fabio Valentini <decathorpe@gmail.com> - 3.4.2-1
- Update to version 3.4.2.

* Thu Jul 02 2020 Fabio Valentini <decathorpe@gmail.com> - 3.4.1-1
- Update to version 3.4.1.

* Thu May 28 2020 Fabio Valentini <decathorpe@gmail.com> - 3.4.0-1
- Update to version 3.4.0.

* Thu Apr 30 2020 Fabio Valentini <decathorpe@gmail.com> - 3.3.0-1
- Update to version 3.3.0.

* Thu Apr 09 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.4-1
- Update to version 3.2.4.

* Thu Apr 02 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.3-1
- Update to version 3.2.3.

* Mon Mar 23 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.2-1
- Update to version 3.2.2.

* Fri Feb 28 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.1-1
- Update to version 3.2.1.

* Fri Feb 15 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1-1
- Update to version 3.1.1.

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.0-1
- Update to version 3.1.0.
- Remove empty blacklist file.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0.1-2
- Drop elementaryOS blacklist in favor of the version shipped with appcenter.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0.1-1
- Update to version 3.0.1.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0-2
- Add missing autostart entry symlink for the daemon.

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0-1
- Update to version 3.0.
- Add gnome-shell search provider sub-package.
- Explicitly disable payment system and curated applications.
- Update blacklist file to current version from elementaryOS.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9-2
- Rebuild for granite5 soname bump.

* Thu Mar 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.9-1
- Update to version 0.2.9.
- Add patch to fix build with the newer vala and PackageKit on f28+.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.8-1
- Update to version 0.2.8.

* Tue Nov 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.7-1
- Update to version 0.2.7.

* Fri Nov 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6-2
- Rebuild for granite soname bump.

* Mon Sep 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6-1
- Update to version 0.2.6.

* Sat Aug 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5-1
- Update to version 0.2.5.
- Include fedora-specific blacklist adapted from elementaryOS.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4-1
- Update to version 0.2.4.

* Thu Jun 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-1
- Update to version 0.2.3.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2-1
- Update to version 0.2.2.

* Sat May 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.1-1
- Update to version 0.2.1.

* Wed May 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2-1
- Update to version 0.2.

* Thu Mar 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4-1
- Update to version 0.1.4.
- Depend on generic icon again, since it _should_ work.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-7
- Add patch to rename generic icon to something branded.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com>
- Remove explicit BR: /usr/bin/pkgconfig.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-6
- Explicitly depend on /usr/bin/pkg-config.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-5
- Add missing scriptlets.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-4
- Include icon to fix appdata metadata generation.

* Tue Jan 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-3
- Clean up spec file.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-2
- Enable libunity support.

* Mon Dec 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-1
- Update to version 0.1.3.

* Sun Nov 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-2
- Build out of tree.

* Sat Oct 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Update to version 0.1.2.

* Fri Oct 07 2016 Neal Gompa <ngompa13@gmail.com> - 0.1.1-4
- Add patch to support AppStream 0.10.0 in F25 (LP#1626398)

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-3
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-2
- Spec file cleanups.

* Tue Sep 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.

* Sat Sep 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-2
- Require PackageKit.

* Thu Aug 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Update to version 0.1.

