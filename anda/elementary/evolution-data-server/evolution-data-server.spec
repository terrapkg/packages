Name:           evolution-data-server
Version:        3.44.4
Release:        %autorelease
Summary:        A single database for common, desktop-wide information, such as address books or calendar events.
License:        LGPLv2+
Source0:        https://github.com/GNOME/%{name}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cmake gcc-c++ cairo glib-devel gtk+-devel glib2-devel krb5-devel openldap nspr-devel nss-devel gperf pkgconfig(libsoup-2.4) pkgconfig(libxml-2.0) libicu-devel pkgconfig(gtk+-3.0) pkgconfig(gcr-3) pkgconfig(json-glib-1.0) pkgconfig(webkit2gtk-4.0) pkgconfig(goa-1.0) pkgconfig(gweather4) pkgconfig(libcanberra-gtk3) pkgconfig(libgdata) pkgconfig(libsecret-unstable) libdb-devel glibc-common pkgconfig(libical-glib) perl
Requires:       evolution-data-server-langpacks = 3.46.0-1.fc37
Requires:       libc.so.6(GLIBC_2.34)(64bit) libcairo.so.2()(64bit) libcanberra-gtk3.so.0()(64bit) libcanberra.so.0()(64bit) libgcc_s.so.1()(64bit) libgcc_s.so.1(GCC_3.0)(64bit) libgcc_s.so.1(GCC_3.3.1)(64bit) libgdk-3.so.0()(64bit) libgio-2.0.so.0()(64bit) libglib-2.0.so.0()(64bit) libgmodule-2.0.so.0()(64bit) libgoa-1.0.so.0()(64bit) libgobject-2.0.so.0()(64bit) libgssapi_krb5.so.2()(64bit) libgssapi_krb5.so.2(gssapi_krb5_2_MIT)(64bit) libgtk-3.so.0()(64bit) libgtk-4.so.1()(64bit) libgweather-4.so.0()(64bit) libical-glib.so.3()(64bit) libical.so.3()(64bit) libicui18n.so.71()(64bit) libicuuc.so.71()(64bit) libjson-glib-1.0.so.0()(64bit) libjson-glib-1.0.so.0(libjson-glib-1.0.so.0)(64bit) liblber.so.2()(64bit) liblber.so.2(OPENLDAP_2.200)(64bit) libldap.so.2()(64bit) libldap.so.2(OPENLDAP_2.200)(64bit) libnspr4.so()(64bit) libnss3.so()(64bit) libnss3.so(NSS_3.12)(64bit) libnss3.so(NSS_3.2)(64bit) libnss3.so(NSS_3.3)(64bit) libnss3.so(NSS_3.4)(64bit) libnss3.so(NSS_3.7)(64bit) libnss3.so(NSS_3.9.2)(64bit) libpango-1.0.so.0()(64bit) libphonenumber.so.8()(64bit) libsecret-1.so.0()(64bit) libsmime3.so()(64bit) libsmime3.so(NSS_3.2)(64bit) libsmime3.so(NSS_3.4)(64bit) libsmime3.so(NSS_3.4.1)(64bit) libsmime3.so(NSS_3.6)(64bit) libsoup-3.0.so.0()(64bit) libsqlite3.so.0()(64bit) libssl3.so()(64bit) libssl3.so(NSS_3.2)(64bit) libstdc++.so.6()(64bit) libstdc++.so.6(CXXABI_1.3)(64bit) libstdc++.so.6(CXXABI_1.3.9)(64bit) libstdc++.so.6(GLIBCXX_3.4)(64bit) libstdc++.so.6(GLIBCXX_3.4.20)(64bit) libwebkit2gtk-4.1.so.0()(64bit) libwebkit2gtk-5.0.so.0()(64bit) libxml2.so.2()(64bit) libxml2.so.2(LIBXML2_2.4.30)(64bit) libxml2.so.2(LIBXML2_2.5.8)(64bit) libxml2.so.2(LIBXML2_2.6.0)(64bit) libxml2.so.2(LIBXML2_2.7.3)(64bit) libxml2.so.2(LIBXML2_2.9.0)(64bit) libz.so.1()(64bit) rtld(GNU_HASH)
# TODO tidy up the requires (some redundant)
#? this is the requires for evolution-data-server pkg in f37 (version 3.46.0 as of writing)

