# Created by pyp2rpm-3.3.8
%global pypi_name protobuf

Name:           python-%{pypi_name}
Version:        5.28.2
Release:        1%?dist
Summary:        Protocol Buffers

License:        BSD-3-Clause
URL:            https://developers.google.com/protocol-buffers/
Source0:        %{pypi_source}

BuildRequires:  python3-devel gcc
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
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitearch}/google
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}-nspkg.pth

%changelog
* Sun Feb 19 2023 windowsboy111 <wboy111@outlook.com> - 4.22.0-1
- Bump.

* Tue Jan 10 2023 windowsboy111 <wboy111@outlook.com> - 4.21.12-1
- Initial package.
