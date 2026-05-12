%global pypi_name stable_ts
%global real_name stable-ts
%global _desc Transcription, forced alignment, and audio indexing with OpenAI's Whisper.

Name:			python-%{real_name}
Version:		2.19.1
Release:		2%{?dist}
Summary:		Transcription, forced alignment, and audio indexing with OpenAI's Whisper
License:		MIT
URL:			https://github.com/jianfch/stable-ts
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{real_name}
Summary:        %{summary}
Obsoletes:      python3-%{pypi_name} < %{evr}
%{?python_provide:%python_provide python3-%{real_name}}

%description -n python3-%{real_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i "s/openai-whisper==20230308/openai-whisper/" setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files stable_whisper

%files -n python3-%{real_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/%{real_name}

%changelog
* Mon May 04 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
