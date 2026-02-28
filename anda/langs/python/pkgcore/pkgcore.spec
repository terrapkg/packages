%global pypi_name pkgcore
%global _desc A framework for package management.

Name:			python-%{pypi_name}
Version:		0.12.32
Release:		1%?dist
Summary:		A framework for package management
License:		BSD-3-Clause
URL:			https://pkgcore.github.io/pkgcore
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-build
BuildRequires:  python3-wheel
BuildRequires:  python3-snakeoil
BuildRequires:  python3-flit-core
BuildRequires:  make

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%pkg_completion -n python3-%{pypi_name} -B pquery
%pkg_completion -n python3-%{pypi_name} -z pkgcore

%prep
%autosetup -n pkgcore-%{version}

%build
export PYTHONPATH=%{_builddir}/pkgcore-%{version}:$PYTHONPATH
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pkgcore
install -Dm755 data/lib/pkgcore/ebd/helpers/common/pkgcore-ebuild-helper    %{buildroot}%{_bindir}/pkgcore-ebuild-helper
install -Dm755 data/lib/pkgcore/ebd/helpers/common/pkgcore-ipc-helper       %{buildroot}%{_bindir}/pkgcore-ipc-helper
install -Dm755 data/lib/pkgcore/shell/bin/pkgcore-sh-helper                 %{buildroot}%{_bindir}/pkgcore-sh-helper

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/patom
%{_bindir}/pclean
%{_bindir}/pclonecache
%{_bindir}/pconfig
%{_bindir}/pebuild
%{_bindir}/pinspect
%{_bindir}/pmaint
%{_bindir}/pmerge
%{_bindir}/pquery
%{_bindir}/pkgcore-ebuild-helper
%{_bindir}/pkgcore-ipc-helper
%{_bindir}/pkgcore-sh-helper
%{_usr}/lib/%{pypi_name}/
%{_datadir}/%{pypi_name}/*

%changelog
* Fri Feb 13 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
