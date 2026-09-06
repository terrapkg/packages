%if %{defined fedora}
%bcond_without tests
%else
%bcond_with tests
%endif

Name:           ansible-collection-onepassword-connect
Version:        2.4.0
Release:        1%{?dist}
Summary:        Contains modules that interact with your 1Password Connect deployment
License:        GPL-3.0-or-later
URL:            %{ansible_collection_url onepassword connect}
Source0:        https://github.com/1Password/ansible-onepasswordconnect-collection/archive/refs/tags/v%{version}.tar.gz
Patch0:         doc-files.patch
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
%endif

BuildArch:      noarch

%description
The 1Password Connect collection contains modules that interact
with your 1Password Connect deployment. The modules communicate
with the 1Password Connect API to support Vault Item
create/read/update/delete operations.

%prep
%autosetup -n ansible-onepasswordconnect-collection-%{version} -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Ansible_collections/#_shebangs
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%build
%ansible_collection_build

%install
%ansible_collection_install

%if %{with tests}
%check
%ansible_test_unit
%endif

%files -f %{ansible_collection_filelist}
%license LICENSE.md
%doc CHANGELOG.md README.md USAGEGUIDE.md CHANGELOG.rst

%changelog
* Sun Jun 14 2026 Owen Zimmerman <owen@fyralabs.com> - 2.4.0-1
- Initial commit
