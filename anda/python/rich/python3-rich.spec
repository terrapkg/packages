# Created by pyp2rpm-3.3.8
%global pypi_name rich
%global pypi_version 13.3.2

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal

License:        None
URL:            https://github.com/Textualize/rich
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
%{summary}.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(ipywidgets) >= 7.5.1 with python3dist(ipywidgets) < 9~~)
Requires:       (python3dist(markdown-it-py) >= 2.2 with python3dist(markdown-it-py) < 3~~)
Requires:       (python3dist(pygments) >= 2.13 with python3dist(pygments) < 3~~)
Requires:       (python3dist(typing-extensions) >= 4 with python3dist(typing-extensions) < 5~~)
%description -n python3-%{pypi_name}
%{summary}.


%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Sun Mar 19 2023 windowsboy111 <wboy111@outlook.com> - 13.3.2-1
- Initial package.
