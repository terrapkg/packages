Name:           terra-mock-configs
Version:        11
Release:        1%{?dist}
Summary:        Mock configs for Terra repos

License:        MIT
URL:            https://terra.fyralabs.com
Source0:        terra.tpl
Source3:        terra-39-x86_64.cfg
Source4:        terra-39-aarch64.cfg
Source5:        terra-40-x86_64.cfg
Source6:        terra-40-aarch64.cfg
Source7:        terra-40-i386.cfg
Source8:        terra-39-i386.cfg
Source9:        terra-rawhide-x86_64.cfg
Source10:       terra-rawhide-aarch64.cfg
Source11:       terra-rawhide-i386.cfg


BuildRequires:  mock-core-configs
Requires:       mock-core-configs
BuildArch:      noarch

Provides: anda-mock-configs = %{version}-%{release}
Obsoletes: anda-mock-configs < 3-2%{?dist}

%description
%{summary}

%prep

%build

%install
mkdir -p %{buildroot}%{_sysusersdir}
mkdir -p %{buildroot}%{_sysconfdir}/mock/templates

cp -v %{SOURCE0} %{buildroot}%{_sysconfdir}/mock/templates/
cp -v %{SOURCE3} %{buildroot}%{_sysconfdir}/mock/
cp -v %{SOURCE4} %{buildroot}%{_sysconfdir}/mock/
cp -v %{SOURCE5} %{buildroot}%{_sysconfdir}/mock/
cp -v %{SOURCE6} %{buildroot}%{_sysconfdir}/mock/
cp -v %{SOURCE7} %{buildroot}%{_sysconfdir}/mock/
cp -v %{SOURCE8} %{buildroot}%{_sysconfdir}/mock/
cp -v %{SOURCE9} %{buildroot}%{_sysconfdir}/mock/
cp -v %{SOURCE10} %{buildroot}%{_sysconfdir}/mock/
cp -v %{SOURCE11} %{buildroot}%{_sysconfdir}/mock/


%files
%config %{_sysconfdir}/mock/templates/terra.tpl
%config %{_sysconfdir}/mock/terra-*-x86_64.cfg
%config %{_sysconfdir}/mock/terra-*-aarch64.cfg
%config %{_sysconfdir}/mock/terra-*-i386.cfg


%changelog
* Wed Jul 18 2024 Cappy Ishihara <cappy@fyralabs.com> - 11-1
- Include multilib mock files for x86-based systems (backwards compatibility)

* Wed Jul 10 2024 madonuko <mado@fyralabs.com> - 10-1
- Include mock files for Terra 40
- Remove mock files for Terra 38

* Mon Jan 08 2024 Lleyton Gray <lleyton@fyralabs.com> - 7-1
- Bump ccache max size to 10G

* Wed Aug 16 2023 madonuko <mado@fyralabs.com> - 6-1
- Remove RPM Fusion

* Wed Aug 16 2023 Lleyton Gray <lleyton@fyralabs.com> - 5-1
- Update for Terra 39

* Thu May 18 2023 Lleyton Gray <lleyton@fyralabs.com>
- Rename to terra-mock-configs and rename files to terra

* Mon Oct 03 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Intial Release
