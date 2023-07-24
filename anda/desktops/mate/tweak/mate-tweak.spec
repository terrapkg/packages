Name:		mate-tweak
Version:	22.10.0
Release:	1%?dist
Summary:	Tweak tool for the MATE Desktop
License:	GPL-2.0
URL:		https://github.com/ubuntu-mate/mate-tweak
Source0:	%url/archive/refs/tags/%version.tar.gz
Requires:	python3

%description
This is MATE Tweak, a fork of mintDesktop.

%prep
%autosetup

%build
python setup.py install

%install

%files
%doc README.md
%license COPYING

%changelog
%autochangelog
