%global fusionsrc_commit 91b92ea4846982e5d9eb58744fda70f75d0faf8d

# globals for x264-0.164-20231001git31e19f92.tar.bz2
%global api 164
%global gitdate 20231001
%global gitversion 31e19f92
%global gitlongver 31e19f92f00c7003fa115047ce50978bc98c3a0d

%global snapshot %{gitdate}git%{gitversion}
%global gver .%{gitdate}git%{gitversion}
%global branch stable

%global _with_bootstrap 1

%{?_with_bootstrap:
%global _without_gpac 1
%global _without_libavformat 1
%global _without_libswscale  1
}

# Reduce dependencies to build x264-libs on i686
%if 0%{?fedora}
%ifarch i686
%global _without_gpac 1
%global _without_libavformat 1
%global _without_libswscale  1
%endif
%endif

#Whitelist of arches with dedicated ASM code
%global asmarch aarch64 armv7hl armv7hnl i686 ppc64 ppc64le x86_64
%ifnarch %{asmarch}
%global _without_asm 1
%endif

Summary: H264/AVC video streams encoder
Name: x264-bootstrap
Version: 0.0.%{api}
Release: 15%{?gver}%{?_with_bootstrap:_bootstrap}%{?dist}
License: GPLv2+
URL: https://www.videolan.org/developers/x264.html
Source0: https://code.videolan.org/videolan/x264/-/archive/%gitversion.tar.bz2
Source1: https://raw.githubusercontent.com/rpmfusion/x264/%fusionsrc_commit/x264-snapshot.sh
Source2: https://raw.githubusercontent.com/rpmfusion/x264/%fusionsrc_commit/version.h

# don't remove config.h and don't re-run version.sh
Patch0: https://raw.githubusercontent.com/rpmfusion/x264/%fusionsrc_commit/x264-nover.patch
# add 10b suffix to high bit depth build
Patch1: https://raw.githubusercontent.com/rpmfusion/x264/%fusionsrc_commit/x264-10b.patch
# fix assignment from incompatible pointer type errors
Patch2: https://raw.githubusercontent.com/rpmfusion/x264/%fusionsrc_commit/x264-altivec-incompatible-pointer-type.patch
Patch11: https://raw.githubusercontent.com/rpmfusion/x264/%fusionsrc_commit/x264-opencl.patch

BuildRequires: anda-srpm-macros git-core
BuildRequires: gcc
%{!?_without_gpac:BuildRequires: gpac-static >= 1.0.1 zlib-devel openssl-devel libpng-devel libjpeg-devel xz-devel libglvnd-devel mesa-libGLU-devel faad2-devel libmad-devel xvidcore-devel a52dec-devel libvorbis-devel libtheora-devel openjpeg2-devel }
%{!?_without_libavformat:BuildRequires: ffmpeg-devel}
%{?_with_ffmpegsource:BuildRequires: ffmpegsource-devel}
# https://bugzilla.rpmfusion.org/show_bug.cgi?id=3975
%ifarch armv7hl armv7hnl
BuildRequires: execstack
%endif
%ifarch %{asmarch}
BuildRequires: nasm
%endif
BuildRequires: pkgconfig(bash-completion)
# we need to enforce the exact EVR for an ISA - not only the same ABI
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: ffmpeg-libs%{?_isa}
Provides: x264 = %version-%release

%description
x264 is a free library for encoding H264/AVC video streams, written from
scratch.

This package contains the frontend.

%package libs
Summary: Library for encoding H264/AVC video streams
Recommends: %{_libdir}/libOpenCL.so.1
Provides: x264-libs = %version-%release

%description libs
x264 is a free library for encoding H264/AVC video streams, written from
scratch.

%package devel
Summary: Development files for the x264 library
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Provides: x264-devel = %version-%release

%description devel
x264 is a free library for encoding H264/AVC video streams, written from
scratch.

This package contains the development files.

%global x_configure \
./configure \\\
    --host=%{_host} \\\
    --prefix=%{_prefix} \\\
    --exec-prefix=%{_exec_prefix} \\\
    --bindir=%{_bindir} \\\
    --includedir=%{_includedir} \\\
    --libdir=%{_libdir} \\\
    %{?_without_libavformat:--disable-lavf} \\\
    %{?_without_libswscale:--disable-swscale} \\\
    %{!?_with_ffmpegsource:--disable-ffms} \\\
    --enable-debug \\\
    --enable-shared \\\
    --system-libx264 \\\
    --enable-pic

