%global commit 4992a813c160e037712b0793cd0488275cb3d195
%global commit_date 20260120
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global pypi_name types-colorama
%global _desc Typing stubs for colorama.

Name:			python-%{pypi_name}
Version:		0~%{commit_date}git.%shortcommit
Release:		1%?dist
Summary:		Typing stubs for colorama
License:		Apache-2.0
URL:			https://github.com/python/typeshed
Source0:		%url/archive/%commit/typeshed-%commit.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3-colorama
Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       types-colorama
Provides:       python%{python3_pkgversion}dist(types-colorama)
Provides:       python3.13dist(types-colorama)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n typeshed-%{commit}

%build
# Not needed for stub file package

%install
mkdir -p %{buildroot}%{python3_sitelib}/colorama-stubs
install -Dm755 stubs/colorama/colorama/*.pyi          %{buildroot}%{python3_sitelib}/colorama-stubs/
install -Dm755 stubs/colorama/METADATA.toml         %{buildroot}%{python3_sitelib}/colorama-stubs/METADATA.toml

%files -n python3-%{pypi_name}
%doc README.md MAINTAINERS.md CONTRIBUTING.md
%license LICENSE
%python3_sitelib/colorama-stubs/METADATA.toml
%{python3_sitelib}/colorama-stubs/*.pyi

%changelog
* Tue Sep 30 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
