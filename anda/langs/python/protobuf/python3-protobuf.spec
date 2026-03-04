# Created by pyp2rpm-3.3.8
%global pypi_name protobuf

Name:           python-%{pypi_name}
Version:        7.34.0
Release:        1%?dist
Summary:        Protocol Buffers

License:        BSD-3-Clause
URL:            https://developers.google.com/protocol-buffers/
Source0:        %{pypi_source}

BuildRequires:  python3-devel gcc
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

%description
Protocol Buffers are Google's data interchange format

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Protocol Buffers are Google's data interchange format


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if 0%{?fedora} <= 41 || 0%{?rhel}
%py3_build
%else
%pyproject_wheel
%endif

%install
%if 0%{?fedora} <= 41 || 0%{?rhel}
%py3_install
%else
%pyproject_install
%endif

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitearch}/google/
%if 0%{?fedora} <= 41 || 0%{?rhel}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%else
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/
%endif

%changelog
* Sun Feb 19 2023 madonuko <mado@fyralabs.com> - 4.22.0-1
- Bump.

* Tue Jan 10 2023 madonuko <mado@fyralabs.com> - 4.21.12-1
- Initial package.
