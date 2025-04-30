%global debug_package %nil
%define _python_dist_allow_version_zero # upstream issue?

Name:			python3-ops2deb
Version:		2.6.0
Release:		1%?dist
Summary:		Generate Debian packages for common devops tools
License:		MIT
URL:			https://github.com/upciti/ops2deb
Source0:		%url/archive/refs/tags/%version.tar.gz
BuildRequires:	python3-devel poetry python3.10
BuildRequires:	python3dist(setuptools)
BuildArch:		noarch

%description
ops2deb is designed to generate Debian packages for common devops tools, but
can be used to package any portable application. It consumes a configuration
file and outputs .deb packages. ops2deb can also track new releases of upstream
applications and automatically bump application versions in its configuration
file.


%prep
%autosetup -n ops2deb-%version

%build
poetry build

%install
python3.10 -m ensurepip
python3.10 -m pip install installer
python3.10 -m installer --destdir=%buildroot dist/*.whl
rm -rf %buildroot/%python3_sitelib/*/__pycache__

%files
%license LICENSE
%doc README.md
/usr/bin/ops2deb
/usr/lib/python3*/site-packages/ops2deb*

%changelog
* Fri Apr 28 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2.4.1-1
- Initial package.
