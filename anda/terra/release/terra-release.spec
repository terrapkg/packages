Name:           terra-release
Version:        10
Release:        1
Summary:        Release package for Terra

License:        MIT
URL:            https://terra.fyralabs.com
Source0:        terra.repo
BuildArch:      noarch

%dnl We probably shouldn't do this in Rawhide!
%dnl Requires:       system-release(%{version})

%description
Release package for Terra, containing the Terra repository configuration.

%prep

%build

%install
install -D -p -m 0644 -t %{buildroot}%{_sysconfdir}/yum.repos.d %{SOURCE0}

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/terra.repo

%changelog
* Wed Sep 10 2024 madonuko <mado@fyralabs.com> - 10-1
- Update for Terra EL 10
