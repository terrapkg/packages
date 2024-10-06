%global commit_date 20241005

%global commit c357dc068583795f0500cf77926f75da4597d59b
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

%{?systemd_requires}
BuildRequires:  systemd-rpm-macros

%description
%summary

%prep
%autosetup -n chromebook-usbc-fix-%commit

%install
mkdir -p %buildroot%{_sysconfdir}/chromebook-usbc-fix/
install -Dm755 chromebook-usbc.service %buildroot%{_sysconfdir}/chromebook-usbc-fix/chromebook-usbc.service

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
%{_bindir}/chromebook-usbc-fix

%changelog
* Sat Oct 5 2024 Owen-sz <owen@fyralabs.com>
- Initial package.
