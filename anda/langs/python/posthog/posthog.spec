%global pypi_name posthog
%global _desc Send usage data from your Python code to PostHog.

Name:			python-%{pypi_name}
Version:		7.5.1
Release:		1%?dist
Summary:		Send usage data from your Python code to PostHog
License:		MIT
URL:			https://posthog.com/docs/libraries/python
Source0:		%{pypi_source}
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
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Sat Jan 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
