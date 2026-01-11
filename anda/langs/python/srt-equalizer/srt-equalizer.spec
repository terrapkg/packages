%global pypi_name srt-equalizer
%global _desc A Python module to transform subtitle line lengths, splitting into multiple subtitle fragments if necessary.

Name:			python-%{pypi_name}
Version:		0.1.11
Release:		1%?dist
Summary:		A Python module to transform subtitle line lengths, splitting into multiple subtitle fragments if necessary
License:		MIT
URL:			https://github.com/peterk/srt_equalizer
Source0:		https://github.com/peterk/srt_equalizer/archive/refs/tags/v%version.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n srt_equalizer-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files srt_equalizer

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Sat Jan 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
