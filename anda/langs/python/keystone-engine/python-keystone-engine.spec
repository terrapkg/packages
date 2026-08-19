Name:           python-keystone-engine
Version:        0.9.2
Release:        %autorelease
Summary:        Keystone assembler engine

License:        GPL-2.0-only
URL:            https://pypi.org/project/keystone-engine
Packager:       madonuko <mado@fyralabs.com>
Source:         %{pypi_source keystone-engine}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
Keystone is a lightweight multi-platform, multi-architecture assembler framework.}

%description %_description

%package -n     python3-keystone-engine
Summary:        %{summary}

%description -n python3-keystone-engine %_description


%prep
%autosetup -p1 -n keystone-engine-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files keystone


%check
%pyproject_check_import


%files -n python3-keystone-engine -f %{pyproject_files}


%changelog
%autochangelog