%ifarch aarch64
BuildRequires: ld-linux-aarch64.so.1()(64bit) ld-linux-aarch64.so.1(GLIBC_2.17)(64bit)
%else
BuildRequires: mold
%endif


%description
The Evolution Data Server package provides a unified backend for programs that work with
contacts, tasks, and calendar information. It was originally developed for Evolution
(hence the name), but is now used by other packages as well. 


%prep
%autosetup -n evolution-data-server-%{version}


%build
%cmake -Wno-dev -DWITH_NSPR_INCLUDES=/usr/include/nspr4 -DWITH_NSS_INCLUDES=/usr/include/nss3 -DWITH_OPENLDAP=OFF -DWITH_GWEATHER4=ON
%cmake_build


%install
%cmake_install


%files
%doc README
%license COPYING
# /usr/include/evolution-data-server/camel
# /usr/lib/debug/usr/lib64/libcamel*
# /usr/lib/debug/usr/libexec/camel*
# /usr/lib64/evolution-data-server/camel-providers/
# /usr/lib64/libcamel-1.2.so{,.63{,.0.0}}
# /usr/lib64/pkgconfig/camel-1.2.pc
# /usr/libexec/camel-gpg-photo-saver
# /usr/libexec/camel-index-control-1.2
# /usr/libexec/camel-lock-helper-1.2
# /usr/include/evolution-data-server/camel

/usr/include/evolution-data-server/
/usr/lib/debug/usr/lib64/lib{camel,ebackend,ebook,ecal,edata-{book,cal},edataserver{,ui}}-*
/usr/lib64/lib{camel,ebackend,ebook,ecal,edata-{book,cal},edataserver{,ui}}*
/usr/lib64/pkgconfig/camel-1.2.pc
/usr/lib64/pkgconfig/evolution-data-server-1.2.pc
/usr/lib64/pkgconfig/libebackend-1.2.pc
/usr/lib64/pkgconfig/libebook-1.2.pc
/usr/lib64/pkgconfig/libebook-contacts-1.2.pc
/usr/lib64/pkgconfig/libecal-2.0.pc
/usr/lib64/pkgconfig/libedata-book-1.2.pc
/usr/lib64/pkgconfig/libedata-cal-2.0.pc
/usr/lib64/pkgconfig/libedataserver-1.2.pc
/usr/lib64/pkgconfig/libedataserverui-1.2.pc
/usr/share/locale/am/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/ar/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/as/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/ast/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/az/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/be/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/bg/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/bn/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/bn_IN/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/bs/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/ca/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/ca@valencia/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/cs/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/cy/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/da/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/de/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/dz/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/el/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/en@shaw/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/en_AU/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/en_CA/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/en_GB/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/eo/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/es/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/et/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/eu/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/fa/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/fi/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/fr/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/fur/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/ga/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/gl/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/gu/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/he/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/hi/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/hr/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/hu/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/id/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/is/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/it/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/ja/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/ka/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/kk/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/km/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/kn/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/ko/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/ku/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/lt/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/lv/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/mai/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/mk/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/ml/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/mn/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/mr/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/ms/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/nb/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/ne/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/nl/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/nn/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/oc/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/or/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/pa/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/pl/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/pt/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/pt_BR/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/ro/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/ru/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/rw/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/si/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/sk/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/sl/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/sq/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/sr/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/sr@latin/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/sv/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/ta/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/te/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/tg/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/th/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/tr/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/ug/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/uk/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/vi/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/wa/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/xh/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/zh_CN/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/zh_HK/LC_MESSAGES/evolution-data-server.mo
/usr/share/locale/zh_TW/LC_MESSAGES/evolution-data-server.mo

