%global pypi_name proton-vpn-api-core
%global _desc A facade to the other Proton VPN components, exposing a uniform API to the available Proton VPN services.
# Needs to be pinned to this commit for now.
%global protun_commit 5f5f4c9f7bb6c96a10a5c42747dccdf7ee656039

%global __requires_exclude ^python3\\.14dist\\(proton-vpn-local-agent\\)$

# A lot of this spec has been based on the Arch Linux build - https://gitlab.archlinux.org/archlinux/packaging/packages/python-proton-vpn-api-core/-/blob/main/PKGBUILD?ref_type=heads

Name:			python-%{pypi_name}
Version:		5.5.15
Release:		2%{?dist}
Summary:		A facade to the other Proton VPN components
License:		GPL-3.0-Only
URL:			https://github.com/ProtonVPN/python-proton-vpn-api-core
Source0:		%{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/ProtonVPN/protun/archive/%{protun_commit}.tar.gz
Patch0:         fix-protun-protocol.patch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  cargo-rpm-macros

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       %{pypi_name}
Requires:       python3-proton-vpn-local-agent
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%git_clone %{url} v%{version}
cd python-proton-vpn-api-core
%autopatch -p1
# The submodule 404s so we need to fetch it manually.
rm -rf dependencies/protun
mkdir -p dependencies/protun

tar -xf %{S:1} -C dependencies/protun --strip-components=1

sed -i 's|sparse+https://rust.gitlab-pages.protontech.ch/shared/registry/index/|sparse+https://rust-registry.proton.me/index/|g' Cargo.lock
sed -i \
    -e 's|e96081b45cc7a830262dcbac2a79b58bc312aab0672c4c1c51fd8c28b03ca987|d6cbef9a3ddc5f97501607f1a689c459a1894069745b4cede7c519b71bb64434|' \
    -e 's|8e4b9d4c0cb1aa4096f9f7bdabc120323c7b6d110efba90d258c0150a65a7e12|4c2654d02228a2e4ccb4edf1883cb2838d9640e19012f75e0cad7afcb468f2d5|' \
    -e 's|90c6da77725af99bfa1dd9bed7b7c3481c087cd89a8a0a1d7e45e15ed3a3377d|0a7b06dd92ace9b23a49beeb33511ef6bcc04355e314f1f8ee8aadbe8c613b98|' \
    -e 's|161e33ea4b9b564a0910b8948ef55bf8183504f0c5911e2354cfabcebae25910|57143360edc0690cec81daa6d4f20ee17fd741670b270c4deee0b5247ebb036f|' \
    -e 's|fcd725b3baebb44befaf9a37e158e7cbfb044e32324469ae765c8e052755f323|7707bef2e4e2d3fb1e9f2d1abf67b2ae7235be299e53bc45771f4de3c40e976b|' \
    -e 's|23e1d1a18fc6a68c4622b25e7a45fd8e50d41d2607e71a346b986691a3b1507b|64499d4117fcba0ad93e6444cd75dbc5985752d80b645762a999be305c57ceeb|' \
    -e '/name = "proton-pfff-module"/,/^$/ s/version = "0.6.4"/version = "0.6.5"/' \
    -e '/name = "proton-vpn-netstack"/,/^$/ s/version = "0.6.0"/version = "0.6.3"/' \
    Cargo.lock

%cargo_prep_online

%build
export CARGO_REGISTRIES_PROTON_PUBLIC_INDEX="sparse+https://rust-registry.proton.me/index/"
export CARGO_REGISTRIES_PROTON_INDEX="sparse+https://rust-registry.proton.me/index/"
%pyproject_wheel
%cargo_build -- --locked \
--bin nm-protun-service \
--bin nm-protun-auth-dialog \
--lib \
--features 'protun,nm_protun_auth_dialog,python,core,local_agent'

%install
%pyproject_install
%pyproject_save_files proton

mkdir -p %{buildroot}%{_prefix}/lib/NetworkManager/VPN

install -Dm644 target/rpm/libproton_vpn_platform.so %{buildroot}%{python3_sitelib}/proton/vpn/platform.abi3.so
install -Dm755 target/rpm/nm-protun-service         %{buildroot}%{_libexecdir}/nm-protun-service
install -Dm755 target/rpm/nm-protun-auth-dialog     %{buildroot}%{_libexecdir}/nm-protun-auth-dialog
install -Dm644 resources/nm-protun-service.conf     %{buildroot}%{_datadir}/dbus-1/system.d/nm-protun-service.conf

sed -e 's|program=.*|program=%{_libexecdir}/nm-protun-service|' \
    -e 's|auth-dialog=.*|auth-dialog=%{_libexecdir}/nm-protun-auth-dialog|' \
    resources/nm-protun.name > %{buildroot}%{_prefix}/lib/NetworkManager/VPN/nm-protun.name

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CODEOWNERS docs/*
%license LICENSE
%defattr(-,root,root)
%{python3_sitelib}/proton/vpn/platform.abi3.so
%{_libexecdir}/nm-protun-service
%{_libexecdir}/nm-protun-auth-dialog
%{_datadir}/dbus-1/system.d/nm-protun-service.conf
%{_prefix}/lib/NetworkManager/VPN/nm-protun.name

%changelog
* Fri Aug 28 2026 Owen Zimmerman <owen@fyralabs.com>
- Build rust utilities

* Sat Jan 17 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
