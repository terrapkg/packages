%global commit f7ecb30c65ee5f7870e921bc0a2354df8e1e8100
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250225
%global ver 1.0
%global debug_package %{nil}
%global modulename t150-driver

Name:           dkms-%{modulename}
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Thrustmaster T150 steering wheel kernel module (DKMS)
License:        GPL-2.0-only
URL:            https://github.com/scarburato/t150_driver
Source0:        %{url}/archive/%{commit}.tar.gz#/t150_driver-%{shortcommit}.tar.gz
Source1:        %{name}.conf
Source2:        no-weak-modules.conf
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Conflicts:      akmod-%{modulename}
BuildArch:      noarch

%description
Linux driver for Thrustmaster T150 Steering Wheel USB.

%prep
%autosetup -p1 -n t150_driver-%{commit}

cp -f %{SOURCE1} dkms.conf
sed -i -e 's/__VERSION_STRING/%{version}/g' dkms.conf

%build

%install
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
cp -fr hid-t150 dkms_make.mak dkms.conf %{buildroot}%{_usrsrc}/%{modulename}-%{version}/

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
* Thu Apr 02 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package
