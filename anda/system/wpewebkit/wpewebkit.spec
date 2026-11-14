%global toolchain clang

Name:           wpewebkit
Version:        2.54.2
Release:        1%{?dist}
Summary:        A WebKit port optimized for low-end devices

SourceLicense:  BSD-2-Clause AND BSD-3-Clause AND LGPL-2.0-or-later AND LGPL-2.1-or-later
License:        BSD-2-Clause AND BSD-3-Clause AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND Apache-2.0 AND (Apache-2.0 OR MIT OR BSL-1.0) AND Apache-2.0 WITH LLVM-exception AND (Apache-2.0 WITH LLVM-exception OR BSL-1.0) AND (AFL-2.0 OR LGPL-2.0-or-later) AND BSL-1.0 AND bzip2-1.0.6 AND CC0-1.0 AND GPL-2.0-or-later WITH Bison-exception-2.2 AND GPL-3.0-or-later WITH Bison-exception-2.2 AND ISC AND (LGPL-2.1-or-later OR MPL-1.1 OR GPL-2.0-only) AND MIT AND MIT-Khronos-old AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later) AND MPL-2.0 AND NCSA AND (NCSA OR MIT) AND OFL-1.1 AND SunPro AND Unicode-3.0
URL:            https://www.wpewebkit.org/
Source0:        https://wpewebkit.org/releases/%{name}-%{version}.tar.xz
# Fix a build race: the JavaScriptCoreJIT PCH subtarget was not ordered after
# the JavaScriptCore forwarding header copy targets.
Patch0:         jsc-subtarget-header-deps.patch

BuildRequires: atk-devel at-spi2-atk-devel
BuildRequires: bison
BuildRequires: cmake
BuildRequires: enchant2-devel
BuildRequires: expat-devel
BuildRequires: flex
BuildRequires: flite-devel
BuildRequires: clang
BuildRequires: lld
BuildRequires: gperf
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-bad-free-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: harfbuzz-devel
BuildRequires: hyphen-devel
BuildRequires: libatomic
BuildRequires: libepoxy-devel
BuildRequires: libicu-devel
BuildRequires: libinput-devel
BuildRequires: libjpeg-devel
BuildRequires: libjxl-devel
BuildRequires: libmanette-devel
BuildRequires: libpng-devel
BuildRequires: libwebp-devel
BuildRequires: libwpe-devel
BuildRequires: libxslt-devel
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libgbm-devel
BuildRequires: ninja-build
BuildRequires: openssl-devel
BuildRequires: perl(English)
BuildRequires: perl(File::Copy::Recursive)
BuildRequires: perl-File-Find
BuildRequires: perl(FindBin)
BuildRequires: perl(JSON::PP)
BuildRequires: perl(lib)
BuildRequires: perl(Switch)
BuildRequires: perl-bignum
BuildRequires: python3
BuildRequires: ruby
BuildRequires: rubygem(getoptlong)
BuildRequires: rubygem-json
BuildRequires: rubygems
BuildRequires: sqlite-devel
BuildRequires: systemd-devel
BuildRequires: unifdef
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel
BuildRequires: woff2-devel
BuildRequires: wpebackend-fdo-devel
BuildRequires: bubblewrap
BuildRequires: libgcrypt-devel
BuildRequires: libseccomp-devel
BuildRequires: xdg-dbus-proxy
BuildRequires: lcms2-devel

BuildRequires: pkgconfig(libavif)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libtasn1)
BuildRequires: pkgconfig(libsoup-3.0)

Requires: atk
Requires: at-spi2-atk
Requires: bubblewrap
Requires: xdg-dbus-proxy

Packager: Cypress Reed <cypress@fyralabs.com>

%description
WPE allows embedders to create simple and performant systems based on
Web platform technologies. It is designed with hardware acceleration
in mind, leveraging common 3D graphics APIs for best performance.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries, build data, and header
files for developing applications that use %{name}

%prep
%autosetup -p1 -n wpewebkit-%{version}

%conf
# WebKit's LTO_MODE handles LTO itself; don't let redhat-rpm-config add
# -flto=thin on top (which also made riscv64 get LTO anyway).
# Must come before anything below that expands optflags/build_ldflags.
%global _lto_cflags %{nil}

# Only emit line tables. Full -g makes ThinLTO links and find-debuginfo/dwz
# take a very long time and huge amounts of RAM, and backtraces work fine with -g1.
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')

# WebKit only picks lld when LTO_MODE is set, use it everywhere.
%global build_ldflags %{build_ldflags} -fuse-ld=lld

# dwz can't handle clang's DWARF 5 output (.debug_str_offsets) and bails anyway.
%global _find_debuginfo_dwz_opts %{nil}

# Multithreaded zstd at the default level, the huge payloads are otherwise
# compressed on a single core.
%global _binary_payload w19T.zstdio

