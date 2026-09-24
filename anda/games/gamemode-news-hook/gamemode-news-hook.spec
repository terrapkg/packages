%global __brp_python_bytecompile %{nil}

Name:           gamemode-news-hook
Version:        1.4.0
Release:        1%{?dist}
Summary:        Replace Steam Game Mode update cards with custom announcements

License:        MIT
URL:            https://github.com/honjow/gamemode-news-hook
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>

BuildArch:      noarch
BuildRequires:  systemd-rpm-macros

Requires:       python3
Recommends:     python3-systemd

%description
%{summary}.

Injects JavaScript into Steam's CEF pages via the remote debugging protocol to
replace Valve event cards with custom announcements from a repository.

%prep
%autosetup -n %{name}-%{version}

%install
install -Dm755 src/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 src/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf
install -dm755 %{buildroot}%{_prefix}/lib/%{name}
install -m644 -t %{buildroot}%{_prefix}/lib/%{name} src/lib/*.py
install -dm755 %{buildroot}%{_prefix}/lib/%{name}/js
install -m644 -t %{buildroot}%{_prefix}/lib/%{name}/js src/lib/js/*.js
install -Dm644 src/systemd/%{name}.service %{buildroot}%{_userunitdir}/%{name}.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun %{name}.service

%files
%license LICENSE
%doc docs/README.md docs/steam-event-api.md
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%dir %{_prefix}/lib/%{name}
%{_prefix}/lib/%{name}/*.py
%dir %{_prefix}/lib/%{name}/js
%{_prefix}/lib/%{name}/js/*.js
%{_userunitdir}/%{name}.service

%changelog
* Mon Jul 20 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 1.4.0-1
- Initial package
