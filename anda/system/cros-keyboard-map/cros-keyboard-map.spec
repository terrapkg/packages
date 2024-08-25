%global commit_date 20240824

%global tree_commit b2e69368f96bdf7562dc1a95a0d863c794756842
%global tree_shortcommit %(c=%{tree_commit}; echo ${c:0:7})

%global um_commit 46892acafb2fff3f3ace425d4694382c92645feb
%global um_shortcommit %(c=%{um_commit}; echo ${c:0:7})

%global debug_package %{nil}
%define __os_install_post %{nil}

Name:           cros-keyboard-map
Version:        %commit_date.%tree_shortcommit.%um_shortcommit
Release:        1%?dist

License:        BSD-3-Clause and GPLv3
Summary:        Utility to generate keyd configurations for use on Chromebooks
URL:            https://github.com/Ultramarine-Linux/cros-keyboard-map
Source0:        https://github.com/WeirdTreeThing/cros-keyboard-map/archive/%{tree_commit}/cros-keyboard-map-%{tree_commit}.tar.gz
Source1:        https://github.com/Ultramarine-Linux/cros-keyboard-map/archive/%{um_commit}/cros-keyboard-map-%{um_commit}.tar.gz

%{?systemd_requires}
BuildRequires:  systemd-rpm-macros
Requires:       keyd python3 python3-libfdt

%description
Bash script and systemd service to apply WeirdTreeThing's Chromebook keyboard maps.

%prep
%autosetup -n cros-keyboard-map-%tree_commit
tar --strip-components=1 -zxvf %{SOURCE1}

%install
mkdir -p %buildroot%{_sysconfdir}/cros-keyboard-map/configs
install -Dm755 cros-keyboard-map.py %buildroot%{_sysconfdir}/cros-keyboard-map/cros-keyboard-map.py
cp configs/* %buildroot%{_sysconfdir}/cros-keyboard-map/configs

mkdir -p %buildroot%{_bindir}
install -Dm755 um-generate-cros-keymap %{buildroot}%{_bindir}/um-generate-cros-keymap
mkdir -p %buildroot%{_unitdir}
install -Dm644 cros-keyboard-map.service %{buildroot}%{_unitdir}/cros-keyboard-map.service
chmod +x %buildroot%{_bindir}/um-generate-cros-keymap

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
%{_sysconfdir}/cros-keyboard-map/*
%{_unitdir}/cros-keyboard-map.service
%{_bindir}/um-generate-cros-keymap

%changelog
* Sat Aug 24 2024 junefish <june@fyralabs.com>
- Split off into seperate git repo.
* Sat May 4 2024 Owen-sz <owen@fyralabs.com>
- Initial package.
