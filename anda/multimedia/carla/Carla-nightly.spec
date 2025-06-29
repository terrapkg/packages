%global pname   carla
%global ver     v2.5.9
%global commit  e8ee9d8a2864a4398d18e180ae3e8622e38a6350
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20250629

Name:           Carla-nightly
Version:        %(echo %ver | tr -d 'v')^%commit_date.git~%shortcommit
Release:        1%?dist
Summary:        Audio plugin host

# The entire source code is GPLv2+ except
# - BSD
# source/modules/lilv/lilv-0.24.0/waf
# source/modules/lilv/serd-0.24.0/waf
# source/modules/lilv/sord-0.16.0/waf
# source/modules/lilv/sratom-0.6.0/waf
# source/modules/audio_decoder/ffcompat.h
# source/modules/rtaudio/include/soundcard.h
# - Boost
# source/modules/hylia/link/asio/*
# - ISC
# source/jackbridge/*
# source/modules/dgl/*
# source/modules/distrho/*
# source/modules/lilv/*
# source/modules/water/buffers/AudioSampleBuffer.h
# source/modules/water/containers
# source/modules/water/files/*
# source/modules/water/maths/*
# source/modules/water/memory/*
# source/modules/water/midi/*
# source/modules/water/misc/*
# source/modules/water/streams/OutputStream.h
# source/modules/water/synthesisers/*
# source/modules/water/text/*
# source/modules/water/threads/*
# source/modules/water/xml/*
# source/utils/CarlaJuceUtils.hpp
# - MIT/Expat
# source/modules/rtaudio/RtAudio.cpp
# source/modules/rtaudio/RtAudio.h
# source/modules/rtmidi/RtMidi.cpp
# source/modules/rtmidi/RtMidi.h
# source/modules/sfzero/LICENSE
# - zlib
# source/modules/dgl/src/nanovg/LICENSE.txt
# source/modules/dgl/src/nanovg/fontstash.h
# source/modules/dgl/src/nanovg/nanovg.c
# source/modules/dgl/src/nanovg/nanovg.h
# source/modules/dgl/src/nanovg/nanovg_gl.h
# source/modules/dgl/src/nanovg/nanovg_gl_utils.h

Epoch:   1
License:        GPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND ISC AND MIT AND Zlib
URL:            https://github.com/falkTX/Carla
Source0:        https://github.com/falkTX/Carla/archive/%commit.tar.gz
# https://github.com/falkTX/Carla/issues/1444
Patch0:         Carla-2.5-libdir.patch
Patch1:         Carla-single-libs-path.patch
# https://github.com/falkTX/Carla/pull/1933
# Support pyliblo3 as well as liblo (to work on F41+)
Patch2:         0001-carla_host_control-import-from-pyliblo3-if-available.patch
Patch3:         Carla-QT5_LINK_FLAGS-bad-rpath.patch
Packager:       madonuko <mado@fyralabs.com>
Provides:       Carla = %epoch:%version-%release
Conflicts:      Carla

BuildRequires:  gcc gcc-c++
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(mxml)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  python3-qt5-base
BuildRequires:  python3-file-magic
BuildRequires:  python3-rdflib
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(zlib)
Buildrequires:  pkgconfig(libmagic)
BuildRequires:  cmake(SDL2)
BuildRequires:  cmake(SDL3)
BuildRequires:  ffmpeg-devel
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
Requires:       python3-qt5
Requires:       python-pyliblo3
Requires:       hicolor-icon-theme
Requires:       shared-mime-info
Requires:       a2jmidid


