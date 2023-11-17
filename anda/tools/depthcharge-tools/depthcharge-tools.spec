Name:			depthcharge-tools
Version:		0.6.2
Release:		1%?dist
Summary:		Tools to manage the Chrome OS bootloader
License:		GPL-2.0-or-later
URL:			https://github.com/alpernebbi/depthcharge-tools
Source0:		%url/archive/v%version/v%version.tar.gz
Requires:		vboot-utils dtc gzip lz4 python3-setuptools uboot-tools vboot-utils xz
BuildRequires:	python3-setuptools python3-rpm-macros
BuildArch:		noarch

%description
depthcharge-tools is a collection of tools that ease and automate interacting
with depthcharge, the Chrome OS bootloader.

%prep
%autosetup

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root=%buildroot

%files
%doc README.rst
%license LICENSE
%_bindir/depthchargectl
%_bindir/mkdepthcharge
%_prefix/lib/python%python3_version/%name-%version-py%python3_version.egg-info/
%_prefix/lib/python%python3_version/%name/

%changelog
%autochangelog
