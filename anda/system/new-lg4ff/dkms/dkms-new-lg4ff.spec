%global commit 2092db19f7b40854e0427a1b2e39eda9f8d0c3cd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250528
%global ver 0.5.0
%global debug_package %{nil}
%global modulename new-lg4ff

Name:           dkms-%{modulename}
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        2%{?dist}
Summary:        Logitech force feedback kernel module (DKMS)
License:        GPL-2.0-only
URL:            https://github.com/berarma/%{modulename}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{modulename}-%{shortcommit}.tar.gz
Source1:        %{name}.conf
Source2:        no-weak-modules.conf
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Conflicts:      akmod-%{modulename}
Provides:       %{modulename}-kmod
BuildArch:      noarch

%description
Experimental Logitech force feedback module for Linux.

%prep
%autosetup -p1 -n %{modulename}-%{commit}

cp -f %{SOURCE1} dkms.conf
sed -i -e 's/__VERSION_STRING/%{version}/g' dkms.conf

%build

%install
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
cp -fr Kbuild Makefile *.c *.h usbhid dkms.conf %{buildroot}%{_usrsrc}/%{modulename}-%{version}/

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
