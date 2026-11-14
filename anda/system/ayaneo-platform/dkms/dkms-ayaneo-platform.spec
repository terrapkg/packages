%global debug_package %{nil}
%global modulename ayaneo-platform

Name:           dkms-%{modulename}
Version:        0.3.5
Release:        1%{?dist}
Summary:        Platform driver for AYANEO x86 handhelds
License:        GPL-2.0-or-later
URL:            https://github.com/ShadowBlip/%{modulename}
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      x86_64
BuildRequires:  sed

Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Requires:       gcc
Requires:       make
Requires:       kernel-devel
Requires(post): dkms
Requires(preun): dkms
Conflicts:      akmod-%{modulename}
Provides:       %{modulename}-kmod = %{?epoch:%{epoch}:}%{version}

%description
Platform driver for AYANEO x86 handhelds, exposing RGB LED control and
bypass charging through sysfs. DKMS rebuilds the module on kernel upgrades.

%prep
%autosetup -n %{modulename}-%{version}
sed -i -e 's/^PACKAGE_VERSION=.*/PACKAGE_VERSION="%{version}"/' \
    -e 's|^DEST_MODULE_LOCATION\[0\]=.*|DEST_MODULE_LOCATION[0]="/kernel/drivers/platform/x86"|' \
    dkms.conf
echo "%{version}" > VERSION

%install
install -d %{buildroot}%{_usrsrc}/%{modulename}-%{version}
install -m 0644 %{modulename}.c Makefile dkms.conf VERSION \
    %{buildroot}%{_usrsrc}/%{modulename}-%{version}/

%post
dkms add -m %{modulename} -v %{version} --rpm_safe_upgrade || exit $?
dkms build -m %{modulename} -v %{version} || exit $?
dkms install -m %{modulename} -v %{version} --force

%preun
dkms remove -m %{modulename} -v %{version} --all --rpm_safe_upgrade

%files
%license LICENSE
%doc README.md
%{_usrsrc}/%{modulename}-%{version}/

%changelog
* Thu Oct 22 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 0.3.5-1
- Initial package
