%global pypi_name proton-vpn-api-core
%global _desc A facade to the other Proton VPN components, exposing a uniform API to the available Proton VPN services.
%global protun_commit 12e7755a112f59b7b843da79290b3de25febf653
%global proton_registry sparse+https://rust-registry.proton.me/index/

%global __requires_exclude ^python3\\.14dist\\(proton-vpn-local-agent\\)$

# A lot of this spec has been based on the Arch Linux build - https://gitlab.archlinux.org/archlinux/packaging/packages/python-proton-vpn-api-core/-/blob/main/PKGBUILD?ref_type=heads

Name:			python-%{pypi_name}
Version:		5.8.11
Release:		1%{?dist}
Summary:		A facade to the other Proton VPN components
License:		GPL-3.0-Only
URL:			https://github.com/ProtonVPN/python-proton-vpn-api-core
Source0:		%{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/ProtonVPN/protun/archive/%{protun_commit}.tar.gz
Patch0:         fix-protun-dbus-startup-race.patch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  cargo-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libnftnl)

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       %{pypi_name}
Requires:       NetworkManager-openvpn
Obsoletes:      python3-proton-vpn-local-agent < 1.6.3-3
Provides:       python3-proton-vpn-local-agent
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%git_clone %{url} v%{version}
cd python-proton-vpn-api-core
%autopatch -p1
sed -i '/^SystemdService=/d' resources/nm-protun.name

rm -rf dependencies/protun
mkdir -p dependencies/protun
tar -xf %{S:1} -C dependencies/protun --strip-components=1
export CARGO_REGISTRIES_PROTON_INDEX='%{proton_registry}'
%cargo_prep_online
cat >> %{_cargo_home}/config.toml << EOF

[registries.proton]
index = "%{proton_registry}"
EOF

%build
export CARGO_REGISTRIES_PROTON_PUBLIC_INDEX="sparse+https://rust-registry.proton.me/index/"
%cargo_build -- \
--bin nm-protun-service \
--bin proton-vpn-kill-switch-service \
--lib \
--features 'protun,python,core,local_agent,kill_switch,telemetry'

install -Dpm0755 target/rpm/libproton_vpn_platform.so proton/vpn/platform.abi3.so

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files proton

mkdir -p %{buildroot}%{_prefix}/lib/NetworkManager/VPN

install -Dm755 target/rpm/nm-protun-service                   %{buildroot}%{_libexecdir}/nm-protun-service
install -Dm644 resources/nm-protun-service.conf               %{buildroot}%{_datadir}/dbus-1/system.d/nm-protun-service.conf
sed -e 's|^program=.*|program=%{_libexecdir}/nm-protun-service|' \
    resources/nm-protun.name > %{buildroot}%{_prefix}/lib/NetworkManager/VPN/nm-protun.name

install -Dm755 target/rpm/proton-vpn-kill-switch-service      %{buildroot}%{_libexecdir}/proton-vpn-kill-switch-service
install -Dm644 resources/proton-vpn-kill-switch.conf          %{buildroot}%{_datadir}/dbus-1/system.d/me.proton.vpn.kill_switch.conf
install -Dm644 resources/proton-vpn-kill-switch.dbus-service  %{buildroot}%{_datadir}/dbus-1/system-services/me.proton.vpn.kill_switch.service
install -Dm644 resources/proton-vpn-kill-switch-boot.service  %{buildroot}%{_unitdir}/proton-vpn-kill-switch-boot.service

%preun -n python3-%{pypi_name}
if [ $1 -eq 0 ]; then
    if ! ks_error=$(busctl call \
            me.proton.vpn.kill_switch /me/proton/vpn/kill_switch \
            me.proton.vpn.kill_switch Disable 2>&1); then
        echo "warning: could not disable the Proton VPN kill switch: ${ks_error}" >&2
    fi
    systemctl disable proton-vpn-kill-switch-boot.service >/dev/null 2>&1 || :
fi

%postun -n python3-%{pypi_name}
pkill -f "^%{_libexecdir}/proton-vpn-kill-switch-service" || :

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CODEOWNERS docs/*
%license LICENSE
%defattr(-,root,root)
%{_libexecdir}/nm-protun-service
%{_libexecdir}/proton-vpn-kill-switch-service
%{_datadir}/dbus-1/system.d/nm-protun-service.conf
%{_datadir}/dbus-1/system.d/me.proton.vpn.kill_switch.conf
%{_datadir}/dbus-1/system-services/me.proton.vpn.kill_switch.service
%{_prefix}/lib/NetworkManager/VPN/nm-protun.name
%{_unitdir}/proton-vpn-kill-switch-boot.service

%changelog
* Sun Oct 18 2026 Owen Zimmerman <owen@fyralabs.com>
- Update for 5.8.7

* Fri Aug 28 2026 Owen Zimmerman <owen@fyralabs.com>
- Build rust utilities

* Sat Jan 17 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
