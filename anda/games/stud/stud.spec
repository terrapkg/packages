%global appid io.github.catpieleaf.Stud

%global debug_package %{nil}

Name:           stud
Version:        2.0.2
Release:        1%{?dist}
Summary:        An Unofficial Open-Source Roblox Launcher for Linux

License:        AGPL-3.0-or-later
URL:            https://github.com/CatPieLeaf/Stud
Source0:        %{url}/releases/download/%{version}/stud-%{version}-x86_64.tar.zst
Packager:       CatPieLeaf <catpieleaf@proton.me>

ExclusiveArch:  x86_64

BuildRequires:  anda-srpm-macros
BuildRequires:  zstd

Requires:       hicolor-icon-theme
Requires:       SDL3 >= 3.4.0
Requires:       libvulkan.so.1()(64bit)
Requires:       libavcodec-free
Requires:       libavutil-free
Requires:       gamemode
Suggests:       mangohud

Provides:       bundled(rosemary)
Provides:       bundled(fidelityfx-fsr1)
Provides:       bundled(snapdragon-gsr)
Provides:       bundled(mpv-prescalers)
Provides:       bundled(volk)
Provides:       bundled(miniz)
Provides:       bundled(json)

%description
Stud runs the real, unmodified Roblox macOS client on your Linux desktop, in
its own window, with your mouse and keyboard, through Rosemary. No virtual
machine, no emulator.

It downloads and updates the client from Roblox's own servers before each
launch, and runs Roblox Studio too. Links from a browser open straight into
the experience. FastFlags, customizations, Discord Rich Presence with a join
button, game history and an optional note of the server's country come with
it.

Roblox is not included: Stud downloads it from Roblox's own servers, and
Roblox remains subject to its own terms. Stud is an independent project, not
affiliated with, endorsed by or approved by Roblox Corporation.

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
%{_libexecdir}/%{name}/
%{_datadir}/applications/%{appid}*.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_datadir}/mime/packages/%{appid}.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}*.png
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Nov 15 2026 CatPieLeaf <catpieleaf@proton.me> - 2.0.1-1
- Fixed: Roblox could close on its own every time you launched it after logging in
- Fixed: Discord Rich Presence switched to "In the Roblox app" after a game teleported you, for example into a lobby
- New: a Debug page in Settings, to export logs, copy system info, repair Roblox and clear Stud's data
- When Roblox puts your account on a test channel, Stud now installs that channel's build
- When Roblox closes before its window opens, Stud now says so instead of closing silently

* Sun Nov 15 2026 CatPieLeaf <catpieleaf@proton.me> - 2.0.0-1
- Stud now runs the real Roblox macOS desktop client on Rosemary, instead of the Android app
- No more APKs: Stud downloads Roblox from Roblox's own servers and keeps it up to date before every launch
- Stud now has a welcome screen, offering to choose between Roblox Studio and Roblox Player
- .rbxl and .rbxlx place files open straight in Studio
- Customizations: textures, sounds, fonts and cursors, plus import from Bloxstrap, Fishstrap and Froststrap
- FastFlags: profiles, presets, and a warning for non whitelisted fflags.
- Roblox's own settings (volume, sensitivity, camera...) editable from Stud
- Server history: see where each server was, and rejoin it
- Launch wrapper and environment variables, for gamescope, prime-run and the like
- The AppImage now updates itself
- Updating from 1.x frees gigabytes: the Android engine, APK and caches are removed, and your settings, FFlags, customizations and logs are kept

* Sun Nov 08 2026 CatPieLeaf <catpieleaf@proton.me> - 1.2.14-1
- Fixed: Stud froze for about 8 seconds at every launch, on every GPU
- Fixed: voice chat stayed on "connecting" forever, or timed out saying it couldn't use the microphone
- Fixed: Roblox could make every other application's sound crackle or clip
- Improved: faster loading on AMD GPUs
- Improved: many more controllers are recognised and mapped correctly

* Fri Nov 06 2026 CatPieLeaf <catpieleaf@proton.me> - 1.2.13-1
- Fixed: Windows Graphical Parity turned off without saying so when your APK was older than the Windows client
- Changed: the README now points to Uptodown and APKMirror for getting an APK

* Fri Nov 06 2026 CatPieLeaf <catpieleaf@proton.me> - 1.2.12-1
- Fixed: Plastic surfaces in Windows Graphical Parity could break up into big flat triangles, and looked wrong up close
- New: Stud reopens the way you left it: windowed, maximized or fullscreen, at the same size
- New: Roblox's own Fullscreen option in the in-game menu now works
- F11 and the in-game Fullscreen option now stay in step
- Better: Windows Graphical Parity looks closer to Windows
- Better: Stud no longer runs with limits meant for phones

* Thu Nov 05 2026 CatPieLeaf <catpieleaf@proton.me> - 1.2.11-1
- Fixed: the game could look blurry in a window on a scaled display (125%%, 130%%...)
- Fixed: Discord Rich Presence didn't show if Equibop, Vesktop or Discord opened or restarted after Stud
- Voice chat: Stud now gives Roblox what it needs for the microphone and calls
- Fixed: failed launches that left an empty window, or an invisible Stud running forever
- Fixed: saving Settings could reset settings you'd edited by hand
- Fixed: the pointer could stay trapped in the window after Alt-Tab or leaving a game
- Fixed: Ctrl+A, C, X and V in text boxes on AZERTY and Dvorak
- Fixed: the first paste of a session did nothing on Wayland
- Old APK copies are now cleaned up, which can free gigabytes
- Roblox's sandbox is stricter, and logs no longer carry join tickets or your account name
- Dozens of safety and stability fixes

* Thu Nov 05 2026 CatPieLeaf <catpieleaf@proton.me> - 1.2.10-1
- New: logging in and creating accounts now happen on Roblox's own website, inside a Stud window
- Fixed: the login security check that never finished
- New: Stud checks a Roblox APK before importing it, and says what's missing if it can't run it
- Fixed: a crafted link could make Stud send your Roblox session to another website
- Fixed: music no longer lags for a moment when you open the Esc menu
- The microphone now only runs while Roblox is actually using it
- X11: text boxes stay inside Stud's window, OpenGL mode shows its window again, and MangoHud no longer breaks it
- Discord: Rich Presence now finds Flatpak, Vesktop/Equibop and Snap Discord
- Multiple monitors: rotated screens and refresh rates are now correct
- Fixed: rare random crashes, and freezes that never ended
- Dozens of safety and stability fixes

* Mon Nov 02 2026 CatPieLeaf <catpieleaf@proton.me> - 1.2.9-1
- Fixed: the Flatpak started, but Roblox never opened
- New defaults: HiDPI off, upscaling on (RAVU on Vulkan, SGSR on OpenGL)

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
