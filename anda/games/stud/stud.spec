%global appid io.github.catpieleaf.Stud

# Installs the release archive Stud's CI builds, prebuilt ANGLE and bionic
# included.
%global debug_package %{nil}

# Prebuilt bionic and ANGLE binaries, not safe to strip.
%global __brp_strip %{nil}
%global __brp_strip_comment_note %{nil}
%global __brp_strip_static_archive %{nil}

%global __requires_exclude_from ^%{_prefix}/lib/stud/android-bionic/.*|^%{_prefix}/lib/stud/gfxstream-guest/.*|^%{_libexecdir}/stud/lib64/.*|^%{_libexecdir}/stud/stud-runtime-bionic$
%global __provides_exclude_from ^%{_prefix}/lib/stud/.*|^%{_libexecdir}/stud/lib64/.*|^%{_libexecdir}/stud/libstud_present_layer\.so$

Name:           stud
Version:        1.2.10
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
Recommends:     (libavcodec-free or ffmpeg-libs)
Requires:       libEGL.so.1()(64bit)
Requires:       libGLESv2.so.2()(64bit)
Recommends:     libxkbcommon-x11.so.0()(64bit)
Recommends:     libX11-xcb.so.1()(64bit)

Provides:       bundled(bionic)
Provides:       bundled(gfxstream)
Provides:       bundled(mesa)
Provides:       bundled(fidelityfx-fsr1)
Provides:       bundled(snapdragon-gsr)
Provides:       bundled(mpv-prescalers)
Provides:       bundled(volk)
Provides:       bundled(xxhash)
Provides:       bundled(miniaudio)
Provides:       bundled(miniz)
Provides:       bundled(json)
Provides:       bundled(libjnivm)
Provides:       bundled(zydis)
Provides:       bundled(zycore)

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
* Mon Nov 02 2026 CatPieLeaf <catpieleaf@proton.me> - 1.2.8-1
- New setting: HQ Textures (Unstable), in Settings > Graphics
- Textures and game cursors (like Regretevator's) are sharp instead of blurry and blocky
- Keyboard layouts: AZERTY walks on ZQSD, and the number row is the hotbar on every layout

* Mon Nov 02 2026 CatPieLeaf <catpieleaf@proton.me> - 1.2.7-1
- OpenGL mode rebuilt on gfxstream: MSAA, UI gradients and correct highlight outlines on OpenGL
- Windows Graphical Parity (Beta) now works in OpenGL mode as well as Vulkan
- A lot of performance work on the Vulkan path: textures, pipelines, the connection to the engine, and the GPU's own work per frame
- A loading screen while Stud starts, so there's something to look at before the game window appears
- Building from source now needs meson

* Sat Oct 24 2026 CatPieLeaf <catpieleaf@proton.me> - 1.2.6-1
- New setting, on by default: Windows Graphical Parity (Beta), in Settings > Graphics
- Parts get the Windows client's materials: reflections, the shine of sunlight on them, and their normal maps
- Highlight outlines are drawn with High quality MSAA, as they are on Windows

* Sat Oct 24 2026 CatPieLeaf <catpieleaf@proton.me> - 1.2.5-1
- New setting, on by default: Windows Graphical Parity (Beta), in Settings > Graphics
- Parts get the Windows client's materials: reflections, the shine of sunlight on them, and their normal maps
- Highlight outlines are drawn with High quality MSAA, as they are on Windows

* Fri Oct 23 2026 CatPieLeaf <catpieleaf@proton.me> - 1.2.4-1
- Roblox 2.744.1081 opens and plays again
- A Roblox update that needs an Android function Stud doesn't have yet no longer stops the game from opening

* Fri Oct 23 2026 CatPieLeaf <catpieleaf@proton.me> - 1.2.3-1
- Roblox 2.744.1081 opens and plays again
- A Roblox update that needs an Android function Stud doesn't have yet no longer stops the game from opening

* Thu Oct 22 2026 CatPieLeaf <catpieleaf@proton.me> - 1.2.2-1
- Leaving a game, from the menu or by closing the window, no longer freezes Stud
- The camera and cursor no longer stop for a moment every second
- Audio no longer waits for the renderer, so a busy frame is no longer a gap in the sound
- Pasting a script keeps every line, and a very long line no longer crashes Stud
- F11 toggles fullscreen
- The AppImage's login page no longer crashes
- Stud is now a Nix flake

* Tue Oct 06 2026 CatPieLeaf <catpieleaf@proton.me> - 1.2.1-1
- Big performance improvements: the game waits on Stud's renderer far less every frame
- GameMode switch in Settings
- Leaving first person while holding a mouse button no longer teleports the cursor
- An unfocused Stud window no longer grabs or moves your mouse
- X11 mouse look is no longer twice as sensitive as on Wayland
- Stud warns you when the imported Roblox build is out of date

* Sun Oct 04 2026 CatPieLeaf <catpieleaf@proton.me> - 1.2.0-1
- NVIDIA Freezes are GONE!
- Stud presents the game's frames itself, on Wayland and on X11
- No more lag on launching stud
- No black flashes on X11 when a game opens
- Mouse lock and the captured pointer behave the way the game expects
- ANGLE is gone

* Fri Oct 02 2026 CatPieLeaf <catpieleaf@proton.me> - 1.1.11-1
- Resizing, maximizing and restoring the window is smooth on Wayland and X11
- Fixed a leak that made Stud slower the longer it ran
- The AppImage now carries everything it needs, glibc and graphics drivers included, and runs on FUSE-less systems
- The AppImage can update itself in place with AppImageUpdate and other updaters

* Wed Sep 30 2026 CatPieLeaf <catpieleaf@proton.me> - 1.1.10-1
- Initial package
