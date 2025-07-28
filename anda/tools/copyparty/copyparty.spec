%global debug_package %nil #needed to avoid "empty %files file" errors

Name:           copyparty
Version:        1.18.5
Release:        1%?dist
Summary:        Portable, featureful, and fast file server 
URL:            https://github.com/9001/copyparty
Source0:        %url/archive/refs/tags/v%version.tar.gz
License:        MIT
BuildRequires:  python3-devel python3-pip
BuildRequires:  python3dist(wheel) python3dist(build) python3dist(jinja2)
BuildRequires:  python3dist(setuptools) python3dist(installer)
Requires:       python3
BuildArch:		noarch
Packager:       Riley Loo <dev@zackerthescar.com>

%description
Portable file server with accelerated resumable uploads, dedup, WebDAV, 
FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file, no 
(runtime) deps (other than Python itself)
 
%prep
%autosetup -n copyparty-%version

%build
python3 -m build
 
%install
python3 -m ensurepip
python3 -m installer --destdir=%buildroot dist/*.whl
rm -rf %buildroot/%python3_sitelib/*/__pycache__
rm -rf %buildroot/usr/bin/*.py

%files
%license /usr/share/doc/copyparty/LICENSE
%doc /usr/share/doc/copyparty/README.md
/usr/bin/copyparty
/usr/bin/partyfuse
/usr/bin/u2c
/usr/lib/python3*/site-packages/copyparty*
 
%changelog
* Mon Jul 28 2025 Riley Loo <dev@zackerthescar.com>
- Initial package
