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
/usr/include/evolution-data-server/
/usr/lib64/lib{camel,ebackend,ebook,ecal,edata-{book,cal},edataserver}*
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
/usr/share/locale/*/LC_MESSAGES/evolution-data-server.mo
/etc/xdg/autostart/org.gnome.Evolution-alarm-notify.desktop
/usr/lib/systemd/user/evolution-*-factory.service
/usr/lib64/evolution-data-server/
/usr/libexec/camel-*
/usr/libexec/evolution-*
/usr/share/GConf/gsettings/evolution-data-server.convert
/usr/share/applications/org.gnome.Evolution-alarm-notify.desktop
/usr/share/dbus-1/services/org.gnome.evolution.dataserver.*.service
/usr/share/evolution-data-server/icons/hicolor/*/status/*.png
/usr/share/glib-2.0/schemas/org.gnome.Evolution.*.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution-data-server.*.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution-data-server.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution.eds-shell.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution.shell.network-config.gschema.xml
/usr/share/pixmaps/evolution-data-server/category_*_16.png
/usr/lib/systemd/user/evolution-source-registry.service
/usr/lib/systemd/user/evolution-user-prompter.service


%changelog
* Sun Oct 16 2022 windowsboy111 <windowsboy111@fyralabs.com> - 3.44.4
- Initial package.
