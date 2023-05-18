Name:           terra-mock-configs
Version:        4
Release:        1%{?dist}
Summary:        Mock configs for Terra repos

License:        MIT
URL:            http://terra.fyralabs.com
Source0:        terra.tpl
Source1:        terra-38-x86_64.cfg
Source2:        terra-38-aarch64.cfg

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

# For legacy compatibility, remove in next Terra release
ln -s %{_sysconfdir}/mock/templates/terra.tpl %{buildroot}%{_sysconfdir}/mock/templates/anda.tpl
ln -s %{_sysconfdir}/mock/terra-38-x86_64.cfg %{buildroot}%{_sysconfdir}/mock/anda-38-x86_64.cfg
ln -s %{_sysconfdir}/mock/terra-38-aarch64.cfg %{buildroot}%{_sysconfdir}/mock/anda-38-aarch64.cfg

%files
%{_sysconfdir}/mock/templates/terra.tpl
%{_sysconfdir}/mock/terra-38-x86_64.cfg
%{_sysconfdir}/mock/terra-38-aarch64.cfg
%{_sysconfdir}/mock/templates/anda.tpl
%{_sysconfdir}/mock/anda-38-x86_64.cfg
%{_sysconfdir}/mock/anda-38-aarch64.cfg

%changelog
* Thu May 18 2023 Lleyton Gray <lleyton@fyralabs.com>
- Rename to terra-mock-configs and rename files to terra
* Mon Oct 03 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Intial Release