# JIT is broken on ARM systems with new ARMv8.5 BTI extension at the moment
# Cf. https://bugzilla.redhat.com/show_bug.cgi?id=2130009
# Cf. https://bugs.webkit.org/show_bug.cgi?id=245697
# Disable BTI until this is fixed upstream.
%ifarch aarch64
%global optflags %(echo %{optflags} | sed 's/-mbranch-protection=standard /-mbranch-protection=pac-ret /')
%endif

%cmake \
%ifnarch riscv64
  -DLTO_MODE=thin \
%endif
  -DPORT=WPE \
  -DCMAKE_BUILD_TYPE=Release \
  -DENABLE_MINIBROWSER=ON \
  -DENABLE_DOCUMENTATION=OFF \
  -DENABLE_INTROSPECTION=OFF \
  -DUSE_LIBBACKTRACE=OFF \
  -DENABLE_WPE_PLATFORM=ON \
  -GNinja

%build
# Show the build time in the status
export NINJA_STATUS="[%f/%t][%e] "
%cmake_build

%install
%cmake_install

# Many bundled license files share a name (e.g. "LICENSE"), so flatten each
# path into the filename: Source/ThirdParty/skia/LICENSE -> Source.ThirdParty.skia.LICENSE
mkdir -p _license_files
for f in \
  Source/WebCore/LICENSE-APPLE \
  Source/WebCore/LICENSE-LGPL-2 \
  Source/WebCore/LICENSE-LGPL-2.1 \
  Source/JavaScriptCore/COPYING.LIB \
  Source/JavaScriptCore/disassembler/ARM64/LICENSE-binja.txt \
  Source/JavaScriptCore/disassembler/zydis/LICENSE-zycore.txt \
  Source/JavaScriptCore/disassembler/zydis/LICENSE-zydis.txt \
  Source/JavaScriptCore/runtime/temporal/core/LICENSE-icu4x.txt \
  Source/JavaScriptCore/runtime/temporal/core/LICENSE-temporal_rs.txt \
  Source/WTF/LICENSE-LLVM.txt \
  Source/WTF/LICENSE-dragonbox.txt \
  Source/WTF/LICENSE-libc++.txt \
  Source/WTF/LICENSE-simde.txt \
  Source/WTF/wtf/dtoa/COPYING \
  Source/WTF/wtf/dtoa/LICENSE \
  Source/WTF/wtf/fast_float/LICENSE \
  Source/WTF/wtf/simdutf/LICENSE-simdutf.txt \
  Source/bmalloc/mimalloc/mimalloc/LICENSE \
  Source/WebInspectorUI/UserInterface/External/CSSDocumentation/LICENSE \
  Source/WebInspectorUI/UserInterface/External/CodeMirror/LICENSE \
  Source/WebInspectorUI/UserInterface/External/Esprima/LICENSE \
  Source/WebInspectorUI/UserInterface/External/three.js/LICENSE \
  Source/ThirdParty/ANGLE/LICENSE \
  Source/ThirdParty/ANGLE/src/common/third_party/xxhash/LICENSE \
  Source/ThirdParty/ANGLE/src/third_party/ceval/LICENSE \
  Source/ThirdParty/ANGLE/tools/flex-bison/third_party/skeletons/LICENSE \
  Source/ThirdParty/skia/LICENSE \
  Source/ThirdParty/skia/modules/skcms/LICENSE \
  Source/ThirdParty/pdfjs/LICENSE \
  Source/ThirdParty/pdfjs/web/cmaps/LICENSE \
  Source/ThirdParty/pdfjs/web/iccs/LICENSE \
  Source/ThirdParty/pdfjs/web/standard_fonts/LICENSE_FOXIT \
  Source/ThirdParty/pdfjs/web/standard_fonts/LICENSE_LIBERATION \
  Source/ThirdParty/pdfjs/web/wasm/LICENSE_JBIG2 \
  Source/ThirdParty/pdfjs/web/wasm/LICENSE_OPENJPEG \
  Source/ThirdParty/pdfjs/web/wasm/LICENSE_PDFJS_JBIG2 \
  Source/ThirdParty/pdfjs/web/wasm/LICENSE_PDFJS_OPENJPEG \
  Source/ThirdParty/pdfjs/web/wasm/LICENSE_PDFJS_QCMS \
  Source/ThirdParty/pdfjs/web/wasm/LICENSE_QCMS
do
  cp -p "$f" "_license_files/${f//\//.}"
done

%files
%{_bindir}/WPEWebDriver
%{_libdir}/libWPEWebKit-2.0.so.*
%{_libexecdir}/wpe-webkit-2.0
%{_libdir}/wpe-webkit-2.0
%{_datadir}/wpe-webkit-2.0
%doc NEWS
%license _license_files/*

%files devel
%{_includedir}/wpe-webkit-2.0
%{_libdir}/libWPEWebKit-2.0.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Fri Oct 16 2026 Cypress Reed <cypress@fyralabs.com>
- port to Terra from COPR philn/wpewebkit
