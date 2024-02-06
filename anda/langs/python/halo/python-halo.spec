# Created by pyp2rpm-3.3.10
%global pypi_name halo
%global pypi_version 0.0.31

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Beautiful terminal spinners in Python

License:        MIT
URL:            https://github.com/manrajgrover/halo
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(backports.shutil-get-terminal-size) >= 1
BuildRequires:  python3dist(colorama) >= 0.3.9
BuildRequires:  python3dist(coverage) >= 4.4.1
BuildRequires:  python3dist(ipython) = 5.7
BuildRequires:  python3dist(ipywidgets) = 7.1
BuildRequires:  python3dist(log-symbols) >= 0.0.14
BuildRequires:  python3dist(nose) >= 1.3.7
BuildRequires:  python3dist(pylint) >= 1.7.2
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.12
BuildRequires:  python3dist(spinners) >= 0.0.24
BuildRequires:  python3dist(termcolor) >= 1.1
BuildRequires:  python3dist(tox) >= 2.8.2
BuildRequires:  python3dist(twine) >= 1.12.1

%description
Beautiful spinners for terminal, IPython and Jupyter.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(backports.shutil-get-terminal-size) >= 1
Requires:       python3dist(colorama) >= 0.3.9
Requires:       python3dist(ipython) = 5.7
Requires:       python3dist(ipywidgets) = 7.1
Requires:       python3dist(log-symbols) >= 0.0.14
Requires:       python3dist(six) >= 1.12
Requires:       python3dist(spinners) >= 0.0.24
Requires:       python3dist(termcolor) >= 1.1
%description -n python3-%{pypi_name}
Beautiful spinners for terminal, IPython and Jupyter.

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Feb 06 2024 madomado <madonuko@outlook.com> - 0.0.31-1
- Initial package.
