# Binary package, no debuginfo should be generated
%global debug_package %{nil}
%global appid com.valvesoftware.Steam

Name:           steam
Version:        1.0.0.86
Release:        1%{?dist}
Summary:        Installer for the Steam software distribution service
# Redistribution and repackaging for Linux is allowed, see license file. udev rules are MIT.
License:        Steam License Agreement and MIT
URL:            http://www.steampowered.com/
ExclusiveArch:  x86_64
Packager:       Cappy Ishihara <cappy@fyralabs.com>

Source0:        https://repo.steampowered.com/%{name}/archive/beta/%{name}_%{version}.tar.gz
Source1:        https://github.com/terrapkg/pkg-steam/raw/refs/heads/main/steam.sh
Source2:        https://github.com/terrapkg/pkg-steam/raw/refs/heads/main/steam.csh
Source5:        https://github.com/terrapkg/pkg-steam/raw/refs/heads/main/README.Fedora

# Ghost touches in Big Picture mode:
# https://github.com/ValveSoftware/steam-for-linux/issues/3384
# https://bugzilla.kernel.org/show_bug.cgi?id=28912
# https://github.com/denilsonsa/udev-joystick-blacklist
# https://github.com/systemd/systemd/issues/32773

# Configure limits in systemd
Source6:        https://github.com/terrapkg/pkg-steam/raw/refs/heads/main/01-steam.conf

# Steam restart script
Source7:       steamrestart.sh

# Do not install desktop file in lib/steam, do not install apt sources
Patch0:         https://github.com/terrapkg/pkg-steam/raw/refs/heads/main/steam-makefile.patch
# Do not try to copy steam.desktop to the user's desktop from lib/steam
Patch1:         https://github.com/terrapkg/pkg-steam/raw/refs/heads/main/steam-no-icon-on-desktop.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  systemd

# Required for the basic runtime
Requires:       glibc(x86-32)
Requires:       libdrm(x86-32)
Requires:       libglvnd-glx(x86-32)
Requires:       libnsl(x86-32)

# Required to run the initial setup
Requires:       tar
Requires:       zenity
Requires:       xz

# Required for basic gaming, also for native 32 bit games:
Requires:       mesa-dri-drivers
Requires:       mesa-dri-drivers(x86-32)
Requires:       mesa-vulkan-drivers
Requires:       mesa-vulkan-drivers(x86-32)
Requires:       vulkan-loader
Requires:       vulkan-loader(x86-32)

# Hardware stuff (permissions on devices, hardware updater, etc.):
Recommends:     hidapi
Requires:       steam-devices

# These libraries are also part of the Ubuntu runtime at:
#   ~/.local/share/Steam/ubuntu12_32
#   ~/.local/share/Steam/ubuntu12_64
# Steam client uses the system ones if available; so override where there is a
# benefit using the native system libaries or just to match when the native 64
# bit packages are already installed.
Requires:       bzip2-libs
Requires:       bzip2-libs(x86-32)
Requires:       fontconfig
Requires:       fontconfig(x86-32)
Requires:       libICE
Requires:       libICE(x86-32)
Requires:       libnsl
Requires:       libnsl(x86-32)
Requires:       libXext
Requires:       libXext(x86-32)
Requires:       libXinerama
Requires:       libXinerama(x86-32)
Requires:       libXtst
Requires:       libXtst(x86-32)
Requires:       libva
Requires:       libva(x86-32)
Requires:       libvdpau
Requires:       libvdpau(x86-32)
Requires:       mesa-libGL
Requires:       mesa-libGL(x86-32)
Requires:       NetworkManager-libnm
Requires:       NetworkManager-libnm(x86-32)
Requires:       nss
Requires:       nss(x86-32)
Requires:       openal-soft
Requires:       openal-soft(x86-32)
Requires:       pipewire-libs
Requires:       pipewire-libs(x86-32)
Requires:       pulseaudio-libs
Requires:       pulseaudio-libs(x86-32)
%if %{defined fedora}
Requires:       SDL3
Requires:       SDL3(x86-32)
%endif
# The client does not override only the ones linked at:
#   ~/.local/share/Steam/ubuntu12_32/steam-runtime/pinned_libs_32
#   ~/.local/share/Steam/ubuntu12_32/steam-runtime/pinned_libs_64
# At the moment of writing, the pinned ones belong to these packages:
#   gtk2
#   libcurl
#   libdbusmenu
#   libdbusmenu-gtk2
#   mesa-libGLU
# And yes, the "ubuntu12_32" directory twice above is not a typo. Windows style (system32...).

