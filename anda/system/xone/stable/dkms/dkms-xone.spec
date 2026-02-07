%global debug_package %{nil}
%global modulename xone

Name:           dkms-%{modulename}
Version:        0.5.5
Release:        1%?dist
%if 0%{?fedora} <= 43 || 0%{?rhel} <= 10
Epoch:          2
%endif
Summary:        Linux kernel driver for Xbox One and Xbox Series X|S accessories
License:        GPL-2.0-or-later
URL:            https://github.com/dlundqvist/xone
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        no-weak-modules.conf
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Conflicts:      akmod-%{modulename}
Conflicts:      %{modulename}-nightly-kmod
Provides:       %{modulename}-kmod
%if 0%{?fedora} <= 43 || 0%{?rhel} <= 10
Obsoletes:      %{name} < %{?epoch:%{epoch}:}0.3.4
%endif
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

%description
Linux kernel driver for Xbox One and Xbox Series X|S accessories.

%prep
%autosetup -p1 -n %{modulename}-%{version}

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
