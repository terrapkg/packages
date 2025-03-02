%global commit 8d20a23e38883f45c78f48c8574ac93945b4cb03
%global date 20241224
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 0.9.7
%global real_name xpadneo

Name:           %{real_name}-kmod-common
Version:        %{ver}^%{date}git.%{shortcommit}
Release:        2%{?dist}
Summary:        Advanced Linux Driver for Xbox One Wireless Gamepad common files
License:        GPL-3.0
URL:            https://atar-axis.github.io/%{real_name}
Source0:        https://github.com/atar-axis/%{real_name}/archive/%{commit}.tar.gz#/%{real_name}-%{shortcommit}.tar.gz
Source1:        io.github.xpadneo.metainfo.xml
BuildRequires:  systemd-rpm-macros
Provides:       %{real_name}-kmod-common = %{?epoch:%{epoch}:}%{version}
Provides:       %{real_name} = %{version}-%{release}
BuildArch:      noarch
Packager:       ShinyGil <rockgrub@disroot.org>

%description
Advanced Linux Driver for Xbox One Wireless Gamepad common files.
 
%prep
%autosetup -p1 -n %{real_name}-%{commit}

%install
# Aliases:
install -Dpm644 hid-%{real_name}/etc-modprobe.d/%{real_name}.conf -t %{buildroot}%{_modprobedir}

# UDev rules:
install -Dpm644 hid-%{real_name}/etc-udev-rules.d/*.rules -t %{buildroot}%{_udevrulesdir}/

# Metadata
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/io.github.xpadneo.metainfo.xml

%files
%license LICENSE
%doc docs/*.md
%{_modprobedir}/%{real_name}.conf
%{_udevrulesdir}/60-%{real_name}.rules
%{_udevrulesdir}/70-%{real_name}-disable-hidraw.rules
%{_datadir}/metainfo/io.github.xpadneo.metainfo.xml

%changelog
%autochangelog
