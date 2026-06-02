%global pypi_name ffmpeg-python
%global _desc Python bindings for FFmpeg - with complex filtering support.

Name:			python-%{pypi_name}
Version:		0.2.0
Release:		1%?dist
Summary:		Python bindings for FFmpeg - with complex filtering support
License:		Apache-2.0
URL:			https://github.com/kkroening/ffmpeg-python
Source0:		%url/archive/refs/tags/%version.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-wheel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n ffmpeg-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ffmpeg

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Thu Jan 15 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
