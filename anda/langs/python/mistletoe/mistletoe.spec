%global pypi_name mistletoe
%global _desc A rough port of Node.js's EventEmitter to Python with a few tricks of its own.

Name:			python-%{pypi_name}
Version:		1.5.1
Release:		1%?dist
Summary:		A rough port of Node.js's EventEmitter to Python with a few tricks of its own
License:		MIT
URL:			https://github.com/miyuchina/mistletoe
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
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
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mistletoe

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/mistletoe

%changelog
* Sat Mar 14 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
