Name:           terra-release
Version:        39
Release:        1
Summary:        Release package for Terra

License:        MIT
URL:            https://terra.fyralabs.com
Source0:        terra.repo
BuildArch:      noarch

Requires:       system-release(%{version})

%description
Release package for Terra, containing the Terra repository configuration.

%prep

%build

%install
install -D -p -m 0644 -t %{buildroot}%{_sysconfdir}/yum.repos.d %{SOURCE0}

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/terra.repo

%changelog
* Wed Sug 16 2023 Lleyton Gray <lleyton@fyralabs.com> - 39-1
- Update for Terra 39

* Sat May 6 2023 Lleyton Gray <lleyton@fyralabs.com> - 38-1
- Initial package
