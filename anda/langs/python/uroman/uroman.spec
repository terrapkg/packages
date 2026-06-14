%global pypi_name uroman
%global _desc Universal Romanizer that can convert any unicode script to roman (latin) script.

Name:			python-%{pypi_name}
Version:		1.3.1.1
Release:		2%{?dist}
Summary:		Universal Romanizer that can convert any unicode script to roman (latin) script
License:		GPL-3.0-or-later
URL:			https://github.com/isi-nlp/uroman
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-hatchling

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}
rm -r %{buildroot}%{python3_sitelib}/LICENSE.txt
rm -r %{buildroot}%{python3_sitelib}/README.md
rm -r %{buildroot}%{python3_sitelib}/pyproject.toml
rm -r %{buildroot}%{python3_sitelib}/requirements.txt

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{_bindir}/uroman

%changelog
* Sun May 24 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
