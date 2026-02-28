Name:           terra-appstream-helper
Version:        0.1.10
Release:        1%?dist
Summary:        Scripts and RPM macros to help with AppStream metadata generation for Terra
License:        GPL-3.0-or-Later
URL:            https://github.com/terrapkg/appstream-helper
Source:         %{url}/archive/refs/tags/v%version.tar.gz
BuildArch:      noarch
Requires:       python3-%{name} = %{evr}
BuildRequires:  anda-srpm-macros python3-devel python3-installer pyproject-rpm-macros python3dist(pip) python3dist(setuptools) python3dist(wheel)

%description
%{summary}.

%package -n     python3-%{name}
Summary:        Python files for %{name}
Requires:       %{name} = %{evr}
BuildArch:      noarch

%description -n python3-%{name}
Python files needed for %{name}.

%prep
%autosetup -n appstream-helper-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l terra_appstream_helper
install -Dpm644 terra-appstream.macros %buildroot%_rpmmacrodir/macros.terra-appstream

%files
%license LICENSE
%doc README.md
%{_bindir}/terra-appstream-helper
%{_rpmmacrodir}/macros.terra-appstream



%files -n python3-%{name} -f %{pyproject_files}



%changelog
%autochangelog