# Required for the firewall rules
# http://fedoraproject.org/wiki/PackagingDrafts/ScriptletSnippets/Firewalld
Requires:       firewalld-filesystem
Requires(post): firewalld-filesystem

# Required by Feral interactive games
Requires:       libatomic
Requires:       libatomic(x86-32)

# Required by Shank
Requires:       (alsa-plugins-pulseaudio if pulseaudio)

# Game performance is increased with gamemode (for games that support it)
Recommends:     (falcond or gamemode)
Recommends:     (gnome-shell-extension-appindicator if gnome-shell)

# Proton uses xdg-desktop-portal to open URLs from inside a container
Requires:       xdg-desktop-portal
Recommends:     (xdg-desktop-portal-gtk if gnome-shell)
Recommends:     (xdg-desktop-portal-kde if kwin)

# Prevent log spam when thse are not pulled in as dependencies of full desktops
Recommends:     dbus-x11
Recommends:     xdg-user-dirs

# Allow using Steam Runtime Launch Options
Recommends:     gobject-introspection

# Automatic loading of the ntsync module
Recommends:     ntsync-autoload
# -rm is usually better for Steam
Recommends:     udev-joystick-blacklist-rm
Requires:       (udev-joystick-blacklist-rm or udev-joystick-blacklist)

# Workaround for GNOME issues with libei
Recommends:     (extest-%{name} if gnome-shell)

%description
Steam is a software distribution service with an online store, automated
installation, automatic updates, achievements, SteamCloud synchronized savegame
and screenshot functionality, and many social features.

This package contains the installer for the Steam software distribution service.

%package arch-transition
Summary: Transition package for migrating Steam from i686 to x86_64
Requires: %{name} = %{evr}
Provides: steam = 1.0.0.85-11
Obsoletes: steam < 1.0.0.85-11
BuildArch: noarch

%description arch-transition
This package is used to migrate Steam installations from the
legacy i686 package layout to the x86_64 package layout.

It exists only to handle package replacement and dependency
changes during upgrades, and can be safely removed once the
transition is complete.

%prep
%autosetup -p1 -n %{name}-launcher

cp %{SOURCE5} .

%build
# Nothing to build

%install
%make_install

rm -fr %{buildroot}%{_docdir}/%{name}/ \
    %{buildroot}%{_bindir}/%{name}deps

# Environment files
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -pm 644 %{SOURCE1} %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d

# Raise file descriptor limit
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system.conf.d/
mkdir -p %{buildroot}%{_prefix}/lib/systemd/user.conf.d/
install -m 644 -p %{SOURCE6} %{buildroot}%{_prefix}/lib/systemd/system.conf.d/
install -m 644 -p %{SOURCE6} %{buildroot}%{_prefix}/lib/systemd/user.conf.d/
install -m 775 -p %{SOURCE7} %{buildroot}%{_bindir}/steamrestart

# https://github.com/ValveSoftware/steam-for-linux/issues/9940
desktop-file-edit --remove-key=PrefersNonDefaultGPU %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-edit --remove-key=X-KDE-RunOnDiscreteGpu %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml

%files
%license COPYING steam_subscriber_agreement.txt
%doc debian/changelog README.Fedora
%{_bindir}/%{name}
%{_bindir}/steamrestart
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}_tray_mono.png
%{_prefix}/lib/%{name}/
%{_mandir}/man6/%{name}.*
%{_metainfodir}/%{appid}.metainfo.xml
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.*sh
%dir %{_prefix}/lib/systemd/system.conf.d/
%{_prefix}/lib/systemd/system.conf.d/01-steam.conf
%dir %{_prefix}/lib/systemd/user.conf.d/
%{_prefix}/lib/systemd/user.conf.d/01-steam.conf

%files arch-transition

%changelog
* Fri Jun 5 2026 Gilver E. <roachy@fyralabs.com> - 1.0.0.85-11
- Update for architecture transition
* Sun Sep 01 2024 Simone Caronni <negativo17@gmail.com> - 1.0.0.81-1
- Update to 1.0.0.81.

