%global pypi_name srt
%global _desc A simple library and set of tools for parsing, modifying, and composing SRT files.

Name:			python-%{pypi_name}
Version:		3.5.3
Release:		1%?dist
Summary:		A simple library and set of tools for parsing, modifying, and composing SRT files
License:		MIT
URL:			https://github.com/cdown/srt
Source0:		%{pypi_source}
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
%autosetup -n srt-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files srt_tools

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/srt
%{_bindir}/srt-deduplicate
%{_bindir}/srt-fixed-timeshift
%{_bindir}/srt-linear-timeshift
%{_bindir}/srt-lines-matching
%{_bindir}/srt-mux
%{_bindir}/srt-normalise
%{_bindir}/srt-play
%{_bindir}/srt-process
%{python3_sitelib}/__pycache__/srt.cpython-314.opt-1.pyc
%{python3_sitelib}/__pycache__/srt.cpython-314.pyc
%{python3_sitelib}/srt.py

%changelog
* Sat Jan 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
