Name:           terra-mock-configs
Version:        1.2.0
Release:        1%?dist
Epoch:          1
Summary:        Mock configs for Terra repos

License:        MIT
URL:            https://github.com/terrapkg/mock-configs
Source0:        %url/archive/refs/tags/v%version.tar.gz

BuildRequires:  mock-core-configs
Requires:       mock-core-configs
BuildArch:      noarch

Provides: anda-mock-configs = %{epoch}:%{version}-%{release}
Obsoletes: anda-mock-configs < 3-2%{?dist}

%description
%{summary}

%prep
%autosetup -n mock-configs-%version

%build

%install
mkdir -p %{buildroot}%{_sysusersdir}
mkdir -p %{buildroot}%{_sysconfdir}/mock/templates

cp -v terra.tpl %{buildroot}%{_sysconfdir}/mock/templates/
cp -v *.cfg %{buildroot}%{_sysconfdir}/mock/

%files
%config %{_sysconfdir}/mock/templates/terra.tpl
%config %{_sysconfdir}/mock/terra-*-x86_64.cfg
%config %{_sysconfdir}/mock/terra-*-aarch64.cfg
%config %{_sysconfdir}/mock/terra-*-i386.cfg

%changelog
* Fri Jul 26 2024 madonuko <mado@fyralabs.com> - 1:1.1.0-1
- Include mock files for Terra 41

* Mon Jul 22 2024 Lleyton Gray <lleyton@fyralabs.com> - 1:1.0.0-1
- Migrate to pulling configs from an external repository

* Thu Jul 18 2024 Cappy Ishihara <cappy@fyralabs.com> - 11-1
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
