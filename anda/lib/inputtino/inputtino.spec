%global commit 504f0abc7da8ebc351f8300fb2ed98db5438ee48
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250816

Name:           inputtino
Version:        0^%{commitdate}.%{shortcommit}
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/games-on-whales/%{name}
Source:         %{url}/archive/%{commit}.tar.gz
Patch0:         fix-pkgconfig-install-location.patch
Summary:        A virtual input library: supports mouse, keyboard, joypad, trackpad and more 
Packager:       metcya <metcya@gmail.com>

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(sdl2)

%description
An easy to use virtual input library for Linux built on top of uinput, evdev
and uhid.

%package devel
%pkg_devel_files

%prep
%autosetup -n %{name}-%{commit} -p1

%build
%cmake -DBUILD_TESTING=OFF \
       -DLIBINPUTTINO_INSTALL=ON
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
# huh?
%{_libdir}/liblib%{name}.so.*

%changelog
* Mon Jan 05 2026 metcya <metcya@gmail.com> - 0^20250816.504f0ab
- Initial package 

