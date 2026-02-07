%global appid org.praat.praat
%global name_pretty Praat
%global appstream_component desktop-application
%global org "org.praat"

Name:             praat
Version:          6.4.59
Release:          2%{?dist}
URL:              https://www.praat.org
Source0:          https://github.com/praat/praat.github.io/archive/refs/tags/v%{version}.tar.gz
Source1:          %appid.metainfo.xml
License:          GPL-3.0-or-later AND LGPL-2.1-or-later AND MIT AND GPL-2.0-or-later AND BSD-3-Clause AND Unicode-3.0 AND BSL-1.0

Requires:         gtk3 pulseaudio-libs alsa-lib pipewire-jack-audio-connection-kit
BuildRequires:    gcc g++ gtk3-devel pulseaudio-libs-devel alsa-lib-devel pipewire-jack-audio-connection-kit-devel
# for lscpu check below
BuildRequires:    util-linux
# to install desktop file
BuildRequires:    desktop-file-utils
# to generate the icon files
BuildRequires:    libicns-utils
# to generate the appstream metadata
BuildRequires:    terra-appstream-helper

Summary:          Praat: Doing Phonetics By Computer

Packager:         june-fish <june@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n praat.github.io-%{version}

%build
# .LE makefile hardcodes little endian
if [[ "$(lscpu | grep Endian)" == *"Little Endian"* ]]
then
  cp makefiles/makefile.defs.linux.pulse-gcc.LE ./makefile.defs
elif [[ "%{lscpu | grep Endian}" == *"Big Endian"* ]]
then
  cp makefiles/makefile.defs.linux.pulse-gcc.BE ./makefile.defs
fi

%make_build

%install
install -pDm755 praat %{buildroot}%{_bindir}/praat
%__desktop_file_install main/praat.desktop

# https://build.opensuse.org/projects/openSUSE:Factory/packages/praat/files/praat.spec?expand=1
icns2png -x -d32 main/Praat.icns
for s in 16 32 48 128; do
   if [ -f Praat_${s}x${s}x32.png ]; then
      install -Dm0644 Praat_${s}x${s}x32.png %{buildroot}%{_hicolordir}/${s}x${s}/apps/%{name}.png
   fi
done

%terra_appstream -o %{SOURCE1}

%files
%license docs/LICENSE.txt
%license external/*/LICENSE*
%license external/*/COPYING*
%doc README.md
%{_bindir}/praat
%{_datadir}/applications/praat.desktop
%{_hicolordir}/16x16/apps/%{name}.png
%{_hicolordir}/32x32/apps/%{name}.png
%{_hicolordir}/48x48/apps/%{name}.png
%{_hicolordir}/128x128/apps/%{name}.png
%{_metainfodir}/%appid.metainfo.xml

%changelog
* Fri Feb 06 2026 june-fish <git@june.fish> - 6.4.59
- Initial Package
