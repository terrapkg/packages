%global pypi_name antlr4-python3-runtime
%global _desc Python 3 runtime libraries for ANTLR 4.

%global commit 23ed92cc6655f7def5d1447f51cb4c9657400f9d
%global commit_date 20150607
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global ver 4.9.3

Name:			python-%{pypi_name}
Version:		%{ver}^%{commit_date}git.%{shortcommit}
Release:		1%?dist
Summary:		Python 3 runtime libraries for ANTLR 4
License:		BSD
URL:			https://www.antlr.org/
Source0:		https://github.com/parrt/antlr4-python3/archive/%commit/antlr4-python3-%commit.tar.gz
Source1:        https://github.com/s-a/license/blob/master/_licenses/bsd-3-clause.txt
Patch0:         shebang.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

Conflicts:      python3-antlr4-runtime

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%package -n     python3-%{pypi_name}-doc
Summary:        documentation for python3-%{pypi_name}

%description -n python3-%{pypi_name}-doc
documentation for python3-%{pypi_name}.

%prep
%autosetup -n antlr4-python3-%{commit} -p1
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
install -Dm755 bin/pygrun %{buildroot}%{_bindir}/pygrun
%pyproject_save_files antlr4

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.txt RELEASE-4.5.txt
%license bsd-3-clause.txt
%{_bindir}/pygrun

%changelog
* Thu Jan 08 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
