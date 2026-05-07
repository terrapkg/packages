%global pypi_name gevent-websocket
%global _desc gevent-websocket is a WebSocket library for the gevent networking library.

Name:			python-%{pypi_name}
Version:		0.10.1
Release:		1%{?dist}
Summary:		gevent-websocket is a WebSocket library for the gevent networking library
License:		Apache-2.0
URL:			https://github.com/cynepiaadmin/geventwebsocket
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
%pyproject_save_files geventwebsocket

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Thu May 07 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
