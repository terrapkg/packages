%global pypi_name easyspeak-linux
%global _desc Voice control for Linux desktops. Fully local, no cloud, Wayland-native.

Name:			python-%{pypi_name}
Version:		0.3.0
Release:		1%{?dist}
Summary:		Voice control for Linux desktops. Fully local, no cloud, Wayland-native
License:		GPL-3.0-or-later
URL:			https://github.com/ctsdownloads/easyspeak
Source0:		%{url}/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n easyspeak-%{version}
sed -E '/^requires-python/c requires-python = ">=3.10"' -i pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files easyspeak

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CONTRIBUTING.md
%license LICENSE

%changelog
* Sun Jun 07 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
