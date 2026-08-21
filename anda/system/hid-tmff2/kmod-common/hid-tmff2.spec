%global commit c6157ea211dbebbac5ac6abad1aba74c86cde759
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260819
%global ver 0.83

Name:           hid-tmff2
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Thrustmaster Force Feedback driver common files
License:        GPL-2.0-only
URL:            https://github.com/Kimplul/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Requires:       %{name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
BuildArch:      noarch

%description
Linux kernel module for Thrustmaster T300RS, T248 and (experimental) TX, T128,
T598, T-GT II and TS-XW wheels. This package contains common files shared
between the akmod and dkms variants.

%package       akmod-modules
Summary:       Modules for Akmods
Requires:      %{name}-kmod = %{?epoch:%{epoch}:}%{version}
BuildArch:     noarch

%description   akmod-modules
Akmods modules for the akmod-%{name} package.

%prep
%autosetup -p1 -n %{name}-%{commit}

# Extract module names from Kbuild for modules-load.d
echo hid-tmff-new > %{name}.conf

%install
# Akmods modules
install -Dm644 %{name}.conf -t %{buildroot}%{_modulesloaddir}

%files
%license LICENSE
%doc README.md
%{_udevrulesdir}/99-thrustmaster.rules

%files akmod-modules
%{_modulesloaddir}/%{name}.conf

%changelog
* Thu Apr 02 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package
