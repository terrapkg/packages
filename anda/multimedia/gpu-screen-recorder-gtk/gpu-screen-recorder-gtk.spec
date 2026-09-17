Name:           gpu-screen-recorder-gtk
Version:        5.8.1
Release:        1%{dist}
Summary:        A shadowplay-like screen recorder for Linux, The fastest screen recorder for Linux
License:        GPL-3.0-or-later
URL:            https://git.dec05eba.com/%{name}/about
Source0:        https://dec05eba.com/snapshot/%{name}.git.%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:  desktop-file-utils
Requires:       gpu-screen-recorder

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Shadowplay like screen recorder for Linux. This package exposes the GTK3 UI.

%prep
%autosetup -C

%conf
%meson

%build
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_appsdir}/com.dec05eba.gpu_screen_recorder.desktop
%{_hicolordir}/*x*/apps/*.*.gpu_screen_recorder.png
%{_hicolordir}/*x*/status/*.*.gpu_screen_recorder.*.png

%changelog
* Thu Sep 17 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
