Name:           python-nmcli
Version:        1.8.0
Release:        1%?dist
Summary:        A python wrapper library for the network-manager cli client

License:        MIT
URL:            https://github.com/ushiboy/nmcli
Source:         %{pypi_source nmcli}
Packager:       madonuko <mado@fyralabs.com>

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools


%global _description %{expand:
nmcli is a python wrapper library for the network-manager cli client.}

%description %_description

%package -n     python3-nmcli
Summary:        %{summary}

%description -n python3-nmcli %_description


%prep
%autosetup -p1 -n nmcli-%{version}

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files nmcli


%check
%pyproject_check_import


%files -n python3-nmcli -f %{pyproject_files}
%doc README.md
%license LICENSE.txt


%changelog
* Sun Jun 28 2026 madonuko <mado@fyralabs.com> - 1.8.0-1
- Initial package
