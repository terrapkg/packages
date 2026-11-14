%global pypi_name isosurfaces
%global _desc Construct isolines/isosurfaces of a 2D/3D scalar field defined by a function.

Name:           python-%{pypi_name}
Version:        0.1.2
Release:        1%{?dist}
Summary:        Construct isolines/isosurfaces of a 2D/3D scalar field defined by a function
License:        MIT
URL:            https://github.com/jared-hughes/isosurfaces
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

Packager:       Jan200101 <sentrycraft123@gmail.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -C

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Fri Oct 23 2026 Jan200101 <sentrycraft123@gmail.com> - 0.1.2-1
- Initial package
