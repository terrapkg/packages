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
Requires:		libXi libXinerama libXft libXfixes libXtst libX11
Recommends:		libwayland-client cairo libxkbcommon

%description
warpd is a modal keyboard driven interface for mouse manipulation.

%prep
%forgesetup

%build
%make_build

%install
%make_install

%files
/usr/local/bin/warpd
/usr/local/share/man/man1/warpd*

%changelog
* Thu Jun 15 2023 windowsboy111 <windowsboy111@fyralabs.com> - 1.3.5-1
- Initial package.

