%define debug_package %nil
%global ver v0.2.0-beta.15

Name:           monksynth
Version:        %(echo %ver | sed 's/^v//;s/-/~/g')
Release:        1%?dist
Summary:        A monophonic vocal synthesizer using FOF synthesis, inspired by Delay Lama

License:        MIT
URL:            https://github.com/JonET/monksynth
Packager:       madonuko <mado@fyralabs.com>
Source0:        %url/archive/refs/tags/%ver.tar.gz
BuildRequires:  gcc gcc-c++
BuildRequires:  cmake-rpm-macros cmake
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(atkmm-1.6)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(gtk+-3.0)

BuildSystem:        cmake
%dnl BuildOption(conf):  -DSMTG_PLUGIN_TARGET_PATH=%buildroot/usr/lib/vst3/%name/
BuildOption(build): --target MonkSynth


%description
A monophonic vocal synthesizer that sounds like a monk chanting. Built using formant-wave-function (FOF) synthesis, inspired by the classic Delay Lama VST plugin by AudioNerdz (2002).

%conf -p
cd cpp
mkdir -p %buildroot/usr/lib/vst3/%name
ln %buildroot/usr/lib/vst3/%name/ ~/.vst3
%dnl export SMTG_PLUGIN_TARGET_PATH=%buildroot/usr/lib/vst3/%name/

%build -p
cd cpp
sed -i '1a #include <cstdint>' redhat-linux-build/_deps/vst3sdk-src/vstgui4/vstgui/lib/platform/*.h

%install -p
cd cpp

%files
%license LICENSE
%doc README.md SECURITY.md

%changelog
* Thu Jul 23 2026 madonuko <mado@fyralabs.com> - 0.2.0~beta.15-1
- Initial package
