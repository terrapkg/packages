%bcond_without tests

Name:           ansible-collection-vexxhost-kubernetes
Version:        3.5.1
Release:        1%{?dist}
Summary:        Ansible collection for deploying Kubernetes
License:        GPL-3.0-or-later
URL:            %{ansible_collection_url vexxhost kubernetes}
Source0:        https://github.com/vexxhost/ansible-collection-kubernetes/archive/refs/tags/v%{version}.tar.gz
# https://github.com/vexxhost/ansible-collection-kubernetes/issues/367
Source1:        LICENSE
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
BuildRequires:  python3-docker-image-py
%endif

BuildArch:      noarch

%description
This is a collection which contains playbooks and
roles which allow you to deploy a Kubernetes cluster using Ansible.

%prep
%autosetup -n ansible-collection-kubernetes-%{version}

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
%doc README.md

%changelog
* Tue Nov 17 2026 Owen Zimmerman <owen@fyralabs.com> - 3.5.1-1
- Initial commit
