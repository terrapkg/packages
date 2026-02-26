%global dist %{nil}

Name:           terra-release
Version:        %{?fedora:%{fedora}}%{?rhel:%{rhel}}
Release:        1%?dist
Summary:        Release package for Terra

License:        MIT
URL:            https://terra.fyralabs.com
Source0:        terra.repo
Source1:        terra-extras.repo
Source2:        terra-nvidia.repo
Source3:        terra-mesa.repo
Source4:        terra-multimedia.repo
BuildArch:      noarch

%dnl We probably shouldn't do this in Rawhide!
%dnl Requires:       system-release(%{version})

Requires:       terra-gpg-keys

%description
Release package for Terra, containing the Terra repository configuration.

%package extras
Summary: Release package for Terra Extras
Obsoletes: terra-release-extra < 42-3
Provides: terra-release-extra = %version-%release

Requires:       terra-gpg-keys

%description extras
Release package for Terra Extras, which is a repository with packages that might cause
conflict with Fedora.

%package nvidia
Summary: Release package for the nvidia subrepo of Terra Extras

Requires:       terra-gpg-keys

%description nvidia
Release package for the Terra Extras nvidia subrepo, which provides nvidia drivers that might cause a conflict with Fedora.

%package mesa
Summary: Release package for the mesa subrepo of Terra Extras

Requires:       terra-gpg-keys

%description mesa
Release package for the Terra Extras mesa subrepo, which provides a patched and updated version of mesa that might cause a conflict with Fedora.

%package multimedia
Summary: Release package for the multimedia subrepo of Terra Extras

Requires:       terra-gpg-keys

%description multimedia
Release package for the Terra Extras multimedia subrepo, which provides codecs that might cause a conflict with Fedora.

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

%files nvidia
%config(noreplace) %{_sysconfdir}/yum.repos.d/terra-nvidia.repo

%files mesa
%config(noreplace) %{_sysconfdir}/yum.repos.d/terra-mesa.repo

%files multimedia
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
