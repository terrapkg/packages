# Created by pyp2rpm-3.3.10
%global pypi_name umstellar
%global pypi_version 0.2.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Ultramarine Quickstart Tool

Provides:       python3-%{pypi_name} = %{version}-%{release}
Provides:       %{pypi_name} = %{version}-%{release}

License:        GPL-3.0
URL:            https://github.com/Ultramarine-Linux/stellar
Source0:        %{url}/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 Stellar (Stellar)Stellar is a quick-and-dirty GUI post-install menu for
Ultramarine Linux. It's written in Python and uses libadwaita for the UI.We
hacked this together in a few days, just in time for Ultramarine Linux 39 which
happened to get delayed due to some major GNOME 45 porting issues. It's meant
to only be used for Ultramarine Linux 39's Anaconda post-install menu.
Why?So,...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(requests)
Requires:       python3dist(pygobject)
Requires:       anaconda-core
%description -n python3-%{pypi_name}

Stellar is a quick-and-dirty GUI post-install menu for
Ultramarine Linux


%prep
%autosetup -n stellar-%{pypi_version}

%build
%py3_build

%install
%py3_install

# install kickstart file
install -D -m 644 example.ks %{buildroot}%{_datadir}/anaconda/post-scripts/stellar.ks

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info
%{_datadir}/anaconda/post-scripts/stellar.ks

%changelog
* Mon Apr 1 2024 Lleyton Gray <lleyton@fyralabs.com> - 0.2.0-1
- Bump version with various fixes

* Fri Nov 10 2023 Cappy Ishihara <cappy@cappuchino.xyz> - 0.0.1-1
- Initial package.
