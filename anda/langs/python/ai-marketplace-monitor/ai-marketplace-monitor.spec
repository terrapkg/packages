%global pypi_name   ai-marketplace-monitor
%global _desc       An intelligent tool that monitors Facebook Marketplace listings using AI to help you find the best deals. Get instant notifications when items matching your criteria are posted, with AI-powered analysis of each listing.

Name:			    python-%{pypi_name}
Version:		    0.10.16
Release:		    1%?dist
Summary:		    An intelligent tool that monitors Facebook Marketplace listings using AI to help you find the best deals. Get instant notifications when items matching your criteria are posted, with AI-powered analysis of each listing.
License:		    AGPL-3.0-or-later
URL:			    https://github.com/BoPeng/ai-marketplace-monitor
Source0:		    %{pypi_source ai_marketplace_monitor}
BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-hatchling

Packager:	        Its-J <jonah@fyralabs.com>

%description
%_desc

%package -n         python3-%{pypi_name}
Summary:            %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n     python3-%{pypi_name}
%_desc

%prep
%autosetup -C

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ai_marketplace_monitor

%files -n           python3-%{pypi_name} -f %{pyproject_files}
%doc                README.md CHANGELOG.md CODE_OF_CONDUCT.md
%license            LICENSE
%{_bindir}/aimm
%{_bindir}/ai-marketplace-monitor

%changelog
* Mon Oct 26 2026 Its-J <jonah@fyralabs.com> - 0.10.16-1
- Initial package
