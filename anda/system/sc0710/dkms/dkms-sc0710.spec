%global commit f1f5a722ccbdfc571450d9397e5e1b85da31f9d3
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260321
%global ver 0
%global debug_package %{nil}
%global modulename sc0710

Name:           dkms-%{modulename}
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Elgato 4K60 Pro MK.2 / 4K Pro capture card driver (DKMS)
License:        GPL-2.0-only
URL:            https://github.com/Nakildias/%{modulename}
Source0:        https://github.com/Nakildias/%{modulename}/archive/%{commit}.tar.gz#/%{modulename}-%{shortcommit}.tar.gz
Source1:        %{name}.conf
Source2:        no-weak-modules.conf
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Conflicts:      akmod-%{modulename}
Provides:       %{modulename}-kmod
BuildArch:      noarch
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>

%description
Elgato 4K60 Pro MK.2 / 4K Pro capture card driver (DKMS).

%prep
%autosetup -p1 -n %{modulename}-%{commit}

cp -f %{SOURCE1} dkms.conf

sed -i -e 's/__VERSION_STRING/%{version}/g' dkms.conf

%build

%install
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
cp -fr lib Makefile dkms.conf %{buildroot}%{_usrsrc}/%{modulename}-%{version}/

%if 0%{?fedora}
install -Dpm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/dkms/%{modulename}.conf
%endif

%post
dkms add -m %{modulename} -v %{version} -q --rpm_safe_upgrade || :
dkms build -m %{modulename} -v %{version} -q || :
dkms install -m %{modulename} -v %{version} -q --force || :

%preun
dkms remove -m %{modulename} -v %{version} -q --all --rpm_safe_upgrade || :

%files
%{_usrsrc}/%{modulename}-%{version}
%if 0%{?fedora}
%{_sysconfdir}/dkms/%{modulename}.conf
%endif

%changelog
* Fri Apr 03 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package
