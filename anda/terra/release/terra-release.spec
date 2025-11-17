Name:           terra-release
Version:        %{fedora}
Release:        1
Summary:        Release package for Terra

License:        MIT
URL:            https://terra.fyralabs.com
Source0:        terra.repo
Source1:        terra-extras.repo
Source2:        terra-nvidia.repo
Source3:        terra-mesa.repo
Source4:        terra-multimedia.repo
BuildArch:      noarch

Requires:       system-release(%{version})

%description
Release package for Terra, containing the Terra repository configuration.

%package extras
Summary: Release package for Terra Extra
Obsoletes: terra-release-extra < 42-3
Provides: terra-release-extra = %version-%release

%description extras
Release package for Terra Extra, which is a repository with packages that might cause
conflict with Fedora.

%prep

%build

%install
install -D -p -m 0644 -t %{buildroot}%{_sysconfdir}/yum.repos.d %{SOURCE0}
install -Dpm644 -t %buildroot%_sysconfdir/yum.repos.d %SOURCE1
install -Dpm644 -t %buildroot%_sysconfdir/yum.repos.d %SOURCE2
install -Dpm644 -t %buildroot%_sysconfdir/yum.repos.d %SOURCE3
install -Dpm644 -t %buildroot%_sysconfdir/yum.repos.d %SOURCE4

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/terra.repo

%files extras
%config(noreplace) %{_sysconfdir}/yum.repos.d/terra-extras.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/terra-nvidia.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/terra-mesa.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/terra-multimedia.repo

%changelog
* Thu Nov 13 2025 madonuko <mado@fyralabs.com> - 44-1
- Add terra-multimedia

* Sun Jan 12 2025 Cappy Ishihara <cappy@cappuchino.xyz> - 42-4
- Add NVIDIA and Mesa repository streams

* Fri Oct 25 2024 madonuko <mado@fyralabs.com> - 42-2
- Add terra-release-extra

* Thu Nov 16 2023 Lleyton Gray <lleyton@fyralabs.com> - 41-1
- Update for Terra 41 (in this case rawhide)

* Thu Nov 16 2023 Lleyton Gray <lleyton@fyralabs.com> - 40-1
- Update for Terra 40 (in this case rawhide)

* Thu Nov 16 2023 Lleyton Gray <lleyton@fyralabs.com> - 39-2
- Add source repository

* Wed Aug 16 2023 Lleyton Gray <lleyton@fyralabs.com> - 39-1
- Update for Terra 39

* Sat May 6 2023 Lleyton Gray <lleyton@fyralabs.com> - 38-1
- Initial package
