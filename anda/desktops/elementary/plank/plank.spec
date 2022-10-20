%global commit      013d0513bcf029426db19aea4d8b19c7b3b0077c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210202

%global common_description %{expand:
Plank is meant to be the simplest dock on the planet. The goal is to
provide just what a dock needs and absolutely nothing more. It is,
however, a library which can be extended to create other dock programs
with more advanced features.

Thus, Plank is the underlying technology for Docky (starting in version
3.0.0) and aims to provide all the core features while Docky extends it
to add fancier things like Docklets, painters, settings dialogs, etc.}

Name:           plank
Summary:        Stupidly simple Dock
Version:        0.11.89
Release:        11.%{commitdate}.git%{shortcommit}%{?dist}
License:        GPLv3+

URL:            https://launchpad.net/%{name}
# use sources from elementary OS dock "fork" which is actually maintained
# * dropped patented zoom animation
# * fixed session integration
# * support for automatic dark theme
# * migrated from autotools to meson
Source0:        https://github.com/elementary/dock/archive/%{commit}/dock-%{shortcommit}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  help2man
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(cairo) >= 1.13
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gdk-x11-3.0) >= 3.10.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.40.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(granite) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(libbamf3) >= 0.4.0
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi) >= 1.6.99.1
BuildRequires:  pkgconfig(xfixes) >= 5.0

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Requires:       bamf-daemon
Requires:       hicolor-icon-theme

%description %{common_description}


%package        libs
Summary:        Shared libraries for %{name}

%description    libs %{common_description}
This package contains the shared libraries.


%package        docklets
Summary:        Docklets for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    docklets %{common_description}
This package contains the docklets for plank.


%package        devel
Summary:        Development files for %{name}

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel %{common_description}
This package contains the files necessary to develop against plank.


%prep
%autosetup -n dock-%{commit} -p1


%build
%meson -Denable-apport=false
%meson_build


%install
%meson_install

%find_lang %{name}


%check
desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{name}.desktop

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml


%files -f %{name}.lang
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop

%{_bindir}/%{name}

%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/net.launchpad.%{name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/%{name}/

%{_mandir}/man1/%{name}.1*

%files libs
%license COPYING COPYRIGHT
%doc README.md AUTHORS NEWS

%{_libdir}/lib%{name}.so.1*
%dir %{_libdir}/%{name}

%files docklets
%dir %{_libdir}/%{name}/docklets
%{_libdir}/%{name}/docklets/*.so

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%{_includedir}/%{name}/

%{_datadir}/vala/vapi/%{name}.vapi
%{_datadir}/vala/vapi/%{name}.deps


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.89-11.20210202.git013d051
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.89-10.20210202.git013d051
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.89-9.20210202.git013d051
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 18 2021 Fabio Valentini <decathorpe@gmail.com> - 0.11.89-8.20210202.git013d051
- Rebuilt for granite 6 soname bump.

* Sat Feb 06 2021 Fabio Valentini <decathorpe@gmail.com> - 0.11.89-7.20210202.git013d051
- Switch to elementary OS dock sources, commit 013d051.
- Remove all obsolete downstream patches.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.89-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.89-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Fabio Valentini <decathorpe@gmail.com> - 0.11.89-4
- Drop unnecessary build dependency on libdbusmenu.

* Tue Mar 03 2020 Fabio Valentini <decathorpe@gmail.com> - 0.11.89-3
- Include some patches from elementaryOS.
- Port to meson, drop autotools.
- Register with the GNOME session manager.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.89-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 19 2019 Fabio Valentini <decathorpe@gmail.com> - 0.11.89-1
- Update to version 0.11.89.

* Sat Aug 03 2019 Fabio Valentini <decathorpe@gmail.com> - 0.11.4-10
- Add upstream patch to fix FTBFS with vala 0.45+.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.11.4-7
- Hide plank launcher in Pantheon.
- Modernize .spec file.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.4-4
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.11.4-1
- Update to version 0.11.4.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.11.3-2
- Make BR on /usr/bin/pkg-config explicit.

* Sun Jan 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.11.3-1
- Update to version 0.11.3.
- Update .spec file for current Packaging Guidelines.

* Fri Aug 19 2016 Wesley Hearn <whearn@redhat.com> - 0.11.2-1
- Updated to latest version

* Fri Mar 25 2016 Wesley Hearn <whearn@redhat.com> - 0.11.0-2
- Fixed issue in the patent patch

* Thu Mar 17 2016 Wesley Hearn <whearn@redhat.com> - 0.11.0-1
- Updated to latest version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Wesley Hearn <whearn@redhat.com> - 0.10.1-1
- Updated to latest version

* Mon May 04 2015 Wesley Hearn <whearn@redhat.com> - 0.10.0-2
- Disable potential patent issue

* Mon May 04 2015 Wesley Hearn <whearn@redhat.com> - 0.10.0-1
- Updated to latest version

* Mon May 04 2015 Wesley Hearn <whearn@redhat.com> - 0.9.1-1
- Updated to latest upstream

* Wed Jan 28 2015 Wesley Hearn <whearn@redhat.com> - 0.8.1-1
- Updated to latest upstream

* Sat Oct 25 2014 Wesley Hearn <whearn@redhat.com> - 0.7.1-1
- Updated to latest upstream

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Wesley Hearn <whearn@redhat.com> - 0.6.0-1
- New upstream version

* Mon Feb 17 2014 Wesley Hearn <whearn@redhat.com> - 0.5.0-4
- Build against bamf-devel and not bamf4-devel in Fedora 21+

* Mon Feb 17 2014 Wesley Hearn <whearn@redhat.com> - 0.5.0-3
- Removed Group from devel package

* Fri Feb 14 2014 Wesley Hearn <whearn@redhat.com> - 0.5.0-2
- Cleaned up SPEC file

* Tue Jan 14 2014 Wesley Hearn <whearn@redhat.com> - 0.5.0-1
- Updating to new upstream release

* Thu Aug 08 2013 Wesley Hearn <whearn@redhat.com> - 0.3.0-1
- Updating to new upstream release

* Thu Jan 24 2013 Wesley Hearn <whearn@redhat.com> - 0.2.0.734-0.1.20130124bzr
- Updated to 734

* Mon Jan 21 2013 Wesley Hearn <whearn@redhat.com> - 0.2.0.731-1.20130121
- Updates to revision 731
- Fixed version numbers and how I generate the source ball
- Cleaned up spec file some more

* Thu Jan 17 2013 Wesley Hearn <whearn@redhat.com> - 0.0-1.20130117bzr723
- Updated to revision 723
- Cleaned up the spec file some

* Wed Jan 16 2013 Wesley Hearn <whearn@redhat.com> - 0.0-1.20130116bzr722
- Initial package
