%global pypi_name gpt-image
%global _desc Tool to create GPT disk image files.

Name:			python-%{pypi_name}
Version:		0.9.1
Release:		1%?dist
Summary:		Tool to create GPT disk image files
License:		MIT
URL:			https://github.com/swysocki/gpt-image
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n gpt-image-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gpt_image

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Mon Jan 19 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