* Mon Aug 05 2024 Simone Caronni <negativo17@gmail.com> - 1.0.0.79-7
- Fix for Wayland on Fedora 40.

* Sat Aug 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.0.79-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Simone Caronni <negativo17@gmail.com> - 1.0.0.79-5
- Update udev rules.
- Convert udev rule for blocking wrong joystick devices to a systemd hwdb file:
  https://github.com/denilsonsa/udev-joystick-blacklist/issues/58

* Tue May 28 2024 Simone Caronni <negativo17@gmail.com> - 1.0.0.79-4
- Add dependencies when full desktop is not installed.
- Add dependencies for using steam-runtime-launch-options.

* Tue Mar 19 2024 Simone Caronni <negativo17@gmail.com> - 1.0.0.79-3
- Adjust dependencies.

* Sun Feb 18 2024 Simone Caronni <negativo17@gmail.com> - 1.0.0.79-2
- Re-add gnome-shell-extension-appindicator recommendation.

* Sun Feb 18 2024 Simone Caronni <negativo17@gmail.com> - 1.0.0.79-1
- Update to 1.0.0.79.
- Drop gnome-shell-extension-gamemode recommendation (#6853).
- Update udev rules.

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.0.78-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.0.78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 12 2023 Simone Caronni <negativo17@gmail.com> - 1.0.0.78-1
- Update to 1.0.0.78.

* Tue Mar 07 2023 Simone Caronni <negativo17@gmail.com> - 1.0.0.76-1
- Update to 1.0.0.76.
- Separate SPEC file per distribution.
- Trim changelog.

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.0.75-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Fri Jul 22 2022 Simone Caronni <negativo17@gmail.com> - 1.0.0.75-1
- Update to 1.0.0.75.

* Fri Feb 04 2022 Simone Caronni <negativo17@gmail.com> - 1.0.0.74-2
- Add gnome-shell-extension-appindicator if running on Gnome (#6194).
- Require libICE to avoid spamming the console. It's installed by default on a
  Gnome installation but not explicitly required (#6195).

* Fri Dec 10 2021 Simone Caronni <negativo17@gmail.com> - 1.0.0.74-1
- Update to 1.0.0.74.

* Sat Nov 20 2021 Simone Caronni <negativo17@gmail.com> - 1.0.0.73-1
- Update to 1.0.0.73.

* Sat Oct 09 2021 Simone Caronni <negativo17@gmail.com> - 1.0.0.72-1
- Update to 1.0.0.72.

* Fri Aug 27 2021 Simone Caronni <negativo17@gmail.com> - 1.0.0.71-4
- Remove old noruntime provide/obsolete.
- Remove VA-API driver dependencies for RHEL/CentOS 7 and update relevant
  information.
- Remove not really relevant information about controllers from the readme.
- Update steam-devices.

* Wed Aug 25 2021 Nicolas Chauvet <kwizart@gmail.com> - 1.0.0.71-3
- Keep the stream-devices sub-package arched

* Sun Aug 15 2021 Simone Caronni <negativo17@gmail.com> - 1.0.0.71-2
- Steam UDEV subpackage should be noarch.

* Sun Aug 15 2021 Simone Caronni <negativo17@gmail.com> - 1.0.0.71-1
- Update to 1.0.0.71.
- Update README.Fedora with supported controllers.
- Use bundled AppData.

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.0.70-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Simone Caronni <negativo17@gmail.com> - 1.0.0.70-4
- Separate udev rules in separate subpackage to be used also by Valve's Flatpak
  Steam client.
- Use upstream's udev rules as those are newer than what is bundled in the
  installer tarball.

* Tue May 04 2021 Leigh Scott <leigh123linux@gmail.com> - 1.0.0.70-3
- Fix appdata screenshots (rfbz#5984)

* Mon Apr 12 2021 Simone Caronni <negativo17@gmail.com> - 1.0.0.70-2
- Remove new desktop entry specification for Fedora 32 and RHEL/CentOS 7/8.

* Mon Apr 12 2021 Simone Caronni <negativo17@gmail.com> - 1.0.0.70-1
- Update to 1.0.0.70.
- Switch to tarball provided steam-devices udev rules.

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.0.68-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
