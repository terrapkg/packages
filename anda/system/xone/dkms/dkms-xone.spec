%global commit 6b9d59aed71f6de543c481c33df4705d4a590a31
%global date 20241223
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 0.3
%global debug_package %{nil}
%global dkms_name xone

Name:           dkms-%{dkms_name}
Version:        0.3^20241223git.6b9d59a
Release:        1%?dist
Summary:        Linux kernel driver for Xbox One and Xbox Series X|S accessories
License:        GPL-2.0-or-later
URL:            https://github.com/dlundqvist/xone
Source0:        %{url}/archive/%{commit}.tar.gz#/%{dkms_name}-%{shortcommit}.tar.gz
Source1:        dkms-no-weak-modules.conf
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires:       %{dkms_name}-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
BuildArch:      noarch
Packager:       Gilver E. <rockgrub@disroot.org>

%description
Linux kernel driver for Xbox One and Xbox Series X|S accessories.

%prep
%autosetup -p1 -n %{dkms_name}-%{commit}

sed -i \
    -e 's|#VERSION#|%{version}|g' \
    -e 's|kernel/drivers/input/joystick|extra|g' \
    dkms.conf

find . -type f -name '*.c' -exec sed -i "s/#VERSION#/%{version}/" {} \;

%install
# Create empty tree:
mkdir -p %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/
cp -fr auth bus driver transport Kbuild dkms.conf %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/

%if 0%{?fedora}
# Do not enable weak modules support in Fedora (no kABI):
install -Dpm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/dkms/%{dkms_name}.conf
%endif

%post
dkms add -m %{dkms_name} -v %{version} -q --rpm_safe_upgrade || :
# Rebuild and make available for the currently running kernel:
dkms build -m %{dkms_name} -v %{version} -q || :
dkms install -m %{dkms_name} -v %{version} -q --force || :

%preun
# Remove all versions from DKMS registry:
dkms remove -m %{dkms_name} -v %{version} -q --all --rpm_safe_upgrade || :

%files
%{_usrsrc}/%{dkms_name}-%{version}
%if 0%{?fedora}
%{_sysconfdir}/dkms/%{dkms_name}.conf
%endif

%changelog
* Thu Feb 27 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
