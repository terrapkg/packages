## Spec originally from Fedora, only modified for multibranch support and Terra changes

## ...I don't know why they have this here?
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global pypi_name colorthief

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        2%{?dist}
Summary:        Grabs the dominant color or a representative color palette from an image

# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/382
# License file provided by Python module, see:
# rpm -q --licensefiles {python3_sitelib}/{name}-{version}.dist-info/LICENSE
License:        BSD-3-Clause
URL:            https://github.com/fengsp/color-thief-py
Source0:        %{pypi_source}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

%global _description %{expand:
A Python module for grabbing the color palette from an image.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%if 0%{?fedora} <= 41 || 0%{?rhel}
%py3_build
%else
%pyproject_wheel
%endif

%install
%if 0%{?fedora} <= 41 || 0%{?rhel}
%py3_install
%else
%pyproject_install
%pyproject_save_files %{pypi_name}
%endif

%if 0%{?fedora} > 41
%check
%pyproject_check_import
%endif

%if 0%{?fedora} <= 41 || 0%{?rhel}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%else
%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%endif


%changelog
* Mon May 26 2025 Gilver E. <rockgrub@disroot.org> - 0.2.1-1
- Initial port from Fedora
