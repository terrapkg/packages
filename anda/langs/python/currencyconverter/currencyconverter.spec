%global pypi_name   currencyconverter
%global _desc       Currency converter that uses historical rates against a reference currency.

Name:			    python-%{pypi_name}
Version:		    0.18.23
Release:		    1%{?dist}
Summary:		    Currency converter that uses historical rates against a reference currency
License:		    Apache-2.0
URL:			    https://github.com/alexprengere/currencyconverter
Source0:		    %{pypi_source}
BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-pip
BuildRequires:      python3dist(setuptools-scm)

Packager:	        Its-J <jonah@fyralabs.com>

%description
%_desc

%package -n python3-%{pypi_name}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files currency_converter

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/currency_converter

%changelog
* Tue Oct 27 2026 Its-J <jonah@fyralabs.com> - 0.18.22-1
- Initial commit
