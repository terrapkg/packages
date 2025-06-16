%global debug_package %{nil}
%global commit e89983c628d046b2f77af3b6678cc49c2dd58332
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20250521
# Actual "release" version, currently unused as the release versions are back and forth on if on if they use 1.0.0 or 1.0.1
# Use this if they ever stop doing that I guess
%global ver 1.0.1

Name:           intel-ipu6-drivers
Summary:        Common files for Intel IPU6 drivers
Version:        0^%{commit_date}git.%{shortcommit}
Release:        2%?dist
License:        GPL-2.0-or-later
URL:            https://github.com/intel/ipu6-drivers
Source0:        https://github.com/intel/ipu6-drivers/archive/%{commit}/ipu6-drivers-%{shortcommit}.tar.gz
Requires:       ipu6-camera-bins
Requires:       intel-ipu6-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       intel-ipu6-kmod-common = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch:      noarch
Packager:       Gilver E. <rockgrub@disroot.org>

%description
Common files for the Intel IPU6 camera drivers.

%prep
%autosetup -n ipu6-drivers-%{commit}

%build

%install

%files
%license LICENSE
%doc README.md
%doc SECURITY.md

%changelog
* Thu Apr 24 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
