%global commit a5869aa4561bcae91c9fbaf4af33a2255f197eab
%global commit_date 20251004
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           croskbd
Version:        0~%{commit_date}git.%shortcommit
Release:        1%{?dist}
Summary:        Chromebook Keyboard Daemon

License:        BSD-3-Clause
URL:            https://github.com/WeirdTreeThing/croskbd
Source0:        %{url}/archive/%{commit}/croskbd-%{commit}.tar.gz
Patch0:         makefile-install-path-fix.patch

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  make gcc gcc-c++ systemd-rpm-macros

%description
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%make_build

%install
%make_install PREFIX=%{_prefix} INSTALL="/usr/bin/install -p" install install_systemd

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
* Tue Oct 07 2025 Owen-sz <owen@fyralabs.com>
- Initial commit
