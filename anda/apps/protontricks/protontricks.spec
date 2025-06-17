%bcond_with tests
%global pypi_name protontricks

Name:       terra-%{pypi_name}
Version:    1.12.1
Release:    1%{?dist}
Summary:    Simple wrapper that does winetricks things for Proton enabled games
BuildArch:  noarch

License:    GPL-3.0-or-later
URL:        https://github.com/Matoking/protontricks

# GitHub tarball won't work for setuptools-scm
Source0:    %{pypi_source}

BuildRequires: desktop-file-utils
BuildRequires: python3-devel
BuildRequires: python3dist(pip)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(setuptools-scm)
# BuildRequires: python3dist(vdf) >= 3.4
%if %{with tests}
BuildRequires: python3dist(pytest-cov) >= 2.10
BuildRequires: python3dist(pytest) >= 6.0
%endif

Requires:   (terra-winetricks or winetricks-git)
Conflicts:  protontricks

Recommends: yad

Suggests:   zenity
# https://github.com/Matoking/protontricks/blob/master/CHANGELOG.md#1120---2024-09-16
Provides:   bundled(python3-vdf)


%description
A simple wrapper that does winetricks things for Proton enabled games,
requires Winetricks.

This is a fork of the original project created by sirmentio. The original
repository is available at Sirmentio/protontricks.


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%if 0%{?fedora} <= 41
%py3_build
%else
%pyproject_wheel
%endif


%install
%if 0%{?fedora} <= 41
%py3_install
%else
%pyproject_install
%endif

# Remove `protontricks-desktop-install`, since we already install .desktop
# files properly
# https://bugzilla.redhat.com/show_bug.cgi?id=1991684
rm %{buildroot}%{_bindir}/%{pypi_name}-desktop-install


%if %{with tests}
%check
%{py3_test_envvars} %{python3} -m pytest -v
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%endif


%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{pypi_name}-launch
%{_bindir}/%{pypi_name}
%{_datadir}/applications/*.desktop
%{python3_sitelib}/%{pypi_name}/
%if 0%{?fedora} <= 41
%{python3_sitelib}/%{pypi_name}-%{version}*.egg-info/
%else
%{python3_sitelib}/%{pypi_name}-%{version}*.dist-info/
%endif


%changelog
%autochangelog
