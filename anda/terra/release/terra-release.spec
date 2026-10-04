%global dist %{nil}

Name:           terra-release
Version:        %{?fedora:%{fedora}}%{?rhel:%{rhel}}
Release:        2%{?dist}
Summary:        Release package for Terra

License:        GPL-3.0-or-later
URL:            https://terrapkg.com
Source0:        terra.repo
BuildArch:      noarch


Requires:       (epel-release-latest-%{version} or epel-release)
Requires:       terra-gpg-keys

Packager:       Terra Packaging Team <terra@fyralabs.com>

%description
Release package for Terra, containing the Terra repository configuration.

%prep

%build

%install
cp %{SOURCE5} LICENSE
%if 0%{?fedora} >= 45
install -Dpm644 -t %{buildroot}%{_datadir}/dnf5/repos.d %{SOURCE0}
install -Dpm644 -t %{buildroot}%{_datadir}/dnf5/repos.d %{SOURCE1}
install -Dpm644 -t %{buildroot}%{_datadir}/dnf5/repos.d %{SOURCE2}
install -Dpm644 -t %{buildroot}%{_datadir}/dnf5/repos.d %{SOURCE3}
install -Dpm644 -t %{buildroot}%{_datadir}/dnf5/repos.d %{SOURCE4}
%else
install -Dpm644 -t %{buildroot}%{_sysconfdir}/yum.repos.d %{SOURCE0}
install -Dpm644 -t %{buildroot}%{_sysconfdir}/yum.repos.d %{SOURCE1}
install -Dpm644 -t %{buildroot}%{_sysconfdir}/yum.repos.d %{SOURCE2}
install -Dpm644 -t %{buildroot}%{_sysconfdir}/yum.repos.d %{SOURCE3}
install -Dpm644 -t %{buildroot}%{_sysconfdir}/yum.repos.d %{SOURCE4}
%endif

%files
%license LICENSE
%if 0%{?fedora} >= 45
%{_datadir}/dnf5/repos.d/terra.repo
%else
%{_sysconfdir}/yum.repos.d/terra.repo
%endif

%changelog
* Tue Sep 10 2024 madonuko <mado@fyralabs.com> - 10-1
- Update for Terra EL 10
