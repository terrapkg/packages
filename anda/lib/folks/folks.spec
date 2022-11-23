%global folks_module_version 26

Name:           folks
Version:        0.15.5
Release:        4%{?dist}
Summary:        GObject contact aggregation library
Epoch:          1

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/Folks
Source0:        https://download.gnome.org/sources/folks/0.15/folks-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  python3-dbusmock
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  telepathy-glib-vala
BuildRequires:  vala
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.4
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libedataserver-1.2) = 3.44.4
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(telepathy-glib)

%description
libfolks is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers and eventually evolution data server,
Facebook, etc.) to create meta-contacts.

%package        telepathy
Summary:        Folks telepathy backend
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    telepathy
%{name}-telepathy contains the folks telepathy backend.

%package        tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    tools
%{name}-tools contains a database and import tool.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-tools%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/libfolks-dummy.so.26*
%{_libdir}/libfolks-eds.so.26*
%{_libdir}/libfolks.so.26*
%dir %{_libdir}/folks
%dir %{_libdir}/folks/%{folks_module_version}
%dir %{_libdir}/folks/%{folks_module_version}/backends
%{_libdir}/folks/%{folks_module_version}/backends/bluez/
%{_libdir}/folks/%{folks_module_version}/backends/dummy/
%{_libdir}/folks/%{folks_module_version}/backends/eds/
%{_libdir}/folks/%{folks_module_version}/backends/key-file/
%{_libdir}/folks/%{folks_module_version}/backends/ofono/
%{_libdir}/girepository-1.0/Folks-0.7.typelib
%{_libdir}/girepository-1.0/FolksDummy-0.7.typelib
%{_libdir}/girepository-1.0/FolksEds-0.7.typelib
%{_datadir}/GConf/gsettings/folks.convert
%{_datadir}/glib-2.0/schemas/org.freedesktop.folks.gschema.xml

%files telepathy
%{_libdir}/libfolks-telepathy.so.26*
%{_libdir}/folks/%{folks_module_version}/backends/telepathy
%{_libdir}/girepository-1.0/FolksTelepathy-0.7.typelib

%files tools
%{_bindir}/%{name}-import
%{_bindir}/%{name}-inspect

%files devel
%{_includedir}/folks
%{_libdir}/pkgconfig/folks*.pc
%{_libdir}/libfolks*.so
%{_datadir}/gir-1.0/Folks-0.7.gir
%{_datadir}/gir-1.0/FolksDummy-0.7.gir
%{_datadir}/gir-1.0/FolksEds-0.7.gir
%{_datadir}/gir-1.0/FolksTelepathy-0.7.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/%{name}*

%changelog
* Wed Nov 23 2022 windowsboy111 <windowsboy111@fyralabs.com> - 0.15.5-4
- Fix evolution-data-server version

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.15.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Kalev Lember <klember@redhat.com> - 1:0.15.5-2
- Rebuilt for evolution-data-server soname bump

* Wed Mar 23 2022 David King <amigadave@amigadave.com> - 1:0.15.5-1
- Update to 0.15.5

* Sat Feb 12 2022 Jeff Law <jeffreyalaw@gmail.com> - 1:0.15.4-3
- Re-enable LTO

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 David King <amigadave@amigadave.com> - 1:0.15.4-1
- Update to 0.15.4

* Tue Aug 03 2021 Kalev Lember <klember@redhat.com> - 1:0.15.3-1
- Update to 0.15.3

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.15.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 16 2021 Kalev Lember <klember@redhat.com> - 1:0.15.2-2
- Drop temporary ABI compat

* Tue Feb 16 2021 Kalev Lember <klember@redhat.com> - 1:0.15.2-1
- Update to 0.15.2

* Fri Feb 12 2021 Milan Crha <mcrha@redhat.com> - 1:0.14.0-7
- Rebuilt for evolution-data-server soname version bump

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Jeff Law <law@redhat.com> - 1:0.14.0-3
- Disable LTO

* Tue Jul 07 2020 Milan Crha <mcrha@redhat.com> - 1:0.14.0-2
- Rebuilt for evolution-data-server soname version bump

* Wed Mar 11 2020 Kalev Lember <klember@redhat.com> - 1:0.14.0-1
- Update to 0.14.0
- Update download URLs