%prep
%setup -q -n x264-%gitversion-%gitlongver

mkdir x264-0.%{api}-%{snapshot}
pushd x264-0.%{api}-%{snapshot}
git init
git remote add origin https://code.videolan.org/videolan/x264.git
git fetch --depth 1 origin %gitlongver
git checkout FETCH_HEAD
sh version.sh > ./version.h

cp %{SOURCE2} .
%patch -P0 -p1 -b .nover
%patch -P1 -p1 -b .10b
%patch -P2 -p1 -b .ptr
%patch -P11 -p1 -b .opencl
popd

for variant in generic generic10 ; do
  rm -rf ${variant}
  cp -pr x264-0.%{api}-%{snapshot} ${variant}
done


%build
%set_build_flags
pushd generic
%{x_configure}\
    %{?_without_asm:--disable-asm}

%make_build
popd

pushd generic10
%{x_configure}\
    %{?_without_asm:--disable-asm}\
    --disable-cli\
    --disable-opencl \
    --bit-depth=10

%make_build
popd

%install
# NOTE: the order is important here! We want the generic devel stuff
for variant in generic10 generic ; do
pushd ${variant}
%make_install
popd
done

#Fix timestamp on x264 generated headers
touch -r generic/version.h %{buildroot}%{_includedir}/x264.h %{buildroot}%{_includedir}/x264_config.h

# https://bugzilla.rpmfusion.org/show_bug.cgi?id=3975
%ifarch armv7hl armv7hnl
execstack -c %{buildroot}%{_libdir}/libx264{,10b}.so.%{api}
%endif

install -dm755 %{buildroot}%{_pkgdocdir}
install -pm644 generic/{AUTHORS,COPYING} %{buildroot}%{_pkgdocdir}/


%ldconfig_scriptlets libs


%files
%{_bindir}/x264
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/x264

%files libs
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%license %{_pkgdocdir}/COPYING
%{_libdir}/libx264.so.%{api}
%{_libdir}/libx26410b.so.%{api}

