Name:			keyd
Version:		2.4.3
Release:		1%?dist
Summary:		Key remapping daemon for linux
URL:			https://github.com/rvaiya/keyd
License:		MIT
Source0:		%url/archive/refs/tags/v%version.tar.gz
Suggests:		python3 python3-xlib
Requires:		kernel-headers
BuildRequires:	gcc mold make

%description
keyd provides a flexible system wide daemon which remaps keys using kernel
level input primitives (evdev, uinput).

%prep
%autosetup

%build
%make_build

%install
%make_install

%files
%doc README.md
%license LICENSE
/usr/bin/keyd
/usr/bin/keyd-application-mapper
/usr/share/doc/keyd/
/usr/share/keyd
/usr/share/man/man1/keyd-application-mapper.1.gz
/usr/share/man/man1/kyed.1.gz

%changelog
* Tue May 23 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2.4.3-1
- Initial package
