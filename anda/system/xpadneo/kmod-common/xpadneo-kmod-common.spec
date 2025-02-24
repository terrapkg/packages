%global commit 8d20a23e38883f45c78f48c8574ac93945b4cb03
%global date 20241224
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 0.9.7

%global real_name xpadneo

Name:           %{real_name}-kmod-common
Version:        %{ver}^%{date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Advanced Linux Driver for Xbox One Wireless Gamepad common files
License:        GPLv3
URL:            https://atar-axis.github.io/%{real_name}
BuildArch:      noarch
Source0:        https://github.com/atar-axis/%{real_name}/archive/%{commit}.tar.gz#/%{real_name}-%{shortcommit}.tar.gz
Source1:        io.github.xpadneo.metainfo.xml

# UDev rule location (_udevrulesdir) and systemd macros:
BuildRequires:  systemd-rpm-macros

Requires:       %{real_name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{real_name}-kmod-common = %{?epoch:%{epoch}:}%{version}

%description
Advanced Linux Driver for Xbox One Wireless Gamepad common files.
 
%prep
%autosetup -p1 -n %{real_name}-%{commit}

%install
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_prefix}/lib/modprobe.d/

# Aliases:
install -p -m 0644 hid-%{real_name}/etc-modprobe.d/%{real_name}.conf %{buildroot}%{_prefix}/lib/modprobe.d/

# UDev rules:
install -p -m 644 hid-%{real_name}/etc-udev-rules.d/*.rules %{buildroot}%{_udevrulesdir}/

# Metadata
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/io.github.xpadneo.metainfo.xml

%files
%license LICENSE
%doc docs/*.md
%{_prefix}/lib/modprobe.d/%{real_name}.conf
%{_udevrulesdir}/60-%{real_name}.rules
%{_udevrulesdir}/70-%{real_name}-disable-hidraw.rules
%{_datadir}/metainfo/io.github.xpadneo.metainfo.xml

%changelog
%autochangelog