# Dont provide or require internal libs. Using new rpm builtin filtering,
# see https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering#Private_Libraries
%global _privatelibs libjack[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$


%description
Carla is a fully-featured audio plugin host, with support for many audio drivers
and plugin formats.
It's open source and licensed under the GNU General Public License, version 2 or
later.
Features

    LADSPA, DSSI, LV2 and VST plugin formats
    SF2/3 and SFZ sound banks
    Internal audio and midi file player
    Automation of plugin parameters via MIDI CC
    Remote control over OSC
    Rack and Patchbay processing modes, plus Single and Multi-Client if using
    JACK
    Native audio drivers (ALSA, DirectSound, CoreAudio, etc) and JACK

In experimental phase / work in progress:

    Export any Carla loadable plugin or sound bank as an LV2 plugin
    Plugin bridge support (such as running 32bit plugins on a 64bit Carla, or
    Windows plugins on Linux)
    Run JACK applications as audio plugins
    Transport controls, sync with JACK Transport or Ableton Link

Carla is also available as an LV2 plugin for MacOS and Linux, and VST plugin for
Linux.

%package        devel
Summary:        Header files to access Carla's API
Requires:       Carla-nightly%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       Carla-devel = %epoch:%version-%release

%description devel
This package contains header files needed when writing software using
Carla's several APIs.

%package        vst
Summary:        CarlaRack and CarlaPatchbay VST plugins
Requires:       Carla-nightly%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       Carla-vst = %epoch:%version-%release

%description    vst
This package contains Carla VST plugins, including CarlaPatchbayFX,
CarlaPatchbay, CarlaRackFX, and CarlaRack.

%package     -n lv2-%{pname}-nightly
Summary:        LV2 plugin
Requires:       Carla-nightly%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       lv2-%{pname} = %epoch:%version-%release

%description -n lv2-%{pname}-nightly
This package contains the Carla LV2 plugin.

%prep
#%%autosetup -p0 -n %Carla-%%{version}
%setup -qn Carla-%{commit}
%patch 0 -p1
%patch 1 -p0
%patch 2 -p1
%patch 3 -p1

# remove windows stuff
rm -rf data/{macos,windows}

# E: wrong-script-interpreter /usr/lib64/python3/dist-packages/carla_backend.py /usr/bin/env python3
find . -type f \( -name "*.py" \) -exec sed -i "s|#!/usr/bin/env python3|#!%{__python3}|g" {} \;
sed -i "s|#!/usr/bin/env python3|#!%{__python3}|" source/frontend/{carla,carla-control,carla-jack-multi,carla-jack-single,carla-patchbay,carla-rack}
sed -i "s|#!/usr/bin/env python|#!%{__python3}|" source/frontend/widgets/paramspinbox.py

# fix libdir path
sed -i "s|/lib/carla|/%{_lib}/carla|" data/{carla,carla-control,carla-database,carla-jack-multi,carla-jack-single,carla-patchbay,carla-rack,carla-settings}

# Fix metainfo install dir
sed -i -e 's|$(DESTDIR)$(PREFIX)/share/appdata/studio.kx.carla.appdata.xml|$(DESTDIR)$(PREFIX)/share/metainfo/studio.kx.carla.appdata.xml|g' Makefile
sed -i -e 's|$(DESTDIR)$(PREFIX)/share/appdata|$(DESTDIR)$(PREFIX)/share/metainfo|g' Makefile

%build
%{set_build_flags}
# list build configuration, no need for optflags or -j
make features
%make_build SKIP_STRIPPING=true NOOPT=true V=1

%install 
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}

# Create a vst directory
install -m 755 -d %{buildroot}/%{_libdir}/vst/

# E: non-executable-script /usr/share/carla/paramspinbox.py 644 /usr/bin/env python
find %{buildroot} -type f \( -name "*.py" \) -exec chmod a+x {} \;

# E: non-executable-script /usr/share/carla/carla 644 /usr/bin/python3
chmod a+x %{buildroot}%{_datadir}/%{pname}/{carla,carla-control,carla-jack-multi,carla-jack-single,carla-patchbay,carla-rack}

# fix perm due rpmlint W: unstripped-binary-or-object /usr/lib64/carla/libcarla_interposer-jack-x11.so
find %{buildroot}%{_libdir} -name '*.so' -exec chmod +x '{}' ';'

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/studio.kx.carla.appdata.xml

