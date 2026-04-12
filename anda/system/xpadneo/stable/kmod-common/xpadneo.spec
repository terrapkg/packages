%global appid io.github.atar_axis.xpadneo

Name:           xpadneo
Version:        0.10.2
Release:        1%{?dist}
%if 0%{?fedora} <= 45
Epoch:          1
%endif
Summary:        Advanced Linux Driver for Xbox One Wireless Gamepad common files
License:        GPL-2.0-only AND GPL-3.0-or-later
URL:            https://atar-axis.github.io/%{name}
Source0:        https://github.com/atar-axis/xpadneo/archive/refs/tags/v%{version}.tar.gz
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
%autosetup -p1 -n %{name}-%{version}
%{__sed} -nE '/^BUILT_MODULE_NAME/{s@^.+"(.+)"@\1@; s|-|_|g; p}' hid-%{name}/dkms.conf.in > %{name}.conf

%install
%{__make} install-all PREFIX="%{buildroot}" ETC_PREFIX="%{_prefix}/lib" VERSION="%{version}"

# Akmods modules
install -Dm644 %{name}.conf -t %{buildroot}%{_modulesloaddir}

%files
%license LICENSE.md
# Let RPM handle the docs
%doc %{_docdir}/%{name}/*
%{_modprobedir}/%{name}.conf
%{_udevrulesdir}/60-%{name}.rules
%{_udevrulesdir}/70-%{name}-disable-hidraw.rules
%{_metainfodir}/%{appid}.metainfo.xml

%files akmod-modules
%{_modulesloaddir}/%{name}.conf

%changelog
* Sat Apr 11 2026 Gilver E. <roachy@fyralabs.com> - 1:0.10.2-1
- Initial stable package
