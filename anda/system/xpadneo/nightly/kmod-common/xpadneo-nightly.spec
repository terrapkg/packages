%global commit 45f39820edc2c3fc5605bfe4daea471263678ed1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260411
%global ver 0.10.2
%global appid io.github.atar_axis.xpadneo

Name:           xpadneo-nightly
Version:        %{ver}^%{commitdate}git%{shortcommit}
Release:        3%{?dist}
Summary:        Advanced Linux Driver for Xbox One Wireless Gamepad common files
License:        GPL-2.0-only AND GPL-3.0-or-later
URL:            https://atar-axis.github.io/xpadneo
Source0:        https://github.com/atar-axis/xpadneo/archive/%{commit}.tar.gz#/xpadneo-%{shortcommit}.tar.gz
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires:       %{name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
Obsoletes:      %{name}-kmod-common < %{?epoch:%{epoch}:}0.9.7^20241224git.8d20a23-5%{?dist}
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

%description
Advanced Linux Driver for Xbox One Wireless Gamepad common files.

%package       akmod-modules
Summary:       Modules for Akmods
Requires:      %{name}-kmod = %{?epoch:%{epoch}:}%{version}
BuildArch:     noarch

%description   akmod-modules
Akmods modules for the akmod-%{name} package.
 
%prep
%autosetup -p1 -n xpadneo-%{commit}
/usr/bin/sed -nE '/^BUILT_MODULE_NAME/{s@^.+"(.+)"@\1@; s|-|_|g; p}' hid-xpadneo/dkms.conf.in > xpadneo.conf

%install
%{__make} install-all PREFIX="%{buildroot}" ETC_PREFIX="%{_prefix}/lib" VERSION="%{version}"

# Akmods modules
install -Dm644 xpadneo.conf -t %{buildroot}%{_modulesloaddir}

%files
%license LICENSE.md
# Let RPM handle the docs
%doc %{_docdir}/xpadneo/*
%{_modprobedir}/xpadneo.conf
%{_udevrulesdir}/60-xpadneo.rules
%{_udevrulesdir}/70-xpadneo-disable-hidraw.rules
%{_metainfodir}/%{appid}.metainfo.xml

%files akmod-modules
%{_modulesloaddir}/xpadneo.conf

%changelog
* Sat Apr 11 2026 Gilver E. <roachy@fyralabs.com> - 0.10.2^45f3982git20260411
- Separated nightly builds into their own packages
* Fri Mar 07 2025 Gilver E. <rockgrub@disroot.org>
- Package refactoring
