%global pypi_name glcontext
%global _desc a library providing OpenGL implementation for ModernGL on multiple platforms.

Name:           python-%{pypi_name}
Version:        3.1.0
Release:        1%{?dist}
Summary:        a library providing OpenGL implementation for ModernGL on multiple platforms.
License:        MIT
URL:            https://github.com/jared-hughes/isosurfaces
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  gcc gcc-c++
BuildRequires:  libX11-devel

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
* Fri Oct 23 2026 Jan200101 <sentrycraft123@gmail.com> - 3.1.0-1
- Initial package

