%define unmangled_name proton-core
%define github_repo_name python-proton-core
%global _desc The proton-core component contains core logic used by the other Proton components.

Name:       python-proton-core
Version:    0.7.0
Release:    1%?dist
Summary:    %{unmangled_name} library
License:    GPL-3.0-or-later
URL:        https://github.com/ProtonVPN/%{github_repo_name}
Source:     %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildArch:      noarch

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n python3-%{unmangled_name}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{unmangled_name}}

%description -n python3-%{unmangled_name}
%_desc

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files proton

%files -n python3-%{unmangled_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Tue Feb 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
