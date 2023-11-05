# ref: https://src.fedoraproject.org/rpms/openh264
%global commit1 3a01c086d1b0394238ff1b5ad22e76022830625a
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

%global openh264_version 2.3.1
%global gst_version 1.22.6

Name:           openh264
Version:        %{openh264_version}
# Also bump the Release tag for gstreamer1-plugin-openh264 down below
Release:        3%{?dist}
Summary:        H.264 codec library

License:        BSD
URL:            https://www.openh264.org/
Source0:        https://github.com/cisco/openh264/archive/v%{openh264_version}/openh264-%{openh264_version}.tar.gz
Source1:        https://github.com/mozilla/gmp-api/archive/%{commit1}/gmp-api-%{shortcommit1}.tar.gz
# The source is:
# http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%%{gst_version}.tar.xz
# modified with gst-p-bad-cleanup.sh from SOURCE3
Source2:        gst-plugins-bad-openh264-%{gst_version}.tar.xz
Source3:        gst-p-bad-cleanup.sh

# Don't use pkg-config for finding openh264 as we are building against an in-tree copy
Patch2:         hardcode-openh264-dep.patch

BuildRequires:  gcc-c++
BuildRequires:  gstreamer1-devel >= %{gst_version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{gst_version}
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  nasm

%description
OpenH264 is a codec library which supports H.264 encoding and decoding. It is
suitable for use in real time applications such as WebRTC.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{openh264_version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package     -n mozilla-openh264
Summary:        H.264 codec support for Mozilla browsers
Requires:       %{name}%{?_isa} = %{openh264_version}-%{release}
Requires:       mozilla-filesystem%{?_isa}

%description -n mozilla-openh264
The mozilla-openh264 package contains a H.264 codec plugin for Mozilla
browsers.


%package     -n gstreamer1-plugin-openh264
Version:        %{gst_version}
Release:        2%{?dist}
Summary:        GStreamer H.264 plugin

%description -n gstreamer1-plugin-openh264
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the H.264 plugin.


%prep
%setup -q

# Extract gmp-api archive
tar -xf %{S:1}
mv gmp-api-%{commit1} gmp-api

# Extract gst-plugins-bad-free archive
tar -xf %{S:2}
pushd gst-plugins-bad-%{gst_version}
%patch2 -p1
popd


%build
# Update the makefile with our build options
# Must be done in %%build in order to pick up correct LDFLAGS.
sed -i -e 's|^CFLAGS_OPT=.*$|CFLAGS_OPT=%{optflags}|' Makefile
sed -i -e 's|^PREFIX=.*$|PREFIX=%{_prefix}|' Makefile
sed -i -e 's|^LIBDIR_NAME=.*$|LIBDIR_NAME=%{_lib}|' Makefile
sed -i -e 's|^SHAREDLIB_DIR=.*$|SHAREDLIB_DIR=%{_libdir}|' Makefile
sed -i -e '/^CFLAGS_OPT=/i LDFLAGS=%{__global_ldflags}' Makefile

# First build the openh264 libraries
make %{?_smp_mflags}

# ... then build the mozilla plugin
make plugin %{?_smp_mflags}

# ... and finally build the gstreamer plugin against the previously built
# openh264 libraries
pushd gst-plugins-bad-%{gst_version}
CFLAGS="%{build_cflags} -I`pwd`/../codec/api" \
CXXFLAGS="%{build_cflags} -I`pwd`/../codec/api" \
LDFLAGS="%{build_ldflags} -L`pwd`/.." \
%meson \
    --auto-features=disabled \
    -D package-name="Fedora gstreamer1-plugin-openh264 package" \
    -D package-origin="http://www.openh264.org/" \
    -D openh264=enabled
%meson_build
popd


%install
%make_install

# Install mozilla plugin
mkdir -p $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed
cp -a libgmpopenh264.so* gmpopenh264.info $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed/

mkdir -p $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/pref
cat > $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/pref/gmpopenh264.js << EOF
pref("media.gmp-gmpopenh264.autoupdate", false);
pref("media.gmp-gmpopenh264.version", "system-installed");
EOF

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
cat > $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/gmpopenh264.sh << EOF
MOZ_GMP_PATH="${MOZ_GMP_PATH}${MOZ_GMP_PATH:+:}%{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed"
export MOZ_GMP_PATH
EOF

# Remove static libraries
rm $RPM_BUILD_ROOT%{_libdir}/*.a

# Install the gstreamer plugin
pushd gst-plugins-bad-%{gst_version}
%meson_install

# Register as an AppStream component to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/gstreamer-openh264.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2015 Kalev Lember <klember@redhat.com> -->
<component type="codec">
  <id>gstreamer-openh264</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>GStreamer Multimedia Codecs - H.264</name>
  <summary>Multimedia playback for H.264</summary>
  <description>
    <p>
      This addon includes a codec for H.264 playback and encoding.
    </p>
    <p>
      These codecs can be used to encode and decode media files where the
      format is not patent encumbered.
    </p>
    <p>
      A codec decodes audio and video for playback or editing and is also
      used for transmission or storage.
      Different codecs are used in video-conferencing, streaming media and
      video editing applications.
    </p>
  </description>
  <url type="homepage">http://gstreamer.freedesktop.org/</url>
  <url type="bugtracker">https://bugzilla.gnome.org/enter_bug.cgi?product=GStreamer</url>
  <url type="help">http://gstreamer.freedesktop.org/documentation/</url>
  <url type="donation">http://www.gnome.org/friends/</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF

# Remove unwanted gst-plugins-bad files
rm -rf $RPM_BUILD_ROOT%{_bindir}/gst-transcoder-1.0
rm -rf $RPM_BUILD_ROOT%{_includedir}/gstreamer-1.0/
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gstreamer-*.pc
rm -rf $RPM_BUILD_ROOT%{_libdir}/libgst*.so*
rm -rf $RPM_BUILD_ROOT%{_datadir}/gstreamer-1.0/
popd


%files
%license LICENSE
%doc README.md
%{_libdir}/libopenh264.so.7
%{_libdir}/libopenh264.so.%{openh264_version}

%files devel
%{_includedir}/wels/
%{_libdir}/libopenh264.so
%{_libdir}/pkgconfig/openh264.pc

%files -n mozilla-openh264
%{_sysconfdir}/profile.d/gmpopenh264.sh
%dir %{_libdir}/firefox
%dir %{_libdir}/firefox/defaults
%dir %{_libdir}/firefox/defaults/pref
%{_libdir}/firefox/defaults/pref/gmpopenh264.js
%{_libdir}/mozilla/plugins/gmp-gmpopenh264/

%files -n gstreamer1-plugin-openh264
%{_datadir}/appdata/*.appdata.xml
%{_libdir}/gstreamer-1.0/libgstopenh264.so


%changelog
* Thu Aug 17 2023 Dominik Mierzejewski <dominik@greysector.net> - 2.3.1-3
- Add Mozilla plugin path to MOZ_GMP_PATH instead of overriding unconditionally
- Resolves: rhbz#2225112

* Mon Mar 13 2023 Kalev Lember <klember@redhat.com> - 2.3.1-2
- Update gstreamer plugin to 1.22.1

* Thu Sep 29 2022 Kalev Lember <klember@redhat.com> - 2.3.1-1
- Update to 2.3.1

* Wed Aug 10 2022 Kalev Lember <klember@redhat.com> - 2.3.0-2
- Rebuild

* Mon Aug 01 2022 Kalev Lember <klember@redhat.com> - 2.3.0-1
- Update to 2.3.0
- Update gstreamer plugin to 1.20.3

* Wed Mar 16 2022 David King <amigadave@amigadave.com> - 2.2.0-1
- Update to 2.2.0
- Update gstreamer plugin to 1.20.0

* Tue Sep 07 2021 Kalev Lember <klember@redhat.com> - 2.1.1-3
- Update gstreamer plugin to 1.19.1

* Thu Feb 11 2021 Kalev Lember <klember@redhat.com> - 2.1.1-2
- Update gstreamer plugin to 1.18.2
- Remove totem supplements as totem has recommends on
  gstreamer1-plugin-openh264 instead

* Fri May 22 2020 Kalev Lember <klember@redhat.com> - 2.1.1-1
- Update to 2.1.1
- Add totem supplements to gstreamer1-plugin-openh264

* Tue Mar 10 2020 Kalev Lember <klember@redhat.com> - 2.1.0-1
- Update to 2.1.0
- Update gstreamer plugin to 1.16.2

* Mon Jun 17 2019 Kalev Lember <klember@redhat.com> - 2.0.0-1
- Update openh264 to 2.0.0
- Update gstreamer plugin to 1.16.0

* Fri Feb 22 2019 Kalev Lember <klember@redhat.com> - 1.8.0-3
- Update gstreamer plugin to 1.15.1

* Wed Sep 12 2018 Kalev Lember <klember@redhat.com> - 1.8.0-2
- Update gstreamer plugin to 1.14.2

* Wed Jun 27 2018 Kalev Lember <klember@redhat.com> - 1.8.0-1
- Update openh264 to 1.8.0
- Update gstreamer plugin to 1.14.1

* Tue Mar 06 2018 Kalev Lember <klember@redhat.com> - 1.7.0-6
- Update gstreamer plugin to 1.13.90

* Sat Dec 16 2017 Kalev Lember <klember@redhat.com> - 1.7.0-5
- Update gstreamer plugin to 1.12.4

* Tue Sep 19 2017 Kalev Lember <klember@redhat.com> - 1.7.0-4
- Update gstreamer plugin to 1.12.3

* Thu Jul 20 2017 Kalev Lember <klember@redhat.com> - 1.7.0-3
- Update gstreamer plugin to 1.12.2

* Tue Jun 20 2017 Kalev Lember <klember@redhat.com> - 1.7.0-2
- Update gstreamer plugin to 1.12.1

* Fri Jun 16 2017 Kalev Lember <klember@redhat.com> - 1.7.0-1
- Update openh264 to 1.7.0
- Update gstreamer plugin to 1.12.0

* Mon Mar 06 2017 Kalev Lember <klember@redhat.com> - 1.6.0-5
- Update gstreamer plugin to 1.10.4

* Mon Jan 30 2017 Kalev Lember <klember@redhat.com> - 1.6.0-4
- Update gstreamer plugin to 1.10.3

* Mon Dec 05 2016 Kalev Lember <klember@redhat.com> - 1.6.0-3
- Update gstreamer plugin to 1.10.2

* Fri Sep 02 2016 Kalev Lember <klember@redhat.com> - 1.6.0-2
- Update gstreamer plugin to 1.9.2

* Thu Aug 25 2016 Kalev Lember <klember@redhat.com> - 1.6.0-1
- Update openh264 to 1.6.0
- Update gstreamer plugin to 1.8.3

* Thu Apr 28 2016 Kalev Lember <klember@redhat.com> - 1.5.3-0.1.git2706e36
- Update openh264 to 1.5.3 git snapshot
- Update gstreamer plugin to 1.8.1

* Mon Mar 21 2016 Dennis Gilmore <dennis@ausil.us> - 1.5.2-0.4.git21e44bd
- move the mozila-openh264 definition before gstreamer1-plugin-openh264
- gstreamer1-plugin-openh264 redefines version and release messing up requires

* Mon Nov 30 2015 Kalev Lember <klember@redhat.com> - 1.5.2-0.3.git21e44bd
- Include the gstreamer plugin in gstreamer1-plugin-openh264 subpackage

* Thu Nov 26 2015 Kalev Lember <klember@redhat.com> - 1.5.2-0.2.git21e44bd
- Pass Fedora LDFLAGS to the build to get full relro (#1285338)

* Tue Nov 24 2015 Kalev Lember <klember@redhat.com> - 1.5.2-0.1.git21e44bd
- Initial Fedora packaging
