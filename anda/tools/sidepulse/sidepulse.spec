%global commit f9f1d845153b4f3bc23a5e11d87ecde2e36d6479
%global commit_date 20260901
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define _python_dist_allow_version_zero 1

%global real_name sidepulse
%global _desc CLI for sidepulse.

Name:			python-%{real_name}
Version:		0~%{commit_date}git.%{shortcommit}
Release:		1%{?dist}
Summary:		CLI for sidepulse
License:		MIT
URL:			https://github.com/inteliwear/sidepulse
Source0:		%{url}/archive/%{commit}/glasgow-%{commit}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-build
BuildRequires:  python3-setuptools

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package     -n python3-%{real_name}
Summary:        %{summary}
Provides:       sidepulse
%{?python_provide:%python_provide python3-%{real_name}}

%description -n python3-%{real_name}
%_desc

%prep
%autosetup -C

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{real_name}

%files -n python3-%{real_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{python3_sitelib}/agent_monitor/*
%{python3_sitelib}/sidepulse_cli/*
%{_bindir}/agent-monitor
%{_bindir}/agent-status-bar
%{_bindir}/sidepulse
%{_bindir}/sidepulse-reply

%changelog
* Thu Sep 03 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