/etc/xdg/autostart/org.gnome.Evolution-alarm-notify.desktop
/usr/lib/systemd/user/evolution-addressbook-factory.service
/usr/lib/systemd/user/evolution-calendar-factory.service
/usr/lib/systemd/user/evolution-source-registry.service
/usr/lib/systemd/user/evolution-user-prompter.service
/usr/lib64/evolution-data-server/addressbook-backends
/usr/lib64/evolution-data-server/addressbook-backends/libebookbackendcarddav.so
/usr/lib64/evolution-data-server/addressbook-backends/libebookbackendfile.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendcaldav.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendcontacts.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendfile.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendgtasks.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendhttp.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendweather.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendwebdavnotes.so
/usr/lib64/evolution-data-server/camel-providers/libcamelimapx.so
/usr/lib64/evolution-data-server/camel-providers/libcamelimapx.urls
/usr/lib64/evolution-data-server/camel-providers/libcamellocal.so
/usr/lib64/evolution-data-server/camel-providers/libcamellocal.urls
/usr/lib64/evolution-data-server/camel-providers/libcamelnntp.so
/usr/lib64/evolution-data-server/camel-providers/libcamelnntp.urls
/usr/lib64/evolution-data-server/camel-providers/libcamelpop3.so
/usr/lib64/evolution-data-server/camel-providers/libcamelpop3.urls
/usr/lib64/evolution-data-server/camel-providers/libcamelsendmail.so
/usr/lib64/evolution-data-server/camel-providers/libcamelsendmail.urls
/usr/lib64/evolution-data-server/camel-providers/libcamelsmtp.so
/usr/lib64/evolution-data-server/camel-providers/libcamelsmtp.urls
/usr/lib64/evolution-data-server/credential-modules/module-credentials-goa.so
/usr/lib64/evolution-data-server/libedbus-private.so
/usr/lib64/evolution-data-server/registry-modules/module-cache-reaper.so
/usr/lib64/evolution-data-server/registry-modules/module-gnome-online-accounts.so
/usr/lib64/evolution-data-server/registry-modules/module-google-backend.so
/usr/lib64/evolution-data-server/registry-modules/module-oauth2-services.so
/usr/lib64/evolution-data-server/registry-modules/module-outlook-backend.so
/usr/lib64/evolution-data-server/registry-modules/module-secret-monitor.so
/usr/lib64/evolution-data-server/registry-modules/module-trust-prompt.so
/usr/lib64/evolution-data-server/registry-modules/module-webdav-backend.so
/usr/lib64/evolution-data-server/registry-modules/module-yahoo-backend.so
/usr/libexec/camel-gpg-photo-saver
/usr/libexec/camel-index-control-1.2
/usr/libexec/camel-lock-helper-1.2
/usr/libexec/evolution-addressbook-factory
/usr/libexec/evolution-addressbook-factory-subprocess
/usr/libexec/evolution-calendar-factory
/usr/libexec/evolution-calendar-factory-subprocess
/usr/libexec/evolution-data-server/addressbook-export
/usr/libexec/evolution-data-server/evolution-alarm-notify
/usr/libexec/evolution-data-server/list-sources
/usr/libexec/evolution-scan-gconf-tree-xml
/usr/libexec/evolution-source-registry
/usr/libexec/evolution-user-prompter
/usr/share/GConf/gsettings/evolution-data-server.convert
/usr/share/applications/org.gnome.Evolution-alarm-notify.desktop
/usr/share/dbus-1/services/org.gnome.evolution.dataserver.AddressBook10.service
/usr/share/dbus-1/services/org.gnome.evolution.dataserver.Calendar8.service
/usr/share/dbus-1/services/org.gnome.evolution.dataserver.Sources5.service
/usr/share/dbus-1/services/org.gnome.evolution.dataserver.UserPrompter0.service
/usr/share/evolution-data-server/icons/hicolor/16x16/status/appointment-missed.png
/usr/share/evolution-data-server/icons/hicolor/16x16/status/appointment-soon.png
/usr/share/evolution-data-server/icons/hicolor/16x16/status/dialog-password.png
/usr/share/evolution-data-server/icons/hicolor/16x16/status/dialog-warning.png

