Name:           python-keyboard
Version:        0.13.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Hook and simulate keyboard events on Windows and Linux

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/boppreh/keyboard
Source:         %{pypi_source keyboard %{version} zip}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'keyboard' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-keyboard
Summary:        %{summary}

%description -n python3-keyboard %_description


%prep
%autosetup -p1 -n keyboard-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files keyboard


%check
%pyproject_check_import


%files -n python3-keyboard -f %{pyproject_files}


%changelog
%autochangelog
