%global appid io.github.xpadneo

Name:           xpadneo
Version:        0.10
Release:        1%{?dist}
%if 0%{?fedora} <= 45
Epoch:          1
%endif
Summary:        Advanced Linux Driver for Xbox One Wireless Gamepad common files
License:        GPL-2.0-only AND GPL-3.0-or-later
URL:            https://atar-axis.github.io/%{name}
Source0:        https://github.com/atar-axis/%{name}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires:       (akmod-%{name} = %{?epoch:%{epoch}:}%{version} or dkms-%{name} = %{?epoch:%{epoch}:}%{version})
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
Obsoletes:      %{name}-kmod-common < %{?epoch:%{epoch}:}0.9.7^20241224git.8d20a23-5%{?dist}
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

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
%{__sed} -nE '/^BUILT_MODULE_NAME/{s@^.+"(.+)"@\1@; s|-|_|g; p}' hid-%{name}/dkms.conf.in > %{name}.conf

%install
# Aliases:
install -Dpm644 hid-%{name}/etc-modprobe.d/%{name}.conf -t %{buildroot}%{_modprobedir}

# UDev rules:
install -Dpm644 hid-%{name}/etc-udev-rules.d/*.rules -t %{buildroot}%{_udevrulesdir}/

# Metadata
install -Dm644 xpadneo.metainfo.xml %{buildroot}%{_datadir}/metainfo/%{appid}.metainfo.xml

# Akmods modules
install -Dm644 %{name}.conf -t %{buildroot}%{_modulesloaddir}

%files
%license LICENSE
%doc docs/*.md
%{_modprobedir}/%{name}.conf
%{_udevrulesdir}/60-%{name}.rules
%{_udevrulesdir}/70-%{name}-disable-hidraw.rules
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files akmod-modules
%{_modulesloaddir}/%{name}.conf

%changelog
* Sun Mar 15 2026 Gilver E. <roachy@fyralabs.com> - 1:0.10-1
- Initial stable package
