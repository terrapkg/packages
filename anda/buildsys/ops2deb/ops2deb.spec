%global pypi_name ops2deb
%global _desc Generate Debian packages for common devops tools such as kubectl, kustomize, helm.

Name:			python-%{pypi_name}
Version:		2.7.0
Release:		1%?dist
Summary:		Generate Debian packages for common devops tools such as kubectl, kustomize, helm
License:		MIT
URL:			https://github.com/upciti/ops2deb
Source0:		%{pypi_source}
Patch0:			versions.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-poetry

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/ops2deb

%changelog
* Thu Apr 23 2026 Owen Zimmerman <owen@fyralabs.com>
- Switch to modern python packaging methods

* Fri Apr 28 2023 madonuko <mado@fyralabs.com> - 2.4.1-1
- Initial package.
