%global commit cd256807c5f916735ae18749c43d5b0bd73240fa
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250411
%global ver 0.9.7

Name:           xpadneo
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        2%?dist
Summary:        Advanced Linux Driver for Xbox One Wireless Gamepad common files
License:        GPL-3.0
URL:            https://atar-axis.github.io/%{name}
Source0:        https://github.com/atar-axis/%{name}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Source1:        io.github.%{name}.metainfo.xml
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires:       (akmod-%{name} = %{?epoch:%{epoch}:}%{version} or dkms-%{name} = %{?epoch:%{epoch}:}%{version})
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
Obsoletes:      %{name}-kmod-common < %{?epoch:%{epoch}:}0.9.7^20241224git.8d20a23-4%{?dist}
BuildArch:      noarch
Packager:       Gilver E. <rockgrub@disroot.org>

%description
Advanced Linux Driver for Xbox One Wireless Gamepad common files.

%package       akmod-modules
Summary:       Modules for Akmods
Requires:      akmod-%{name}
BuildArch:     noarch

%description   akmod-modules
Akmods modules for the akmod-%{name} package.
 
%prep
%autosetup -p1 -n %{name}-%{commit}
/usr/bin/sed -nE '/^BUILT_MODULE_NAME/{s@^.+"(.+)"@\1@; s|-|_|g; p}' hid-%{name}/dkms.conf.in > %{name}.conf

%install
# Aliases:
install -Dpm644 hid-%{name}/etc-modprobe.d/%{name}.conf -t %{buildroot}%{_modprobedir}

# UDev rules:
install -Dpm644 hid-%{name}/etc-udev-rules.d/*.rules -t %{buildroot}%{_udevrulesdir}/

# Metadata
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/io.github.%{name}.metainfo.xml

# Akmods modules
install -Dm644 %{name}.conf -t %{buildroot}%{_modulesloaddir}

%files
%license LICENSE
%doc docs/*.md
%{_modprobedir}/%{name}.conf
%{_udevrulesdir}/60-%{name}.rules
%{_udevrulesdir}/70-%{name}-disable-hidraw.rules
%{_datadir}/metainfo/io.github.%{name}.metainfo.xml

%files akmod-modules
%{_modulesloaddir}/%{name}.conf

%changelog
* Fri Mar 07 2025 Gilver E. <rockgrub@disroot.org>
- Package refactoring
