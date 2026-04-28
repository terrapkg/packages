%global pypi_name pymusiclooper
%global _desc A python program for repeating music endlessly and creating seamless music loops, with play/export/tagging support.

Name:			python-%{pypi_name}
Version:		3.6.0
Release:		1%?dist
Summary:		A python program for repeating music endlessly and creating seamless music loops, with play/export/tagging support
License:		MIT
URL:			https://github.com/arkrow/PyMusicLooper
Source0:		%{pypi_source}
# Fedora doesn't yet carry pytaglib >=3.0.0
Patch0:         make-dep-installable.patch
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
Provides:       pymusiclooper
Provides:       python3-pymusiclooper
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n pymusiclooper-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pymusiclooper

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CLI_README.md CHANGELOG.md
%license LICENSE
%{_bindir}/pymusiclooper
%python3_sitelib/pymusiclooper-%version.dist-info/*

%changelog
* Fri Dec 26 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
