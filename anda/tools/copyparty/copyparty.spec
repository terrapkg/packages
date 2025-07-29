%global debug_package %nil #needed to avoid "empty %files file" errors

Name:           copyparty
Version:        1.18.6
Release:        1%?dist
Summary:        Portable, featureful, and fast file server 
URL:            https://github.com/9001/copyparty
Source0:        https://files.pythonhosted.org/packages/source/c/copyparty/copyparty-%version.tar.gz
License:        MIT
BuildRequires:  python3-devel python3-pip pyproject-rpm-macros
BuildRequires:  python3dist(wheel) python3dist(build) python3dist(jinja2)
BuildRequires:  python3dist(setuptools) python3dist(installer)
Requires:       python3
Suggests:       ffmpeg python3dist(fuse)
BuildArch:		noarch
Packager:       Riley Loo <dev@zackerthescar.com>

%description
Portable file server with accelerated resumable uploads, dedup, WebDAV, 
FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file, no 
(runtime) deps (other than Python itself)

%package -n     python3-copyparty
Summary:        %{summary}

%description -n python3-copyparty

Portable file server with accelerated resumable uploads, dedup, WebDAV, 
FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file, no 
(runtime) deps (other than Python itself)
 
%prep
%autosetup -n copyparty-%version

%build
%pyproject_wheel

%install
%pyproject_install

%files
%license LICENSE
%doc README.md
%{_bindir}/copyparty
%{_bindir}/partyfuse
%{_bindir}/u2c

%files -n python3-copyparty
%{python3_sitelib}/copyparty*

 
%changelog

* Mon Jul 28 2025 Riley Loo <dev@zackerthescar.com>
- Initial package
