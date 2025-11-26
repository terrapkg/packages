%global dist %{nil}

Name:           terra-release
Version:        %{?fedora:%{fedora}}%{?rhel:%{rhel}}
Release:        6
Summary:        Release package for Terra

License:        MIT
URL:            https://terra.fyralabs.com
Source0:        terra.repo
BuildArch:      noarch

%dnl We probably shouldn't do this in Rawhide!
%dnl Requires:       system-release(%{version})
Requires:       (epel-release-latest-%{version} or epel-release)

%description
Release package for Terra, containing the Terra repository configuration.

%prep

%build

%install
install -D -p -m 0644 -t %{buildroot}%{_sysconfdir}/yum.repos.d %{SOURCE0}

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/terra.repo

%changelog
* Tue Sep 10 2024 madonuko <mado@fyralabs.com> - 10-1
- Update for Terra EL 10
