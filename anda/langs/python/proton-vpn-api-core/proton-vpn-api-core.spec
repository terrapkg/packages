%global pypi_name proton-vpn-api-core
%global _desc A facade to the other Proton VPN components, exposing a uniform API to the available Proton VPN services.

Name:			python-%{pypi_name}
Version:		4.14.3
Release:		1%?dist
Summary:		A facade to the other Proton VPN components
License:		GPL-3.0-Only
URL:			https://github.com/ProtonVPN/python-proton-vpn-api-core
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

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
%autosetup -n python-%{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files proton

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CODEOWNERS
%license LICENSE

%changelog
* Sat Jan 17 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
