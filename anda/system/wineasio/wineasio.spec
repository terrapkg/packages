Name:           wineasio

%global tag v1.2.0
# macro to remove the v from version
%global version_tag %(echo %{tag} | sed 's/^v//')
%global forgeurl https://github.com/wineasio/%{name}


# While this package should have debug headers, we have build issues with them

%define debug_package %{nil}

Version:        %{version_tag}
Release:        %autorelease
Summary:        Wine ASIO driver

License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            %{forgeurl}
Source:         %{forgeurl}/releases/download/%{tag}/wineasio-%{version_tag}.tar.gz

BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  pkgconfig(jack)
BuildRequires:  wine-devel
ExclusiveArch:  x86_64

%description
WineASIO provides an ASIO to JACK driver for WINE.
ASIO is the most common Windows low-latency driver, so is commonly used in audio workstation programs.

You can, for example, use with FLStudio under GNU/Linux systems (together with JACK).

%prep
%autosetup

%build

# remove all cflags because it builds just fine without them, causes issues with asm when the default ones are
# present though

export CFLAGS=""

make clean
make 64


%install
install -Dm755 build64/wineasio64.dll.so %{buildroot}%{_libdir}/wine/%{_arch}-unix/wineasio64.dll.so
install -Dm755 build64/wineasio64.dll %{buildroot}%{_libdir}/wine/%{_arch}-windows/wineasio64.dll
install -Dm755 wineasio-register %{buildroot}%{_bindir}/wineasio-register

pushd gui

%make_install

popd

%files
%license COPYING.LIB COPYING.GUI
%doc README.md

%{_libdir}/wine/%{_arch}-unix/wineasio64.dll.so
%{_libdir}/wine/%{_arch}-windows/wineasio64.dll
%{_bindir}/wineasio-register
%{_bindir}/wineasio-settings
%{_datadir}/wineasio/


%changelog
* Thu Apr 11 2024 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Release
