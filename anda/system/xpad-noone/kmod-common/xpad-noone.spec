%global commit 6970c40930bedd8b58d0764894e0d5f04813b7c5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20240109
%global ver 1.0
%global _description %{expand:
This is the original upstream xpad driver from the Linux kernel with support for XBox One controllers removed. If you are running the xone driver you may have to replace the xpad kernel module with this one to retain the functionality of XBox and XBox 360 controllers.}

Name:          xpad-noone
Version:       %{ver}^%{commitdate}git.%{shortcommit}
Release:       1%{?dist}
License:       GPL-2.0-or-later
Summary:       xpad driver with support for XBox One controllers removed
URL:           https://github.com/medusalix/xpad-noone
Source0:       %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
BuildRequires: sed
BuildRequires: systemd-rpm-macros
Provides:      %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:      (akmod-%{name} = %{?epoch:%{epoch}:}%{version} or dkms-%{name} = %{?epoch:%{epoch}:}%{version})
Conflicts:     xow <= 0.5
Obsoletes:     xow <= 0.5
BuildArch:     noarch
Packager:      Gilver E. <rockgrub@disroot.org>

%description %_description

%package      akmod-modules
Summary:      Modules for Akmods
Requires:     akmod-%{name}
BuildArch:    noarch

%description   akmod-modules
Akmods modules for the akmod-%{name} package.

%prep
%autosetup -n %{name}-%{commit}
/usr/bin/sed -nE '/^BUILT_MODULE_NAME/{s@^.+"(.+)"@\1@; s|-|_|g; p}' dkms.conf > %{name}.conf

%build

%install
install -Dm644 %{name}.conf -t %{buildroot}%{_modulesloaddir}

%files
%doc README.md
%license LICENSE

%files akmod-modules
%{_modulesloaddir}/%{name}.conf

%changelog
* Fri Mar 07 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
