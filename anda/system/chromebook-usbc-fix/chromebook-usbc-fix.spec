%global commit_date 20241005

%global commit cef28b120a39fd459c5864d51c4ad52ecaaf25a0
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global debug_package %{nil}
%define __os_install_post %{nil}

Name:           chromebook-usbc-fix
Version:        %commit_date.%shortcommit
Release:        1%?dist

License:        CCO
Summary:        Fixes usbc on TigerLake and AlderLake Chromebooks
URL:            https://github.com/Ultramarine-Linux/chromebook-usbc-fix
Source:         %url/archive/%{commit}/chromebook-usbc-fix-%{commit}.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

%{?systemd_requires}
BuildRequires:  systemd-rpm-macros

%description
%summary

%prep
%autosetup -n chromebook-usbc-fix-%commit

%install
mkdir -p %buildroot%{_sysconfdir}/chromebook-usbc-fix/
install -Dm755 chromebook-usbc.service %buildroot%{_unitdir}/chromebook-usbc.service

%post
%systemd_post chromebook-usbc.service

%preun
%systemd_preun chromebook-usbc.service

%postun
%systemd_postun_with_restart chromebook-usbc.service

%files
%doc README.md
%license LICENSE
%{_sysconfdir}/chromebook-usbc-fix/*
%{_unitdir}/chromebook-usbc.service

%changelog
* Sat Oct 5 2024 Owen-sz <owen@fyralabs.com>
- Initial package.
