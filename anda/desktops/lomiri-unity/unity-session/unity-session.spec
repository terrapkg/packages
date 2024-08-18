%define _ubuntu_rel 7ubuntu1

Name:    unity-session
Summary: Lightdm profile for Unity 7
Version: 46.0
Release: 1%?dist

License:   GPL-2.0
URL:       https://packages.ubuntu.com/jammy/unity-session
Source0:   http://archive.ubuntu.com/ubuntu/pool/universe/g/gnome-session/unity-session_%{version}-%{_ubuntu_rel}_all.deb
Source1:   https://salsa.debian.org/gnome-team/gnome-session/-/raw/ubuntu/master/debian/data/run-systemd-session
BuildArch: noarch

BuildRequires: systemd-rpm-macros
BuildRequires: binutils
BuildRequires: zstd
Requires:      dbus-tools
Requires:      unity-shell
Requires:      unity-settings-daemon
Recommends:    lightdm

%description
Autostart and profile for Unity 7 in Lightdm.

%prep
%autosetup -T -c

%build
ar x %{SOURCE0}
tar --zstd -xvf data.tar.zst ./usr/share/doc/unity-session/copyright
mv -f usr/share/doc/unity-session/copyright ./COPYING
rm -rf usr

%install
tar --zstd -xvf data.tar.zst -C %{buildroot}
rm -rf %{buildroot}/usr/share/doc

mkdir -p %{buildroot}%{_libexecdir}
# Is needed for xsession but is in gnome-bin. Still noarch as it is a shellscript
install -p -m755 %{SOURCE1} %{buildroot}%{_libexecdir}/run-systemd-session

%files
%license COPYING
%config %{_sysconfdir}/xdg/autostart/nemo-unity-autostart.desktop
%{_userunitdir}/gnome-session.service
%{_userunitdir}/unity-session.target
%{_libexecdir}/run-systemd-session
%{_datadir}/gnome-session/sessions/unity.session
%{_datadir}/lightdm/lightdm.conf.d/50-unity.conf
%{_datadir}/nemo/actions/*.nemo_action
%{_datadir}/xsessions/unity.desktop

%changelog
%autochangelog