%files devel
%doc generic/doc/*
%{_includedir}/x264.h
%{_includedir}/x264_config.h
%{_libdir}/libx264.so
%{_libdir}/libx26410b.so
%{_libdir}/pkgconfig/x264.pc

%changelog
* Tue Oct 08 2024 Nicolas Chauvet <kwizart@gmail.com> - 0.164-15.20231001git31e19f92
- Rebuilt

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.164-14.20231001git31e19f92
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 10 2024 Dominik Mierzejewski <dominik@greysector.net> - 0.164-13.20231001git31e19f92
- Fix "assignment from incompatible pointer type" errors on ppc64le
- Use correct build dependency on bash-completion

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.164-12.20231001git31e19f92
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 12 2023 Leigh Scott <leigh123linux@gmail.com> - 0.164-11.20231001git31e19f92
- Rebuild for new ffmpeg version

* Sun Oct 01 2023 Sérgio Basto <sergio@serjux.com> - 0.164-10.20231001git31e19f92
- Update to x264-0.164-20231001git31e19f92 (stable branch)

* Wed Sep 27 2023 Sérgio Basto <sergio@serjux.com> - 0.164-9.20220602gitbaee400f
- [Bug 6769] Include bash completion definitions for x264

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.164-8.20220602gitbaee400f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 13 2023 Leigh Scott <leigh123linux@gmail.com> - 0.164-7.20220602gitbaee400f
- Rebuild for gpac

* Tue Feb 28 2023 Sérgio Basto <sergio@serjux.com> - 0.164-6.20220602gitbaee400f
- Disable build with gpac until we can build gapc with ffmepg-6

* Tue Feb 28 2023 Leigh Scott <leigh123linux@gmail.com> - 0.164-5.20220602gitbaee400f
- Rebuilt for new ffmpeg

* Sun Feb 19 2023 Leigh Scott <leigh123linux@gmail.com> - 0.164-4.20220602gitbaee400f
- rebuilt

* Sun Sep 04 2022 Leigh Scott <leigh123linux@gmail.com> - 0.164-3.20220602gitbaee400f
- Add requires ffmpeg-libs

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.164-2.20220602gitbaee400f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Mon Jun 06 2022 Sérgio Basto <sergio@serjux.com> - 0.164-1.20220602gitbaee400f
- Update to x264-0.164-20220602gitbaee400f (stable branch)

* Sat Mar 05 2022 Sérgio Basto <sergio@serjux.com> - 0.163-6.20210613git5db6aa6
- Rebuild for new gpac on F36

* Sat Feb 26 2022 Leigh Scott <leigh123linux@gmail.com> - 0.163-5.20210613git5db6aa6
- Rebuild for new gpac

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.163-4.20210613git5db6aa6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 09 2021 Leigh Scott <leigh123linux@gmail.com> - 0.163-3.20210613git5db6aa6
- Rebuilt for new ffmpeg snapshot

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.163-2.20210613git5db6aa6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jun 14 2021 Sérgio Basto <sergio@serjux.com> - 0.163-1.20210613git5db6aa6
- x264-0.163-20210613git5db6aa6 soname bump
- gpac patch accepted upstream with modifications

* Tue Apr 13 2021 Sérgio Basto <sergio@serjux.com> - 0.161-6.20210412git55d517b
- Update to x264-0.161-20210412git55d517b (stable branch)

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.161-5.20210124git544c61f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Sérgio Basto <sergio@serjux.com> - 0.161-4.20210124git544c61f
- Update to 0.161-20210124git544c61f (stable branch)

* Tue Jan 19 2021 Dominik Mierzejewski <rpm@greysector.net> - 0.161-3.20200912gitd198931
- Drop non-asm build for i686 and ppc64 (rfbz#5855)
- Use set_build_flags instead of configure macro for non-autotools script (rfbz#5854)

* Thu Dec 31 2020 Leigh Scott <leigh123linux@gmail.com> - 0.161-2.20200912gitd198931
- Rebuilt for new ffmpeg snapshot

* Wed Nov 18 2020 Sérgio Basto <sergio@serjux.com> - 0.161-1.20200912gitd198931
- Update x264 to api 0.161 (stable branch)

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.160-2.20200702gitcde9a93
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 06 2020 Sérgio Basto <sergio@serjux.com> - 0.160-1.20200702gitcde9a93
- Update to 0.160-20200702gitcde9a93 (stable branch)

* Mon Jul 06 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.159-11.20200409git296494a
- Bump

* Mon Jul 06 2020 Sérgio Basto <sergio@serjux.com> - 0.159-10.20200409git296494a
- Fix detection of gpac try 2

* Mon Jul 06 2020 Sérgio Basto <sergio@serjux.com> - 0.159-9.20200409git296494a
- Fix detection of gpac

* Wed Jun 10 2020 Sérgio Basto <sergio@serjux.com> - 0.159-8.20200409git296494a
- Update to 0.159-20200409git296494a (stable branch)
- Replace all __make _smp_mflags by make_build macro

* Thu Mar 12 2020 Leigh Scott <leigh123linux@gmail.com> - 0.159-7.20191127git1771b55
- Rebuilt for i686

* Wed Mar 11 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.159-6.20191127git1771b55_bootstrap
- bootstrap for i686

* Sat Feb 22 2020 Leigh Scott <leigh123linux@googlemail.com> - 0.159-5.20191127git1771b55
- Rebuild for ffmpeg-4.3 git

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.159-4.20191127git1771b55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.159-3.20191127git1771b55
- Rebuild without bootstrap

* Tue Dec 17 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.159-2.20191127git1771b55_bootstrap
- DO A BOOTSTRAP BUILD

* Mon Dec 16 2019 Sérgio Monteiro Basto <sergio@serjux.com> - 0.159-1.20191127git1771b55
- Update to 0.159-20191127-git1771b55 (stable branch)

* Fri Oct 04 2019 Dominik Mierzejewski <rpm@greysector.net> - 0.157-12.20190717git34c06d1
- don't overwrite generic headers with 10bit on simdarch (rfbz#5071)

* Mon Aug 26 2019 Nicolas Chauvet <kwizart@gmail.com> - 0.157-11.20190717git34c06d1
- Drop hack for arm builders

* Tue Aug 06 2019 Leigh Scott <leigh123linux@gmail.com> - 0.157-10.20190717git34c06d1
- Rebuild for new ffmpeg version

* Wed Jul 17 2019 Sérgio Basto <sergio@serjux.com> - 0.157-9.20190717git34c06d1
- 0.157 update, date 2019-07-17 (stable branch)

* Tue May 07 2019 Sérgio Basto <sergio@serjux.com> - 0.157-8.20190303git72db437
- Revert "Build /usr/bin/x264 with gpac shared lib instead static lib."

* Wed May 01 2019 Leigh Scott <leigh123linux@gmail.com> - 0.157-7.20190303git72db437
- Fix ARM rpm mangle issue

* Tue Apr 30 2019 Sérgio Basto <sergio@serjux.com> - 0.157-6.20190303git72db437_bootstrap
- Bootstrap to fix arm builds

* Mon Apr 29 2019 Sérgio Basto <sergio@serjux.com> - 0.157-5.20190303git72db437
- Enable opencl (which is default) only exist --disable-opencl option
- Disable opencl on 10bit seems that is just prepared for 8bit.
- Build /usr/bin/x264 with gpac shared lib instead static lib.

* Sun Apr 28 2019 Leigh Scott <leigh123linux@gmail.com> - 0.157-4.20190303git72db437
- Fix opencl dlopen (rfbz#5185)

* Tue Mar 12 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.157-3.20190303git72db437
- Disable bootstrap build

* Tue Mar 12 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.157-2.20190303git72db437_bootstrap
- Do the forgotten bootstrap build

* Tue Mar 12 2019 Sérgio Basto <sergio@serjux.com> - 0.157-1.20190303git72db437
- Update to 0.157 (stable branch)
- Rebase patches

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.155-3.20180806git0a84d98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 07 2018 Stefan Becker <chemobejk@gmail.com> - 0.155-2.20180806git0a84d98
- reverse order of generic/generic10 install to fix -devel contents (rfbz #5071)

* Thu Oct 04 2018 Sérgio Basto <sergio@serjux.com> - 0.155-1.20180806git0a84d98
- Update x264 to 0.155
- Rebase x264-10b.patch
- Add a patch to fix linking with --system-libx264 on x86
  ( https://patches.videolan.org/patch/21704/ )

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.152-7.20171224gite9a5903
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.152-6.20171224gite9a5903
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.152-5.20171224gite9a5903
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.152-4.20171224gite9a5903
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.152-3.20171224gite9a5903
- Rebuilt for ffmpeg-3.5 git

* Thu Jan 04 2018 Sérgio Basto <sergio@serjux.com> - 0.152-2.20171224gite9a5903
- un-bootstrap x264

* Sat Dec 30 2017 Sérgio Basto <sergio@serjux.com> - 0.152-1.20171224gite9a5903_bootstrap
- Update x264 to 0.152 and switch asm compiler from yasm to nasm

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.148-22.20170521gitaaa9aa8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Sérgio Basto <sergio@serjux.com> - 0.148-21.20170521gitaaa9aa8
- Update x264 to x264-0.148-20170521-aaa9aa8

* Mon May 22 2017 Sérgio Basto <sergio@serjux.com> - 0.148-20.20170519gitd32d7bf
- Update x264 to x264-0.148-20170519-d32d7bf

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.148-19.20170121git97eaef2
- Rebuild for ffmpeg update

* Wed Mar 22 2017 Sérgio Basto <sergio@serjux.com> - 0.148-18.20170121git97eaef2
- Unbootstrap

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.148-17.20170121git97eaef2_bootstrap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Mar 18 2017 Sérgio Basto <sergio@serjux.com> - 0.148-16.20170121git97eaef2_bootstrap
- Bootstrap for ppc64, ppc64le and aarch64

* Wed Jan 25 2017 Sérgio Basto <sergio@serjux.com> - 0.148-15.20170121git97eaef2
- Update x264 to git stable snapshot of 20170121

* Sat Dec 03 2016 Sérgio Basto <sergio@serjux.com> - 0.148-14.20161201git4d5c8b0
- Update to x264-0.148-20161201-4d5c8b0 stable branch
- Improve x264-snapshot.sh to use date from last commit and print the headers to
  include in x264.spec

* Sat Nov 05 2016 Sérgio Basto <sergio@serjux.com> - 0.148-13.20160924git86b7198
- Rebuilt for new ffmpeg

* Tue Sep 27 2016 Sérgio Basto <sergio@serjux.com> - 0.148-12.20160924git86b7198
- Update to 0.148-20160924-86b7198 version

* Fri Aug 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.148-11.20160614gita5e06b9
- rework asm treatment on i686 and ppc64
- fix adding the 10b suffix to the library name
- correct the list of ASM-enabled arches:
  * ppc64 can be Power5, which doesn't have AltiVec
  * ppc64le always has it
  * no implementation for sparc
- force non-executable stack on armv7 (#3975)
- explicitly disable OpenCL support, it's dlopened at the moment
  and not working without ocl-icd-devel
- drop doc and license from main package, libs already contain it
- update URL

* Thu Aug 18 2016 Sérgio Basto <sergio@serjux.com> - 0.148-10.20160614gita5e06b9
- Add license tag also to x264-libs

* Mon Aug 01 2016 Sérgio Basto <sergio@serjux.com> - 0.148-9.20160614gita5e06b9
- Enable asm in build with 10bit on i686

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.148-8.20160614gita5e06b9
- Rebuilt for ffmpeg-3.1.1

* Tue Jun 21 2016 Sérgio Basto <sergio@serjux.com> - 0.148-7.20160614gita5e06b9
- Update to last stable version upstream.

* Tue Apr 19 2016 Sérgio Basto <sergio@serjux.com> - 0.148-6.20160412gitfd2c324
- Update x264 to 0.148-20160412-fd2c324

* Wed Jan 20 2016 Sérgio Basto <sergio@serjux.com> - 0.148-5.20160118git5c65704
- Fix enable-asm #2

* Tue Jan 19 2016 Sérgio Basto <sergio@serjux.com> - 0.148-4.20160118git5c65704
- Fix enable-asm

* Mon Jan 18 2016 Nicolas Chauvet <kwizart@gmail.com> - 0.148-3.20160118git5c65704
- Restore explicit dependency on -libs - enforce %%{_isa}
- Expand arm arches where asm is available.
- Restore asm only on sse2 and later capable i686

* Mon Jan 18 2016 Sérgio Basto <sergio@serjux.com> - 0.148-2.20151020gita0cd7d3
- Update x264 to 0.148-20160118-5c65704

* Fri Nov 27 2015 Simone Caronni <negativo17@gmail.com>
- Remove obsolete SPEC file tags, defattr were also breaking file permissions,
  all libraries were not executable.
- Enable optimizations in RHEL, they are working since RHEL 6:
  https://bugzilla.rpmfusion.org/show_bug.cgi?id=3260
- Add license and make_install macro as per packaging guidelines.
- Use the default configure macro and remove redundant parameters. Optimizations
  (build flags) are now added by default.

* Wed Oct 21 2015 Sérgio Basto <sergio@serjux.com> - 0.148-1.20151020gita0cd7d3
- Update to x264-0.148, soname bump, git a0cd7d3, date 20151020 .

* Sat Jun 06 2015 Sérgio Basto <sergio@serjux.com> - 0.144-1.20150225gitc8a773e
- Update to x264-0.144, soname bump, git c8a773e from date 20150225 .

* Mon Jun 01 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 0.142-12.20141221git6a301b6
- Added patch to make it build on AArch64.

* Mon Dec 22 2014 Sérgio Basto <sergio@serjux.com> - 0.142-11.20141221git6a301b6
- Update x264-0.142 to git 6a301b6

* Sun Oct 19 2014 Sérgio Basto <sergio@serjux.com> - 0.142-10.20140826git021c0dc
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.142-9.20140826git021c0dc
- Rebuilt for FFmpeg 2.4.x

* Mon Sep 15 2014 Sérgio Basto <sergio@serjux.com> - 0.142-7.20140826git021c0dc
- Update x264-0.142 to git 021c0dc

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 0.142-6.20140728gitaf8e768
- Rebuilt for ffmpeg-2.3

* Mon Jul 28 2014 Sérgio Basto <sergio@serjux.com> - 0.142-5.20140728gitaf8e768
- Update x264-0.142 to git af8e768

* Wed Apr 23 2014 Sérgio Basto <sergio@serjux.com> - 0.142-4.20140423gite260ea5
- Update to git e260ea5 (stable branch)

* Tue Mar 25 2014 Sérgio Basto <sergio@serjux.com> - 0.142-3.20140314gitaff928d
- Rebuilt for ffmpeg-2.2

* Sun Mar 23 2014 Sérgio Basto <sergio@serjux.com> - 0.142-2.20140314gitaff928d
- Un-bootstrap

* Fri Mar 14 2014 Sérgio Basto <sergio@serjux.com> - 0.142-1.20140314gitaff928d_bootstrap
- Update to 0.142 git aff928d (stable branch) and bootstrap

* Mon Mar 10 2014 Sérgio Basto <sergio@serjux.com> - 0.140-3.20140122gitde0bc36
- Un-boostrap

* Wed Mar 05 2014 Sérgio Basto <sergio@serjux.com> - 0.140-2.20140122gitde0bc36
- bootstrap x264 to avoid: 
  /usr/bin/ld: warning: libx264.so.138, needed by
  /usr/lib/gcc/x86_64-redhat-linux/4.8.2/../../../../lib64/libavcodec.so, may conflict with
  libx264.so.140

* Wed Jan 22 2014 Sérgio Basto <sergio@serjux.com> - 0.140-1.20140122gitde0bc36
- Update to 0.140 git de0bc36 (stable branch)
- drop visualize options, ./configure doesn't have --enable-visualize or --disable-visualize, 
anymore

* Tue Nov 05 2013 Sérgio Basto <sergio@serjux.com> - 0.138-2.20131030-c628e3b
- Unbootstrap.

* Sat Nov 02 2013 Sérgio Basto <sergio@serjux.com> - 0.138-1.20131030-c628e3b
- Update to 0.138 git c628e3b (stable branch) and bootstrap for new ffmpeg.

* Fri Oct 18 2013 Sérgio Basto <sergio@serjux.com> - 0.136-1.20131005git3361d59
- Update to 0.136 git 3361d59 (stable branch).

* Mon Sep 30 2013 Sérgio Basto <sergio@serjux.com> - 0.133-3.20130709git585324f
- Fix gpac detection.

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.133-2.20130709git585324f
- Rebuilt for FFmpeg 2.0.x

* Tue Jul 09 2013 Sérgio Basto <sergio@serjux.com> - 0.133-1.20130709git585324f
- Update to git 585324fee380109acd9986388f857f413a60b896 (HEAD of stable branch).

* Sat May 25 2013 Sérgio Basto <sergio@serjux.com> - 0.130-3.20130502git1db4621
- Build without bootstrap for F19.

* Fri May 24 2013 Sérgio Basto <sergio@serjux.com> - 0.130-2.20130502git1db4621
- Build with bootstrap for F19.

* Thu May 02 2013 Sérgio Basto <sergio@serjux.com> - 0.130-1.20130502git1db4621
- Update to git 1db4621

* Tue Mar 05 2013 Sérgio Basto <sergio@serjux.com> - 0.129-3.20130305gite403db4
- Update to git e403db4f9079811f5a1f9a1339e7c85b41800ca7

* Sun Jan 20 2013 Sérgio Basto <sergio@serjux.com> - 0.129-2.20130119git9c4ba4b
- Rebuild for ffmpeg-1.1.1 .

* Sat Jan 19 2013 Sérgio Basto <sergio@serjux.com> - 0.129-1.20130119git9c4ba4b
- Update to 9c4ba4bde8965571159eae2d79f85cabbb47416c, soname bump.
- Changed branch name by api number, is more readable.
- Drop upstreamed patch.

* Fri Nov 23 2012 Sérgio Basto <sergio@serjux.com> - 0.128-2.20121118gitf6a8615
- unbootstrap on F18.

* Mon Nov 19 2012 Sérgio Basto <sergio@serjux.com> - 0.128-1.20121118gitf6a8615
- Update to f6a8615ab0c922ac2cb5c82c9824f6f4742b1725.

* Sat Oct 06 2012 Sérgio Basto <sergio@serjux.com> - 0.125-4.20121006git68dfb7b
- Note: no source update.
- Just add git tag to package name, for faster check upstream.
- Add git tag in x264-snapshot.sh .
- Convert all defines in global. 

* Sun Sep 09 2012 Sérgio Basto <sergio@serjux.com> - 0.125-4.20120909
- unbootstrap on F18.

* Sun Sep 09 2012 Sérgio Basto <sergio@serjux.com> - 0.125-3.20120909
- update x264-0.125 from r2201 to r2209.

* Thu Sep 06 2012 Sérgio Basto <sergio@serjux.com> - 0.125-2.20120904
- unbootstrap

* Tue Sep 04 2012 Sérgio Basto <sergio@serjux.com> - 0.125-1.20120904
- Pulled latest stable patches, which bump version to 0.125.

* Mon Jun 25 2012 Sérgio Basto <sergio@serjux.com> - 0.124-5.20120616
- Fixed detection of gf_malloc and gf_free

* Sun Jun 24 2012 Sérgio Basto <sergio@serjux.com> - 0.124-4.20120616
- unbootstrap.

* Sat Jun 23 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.124-3.20120616
- Rework alternatives build
- Fix SONAME for x26410b

* Sun Jun 17 2012 Sérgio Basto <sergio@serjux.com> - 0.124-2.20120616
- use _libdir to fix build on x86_64.

* Sun Jun 17 2012 Sérgio Basto <sergio@serjux.com> - 0.124-1.20120616
- Update to 20120616
- Add one build with --bit-depth=10
- Enabled bootstrap, after rebuild ffmpeg, we rebuild x264 without bootstrap.

* Tue May 01 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.120-5.20120303
- Forward rhel patch
- Disable ASM on armv5tel armv6l
- Add --with bootstrap conditional
- Use %%{_isa} for devel requires

* Tue Mar 6 2012 Sérgio Basto <sergio@serjux.com> - 0.120-2.20120303
- Enable libavformat , after compile ffmeg with 0.120-1

* Sat Mar 3 2012 Sérgio Basto <sergio@serjux.com> - 0.120-1.20120303
- Change release number, upstream have release numbers at least on stable branch and as ffmpeg
  reported.
- Update to 20120303
- Update x264-nover.patch, as suggest by Joseph D. Wagner <joe@josephdwagner.info> 
- Dropped obsolete Buildroot and Clean.
- add BuildRequires: zlib-devel to enable gpac.

* Wed Feb 22 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.0.0-0.34.20120125
- Rebuilt for F-17 inter branch

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.0.0-0.33.20120125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.0.0-0.32.20120125
- Update to 20120125

* Mon Aug 22 2011 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.31.20110811
- 20110811 snapshot (ABI 116)
- fix snapshot script to include version.h properly
- link x264 binary to the shared library

* Thu Jul 14 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.0.0-0.30.20110714
- Update to 20110714 stable branch (ABI 115)
- Convert x264-snapshot to git (based on ffmpeg script).
- New Build Conditionals --with ffmpegsource libavformat
- Remove shared and strip patches - undeeded anymore
- Remove uneeded convertion of AUTHORS

* Mon Jan 10 2011 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.29.20110227
- 20110227 snapshot (ABI bump)

* Tue Jul 06 2010 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.28.20100706gitd058f37
- 20100706 snapshot (ABI bump)
- drop old Obsoletes:

* Thu Apr 29 2010 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.27.20100429gitd9db8b3
- 20100429 snapshot
- s/%%{ix86}/i686 (rfbz #1075)
- ship more docs in -devel

* Sat Jan 16 2010 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.26.20100116git3d0f110
- 20100116 snapshot (SO version bump)
- don't remove config.h and don't re-run version.sh
- link x264 binary to the shared library
- really don't strip if debug is enabled

* Mon Oct 26 2009 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.26.20091026gitec46ace7
- 20091026 snapshot

* Thu Oct 15 2009 kwizart <kwizart at gmail.com > -  0.0.0-0.25.20091007git496d79d
- Update to 20091007git
- Move simd to %%{_libdir}/sse2

* Thu Mar 26 2009 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.24.20090319gitc109c8
- 20090319 snapshot
- build with static gpac
- fix build on ppc

* Tue Feb 10 2009 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.23.20090119git451ba8d
- 20090119 snapshot
- fix BRs for build-time options

* Sat Dec 20 2008 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.22.20081213git9089d21
- rebuild against new gpac

* Sat Dec 13 2008 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.21.20081213git9089d21
- fix the libs split on x86

* Sat Dec 13 2008 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.20.20081213git9089d21
- 20081213 snapshot
- drop the libs split on x86, it doesn't work right for P3/AthlonXP
- drop obsolete patch

* Thu Dec 04 2008 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.19.20081202git71d34b4.1
- fix compilation on ppc

* Tue Dec 02 2008 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.19.20081202git71d34b4
- 20081202 snapshot
- bring back asm optimized/unoptimized libs split
- rebase and improve patch
- GUI dropped upstream
- dropped redundant BRs

* Mon Nov 17 2008 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.18.20080905
- partially revert latest changes (the separate sse2 libs part) until selinux
  policy catches up

* Fri Nov 07 2008 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.17.20080905
- build libs without asm optimizations for less capable x86 CPUs (livna bug #2066)
- fix missing 0 in Obsoletes version (never caused any problems)

* Fri Sep 05 2008 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.16.20080905
- 20080905 snapshot
- use yasm on all supported arches
- include mp4 output support via gpac by default
- drop/move obsolete fixups from %%prep
- fix icon filename in desktop file

* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.0.0-0.15.20080613
- rebuild

* Sat Jun 14 2008 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.14.20080613
- 20080613 snapshot (.so >= 59 is required by current mencoder)

* Mon May 05 2008 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.13.20080420
- 20080420 snapshot
- split libs into a separate package
- svn -> git
- drop obsolete execstack patch
- fixed summaries and descriptions

* Wed Feb 27 2008 Dominik Mierzejewski <rpm@greysector.net> 0.0.0-0.12.20080227
- 20080227 snapshot
- fix build with gpac

* Tue Nov 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.0.0-0.11.20070819
- Merge freshrpms spec into livna spec for rpmfusion:
- Change version from 0 to 0.0.0 so that it is equal to the freshrpms versions,
  otherwise we would be older according to rpm version compare.
- Add Provides and Obsoletes x264-gtk to x264-gui for upgrade path from
  freshrpms
- Fix icon cache update scripts

* Sun Sep 30 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0-0.10.20070819
- Fix use of execstack on i386, closes livna bug #1659

* Sun Aug 19 2007 Dominik Mierzejewski <rpm@greysector.net> 0-0.9.20070819
- 20070819 snapshot, closes bug #1560

* Thu Nov 09 2006 Dominik Mierzejewski <rpm@greysector.net> 0-0.8.20061028
- use PIC on all platforms, fixes bug #1243

* Sun Oct 29 2006 Dominik Mierzejewski <rpm@greysector.net> 0-0.7.20061028
- fix desktop entry categories for devel

* Sun Oct 29 2006 Ville Skyttä <ville.skytta at iki.fi> - 0-0.6.20061028
- fix BRs
- handle menu icon properly

* Sat Oct 28 2006 Dominik Mierzejewski <rpm@greysector.net> 0-0.5.20061028
- fix bad patch chunk
- fix 32bit build on x86_64

* Sat Oct 28 2006 Ville Skyttä <ville.skytta at iki.fi> - 0-0.4.20061028
- Don't let ./configure to guess arch, pass it ourselves.
- Drop X-Livna desktop entry category.

* Sat Oct 28 2006 Dominik Mierzejewski <rpm@greysector.net> 0-0.3.20061028
- added GUI (based on kwizart's idea)
- latest snapshot
- added some docs to -devel

* Sun Oct 01 2006 Dominik Mierzejewski <rpm@greysector.net> 0-0.2.20061001
- add snapshot generator script
- fix make install
- make nasm/yasm BRs arch-dependent
- configure is not autoconf-based, call it directly

* Sat Sep 30 2006 Dominik Mierzejewski <rpm@greysector.net> 0-0.1.569
- Updated to latest SVN trunk
- specfile cleanups

* Mon Sep 04 2006 Dominik Mierzejewski <rpm@greysector.net> 0-0.1.558
- Updated to latest SVN trunk
- FE compliance

* Sun Mar 12 2006 Dominik Mierzejewski <rpm@greysector.net> 0-0.1.467
- Updated to latest SVN trunk
- Build shared library
- mp4 output requires gpac

* Mon Jan 02 2006 Dominik Mierzejewski <rpm@greysector.net> 0-0.1.394
- Updated to latest SVN trunk
- Change versioning scheme

* Sun Nov 27 2005 Dominik Mierzejewski <rpm@greysector.net> 0.0.375-1
- Updated to latest SVN trunk
- Added pkgconfig file to -devel

* Tue Oct  4 2005 Matthias Saou <http://freshrpms.net/> 0.0.315-1
- Update to svn 315.
- Disable vizualize since otherwise programs trying to link without -lX11 will
  fail (cinelerra in this particular case).

* Mon Aug 15 2005 Matthias Saou <http://freshrpms.net/> 0.0.285-1
- Update to svn 285.
- Add yasm build requirement (needed on x86_64).
- Replace X11 lib with lib/lib64 to fix x86_64 build.

* Tue Aug  2 2005 Matthias Saou <http://freshrpms.net/> 0.0.281-1
- Update to svn 281.

* Mon Jul 11 2005 Matthias Saou <http://freshrpms.net/> 0.0.273-1
- Initial RPM release.
