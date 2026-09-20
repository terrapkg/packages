%global pypi_name gefyra
%global _desc Blazingly-fast, rock-solid, local application development with Kubernetes.

Name:			python-%{pypi_name}
Version:		2.5.5
Release:		1%?dist
Summary:		Blazingly-fast, rock-solid, local application development with Kubernetes.
License:		Apache-2.0
URL:			https://github.com/gefyrahq/gefyra
Source0:		%{pypi_source}
Source1:		https://github.com/gefyrahq/gefyra/blob/main/LICENSE
BuildArch:      noarch

Conflicts:      plan9port

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core

Packager:	    Its-J <jonah@fyralabs.com>

%description
%{_desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{_desc}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}
cp %{SOURCE1} LICENSE

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/g
%{_bindir}/gefyra
%{_bindir}/gefyra-docs
%{_bindir}/setversion

%changelog
* Wed Sep 16 2026 Its-J <jonah@fyralabs.com> - 2.5.5-1
- Initial commit
