%global _desc Official ProtonVPN CLI Linux app.

%global __requires_exclude ^python3\\.14dist\\(proton-vpn-local-agent\\)$

Name:			python-proton-vpn-cli
Version:		0.1.5
Release:		1%?dist
Summary:		Official ProtonVPN CLI Linux app
License:		GPL-3.0-only
URL:			https://github.com/ProtonVPN/proton-vpn-cli
Source0:		%url/archive/refs/tags/v%version.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildArch:      noarch

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-proton-vpn-cli
Summary:        %{summary}
Provides:       proton-vpn-cli
Requires:       python3-proton-vpn-local-agent
%{?python_provide:%python_provide python3-proton-vpn-cli}

%description -n python3-proton-vpn-cli
%_desc

%prep
%autosetup -n proton-vpn-cli-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files proton

%files -n python3-proton-vpn-cli -f %{pyproject_files}
%doc README.md COPYING.md CONTRIBUTING.md CODEOWNERS
%license LICENSE
%{_bindir}/protonvpn

%changelog
* Fri Jan 30 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
