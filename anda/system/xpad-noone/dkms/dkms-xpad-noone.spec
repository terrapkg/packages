%global commit 6970c40930bedd8b58d0764894e0d5f04813b7c5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20240109
%global ver 1.0
%global modulename xpad-noone
%global _description %{expand:
This is the original upstream xpad driver from the Linux kernel with support for XBox One controllers removed. If you are running the xone driver you may have to replace the xpad kernel module with this one to retain the functionality of XBox and XBox 360 controllers.}

Name:          dkms-%{modulename}
Version:       %{ver}^%{commitdate}git.%{shortcommit}
Release:       1%?dist
License:       GPL-2.0-or-later
Summary:       xpad driver with support for XBox One controllers removed
URL:           https://github.com/medusalix/xpad-noone
Source0:       %{url}/archive/%{commit}/%{modulename}-%{commit}.tar.gz#/%{modulename}-%{shortcommit}.tar.gz
Source1:       no-weak-modules.conf
# Extra support for controllers that register as XBox 360 controllers
Patch0:        0000.patch
Requires:      %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:      dkms
Conflicts:     akmod-%{modulename}
BuildArch:     noarch
Packager:      Gilver E. <rockgrub@disroot.org>

%description %_description

%prep
%autosetup -n %{modulename}-%{commit}

%build

%install
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
rm -rf LICENSE README.md
cp -fr ./* %{buildroot}%{_usrsrc}/%{modulename}-%{version}/

%if 0%{?fedora}
install -Dpm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/dkms/%{modulename}.conf
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
* Fri Mar 07 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
