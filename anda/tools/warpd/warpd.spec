Name:			warpd
Version:		1.3.5

%global forgeurl https://github.com/rvaiya/warpd

%forgemeta

Release:		1%?dist
Summary:		Modal keyboard-driven virtual pointer
License:		MIT
URL:			%forgeurl
Source0:		%forgesource

BuildRequires:	make gcc libXi-devel libXinerama-devel libXft-devel libXfixes-devel libXtst-devel libX11-devel cairo-devel libxkbcommon-devel wayland-devel
Recommends:		libwayland-client cairo libxkbcommon

%description
warpd is a modal keyboard driven interface for mouse manipulation.

%prep
%forgesetup

%build
%make_build

%install
mkdir -p %buildroot%_mandir/man1/
%make_install
install -Dm755 %buildroot/usr/local/bin/warpd %buildroot%_bindir/warpd
install -Dm644 %buildroot/usr/local/share/man/man1/warpd* %buildroot%_mandir/man1/
rm %buildroot/usr/local/bin/warpd %buildroot/usr/local/share/man/man1/warpd*

%files
%_bindir/warpd
%_mandir/man1/warpd*

%changelog
* Thu Jun 15 2023 windowsboy111 <windowsboy111@fyralabs.com> - 1.3.5-1
- Initial package.

