%global commit 8187920ed261c7024826f8204cc7bea45153a3da
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260310
%global ver 0.83

%global debug_package %{nil}
%global modulename hid-tmff2

Name:           dkms-%{modulename}
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        4%{?dist}
Summary:        Thrustmaster Force Feedback kernel module (DKMS)
License:        GPL-2.0-only
URL:            https://github.com/Kimplul/%{modulename}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{modulename}-%{shortcommit}.tar.gz
Source1:        %{name}.conf
Source2:        no-weak-modules.conf
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Conflicts:      akmod-%{modulename}
Provides:       %{modulename}-kmod
BuildArch:      noarch

%description
Linux kernel module for Thrustmaster T300RS, T248 and (experimental) TX, T128,
T598, T-GT II and TS-XW wheels.

%prep
%autosetup -p1 -n %{modulename}-%{commit}

# Stub out the hid-tminit submodule (superseded by in-kernel hid-thrustmaster)
mkdir -p deps/hid-tminit
printf 'all:\ninstall:\nclean:\n' > deps/hid-tminit/Makefile

cp -f %{SOURCE1} dkms/dkms.conf
sed -i -e 's/__VERSION_STRING/%{version}/g' dkms/dkms.conf

%build

%install
# Create empty tree:
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
cp -fr Kbuild Makefile src deps %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
install -Dpm644 dkms/dkms.conf %{buildroot}%{_usrsrc}/%{modulename}-%{version}/dkms.conf

%if 0%{?fedora}
# Do not enable weak modules support in Fedora (no kABI):
install -Dpm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/dkms/%{modulename}.conf
%endif

%post
dkms add -m %{modulename} -v %{version} -q --rpm_safe_upgrade || :
# Rebuild and make available for the currently running kernel:
dkms build -m %{modulename} -v %{version} -q || :
dkms install -m %{modulename} -v %{version} -q --force || :

%preun
# Remove all versions from DKMS registry:
dkms remove -m %{modulename} -v %{version} -q --all --rpm_safe_upgrade || :

%files
%{_usrsrc}/%{modulename}-%{version}
%if 0%{?fedora}
%{_sysconfdir}/dkms/%{modulename}.conf
%endif

%changelog
* Thu Apr 02 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package