* Tue Feb 04 2020 Kalev Lember <klember@redhat.com> - 1:0.13.2-1
- Update to 0.13.2
- Clean up some more cruft left over from autotools build
- No longer require python2 for building

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Kalev Lember <klember@redhat.com> - 1:0.13.1-1
- Update to 0.13.1

* Thu May 23 2019 Adam Williamson <awilliam@redhat.com> - 1:0.12.1-2
- Add patch to extend test timeout to fix build fails

* Tue May 21 2019 Milan Crha <mcrha@redhat.com>
- Add patch to adapt to evolution-data-server's libebook API changes

* Tue Apr 30 2019 Phil Wyett <philwyett@kathenas.org> - 1:0.12.1-1
- Update to 0.12.1
- Convert to meson build
- Fix and cleanup dependencies

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 1:0.11.4-15
- Rebuilt against fixed atk (#1626575)

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:0.11.4-14
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Pete Walter <pwalter@fedoraproject.org> - 1:0.11.4-12
- Enable telepathy backend again and split it out to folks-telepathy subpackage

* Mon Jan 07 2019 Milan Crha <mcrha@redhat.com> - 1:0.11.4-11
- Rebuilt for evolution-data-server soname bump
- Add /usr/bin/dbus-daemon into the BuildRequires (for tests)

* Wed Nov 28 2018 Debarshi Ray <rishi@fedoraproject.org> - 1:0.11.4-10
- Disable Telepathy backend (RH #1654208)

* Mon Nov 12 2018 Milan Crha <mcrha@redhat.com> - 1:0.11.4-9
- Rebuilt for evolution-data-server soname bump

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1:0.11.4-8
- Rebuild with fixed binutils

* Fri Jul 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:0.11.4-7
- Rebuild for new binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 1:0.11.4-5
- Rebuilt for evolution-data-server soname bump

* Tue Jan 16 2018 Marek Kasik <mkasik@redhat.com> - 1:0.11.4-4
- Enable unit tests
- Resolves: #1502676

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Bastien Nocera <bnocera@redhat.com> - 0.11.4-1
+ folks-0.11.4-1
- Update to 0.11.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1:0.11.3-4
- Rebuild for readline 7.x

* Tue Oct 25 2016 Milan Crha <mcrha@redhat.com> - 1:0.11.3-3
- Rebuild for newer evolution-data-server

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 1:0.11.3-2
- BR vala instead of obsolete vala-tools subpackage

* Wed Sep 21 2016 Kalev Lember <klember@redhat.com> - 1:0.11.3-1
- Update to 0.11.3
- Don't set group tags
- Use make_install macro

* Mon Jul 18 2016 Milan Crha <mcrha@redhat.com> - 1:0.11.2-7
- Rebuild for newer evolution-data-server

* Tue Jun 21 2016 Milan Crha <mcrha@redhat.com> - 1:0.11.2-6
- Rebuild for newer evolution-data-server

* Sun Apr 03 2016 Mathieu Bridon <bochecha@daitauha.fr> - 1:0.11.2-5
- Drop the Zeitgeist dependency.

* Tue Feb 16 2016 Milan Crha <mcrha@redhat.com> - 1:0.11.2-4
- Rebuild for newer evolution-data-server

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Kevin Fenzi <kevin@scrye.com> - 0.11.2-2
- Rebuild for new libical

* Sat Dec 05 2015 Kalev Lember <klember@redhat.com> - 1:0.11.2-1
- Update to 0.11.2
- Use license macro for COPYING

* Wed Jul 22 2015 Milan Crha <mcrha@redhat.com> - 1:0.11.1-3
- Rebuild for newer evolution-data-server

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Kalev Lember <kalevlember@gmail.com> - 1:0.11.1-1
- Update to 0.11.1

* Tue Apr 28 2015 Milan Crha <mcrha@redhat.com> - 1:0.11.0-2
- Rebuild for newer evolution-data-server

* Fri Feb 13 2015 Richard Hughes <rhughes@redhat.com> - 1:0.11.0-1
- Update to 0.11.0

* Mon Jan 19 2015 Richard Hughes <rhughes@redhat.com> - 1:0.10.1-1
- Update to 0.10.1

* Mon Nov 03 2014 Richard Hughes <richard@hughsie.com> - 1:0.10.0-4
- Use updated e-d-s and bluez in non-Fedora build

* Mon Nov 03 2014 Richard Hughes <richard@hughsie.com> - 1:0.10.0-3
- Fix non-Fedora build

* Tue Sep 23 2014 Kalev Lember <kalevlember@gmail.com> - 1:0.10.0-2
- Rebuilt for libcamel soname bump

* Fri Sep 12 2014 Kalev Lember <kalevlember@gmail.com> - 1:0.10.0-1
- Update to 0.10.0
- Remove lib64 rpaths
- Tighten subpackage dependencies with the _isa macro
- Drop unneeded -devel subpackage dependencies

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Kalev Lember <kalevlember@gmail.com> - 1:0.9.8-1
- Update to 0.9.8

* Mon Aug 11 2014 Nils Philippsen <nils@redhat.com> - 1:0.9.7.1-4
- add missing files to file list

* Thu Jul 31 2014 Milan Crha <mcrha@redhat.com> - 1:0.9.7.1-3
- Rebuild against newer evolution-data-server

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1:0.9.7.1-2
- Rebuilt for gobject-introspection 1.41.4

* Tue Jun 24 2014 Richard Hughes <rhughes@redhat.com> - 1:0.9.7.1-1
- Update to 0.9.7.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 03 2014 Milan Crha <mcrha@redhat.com> - 1:0.9.6-4
- Rebuild against newer evolution-data-server

* Tue Jan 14 2014 Milan Crha <mcrha@redhat.com> - 1:0.9.6-3
- Rebuild against newer evolution-data-server

* Mon Nov 18 2013 Brian Pepple <bpepple@fedoraproject.org> - 1:0.9.6-2
- Add patch to remove assert that was causing IRC crash. (#1031252)

* Thu Nov 14 2013 Richard Hughes <rhughes@redhat.com> - 1:0.9.6-1
- Update to 0.9.6

* Wed Oct 23 2013 Brian Pepple <bpepple@fedoraproject.org> - 1:0.9.5-2
- Rebuild for latest libcamel.

* Tue Aug 27 2013 Brian Pepple <bpepple@fedoraproject.org> - 1:0.9.5-1
- Update to 0.9.5.

* Mon Aug 19 2013 Brian Pepple <bpepple@fedoraproject.org> - 1:0.9.4-1
- Update to 0.9.4.
- Bump minimum version of eds needed.

* Mon Aug 19 2013 Milan Crha <mcrha@redhat.com> - 1:0.9.3-5
- Rebuild against newer evolution-data-server

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 10 2013 Kalev Lember <kalevlember@gmail.com> - 1:0.9.3-3
- Including missing files
- Disable fatal warnings to fix the build

* Tue Jul 09 2013 Brian Pepple <bpepple@fedoraproject.org> - 1:0.9.3-2
- Rebuild for new libcamel.

* Tue Jun 25 2013 Brian Pepple <bpepple@fedoraproject.org> - 1:0.9.3-1
- Update to 0.9.3.
- Bump minimum version of zeitgeist needed.

* Sat Jun 22 2013 Matthias Clasen <mclasen@redhat.com> - 1:0.9.2-3
- Trim %%changelog

* Fri Jun 21 2013 Matthias Clasen <mclasen@redhat.com> - 1:0.9.2-2
- Install NEWS instead of ChangeLog (saves some space)

* Sat Jun  8 2013 Brian Pepple <bpepple@fedoraproject.org> - 1:0.9.2-1
- Update to 0.9.2.
- Bump minimum version of eds needed.

* Tue Apr 30 2013 Brian Pepple <bpepple@fedoraproject.org> - 1:0.9.1-2
- Rebuild against new eds.

* Tue Feb 19 2013 Richard Hughes <rhughes@redhat.com> - 1:0.9.1-1
- Update to 0.9.1

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Kalev Lember <kalevlember@gmail.com> - 1:0.8.0-4
- Rebuild for new libcamel.

* Tue Nov 20 2012 Milan Crha <mcrha@redhat.com> - 1:0.8.0-3
- Rebuild for new libcamel.

* Thu Oct 25 2012 Milan Crha <mcrha@redhat.com> - 1:0.8.0-2
- Rebuild for new libcamel.

* Thu Oct  4 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:0.8.0-1
- Update to 0.8.0
- Update source url.

* Wed Sep 19 2012 Kalev Lember <kalevlember@gmail.com> - 1:0.7.4.1-2
- Silence glib-compile-schemas scriplets

* Wed Sep 12 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:0.7.4.1-1
- Update to 0.7.4.1.
- Bump minimum requirement for tp-glib and vala.
- Drop staticmember patches. Fixed upstream.

* Mon Aug 27 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:0.7.3-2
- Rebuild for new libcamel.
- Pull upstream patches to fix build errors caused by accessing static members.

* Sun Jul 29 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:0.7.3-1
- Update to 0.7.3.

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 18 2012 Matthias Clasen <mclasen@redhat.com> - 1:0.7.2.2-2
- Rebuild

* Tue Jul  3 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:0.7.2.2-1
- Update to 0.7.2.2.
- Update eds version needed.

* Thu Jun 28 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:0.7.2.1-1
- Update to 0.7.2.1.
- Drop book-uid patch. Fixed upstream.
- Bump minimum version of eds needed.

* Mon Jun 25 2012 Matthias Clasen <mclasen@redhat.com> - 1:0.7.1-2
- Update for e-d-s api change

* Mon Jun 18 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:0.7.1-1
- Update to 0.7.1.
- Bump version of eds and tp-glib needed.
- Add BR on libzeitgeist-devel.

* Wed Jun 13 2012 Cosimo Cecchi <cosimoc@redhat.com> - 1:0.7.0-2
- Disable libsocialweb backend

* Tue Apr 17 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:0.7.0-1
- Update to 0.7.0.
- Update source url.

* Mon Apr 16 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.9-1
- Update to 0.6.9.
- Drop patch that fixed account sync crash. Fixed upstream.

* Thu Apr  5 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.8-4
- Enable inspect tool (#810098)
- Add BR on readline-devel.

* Tue Apr 03 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.8-3
- Rebuild against new tp-glib.

* Fri Mar 30 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.8-2
- Backport patch to fix crash cause by TpAccount are out of sync.
- Bump minimum version of tp-glib needed.

* Mon Mar 26 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.8-1
- Update to 0.6.8.
- Bump minimum verions of libsocialweb-devel and vala-devel.

* Wed Feb 22 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.7-1
- Update to 0.6.7.

* Mon Feb 6 2012 Brian Pepple <bpepple@fedoraproject.org> 1:0.6.6-3
- Rebuild for new eds.

* Sun Jan 08 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.6-2
- Rebuild for new gcc.

* Wed Dec 14 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.6-1
- Update to 0.6.6.
- Drop name details non-null patch. Fixed upstream.

* Wed Nov 30 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:0.6.5-4
- Move the vala vapi files to the devel package where they should be and add the appropriate requires

* Sun Nov 27 2011 Colin Walters <walters@verbum.org> - 1:0.6.5-3
- Add patch from git to fix gnome-shell crashes

* Tue Nov 22 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.5-2
- Rebuild against new eds

* Fri Nov 11 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.5-1
- Update to 0.6.5.

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.6.4.1-3
- Rebuilt for glibc bug#747377

* Mon Oct 24 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.4.1-2
- Rebuld against libcamel.

* Tue Oct 18 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.4.1-1
- Update to 0.6.4.1.

* Tue Oct 18 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.4-1
- Update to 0.6.4.

* Mon Sep 26 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.3.2-1
- Update to 0.6.3.2.

* Sun Sep 25 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.3.1-1
- Update to 0.6.3.1.
- Drop typelib patch. Fixed upstream.

* Wed Sep 21 2011 Matthias Clasen <mclasen@redhat.com> - 1:0.6.3-2
- Fix another typelib problem

* Mon Sep 19 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.3-1
- Update to 0.6.3.
- Drop typelib patch. Fixed upstream.

* Wed Sep 14 2011 Owen Taylor <otaylor@redhat.com> - 1:0.6.2.1-2
- Really fix the typelib to embed the right .so file

* Thu Sep  8 2011 Matthias Clasen <mclasen@redhat.com> - 1:0.6.2.1-1
- Really fix the reentrancy problem, by using 0.6.2.1

* Thu Sep  8 2011 Matthias Clasen <mclasen@redhat.com> - 1:0.6.2-2
- Fix a reentrancy problem that causes gnome-shell to crash

* Thu Sep  8 2011 Matthias Clasen <mclasen@redhat.com> - 1:0.6.2-1
- Update to 0.6.2.1

* Thu Sep  8 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.2-1
- Update to 0.6.2
- Use old libgee api.

* Wed Sep  7 2011 Matthias Clasen <mclasen@redhat.com> - 1:0.6.1-4
- Try again

* Tue Sep 06 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.1-3
- Rebuld against new libcamel.

* Thu Sep  1 2011 Matthias Clasen <mclasen@redhat.com> - 1:0.6.1-2
- Fix up the typelib

* Mon Aug 29 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.1-1
- Update to 0.6.1.
- Drop EDS patch. Fixed upstream.

* Mon Aug 29 2011 Milan Crha <mcrha@redhat.com> - 1:0.6.0-6
- Rebuild against newer evolution-data-server

* Fri Aug 19 2011 Matthias Clasen <mclasen@redhat.com> - 1:0.6.0-4
- Try again to rebuild

* Tue Aug 16 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.0-2
- Rebuld for new eds

* Sat Aug 13 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.6.0-1
- Update to 0.6.0.
- Update source url.
- Add BR on eds-devel and libsocialweb-devel.

* Fri Jun 10 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.5.2-1
- Update to 0.5.2.
- Add BR on GConf2-devel.

* Wed Mar 23 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.4.2-1
- Update to 0.4.2.

* Fri Mar 18 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.4.1-1
- Update to 0.4.1.

* Thu Mar 17 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.4.0-2
- Update source url.

* Thu Mar 17 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.4.0-1
- Update to 0.4.0.

* Mon Feb 14 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.3.6-1
- Update to 0.3.6.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:0.3.4-1
- Update to 0.3.4.

* Tue Dec 14 2010 Brian Pepple <bpepple@fedoraproject.org> - 1:0.3.3-1
- Update to 0.3.3.

* Sun Nov 14 2010 Brian Pepple <bpepple@fedoraproject.org> - 1:0.3.2-1
- Update to 0.3.2.
- Update min version of tp-glib.
- Update source url.
- Drop dso linking patch. Fixed upstream.

* Fri Oct 29 2010 Brian Pepple <bpepple@fedoraproject.org> - 1:0.2.1-1
- Update to 0.2.1.
- Add patch to fix dso linking. (fdo #633511)

* Fri Oct 29 2010 Brian Pepple <bpepple@fedoraproject.org> - 1:0.2.0-4
- Add epoch to devel subpackage requires.

* Mon Oct 25 2010 Brian Pepple <bpepple@fedoraproject.org> - 1:0.2.0-3
- Revert back to 0.2.x until gtk-2.92.1 or greater is in rawhide.

* Wed Oct 20 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1.
- Update source url.
- Update tp-glib version required.

* Wed Sep 29 2010 jkeating - 0.2.0-2
- Rebuilt for gcc bug 634757

* Sat Sep 25 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0.
- Add missing requires to devel subpackage.
- Drop DSO linkng patch. Fixed upstream.

* Sun Sep 12 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.1.17-1
- Update to 0.1.17.
- Add patch to fix DSO linking for import tool.
- Add BR on libxml2-devel so import tool is built.

* Wed Sep  1 2010 Yanko Kaneti <yaneti@declera.com> 0.1.16-1
- New upstream release.

* Thu Aug 30 2010 Yanko Kaneti <yaneti@declera.com> 0.1.15-1
- New upstream release. Drop the RPATH hacks.

* Thu Aug 19 2010 Yanko Kaneti <yaneti@declera.com> 0.1.14.1-1
- New upstream release. Requires vala >= 0.9.6

* Thu Aug 19 2010 Yanko Kaneti <yaneti@declera.com> 0.1.14-2
- Use chrpath to remove the lingering RPATH because the guidelines
  recomended sed makes libtool incapable of building the tp-lowlevel.gir.
  Better solution welcome.

* Wed Aug 18 2010 Yanko Kaneti <yaneti@declera.com> 0.1.14-1
- New upstream. Remove patch and libtool hack.

* Tue Aug 17 2010 Yanko Kaneti <yaneti@declera.com> 0.1.13-4
- Add BR: vala-tools

* Tue Aug 17 2010 Yanko Kaneti <yaneti@declera.com> 0.1.13-3
- Update for the available telepathy-glib vala packaging

* Thu Aug 12 2010 Yanko Kaneti <yaneti@declera.com> 0.1.13-2
- Add BR: libgee-devel

* Thu Aug 12 2010 Yanko Kaneti <yaneti@declera.com> 0.1.13-1
- New upstream release
- Autofoo for the new vala api versioning

* Tue Aug  3 2010 Yanko Kaneti <yaneti@declera.com> 0.1.12-1
- New upstream release

* Mon Aug  2 2010 Yanko Kaneti <yaneti@declera.com> 0.1.11-1
- Packaged for review
