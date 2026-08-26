Name:           cachyos-ananicy-rules
Version:        1.1.48
Release:        1%{?dist}
Summary:        List of rules used to assign specific nice values to specific processes

License:        GPL-3.0-or-later
URL:            https://github.com/CachyOS/ananicy-rules
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Requires:       ananicy-cpp
Packager:       Owen Zimmerman <owen@fyralabs.com>
BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -C

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/ananicy.d
cp 00-default %{buildroot}%{_sysconfdir}/ananicy.d/ -r
cp 00-cgroups.cgroups %{buildroot}%{_sysconfdir}/ananicy.d/ -r
cp 00-types.types %{buildroot}%{_sysconfdir}/ananicy.d/ -r
cp ananicy.conf %{buildroot}%{_sysconfdir}/ananicy.d/ -r

%files
%defattr(-,root,root,-)
%{_sysconfdir}/ananicy.d/*

%changelog
* Thu Jul 30 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
