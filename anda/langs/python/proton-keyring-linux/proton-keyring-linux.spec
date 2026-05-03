%global _desc Python3 Proton linux keyring base implementation.

Name:			python-proton-keyring-linux
Version:		0.2.1
Release:		1%{?dist}
Summary:		Python3 Proton linux keyring base implementation
License:		GPL-3.0-or-later
URL:			https://github.com/ProtonVPN/python-proton-keyring-linux
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-proton-keyring-linux
Summary:        %{summary}
Provides:       proton-keyring-linux
%{?python_provide:%python_provide python3-proton-keyring-linux}

%description -n python3-proton-keyring-linux
%_desc

%prep
%autosetup -n python-proton-keyring-linux-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files proton

%files -n python3-proton-keyring-linux -f %{pyproject_files}
%doc CODEOWNERS
%license LICENSE

%changelog
* Mon Apr 27 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
