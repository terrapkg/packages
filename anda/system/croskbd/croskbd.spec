Name:           croskbd
Version:        0.1.0
Release:        1%{?dist}
Summary:        Chromebook Keyboard Daemon

License:        BSD-3-Clause
URL:            https://github.com/WeirdTreeThing/croskbd
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  make gcc systemd-rpm-macros

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build
%make_build

%install
%make_install DESTDIR=%{buildroot} PREFIX=%{_prefix} install install_systemd

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
