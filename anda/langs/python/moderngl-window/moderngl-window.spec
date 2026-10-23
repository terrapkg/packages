%define debug_package %{nil}

%global pypi_name moderngl-window
%global _desc utility library for ModernGL making window creation and resource loading simple

Name:           python-%{pypi_name}
Version:        3.1.1
Release:        1%{?dist}
Summary:        utility library for ModernGL making window creation and resource loading simple
License:        MIT
URL:            https://github.com/moderngl/moderngl-window
Source0:        %{pypi_source moderngl_window}

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  gcc-c++

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
%pyproject_save_files moderngl_window

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
