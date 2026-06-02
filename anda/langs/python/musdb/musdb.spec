%global pypi_name musdb
%global _desc Python parser and tools for MUSDB18 Music Separation Dataset.

Name:			python-%{pypi_name}
Version:		0.4.3
Release:		1%?dist
Summary:		Python parser and tools for MUSDB18 Music Separation Dataset
License:		MIT
URL:			https://github.com/sigsep/sigsep-mus-db
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
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
%autosetup -n musdb-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files musdb

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/musdbconvert

%changelog
* Thu Jan 15 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
