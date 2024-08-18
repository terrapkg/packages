%global commit b2e69368f96bdf7562dc1a95a0d863c794756842
%global commit_date 20240814
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}
%define __os_install_post %{nil}

Name:           cros-keyboard-map
Version:        %commit_date.%shortcommit
Release:        2%?dist

License:        BSD-3-Clause
Summary:        Utility to generate keyd configurations for use on Chromebooks
URL:            https://github.com/WeirdTreeThing/cros-keyboard-map
Source0:        https://github.com/WeirdTreeThing/cros-keyboard-map/archive/%commit/cros-keyboard-map-%commit.tar.gz

%{?systemd_requires}
BuildRequires:  systemd-rpm-macros
Requires:       keyd python3 python3-libfdt

%description
Set of tools designed to help develop and debug software and firmware on Intel platforms with AudioDSP onboard.

Related to alsa-utils which is also set of utilities but targets AdvancedLinuxSoundArchitecture (ALSA) audience in more general fashion.

%prep
%autosetup -n cros-keyboard-map-%commit

%install
mkdir -p %buildroot/etc/cros-keyboard-map/configs
install -Dm755 cros-keyboard-map.py %buildroot/etc/cros-keyboard-map/cros-keyboard-map.py
cp configs/* %buildroot/etc/cros-keyboard-map/configs

mkdir -p %buildroot/usr/bin
tee %buildroot/usr/bin/um-generate-cros-keymap <<EOF
if (grep -E "^(Nocturne|Atlas|Eve)$" /sys/class/dmi/id/product_name &> /dev/null)
then
	cp /etc/cros-keyboard-map/configs/cros-pixel.conf /etc/cros-keyboard-map/current.config
elif (grep -E "^(Sarien|Arcada)$" /sys/class/dmi/id/product_name &> /dev/null)
then
	cp /etc/cros-keyboard-map/configs/cros-sarien.conf /etc/cros-keyboard-map/current.config
else
	python3 /etc/cros-keyboard-map/cros-keyboard-map.py --file /etc/cros-keyboard-map/current.config
fi

mkdir -p /etc/keyd
if [[ -f /etc/keyd/default.conf ]]; then
	rm /etc/keyd/default.conf
fi
ln -s /etc/cros-keyboard-map/current.config /etc/keyd/default.conf
EOF

mkdir -p %buildroot/etc/systemd/system
tee %buildroot/etc/systemd/system/cros-keyboard-map.service <<EOF
[Unit]
Description=Generate chromebook keyboard layout
Before=keyd.service
After=tmp.mount

[Service]
Type=oneshot
ExecStart=/bin/bash /usr/bin/um-generate-cros-keymap
ExecStartPost=+/usr/bin/systemctl restart keyd.service

[Install]
WantedBy=multi-user.target
EOF
mkdir -p %buildroot/etc/systemd/system-preset
tee %buildroot/etc/systemd/system-preset/00-cros-keyboard-map.preset <<EOF
enable cros-keyboard-map.service
enable keyd.service
EOF
chmod +x %buildroot/usr/bin/um-generate-cros-keymap

%post
%systemd_post cros-keyboard-map.service
%systemd_post keyd.service

%preun
%systemd_preun cros-keyboard-map.service
%systemd_preun keyd.service

%postun
%systemd_postun_with_restart cros-keyboard-map.service
%systemd_postun_with_restart keyd.service

%files
%doc README.md
%license LICENSE
/etc/cros-keyboard-map/*
/etc/systemd/system/cros-keyboard-map.service
/etc/systemd/system-preset/00-cros-keyboard-map.preset
/usr/bin/um-generate-cros-keymap

%changelog
* Sat May 4 2024 Owen-sz <owen@fyralabs.com>
- Initial package.
