Name:			uxplay
Version:		1.68.3
Release:		1%?dist
Summary:		AirPlay Unix mirroring server
License:		GPL-3.0
URL:			https://github.com/FDH2/UxPlay
Source0:		%url/archive/refs/tags/%version.tar.gz
Requires:		openssl libplist avahi gstreamer1-plugin-libav gstreamer1-plugins-bad-free gstreamer1-plugins-good gstreamer1-plugins-base
Recommends:		gstreamer1-vaapi
BuildRequires:	cmake desktop-file-utils systemd-rpm-macros gcc gcc-c++ openssl-devel avahi-compat-libdns_sd-devel
BuildRequires:	pkgconfig(gstreamer-1.0) pkgconfig(gstreamer-sdp-1.0) pkgconfig(gstreamer-video-1.0) pkgconfig(gstreamer-app-1.0) pkgconfig(libplist-2.0)

%description
%summary.

%prep
%autosetup -n UxPlay-%version
cat <<EOF > %name.desktop
[Desktop Entry]
Type=Application
Version=1.0
Name=UxPlay
GenericName=AirPlay server
Exec=%_bindir/uxplay
Icon=computer-apple-ipad-symbolic
Terminal=true
Categories=AudioVideo;
Comment=%summary
EOF

%build
%cmake . -DNO_MARCH_NATIVE=ON
%cmake_build --config Release


%install
mkdir -p %buildroot%_bindir %buildroot%_datadir/applications %buildroot%_mandir/man1
install -Dm755 redhat-linux-build/%name %buildroot%_bindir/
install -Dm644 %name.desktop %buildroot%_datadir/applications/

mv %name.1 %buildroot%_mandir/man1/%name.1

%post
%systemd_post avahi-daemon.service

%preun
%systemd_preun avahi-daemon.service

%postun
%systemd_postun_with_restart avahi-daemon.service

%check
desktop-file-validate %name.desktop

%files
%license LICENSE
%doc README.*
%_bindir/%name
%_datadir/applications/%name.desktop
%_mandir/man1/*

%changelog
%autochangelog
