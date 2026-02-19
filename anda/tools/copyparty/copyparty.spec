%global pypi_name copyparty

Name:           %{pypi_name}
Version:        1.20.7
Release:        1%?dist
Summary:        Portable, featureful, and fast file server 
URL:            https://github.com/9001/copyparty
Source0:        %{pypi_source}
License:        MIT
# For EVR macro
BuildRequires:  anda-srpm-macros
BuildRequires:  python3-devel python3-pip pyproject-rpm-macros
BuildRequires:  python3dist(wheel) python3dist(build) python3dist(jinja2)
BuildRequires:  python3dist(setuptools) python3dist(installer)
Requires:       python3-%{name} = %{evr}
Suggests:       ffmpeg python3dist(fuse) golang-github-cloudflare-cfssl
BuildArch:		noarch
Packager:       Riley Loo <dev@zackerthescar.com>

%description
Portable file server with accelerated resumable uploads, dedup, WebDAV, 
FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file, no deps.

%package -n     python3-%{pypi_name}
Requires:       python3
Summary:        %{summary}
Requires:       %{name} = %{evr}

%description -n python3-%{pypi_name}
Portable file server with accelerated resumable uploads, dedup, WebDAV, 
FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file, no deps.
 
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

%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}*

%changelog
* Mon Jul 28 2025 Riley Loo <dev@zackerthescar.com>
- Initial package
