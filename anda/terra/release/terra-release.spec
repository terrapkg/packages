%global dist %{nil}

Name:           terra-release
Version:        %{?fedora:%{fedora}}%{?rhel:%{rhel}}
Release:        5%{?dist}
Summary:        Release package for Terra

License:        GPL-3.0-or-later
URL:            https://terrapkg.com
Source0:        terra.repo
Source1:        terra-extras.repo
Source2:        terra-nvidia.repo
Source3:        terra-mesa.repo
Source4:        terra-multimedia.repo
Source5:        LICENSE
BuildArch:      noarch

Requires:       terra-gpg-keys

Packager:       Terra Packaging Team <terra@fyralabs.com>

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

%files extras
%license LICENSE
%if 0%{?fedora} >= 45
%{_datadir}/dnf5/repos.d/terra-extras.repo
%else
%{_sysconfdir}/yum.repos.d/terra-extras.repo
%endif

%files nvidia
%license LICENSE
%if 0%{?fedora} >= 45
%{_datadir}/dnf5/repos.d/terra-nvidia.repo
%else
%{_sysconfdir}/yum.repos.d/terra-nvidia.repo
%endif

%files mesa
%license LICENSE
%if 0%{?fedora} >= 45
%{_datadir}/dnf5/repos.d/terra-mesa.repo
%else
%{_sysconfdir}/yum.repos.d/terra-mesa.repo
%endif

%files multimedia
%license LICENSE
%if 0%{?fedora} >= 45
%{_datadir}/dnf5/repos.d/terra-multimedia.repo
%else
%{_sysconfdir}/yum.repos.d/terra-multimedia.repo
%endif

%changelog
* Sun Oct 04 2026 Owen Zimmerman <owen@fyralabs.com> - 45-5
- Drop %%config(noreplace)
- Add repo file comment

* Wed Sep 30 2026 Owen Zimmerman <owen@fyralabs.com> - 45-5
- Update to new repo file directory for F45+
- Install license file
- Unify marco formatting

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
