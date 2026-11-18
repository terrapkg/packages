%global pypi_name docker-image-py
%global _desc Parse docker image as distribution does.

Name:			python-%{pypi_name}
Version:		0.2.0
Release:		1%{?dist}
Summary:		Parse docker image as distribution does
License:		Apache-2.0
URL:			https://github.com/realityone/docker-image-py
Source0:		%{pypi_source docker_image_py}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n docker_image_py-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files docker_image

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Tue Nov 17 2026 Owen Zimmerman <owen@fyralabs.com> - 0.2.0-1
- Initial commit
