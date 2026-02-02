%define debug_package %nil

Name:           powerbuttond
Version:        4.1
Release:        1%?dist
Summary:        Steam Deck power button daemon

License:        BSD
URL:            https://gitlab.steamos.cloud/holo/powerbuttond
Source:		    %{url}/-/archive/v%{version}/powerbuttond-v%{version}.tar.gz
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  make gcc

Provides:       steam-powerbuttond
Obsoletes:      steam-powerbuttond < 3.3
Provides:       steamos-powerbuttond
Obsoletes:      steamos-powerbuttond < 3.3
Provides:       powerbuttond = %evr

%description
Steam Deck power button daemon.

%prep
%autosetup -n powerbuttond-v%{version} -p1

%build
%make_build CFLAGS="$CFLAGS -I%_includedir/libevdev-1.0" LDFLAGS="$LDFLAGS"

%install
%make_install
sed -i 's/Requisite=gamescope-session.service//g' %{buildroot}%{_userunitdir}/steamos-powerbuttond.service
rm -r %{buildroot}/%{_userunitdir}/gamescope-session.service.wants
rm %buildroot%_datadir/licenses/steamos-%name/LICENSE

%post
udevadm control --reload-rules
udevadm trigger
%systemd_user_post steamos-%{name}.service

%preun
%systemd_user_preun steamos-%{name}.service

%postun
%systemd_user_postun steamos-%{name}.service

%files
%license LICENSE
%dir %{_prefix}/lib/hwsupport
%{_prefix}/lib/hwsupport/steamos-%{name}
%{_userunitdir}/steamos-%{name}.service
%{_prefix}/lib/udev/rules.d/70-steamos-power-button.rules
%dir %{_prefix}/lib/udev/hwdb.d
%{_prefix}/lib/udev/hwdb.d/70-steamos-power-button.hwdb

%changelog
* Fri Jan 30 2026 madonuko <mado@fyralabs.com> - 4.0-1
- Ported from https://copr-dist-git.fedorainfracloud.org/packages/gloriouseggroll/nobara-43/steamos-powerbuttond.git/tree/steamos-powerbuttond.spec?h=f43&id=071012e4c4b4a1eda8606753615c9f4ceef33458
