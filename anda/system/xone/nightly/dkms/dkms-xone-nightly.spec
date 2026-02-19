%global commit 725a46c45f06475bf7631d9ca1852f9778df128f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260216
%global ver 0.5.5
%global debug_package %{nil}
%global modulename xone

Name:           dkms-%{modulename}-nightly
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        1%?dist
%if 0%{?fedora} <= 43 || 0%{?rhel} <= 10
Epoch:          1
%endif
Summary:        Linux kernel driver for Xbox One and Xbox Series X|S accessories
License:        GPL-2.0-or-later
URL:            https://github.com/dlundqvist/xone
Source0:        %{url}/archive/%{commit}.tar.gz#/%{modulename}-%{shortcommit}.tar.gz
Source1:        no-weak-modules.conf
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires:       %{modulename}-nightly = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Conflicts:      akmod-%{modulename}-nightly
Conflicts:      %{modulename}-kmod
Provides:       %{modulename}-nightly-kmod = %{?epoch:%{epoch}:}%{version}
%if 0%{?fedora} <= 43 || 0%{?rhel} <= 10
Obsoletes:      dkms-%{modulename} < %{?epoch:%{epoch}:}3.0^20250419git.c682b0c
%endif
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

%description
Linux kernel driver for Xbox One and Xbox Series X|S accessories.

%prep
%autosetup -p1 -n %{modulename}-%{commit}

sed -i \
    -e 's|#VERSION#|%{version}|g' \
    -e 's|kernel/drivers/input/joystick|extra|g' \
    dkms.conf

find . -type f -name '*.c' -exec sed -i "s/#VERSION#/%{version}/" {} \;

%install
# Create empty tree:
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
cp -fr auth bus driver transport Kbuild dkms.conf %{buildroot}%{_usrsrc}/%{modulename}-%{version}/

%if 0%{?fedora}
# Do not enable weak modules support in Fedora (no kABI):
install -Dpm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/dkms/%{modulename}.conf
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
* Thu Feb 27 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
