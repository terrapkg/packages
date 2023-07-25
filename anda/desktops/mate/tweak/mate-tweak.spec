%define debug_package %nil

Name:		mate-tweak
Version:	22.10.0
Release:	1%?dist
Summary:	Tweak tool for the MATE Desktop
License:	GPL-2.0
URL:		https://github.com/ubuntu-mate/mate-tweak
Source0:	%url/archive/refs/tags/%version.tar.gz
Requires:	python3
BuildRequires:	python3dist(setuptools) rpm_macro(py3_build) intltool desktop-file-utils

%description
This is MATE Tweak, a fork of mintDesktop.

%prep
%autosetup
python3 -m ensurepip
python3 -m pip install distutils-extra-python

%build
%py3_build

%install
%py3_install

rm -rf %buildroot%python3_sitearch/__pycache__

%check
desktop-file-validate %buildroot%_datadir/applications/macro-{glx,no-composite,xr_glx_hybrid,xrender}.desktop

%files
%doc README.md
%license COPYING
%_bindir/%name
%_bindir/macro-{xrender,picom,glx,compton,xr_glx_hybrid,no-composite}
%_prefix/lib/%name/
%python3_sitearch/%name-%version-py%python3_version.egg-info
%_datadir/locale/*/LC_MESSAGES/%name.mo
%_mandir/man1/macro-{glx,no-composite,xr_glx_hybrid,xrender}.1
%_mandir/man1/%name.1
%_datadir/applications/%name.desktop
%_datadir/applications/macro-{glx,no-composite,xr_glx_hybrid,xrender}.desktop
%_datadir/polkit-1/actions/org.mate.%name.policy

%changelog
%autochangelog
