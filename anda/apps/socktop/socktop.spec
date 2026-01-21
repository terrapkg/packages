%global ver v1.55.0-test2
%global download_ver %(echo %{ver} | sed 's/v//g')
%global sanitized_ver %(echo %{ver} | sed 's/-//g')

Name:           socktop
Version:        %sanitized_ver
Release:        1%?dist
Summary:        socktop is a remote system monitor with a rich TUI interface
URL:            https://github.com/jasonwitty/socktop
Source0:        %{url}/archive/refs/tags/%{ver}.tar.gz
License:        MIT
BuildRequires:  rust libdrm-devel systemd-rpm-macros cargo-rpm-macros
Requires:       libdrm
Packager:       lux8149 <julianbashirisasimp@gmail.com>

%description
socktop is a remote system monitor with a rich TUI interface, inspired by `top` and `btop`,
that communicates with a lightweight remote agent over WebSockets.

%prep
%autosetup -n %{name}-%{download_ver}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm 755 target/rpm/socktop %{buildroot}%{_bindir}/socktop
install -Dm 755 target/rpm/socktop_agent %{buildroot}%{_bindir}/socktop_agent
install -Dm 644 target/rpm/libsocktop_connector.so %{buildroot}%{_libdir}/libsocktop_connector.so
install -Dm 644 docs/socktop-agent.service %{buildroot}%{_unitdir}/socktop-agent.service
%{cargo_license_online} > LICENSE.dependencies

%post
%systemd_post socktop-agent.service

%preun
%systemd_preun socktop-agent.service

%postun
%systemd_postun_with_restart socktop-agent.service

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/socktop
%{_bindir}/socktop_agent
%{_libdir}/libsocktop_connector.so
%{_unitdir}/socktop-agent.service

%changelog
* Sun Jan 04 2026 lux8149 <julianbashirisasimp@gmail.com>
- Initial Package
