%global toolchain clang

Name:           wpewebkit
Version:        2.54.1
Release:        1%{?dist}
Summary:        A WebKit port optimized for low-end devices

License:        LGPLv2 AND BSD
URL:            https://www.wpewebkit.org/
Source0:        https://wpewebkit.org/releases/%{name}-%{version}.tar.xz

BuildRequires: atk-devel at-spi2-atk-devel
BuildRequires: bison
BuildRequires: cairo-devel
BuildRequires: cmake
BuildRequires: egl-wayland-devel
BuildRequires: enchant2-devel
BuildRequires: expat-devel
BuildRequires: flex
BuildRequires: flite-devel
BuildRequires: clang
BuildRequires: gi-docgen
BuildRequires: gperf
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-bad-free-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: harfbuzz-devel
BuildRequires: hyphen-devel
BuildRequires: pkgconfig(gobject-introspection-1.0)
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
BuildRequires: mold

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
# Increase the DIE limit so our debuginfo packages could be size optimized.
# Decreases the size for x86_64 from ~5G to ~1.1G.
# https://bugzilla.redhat.com/show_bug.cgi?id=1456261
%global _dwz_max_die_limit 250000000

# The _dwz_max_die_limit is being overridden by the arch specific ones from the
# redhat-rpm-config so we need to set the arch specific ones as well - now it
# is only needed for x86_64.
%global _dwz_max_die_limit_x86_64 250000000

# Require 32 GB of RAM per vCPU for debuginfo processing. 16 GB is not enough.
%global _find_debuginfo_opts %limit_build -m 32768

# Reduce debuginfo verbosity 32-bit builds to reduce memory consumption even more.
# https://bugs.webkit.org/show_bug.cgi?id=140176
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/I6IVNA52TXTBRQLKW45CJ5K4RA4WNGMI/
%ifarch %{ix86}
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif

# JIT is broken on ARM systems with new ARMv8.5 BTI extension at the moment
# Cf. https://bugzilla.redhat.com/show_bug.cgi?id=2130009
# Cf. https://bugs.webkit.org/show_bug.cgi?id=245697
# Disable BTI until this is fixed upstream.
%ifarch aarch64
%global optflags %(echo %{optflags} | sed 's/-mbranch-protection=standard /-mbranch-protection=pac-ret /')
%endif

%cmake \
  -DCMAKE_EXE_LINKER_FLAGS=-fuse-ld=lld \
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
# path into the filename: Source/WTF/icu/LICENSE -> Source.WTF.icu.LICENSE
mkdir -p _license_files
for f in \
  Source/JavaScriptCore/disassembler/zydis/LICENSE-zydis.txt \
  Source/JavaScriptCore/disassembler/zydis/LICENSE-zycore.txt \
  Source/WebCore/LICENSE-LGPL-2 \
  Source/WebCore/LICENSE-APPLE \
  Source/WebCore/LICENSE-LGPL-2.1 \
  Source/WTF/LICENSE-libc++.txt \
  Source/WTF/wtf/dtoa/LICENSE \
  Source/WTF/LICENSE-LLVM.txt \
  Source/WTF/icu/LICENSE \
  Source/WebInspectorUI/UserInterface/External/Esprima/LICENSE \
  Source/WebInspectorUI/UserInterface/External/CodeMirror/LICENSE \
  Source/WebInspectorUI/UserInterface/External/three.js/LICENSE \
  Source/WebInspectorUI/UserInterface/External/CSSDocumentation/LICENSE \
  Source/ThirdParty/gtest/LICENSE \
  Source/ThirdParty/ANGLE/src/libANGLE/renderer/vulkan/shaders/src/third_party/ffx_spd/LICENSE \
  Source/ThirdParty/ANGLE/src/libANGLE/renderer/vulkan/shaders/src/third_party/etc_decoder/LICENSE \
  Source/ThirdParty/ANGLE/src/third_party/ceval/LICENSE \
  Source/ThirdParty/ANGLE/src/third_party/volk/LICENSE.md \
  Source/ThirdParty/ANGLE/src/third_party/libXNVCtrl/LICENSE \
  Source/ThirdParty/ANGLE/src/common/third_party/xxhash/LICENSE \
  Source/ThirdParty/ANGLE/src/tests/test_utils/third_party/LICENSE \
  Source/ThirdParty/ANGLE/util/windows/third_party/StackWalker/LICENSE \
  Source/ThirdParty/ANGLE/LICENSE \
  Source/ThirdParty/ANGLE/tools/flex-bison/third_party/m4sugar/LICENSE \
  Source/ThirdParty/ANGLE/tools/flex-bison/third_party/skeletons/LICENSE \
  Source/ThirdParty/ANGLE/third_party/colorama/LICENSE \
  Source/ThirdParty/ANGLE/third_party/r8/LICENSE \
  Source/ThirdParty/ANGLE/third_party/android_system_sdk/LICENSE \
  Source/ThirdParty/ANGLE/third_party/proguard/LICENSE \
  Source/ThirdParty/ANGLE/third_party/flatbuffers/LICENSE \
  Source/ThirdParty/ANGLE/third_party/turbine/LICENSE
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
