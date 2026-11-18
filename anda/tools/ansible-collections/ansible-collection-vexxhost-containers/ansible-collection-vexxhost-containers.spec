%bcond_without tests

Name:           ansible-collection-vexxhost-containers
Version:        1.6.8
Release:        1%{?dist}
Summary:        Playbooks and roles which allow you to deploy container runtimes using Ansible
License:        GPL-3.0-or-later
URL:            %{ansible_collection_url vexxhost containers}
Source0:        https://github.com/vexxhost/ansible-collection-containers/archive/refs/tags/v%{version}.tar.gz
Source1:        LICENSE
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
BuildRequires:  python3-docker-image-py
%endif

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n ansible-collection-containers-%{version}

%build
%ansible_collection_build

%install
%ansible_collection_install
cp %{S:1} LICENSE

%if %{with tests}
%check
%ansible_test_unit
%endif

%files -f %{ansible_collection_filelist}
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
* Tue Nov 17 2026 Owen Zimmerman <owen@fyralabs.com> - 1.6.8-1
- Initial commit
