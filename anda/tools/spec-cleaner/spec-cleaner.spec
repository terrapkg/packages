%global pypi_name spec-cleaner

Name:			%{pypi_name}
Version:		1.3.1
Release:		1%{?dist}
Summary:		Tool that cleans the given RPM spec file according to the style guide
License:		BSD-3-Clause
URL:			https://github.com/rpm-software-management/spec-cleaner
Source0:		%{pypi_source spec_cleaner}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
spec-cleaner is a tool that cleans the given RPM
spec file according to the style guide and returns the result.

%prep
%autosetup -C

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files spec_cleaner

%files -f %{pyproject_files}
%doc README.md
%license COPYING
%{_bindir}/spec-cleaner
%{_prefix}/lib/obs/service/*
%{_datadir}/%{pypi_name}/*

%changelog
* Thu Oct 29 2026 Owen Zimmerman <owen@fyralabs.com> - 1.3.1-1
- Initial commit
