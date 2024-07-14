Name:           terra-mock-configs
Version:        9
Release:        1%{?dist}
Summary:        Mock configs for Terra repos

License:        MIT
URL:            https://terra.fyralabs.com
Source0:        terra.tpl
Source1:        terra-38-x86_64.cfg
Source2:        terra-38-aarch64.cfg
Source3:        terra-39-x86_64.cfg
Source4:        terra-39-aarch64.cfg
Source5:        terra-rawhide-x86_64.cfg
Source6:        terra-rawhide-aarch64.cfg

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
cp -v %{SOURCE1} %{buildroot}%{_sysconfdir}/mock/
cp -v %{SOURCE2} %{buildroot}%{_sysconfdir}/mock/
cp -v %{SOURCE3} %{buildroot}%{_sysconfdir}/mock/
cp -v %{SOURCE4} %{buildroot}%{_sysconfdir}/mock/
cp -v %{SOURCE5} %{buildroot}%{_sysconfdir}/mock/
cp -v %{SOURCE6} %{buildroot}%{_sysconfdir}/mock/

# For legacy compatibility, only while Terra 38 is still alive
ln -s %{_sysconfdir}/mock/templates/terra.tpl %{buildroot}%{_sysconfdir}/mock/templates/anda.tpl
ln -s %{_sysconfdir}/mock/terra-38-x86_64.cfg %{buildroot}%{_sysconfdir}/mock/anda-38-x86_64.cfg
ln -s %{_sysconfdir}/mock/terra-38-aarch64.cfg %{buildroot}%{_sysconfdir}/mock/anda-38-aarch64.cfg

%files
%config %{_sysconfdir}/mock/templates/terra.tpl
%config %{_sysconfdir}/mock/terra-rawhide-x86_64.cfg
%config %{_sysconfdir}/mock/terra-rawhide-aarch64.cfg
%config %{_sysconfdir}/mock/terra-39-x86_64.cfg
%config %{_sysconfdir}/mock/terra-39-aarch64.cfg
%config %{_sysconfdir}/mock/terra-38-x86_64.cfg
%config %{_sysconfdir}/mock/terra-38-aarch64.cfg
%config %{_sysconfdir}/mock/templates/anda.tpl
%config %{_sysconfdir}/mock/anda-38-x86_64.cfg
%config %{_sysconfdir}/mock/anda-38-aarch64.cfg

%changelog
* Mon Jan 15 2024 madonuko <mado@fyralabs.com> - 9.1
- Update for Terra rawhide

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
