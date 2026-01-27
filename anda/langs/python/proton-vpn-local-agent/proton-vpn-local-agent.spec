%define debug_package %{nil}

%global pypi_name proton-vpn-local-agent
%global _desc Proton VPN local agent written in Rust.

Name:			python-%{pypi_name}
Version:		1.6.0
Release:		2%?dist
Summary:		Proton VPN local agent written in Rust
License:		GPL-3.0-only
URL:			https://github.com/ProtonVPN/local-agent-rs
Source0:		%url/archive/refs/tags/%version.tar.gz

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros

# Really cursed but there is no pyproject.toml or setup.py in this package to auto-provide this, and proton-vpn needs this
Provides:       python3.14dist(proton-vpn-local-agent)

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       %{pypi_name}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n local-agent-rs-%{version}
pushd %{name}
%{cargo_prep_online}
popd

%build
pushd %{name}
%{cargo_build}
popd

%install
pushd %{name}
install -Dm0644 target/release/libpython_proton_vpn_local_agent.so %{buildroot}%{_libdir}/proton/local_agent.so
popd

%files -n python3-%{pypi_name}
%doc README.md CODEOWNERS
%{_libdir}/proton/local_agent.so

%changelog
* Sun Jan 18 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
