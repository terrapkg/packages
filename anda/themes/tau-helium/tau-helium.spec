%global ver 1.8.12-11

Summary:        tauOS GTK/GNOME Shell Themes
Name:           tau-helium
Version:        %(echo %ver | sed 's/-/./g')
Release:        1%{?dist}
License:        GPL-3.0
URL:            https://github.com/tau-OS/tau-helium
Source0:        https://github.com/tau-OS/tau-helium/archive/refs/tags/%{ver}.tar.gz
BuildArch:      noarch
BuildRequires:  sass
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  fdupes

%description
A set of GTK/GNOME Shell Themes for tauOS

%prep
%autosetup -n tau-helium-%{ver}

%build
%meson
%meson_build

%install
# Install licenses
mkdir -p licenses
%meson_install
%fdupes %buildroot%_datadir/themes/

%files
%license LICENSE
%doc README.md
%{_datadir}/themes/Helium/*
%{_datadir}/themes/Helium-dark/*

%changelog
* Fri Dec 02 2022 root - 1.1.25-1
- new version

* Fri Dec 02 2022 root - 1.1.24-1
- new version

* Fri Dec 02 2022 root - 1.1.23-1
- new version

* Fri Nov 25 2022 root - 1.1.22-1
- new version

* Fri Nov 18 2022 Lleyton Gray <lleyton@fyralabs.com> - 1.1.21-1
- new version

* Fri Nov 18 2022 Lleyton Gray <lleyton@fyralabs.com> - 1.1.20-1
- new version

* Thu Nov 17 2022 root - 1.1.19-1
- new version

* Sun Nov 13 2022 root - 1.1.18-1
- new version

* Fri Nov 11 2022 Lleyton Gray <lleyton@fyralabs.com> - 1.1.17-1
- new version

* Fri Nov 11 2022 Lleyton Gray <lleyton@fyralabs.com> - 1.1.17-1
- new version

* Wed Jun 22 2022 Lains <lainsce@airmail.cc> - 1.1-52
- Theme freeze exception for 1.1.
- Slight differences for themes.

* Wed Jun 22 2022 Lains <lainsce@airmail.cc> - 1.1-49
- Theme freeze exception for 1.1.
- Merge of GNOME Shell themes.

* Mon May 30 2022 Lains <lainsce@airmail.cc> - 1.1-42
- Theme freeze exception for 1.1.
- An adventure in coloring happened.

* Mon May 30 2022 Lains <lainsce@airmail.cc> - 1.1-32
- Theme freeze exception for 1.1.
- Add missing tauOS HIG css classes helpers.

* Sun May 29 2022 Lains <lainsce@airmail.cc> - 1.1-30
- Theme freeze exception for 1.1.
- Remove GTK3 theme creep and also the tauos specific stylings.

* Fri May 27 2022 Lains <lainsce@airmail.cc> - 1.1-28
- Theme freeze exception for 1.1.
- Fixed borders on GTK3.

* Thu May 26 2022 Lains <lainsce@airmail.cc> - 1.1-27
- Actual Theme freeze for 1.1.
- Added missing tau-specific widget theming.

* Wed May 25 2022 Lains <lainsce@airmail.cc> - 1.1-26
- Theme freeze for 1.1.

* Wed May 25 2022 Lains <lainsce@airmail.cc> - 1.1-25
- Make switches not as wacky in size.

* Tue May 24 2022 Lains <lainsce@airmail.cc> - 1.1-23
- Accessibility-driven design on entries and switches.

* Tue May 24 2022 Lains <lainsce@airmail.cc> - 1.1-22
- Missed some stuff that was breaking the theme.

* Mon May 23 2022 Lains <lainsce@airmail.cc> - 1.1-21
- Reintroduce some stuff otherwise theme breaks on GTK3.

* Sun May 22 2022 Lains <lainsce@airmail.cc> - 1.1-20
- Remove platform-specific css classes and things
- Focus only on tau HIG and basic GTK theming.

* Sat May 21 2022 Lains <lainsce@airmail.cc> - 1.1-19
- Fix typography in general, again.

* Fri May 20 2022 Lains <lainsce@airmail.cc> - 1.1-18
- Fix typography in general.

* Fri May 20 2022 Lains <lainsce@airmail.cc> - 1.1-17
- Fix bg color in Helium-dark GNOME Shell.

* Thu May 19 2022 Lains <lainsce@airmail.cc> - 1.1-16
- Fix more oops.

* Thu May 19 2022 Lains <lainsce@airmail.cc> - 1.1-15
- Fix some oops.

* Wed May 18 2022 Lains <lainsce@airmail.cc> - 1.1-14
- Bring in the tauOS HIG widgetry and stuff.

* Tue May 17 2022 Lains <lainsce@airmail.cc> - 1.1-13
- Make the dark theme content block color not too stark.

* Mon May 16 2022 Lains <lainsce@airmail.cc> - 1.1-12
- Finalize and fix inconsistencies in the Helium GNOME Shell themes

* Sun May 15 2022 Lains <lainsce@airmail.cc> - 1.1-11
- Fix Helium Light GNOME Shell theme

* Fri May 13 2022 Lains <lainsce@airmail.cc> - 1.1-10
- Refine some GTK stuff

* Tue May 10 2022 Lains <lainsce@airmail.cc> - 1.1-9
- Refine some GTK stuff

* Tue May 10 2022 Lains <lainsce@airmail.cc> - 1.1-8
- Finish GTK4 theme

* Mon May 9 2022 Lains <lainsce@airmail.cc> - 1.1-7
- Start GTK4 theme

* Mon May 9 2022 Lains <lainsce@airmail.cc> - 1.1-6
- More improvements in styling

* Mon May 9 2022 Lains <lainsce@airmail.cc> - 1.1-5
- Improvements in styling to match Shell with GTK theme

* Mon May 9 2022 Lains <lainsce@airmail.cc> - 1.1-4
- GNOME shell theme wasn't being installed

* Sun May 8 2022 Lains <lainsce@airmail.cc> - 1.1-3
- Perhaps this is needed

* Sun May 8 2022 Lains <lainsce@airmail.cc> - 1.1-2
- Let's roll our own gtk theme

* Wed May 4 2022 Lains <lainsce@airmail.cc> - 1.1-1.7.2
- Get Helium GNOME Shell theme here

* Tue May 3 2022 Lains <lainsce@airmail.cc> - 1.1-1.7.1
- Get Helium GNOME Shell theme here

* Thu Apr 21 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1.7
- Update adw-gtk3 to v1.7
- Update Build System

* Thu Apr 7 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-2
- Add accent colours

* Thu Apr 7 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1
- Initial Release
