#? https://src.fedoraproject.org/rpms/rtaudio/blob/db1aa72863ccbfd480e22c2f7aefb41ebb8e2360/f/rtaudio.spec
%global commit e5f0774b2156082ec3db998bd6b2a94b66ade8ac
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20260228
%global ver .0.1

Name:           rtaudio-nightly
Version:        %{ver}^%{commit_date}.git.%{shortcommit}
Release:        1%?dist
Summary:        Real-time Audio I/O Library
License:        MIT
URL:            https://github.com/thestk/rtaudio
Source0:        %url/archive/%commit.tar.gz
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
Conflicts:      rtaudio
Provides:       rtaudio = %version-%release

%global _description %{expand:
RtAudio is a set of C++ classes that provide a common API for realtime audio
input/output across different operating systems. RtAudio significantly
simplifies the process of interacting with computer audio hardware. It was
designed with the following objectives:

  * object-oriented C++ design
  * simple, common API across all supported platforms
  * allow simultaneous multi-api support
  * support dynamic connection of devices
  * provide extensive audio device parameter control
  * allow audio device capability probing
  * automatic internal conversion for data format, channel number compensation,
    (de)interleaving, and byte-swapping}

%description %_description


%package devel
Summary:        Real-time Audio I/O Library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      rtaudio-devel
Provides:       rtaudio-devel = %version-%release

%description devel %_description


%prep
%autosetup -n rtaudio-%commit
# Fix encoding issues
for file in tests/teststops.cpp; do
   sed 's|\r||' $file > $file.tmp
   iconv -f ISO-8859-1 -t UTF8 $file.tmp > $file.tmp2
   touch -r $file $file.tmp2
   mv -f $file.tmp2 $file
done


%build
export CFLAGS="%optflags -fPIC"
NOCONFIGURE=1 ./autogen.sh
%configure --with-jack --with-alsa --with-pulse --enable-shared --disable-static --verbose
%make_build

%install
%make_install
%ldconfig_scriptlets


%files
%license doc/doxygen/license.txt
%doc README.md doc/release.txt
%{_libdir}/librtaudio.so.*

%files devel
%doc doc/html doc/images
%{_includedir}/rtaudio/*.h
%{_libdir}/librtaudio.so
%{_libdir}/pkgconfig/rtaudio.pc


%changelog
* Tue Oct 15 2024 Richard Shaw <hobbes1069@gmail.com> - 6.0.1-1
- Update to 6.0.1.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 06 2022 Richard Shaw <hobbes1069@gmail.com> - 5.2.0-1
- Update to 5.2.0.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 5.0.0-1
- Update to 5.0.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.0.11-8
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 15 2012 Brendan Jones <brendan.jones.it@gmail.com> 4.0.11-3
- Update source comments

* Sun Oct 28 2012 Brendan Jones <brendan.jones.it@gmail.com> 4.0.11-2
- Add pulse dependancies

* Sun Oct 14 2012 Brendan Jones <brendan.jones.it@gmail.com> 4.0.11-1
- Update to 4.011

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 05 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 4.0.7-1
- Update to 4.0.7
- Upstream is supporting shared libraries now. Drop the static library

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 4.0.6-1
- Update to 4.0.6

* Sat Feb 28 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 4.0.5-3
- Don't remove the tests/Release directory

* Fri Feb 27 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 4.0.5-2
- Build static library only

* Tue Feb 24 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 4.0.5-1
- Initial build
