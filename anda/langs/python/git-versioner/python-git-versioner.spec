%global module git-versioner
%global upstream __version__

Name:           python-%{module}
Version:        7.1
Release:        %autorelease
Summary:        Manage current / next version for project
License:        MIT
URL:            https://gitlab.com/alelec/%{upstream}
Source:         %{url}/-/archive/v%{version}/%{upstream}-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Manages the version number for the project based on git tags. The goal
of this packages versioning scheme is to avoid ever needing to manually
create versions numbers or update version details in files that need to
be committed to the repository.

The general rule is:
- If on a tag, report that as-is.
- When changes are made / git commits added, auto-increment the
appropriate level of the semantic version.}

%description %_description

%package -n     python3-%{module}
Summary:        %{summary}

%description -n python3-%{module} %_description


%prep
%setup -qn %{upstream}-v%{version}
sed -i 's,0.0.0,%{version},' %{upstream}.py
sed -i 's,0.0-new,%{version},' %{upstream}.py
sed -i 's,0.0+new,%{version},' %{upstream}.py
sed -i 's,0.0,%{version},' %{upstream}.py
sed -i 's,on_tag = False,on_tag = True,' %{upstream}.py
sed -i 's,dirty = True,dirty = False,' %{upstream}.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{upstream}

%check
%pyproject_check_import %{upstream}

%files -n python3-%{module} -f %{pyproject_files}
%{_bindir}/%{module}

%changelog
%autochangelog
