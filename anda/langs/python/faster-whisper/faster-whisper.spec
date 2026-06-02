%global pypi_name faster-whisper
%global _desc Faster Whisper transcription with CTranslate2.

Name:			python-%{pypi_name}
Version:		1.2.1
Release:		1%?dist
Summary:		Faster Whisper transcription with CTranslate2
License:		MIT
URL:			https://github.com/SYSTRAN/faster-whisper
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-installer
BuildRequires:  python3-wheel
BuildRequires:  python3-poetry-core
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
%autosetup -n faster-whisper-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files faster_whisper

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Sun Apr 12 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