%files
%doc README.md
%license doc/GPL.txt doc/LGPL.txt
%{_bindir}/%{pname}
%{_bindir}/%{pname}-control
%{_bindir}/%{pname}-database
%{_bindir}/%{pname}-jack-multi
%{_bindir}/%{pname}-jack-single
%{_bindir}/%{pname}-patchbay
%{_bindir}/%{pname}-rack
%{_bindir}/%{pname}-settings
%{_bindir}/%{pname}-single
%{_bindir}/%{pname}-jack-patchbayplugin
%{_bindir}/%{pname}-osc-gui
%{_libdir}/%{pname}/
%{_datadir}/applications/%{pname}-control.desktop
%{_datadir}/applications/%{pname}.desktop
%{_datadir}/applications/%{pname}-jack-multi.desktop
%{_datadir}/applications/%{pname}-jack-single.desktop
%{_datadir}/applications/%{pname}-patchbay.desktop
%{_datadir}/applications/%{pname}-rack.desktop
%{_datadir}/%{pname}/
%{_datadir}/icons/hicolor/*/apps/%{pname}*.png
%{_datadir}/icons/hicolor/*/apps/%{pname}*.svg
%{_datadir}/mime/packages/%{pname}.xml
%{_datadir}/metainfo/studio.kx.carla.appdata.xml

%files vst
%{_libdir}/vst/

%files -n lv2-%{pname}-nightly
%dir %{_libdir}/lv2
%{_libdir}/lv2/carla.lv2/

%files devel
%{_includedir}/%{pname}/
%{_libdir}/pkgconfig/%{pname}-standalone.pc
%{_libdir}/pkgconfig/%{pname}-utils.pc
%{_libdir}/pkgconfig/%{pname}-native-plugin.pc
%{_libdir}/pkgconfig/%{pname}-host-plugin.pc

%changelog
* Wed Dec 04 2024 madonuko <mado@fyralabs.com> - 1:2.5.9^20241103.git~be2f105-1
- Port to nightly, repackaged for Terra

* Fri Sep 27 2024 Adam Williamson <awilliam@redhat.com> - 1:2.5.9-2
- Backport PR #1933 to support pyliblo3 for F41+

* Fri Sep 27 2024 Martin Gansser <martinkg@fedoraproject.org> - 1:2.5.9-1
- Update to 2.5.9
- Add RR python-pyliblo3
- Remove Carla-0001-fix-prototype.patch

* Wed Aug 07 2024 Martin Gansser <martinkg@fedoraproject.org> - 1:2.5.8-4
- Add Carla-0001-fix-prototype.patch for f41

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Martin Gansser <martinkg@fedoraproject.org> - 1:2.5.8-1
- Update to 2.5.8

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 30 2023 Martin Gansser <martinkg@fedoraproject.org> - 1:2.5.7-1
- Update to 2.5.7

* Sun Aug 06 2023 Martin Gansser <martinkg@fedoraproject.org> - 1:2.5.6-1
- Update to 2.5.6

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 05 2023 Martin Gansser <martinkg@fedoraproject.org> - 1:2.5.5-1
- Update to 2.5.5

* Sun Mar 12 2023 Martin Gansser <martinkg@fedoraproject.org> - 1:2.5.4-1
- Update to 2.5.4

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 15 2023 Martin Gansser <martinkg@fedoraproject.org> - 1:2.5.3-1
- Update to 2.5.3

* Sat Oct 15 2022 Martin Gansser <martinkg@fedoraproject.org> - 1:2.5.2-1
- Update to 2.5.2

* Tue Oct 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 1:2.5.1-1
- Update to 2.5.1

