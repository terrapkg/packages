%define debug_package %nil

Name:		mate-tweak
Version:	22.10.0
Release:	2%?dist
Summary:	Tweak tool for the MATE Desktop
License:	GPL-2.0
URL:		https://github.com/ubuntu-mate/mate-tweak
Source0:	%url/archive/refs/tags/%version.tar.gz
Requires:	python3
BuildRequires:	python3dist(setuptools) python3-devel python3dist(pip) intltool desktop-file-utils

%description
This is MATE Tweak, a fork of mintDesktop.

%prep
%autosetup
python3 -m ensurepip
python3 -m pip install distutils-extra-python

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
desktop-file-install data/*.desktop
cp -r %{buildroot}%{python3_sitelib}%{_prefix} -t %{buildroot} --preserve=all
rm -rf %{buildroot}%{python3_sitelib}%{_prefix}
%endif

%check
desktop-file-validate %buildroot%_datadir/applications/*.desktop

%files
%doc README.md
%license COPYING
%_bindir/%name
%_bindir/marco-{compton,xrender,picom,glx,xr_glx_hybrid,no-composite}
%_prefix/lib/%name/
%_datadir/locale/*/LC_MESSAGES/%name.mo
%_mandir/man1/marco-{glx,no-composite,xr_glx_hybrid,xrender}.1.gz
%_mandir/man1/%name.1.gz
%_datadir/applications/%name.desktop
%_datadir/applications/marco-{glx,no-composite,xr_glx_hybrid,xrender}.desktop
%_datadir/polkit-1/actions/org.mate.%name.policy
%{python3_sitelib}/__pycache__/
%{python3_sitelib}/setup.py
%if 0%{?fedora} <= 41
%{python3_sitelib}/mate_tweak-%version-py3.*.egg-info/
%else
%{python3_sitelib}/mate_tweak-%{version}.dist-info/
%endif

%changelog
%autochangelog
