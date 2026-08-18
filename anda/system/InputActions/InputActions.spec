Name:           inputactions
Version:        0.9.0
Release:        1%{?dist}
Summary:        Linux utility for binding keyboard. mouse, touchpad and touchscreen actions to system actions
License:        GPL-3.0-or-later
URL:            https://wiki.inputactions.org/main
BuildRequires:  cmake-rpm-macros
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  yaml-cpp-devel
BuildRequires:  kwin-devel
BuildRequires:  kf6-kcmutils-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  cmake(CLI11)
Packager:       Owen Zimmerman <owen@fyralabs.com>
BuildSystem:    cmake
# -DINPUTACTIONS_BUILD_HYPRLAND=ON -DINPUTACTIONS_BUILD_STANDALONE=ON
BuildOption(conf):  -DINPUTACTIONS_BUILD_CTL=ON -DINPUTACTIONS_BUILD_KWIN=ON

%description
%{summary}.


%prep
%git_clone https://github.com/taj-ny/InputActions
sed -i '1i #include <unistd.h>' \
    kwin/lib/core/lib/libevdev-cpp/src/libevdev-cpp/Device.cpp \
    kwin/lib/core/src/libinputactions/interfaces/implementations/FileConfigProvider.cpp
sed 's@kwin/wayland/textinput_v1.h@kwin/wayland/textinput_v2.h@g' -i kwin/src/input/KWinVirtualKeyboard.cpp
# HACK: force use of V2 and pray
sed 's@V1@V2@g' -i kwin/src/input/KWinVirtualKeyboard.cpp


%files
%doc README.md
%license LICENSE
%_bindir/inputactions
%_qt6_plugindir/kwin/effects/configs/inputactions_kwin_kcm.so
%_qt6_plugindir/kwin/effects/plugins/kwin_gestures.so


%changelog
* Fri Jul 24 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
