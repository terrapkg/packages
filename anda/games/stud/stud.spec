%global appid io.github.catpieleaf.Stud

# Installs the release archive Stud's CI builds, prebuilt ANGLE and bionic
# included.
%global debug_package %{nil}

# Prebuilt bionic and ANGLE binaries, not safe to strip.
%global __brp_strip %{nil}
%global __brp_strip_comment_note %{nil}
%global __brp_strip_static_archive %{nil}

# Stud loads these Android and ANGLE libraries itself, by path, so rpm must
# not require or provide anything for them.
%global __requires_exclude_from ^%{_prefix}/lib/stud/android-bionic/.*|^%{_libexecdir}/stud/lib64/.*|^%{_libexecdir}/stud/stud-runtime-bionic$
%global __provides_exclude_from ^%{_prefix}/lib/stud/(angle|android-bionic)/.*|^%{_libexecdir}/stud/lib64/.*

Name:           stud
Version:        1.2.1
Release:        1%{?dist}
Summary:        An Unofficial Open-Source Roblox Launcher for Linux

License:        AGPL-3.0-or-later
URL:            https://github.com/CatPieLeaf/Stud
Source0:        %{url}/releases/download/%{version}/stud-%{version}-x86_64.tar.zst
Packager:       CatPieLeaf <catpieleaf@proton.me>

ExclusiveArch:  x86_64

BuildRequires:  anda-srpm-macros
BuildRequires:  zstd

Requires:       bubblewrap
Requires:       hicolor-icon-theme
# Opened at runtime, so rpm can't detect these.
Recommends:     (libavcodec-free or ffmpeg-libs)
Requires:       libEGL.so.1()(64bit)
Requires:       libGLESv2.so.2()(64bit)
Recommends:     libxkbcommon-x11.so.0()(64bit)
Recommends:     libX11-xcb.so.1()(64bit)

Provides:       bundled(angle)
Provides:       bundled(bionic)
Provides:       bundled(swiftshader)
Provides:       bundled(vulkan-loader)
Provides:       bundled(fidelityfx-fsr1)
Provides:       bundled(snapdragon-gsr)
Provides:       bundled(mpv-prescalers)
Provides:       bundled(volk)
Provides:       bundled(xxhash)
Provides:       bundled(miniaudio)
Provides:       bundled(miniz)
Provides:       bundled(json)
Provides:       bundled(libjnivm)

%description
Stud runs the unmodified Roblox app in its own window on a Linux desktop,
played with a mouse and keyboard. It doesn't use a browser, an emulator or
a virtual machine.

Links from a browser open straight into the experience, and the mouse and
keyboard work the way they do in the desktop client. The game can render
below the screen's resolution and still fill it. Discord Rich Presence
shows a button friends can join through, and when you join a server, the
tray menu shows which country it's in.

Roblox isn't included. You supply the Android application package yourself,
and Roblox remains subject to its own terms. Stud is an independent project
and isn't affiliated with, endorsed by or approved by Roblox Corporation.

%prep
%autosetup -c -n %{name}-%{version}

%build

%install
cp -a usr %{buildroot}/

%files
%license %{_datadir}/licenses/%{name}/
%doc %{_datadir}/doc/%{name}/README.md
%doc %{_datadir}/doc/%{name}/copyright
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/
%{_libexecdir}/%{name}/
%{_datadir}/applications/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.png
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Sep 30 2026 CatPieLeaf <catpieleaf@proton.me> - 1.1.10-1
- Initial package
