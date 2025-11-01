%global common_description %{expand:
An advanced rpm-ostree compose system}

Name:           melody
Summary:        An advanced rpm-ostree compose system
Version:        1
Release:        8%{?dist}

License:        GPL-3.0-or-later

URL:            https://github.com/tau-OS/melody
Source0:        https://github.com/tau-OS/melody/archive/refs/heads/main.zip

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(anytree)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(poetry-core)
BuildRequires:  python3dist(rich)

Requires:       python3-dnf
Requires:       python3-melody = %{version}-%{release}

%description %{common_description}


%package -n     python3-melody
Summary:        %{summary}
%description -n python3-melody %{common_description}


%prep
%autosetup -p1 -n melody-main


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files melody


%files
%license LICENSE
%doc README.md
%{_bindir}/melody


%files -n python3-melody -f %{pyproject_files}
%license LICENSE
%doc README.md

%dir %{python3_sitelib}/melody