* Wed Sep 28 2022 Martin Gansser <martinkg@fedoraproject.org> - 1:2.5.0-1
- Update to 2.5.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Martin Gansser <martinkg@fedoraproject.org> - 1:2.4.4-1
- Update to 2.4.4
- Add RR a2jmidid to allow automatically midi input from system (BZ#2101508)

* Sat Apr 16 2022 Martin Gansser <martinkg@fedoraproject.org> - 1:2.4.3-1
- Update to 2.4.3

* Sat Mar 19 2022 Martin Gansser <martinkg@fedoraproject.org> - 1:2.4.2-2
- Add Carla-refresh-plugin-crash.patch

* Sun Feb 20 2022 Martin Gansser <martinkg@fedoraproject.org> - 1:2.4.2-1
- Update to 2.4.2
- Add Carla-single-libs-path.patch

* Sat Jan 29 2022 Martin Gansser <martinkg@fedoraproject.org> - 1:2.4.1-3
- Add Carla-expression-error.patch

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.4.1-1
- Update to 2.4.1

* Fri Aug 20 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.4.0-1
- Update to 2.4.0

* Mon Aug 09 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.3.2-1
- Update to 2.3.2

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.3.1-1
- Update to 2.3.1-1

* Wed Jul 14 2021 Scott Talbert <swt@techie.net> - 1:2.3.0-5
- Replace python3-qt5-devel BD with python3-qt5-base (for pyuic5)

* Wed Jun 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.3.0-4
- Rebuilt for fluidsynth-2.2.1

* Tue Jun 15 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.3.0-3
- Add Carla-libdir.patch

* Wed May 26 2021 Jan Beran <jaberan@redhat.com> - 1:2.3.0-2
- Add carla.appdata.xml file

* Thu Apr 15 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.3.0-1
- Update to 2.3.0

* Thu Feb 18 2021 Neal Gompa <ngompa13@gmail.com> - 1:2.2.0-4
- Drop explicit dep on jack-audio-connection-kit

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 12 2020 Jeff Law <law@redhat.com> - 1:2.2.0-2
- Add missing #includes for gcc-11

* Sun Sep 27 2020 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.0-1
- Update to 2.2.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.0-0.1.rc1
- Update to 2.2.0-0.1.rc1

* Sat May 16 2020 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2-0.1.beta1
- Update to 2.2-0.1.beta1

* Fri May 15 2020 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2-0.1.20200514gitf100892
- Update to 2.2-0.1.20200514gitf100892
- Add ExcludeArch ppc64le due PowerPC is no longer supported by JUCE

* Tue Apr 14 2020 Martin Gansser <martinkg@fedoraproject.org> - 1:2.1-2
- Add epoch to allow update

* Tue Apr 14 2020 Martin Gansser <martinkg@fedoraproject.org> - 1:2.1-1
- Update to 2.1-1

* Wed Apr 08 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.1-6.rc2
- Update to 2.1-6.rc2

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.1-5.beta1.git74eef49
- Rebuild against fluidsynth2

* Fri Feb 07 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.1-4.beta1.git74eef49
- Update to 2.1-4.beta1.git74eef49
- Add Carla-gcc10-include.patch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3.beta13322c9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.1-2.beta1.git3322c9f
- Update to 2.1-2.beta1.git3322c9f
- Dropped BR  non-ntk-fluid
- Dropped BR  pkgconfig(ntk)

* Wed Oct 30 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.1-1.beta1.git3322c9f
- Update to 2.1-1.beta1.git3322c9f

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.11.20190501git41f81a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.10.20190501git41f81a8
- Update to 2.0.0-0.10.20190501git41f81a8

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.9.20181225git2f3a442
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 06 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.8.20181225git2f3a442
- Filtering private libs

* Sat Jan 05 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.7.20181225git2f3a442
- Add RR python3-pyliblo fixes (RHBZ#1663630)

* Fri Jan 04 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.6.20181225git2f3a442
- Add RR jack-audio-connection-kit fixes (RHBZ#1663319) and (RHBZ#1663357)

* Tue Dec 25 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.5.20181225git2f3a442
- Update to 2.0.0-0.5.20181225git2f3a442
- Rework of Carla-bswap.patch

* Fri Dec 21 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.4.20181212git51f2073
- Add lv2-carla subpkg
- Take ownership of lv2/
- Add BR desktop-file-utils
- Add Carla-bswap.patch
- Remove upstream optimisation options

* Thu Dec 20 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.3.20181212git51f2073
- Use correct directory in subpgk vst
- Make build verbose V=1
- Fix debug symbols extraction / stripping

* Wed Dec 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.2.20181212git51f2073
- Add subpkg vst
- Remove group tag
- Remove old BR qt-devel
- New git release use correct desktop files
- Use macro %%{_lib} libdir fix
- Use %%{__python3} macro
- Use %%{_datadir}/%%{pname}/

* Tue Dec 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.1.20181212git51f2073
- Initial build

