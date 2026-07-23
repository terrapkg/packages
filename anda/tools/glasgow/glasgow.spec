%global commit a37e7e95b03d278e6adce14ecab8bae042de2a60
%global commit_date 20260721
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global pypi_name glasgow
%global _desc Scots Army Knife for electronics.

# Errors without setting this for some reason
%global _udevrulesdir /usr/lib/udev/rules.d

Name:			python-%{pypi_name}
Version:		0~%{commit_date}git.%{shortcommit}
Release:		1%{?dist}
Summary:		Scots Army Knife for electronics
License:		0BSD AND Apache-2.0
URL:			https://github.com/GlasgowEmbedded/glasgow
Source0:		%url/archive/%commit/glasgow-%commit.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-build
BuildRequires:  python3-pdm-backend
BuildRequires:  git

Requires:       yosys
Requires:       nextpnr
Requires:       icestorm

Recommends:     python3-aiohttp

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package     -n python3-%{pypi_name}
Summary:        %{summary}
Provides:       glasgow
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n glasgow-%commit

%pyproject_patch_dependency amaranth:drop_constraints
%pyproject_patch_dependency importlib-resources:drop_constraints

%build
export PDM_BUILD_SCM_VERSION=0.1.0
pushd software
%pyproject_wheel
popd

%install
%pyproject_install
%pyproject_save_files glasgow
install -Dm644 config/70-glasgow.rules %{buildroot}%{_udevrulesdir}/70-glasgow.rules

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CODEOWNERS CODE_OF_CONDUCT.md CONTRIBUTING.md
%license LICENSE-0BSD.txt LICENSE-Apache-2.0.txt
%{_bindir}/glasgow
%{_udevrulesdir}/70-glasgow.rules

%changelog
* Mon Sep 29 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