/usr/share/evolution-data-server/icons/hicolor/22x22/status/appointment-missed.png
/usr/share/evolution-data-server/icons/hicolor/22x22/status/appointment-soon.png
/usr/share/evolution-data-server/icons/hicolor/22x22/status/dialog-password.png
/usr/share/evolution-data-server/icons/hicolor/22x22/status/dialog-warning.png
/usr/share/evolution-data-server/icons/hicolor/24x24/status/appointment-missed.png
/usr/share/evolution-data-server/icons/hicolor/24x24/status/appointment-soon.png
/usr/share/evolution-data-server/icons/hicolor/24x24/status/dialog-password.png
/usr/share/evolution-data-server/icons/hicolor/24x24/status/dialog-warning.png
/usr/share/evolution-data-server/icons/hicolor/256x256/status/appointment-missed.png
/usr/share/evolution-data-server/icons/hicolor/256x256/status/appointment-soon.png
/usr/share/evolution-data-server/icons/hicolor/256x256/status/dialog-password.png
/usr/share/evolution-data-server/icons/hicolor/256x256/status/dialog-warning.png
/usr/share/evolution-data-server/icons/hicolor/32x32/status/appointment-missed.png
/usr/share/evolution-data-server/icons/hicolor/32x32/status/appointment-soon.png
/usr/share/evolution-data-server/icons/hicolor/32x32/status/dialog-password.png
/usr/share/evolution-data-server/icons/hicolor/32x32/status/dialog-warning.png
/usr/share/evolution-data-server/icons/hicolor/48x48/status/appointment-missed.png
/usr/share/evolution-data-server/icons/hicolor/48x48/status/appointment-soon.png
/usr/share/evolution-data-server/icons/hicolor/48x48/status/dialog-password.png
/usr/share/evolution-data-server/icons/hicolor/48x48/status/dialog-warning.png
/usr/share/glib-2.0/schemas/org.gnome.Evolution.DefaultSources.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution-data-server.addressbook.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution-data-server.calendar.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution-data-server.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution.eds-shell.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution.shell.network-config.gschema.xml
/usr/share/pixmaps/evolution-data-server/category_birthday_16.png
/usr/share/pixmaps/evolution-data-server/category_business_16.png
/usr/share/pixmaps/evolution-data-server/category_favorites_16.png
/usr/share/pixmaps/evolution-data-server/category_gifts_16.png
/usr/share/pixmaps/evolution-data-server/category_goals_16.png
/usr/share/pixmaps/evolution-data-server/category_holiday-cards_16.png
/usr/share/pixmaps/evolution-data-server/category_holiday_16.png
/usr/share/pixmaps/evolution-data-server/category_hot-contacts_16.png
/usr/share/pixmaps/evolution-data-server/category_ideas_16.png
/usr/share/pixmaps/evolution-data-server/category_international_16.png
/usr/share/pixmaps/evolution-data-server/category_key-customer_16.png
/usr/share/pixmaps/evolution-data-server/category_miscellaneous_16.png
/usr/share/pixmaps/evolution-data-server/category_personal_16.png
/usr/share/pixmaps/evolution-data-server/category_phonecalls_16.png
/usr/share/pixmaps/evolution-data-server/category_status_16.png
/usr/share/pixmaps/evolution-data-server/category_strategies_16.png
/usr/share/pixmaps/evolution-data-server/category_suppliers_16.png
/usr/share/pixmaps/evolution-data-server/category_time-and-expenses_16.png


%changelog
* Sun Oct 16 2022 windowsboy111 <windowsboy111@fyralabs.com> - 3.44.4
- Initial package.
