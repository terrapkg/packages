%global commit 9d1f5098b716681d087cca695ad714218a18d4e8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date %(date '+%Y%m%d')
Name:           joycond
Version:        %{commit_date}.git~%{shortcommit}
Release:        1%?dist
Summary:        Userspace daemon to combine joy-cons from the hid-nintendo kernel driver
License:        GPL-3.0-or-later
URL:            https://github.com/DanielOgorchock/joycond
Source0:        %url/archive/%{commit}/%{commit}.tar.gz#/%{name}-%{commit_date}.git~%{shortcommit}.tar.gz
Patch0:         https://github.com/terrapkg/pkg-joycond/raw/refs/heads/main/0001-Revert-virt_ctrlr_passthrough-send-uevent-change-eve.patch
Packager:       Cappy Ishihara <cappy@fyralabs.com>
BuildRequires:  libevdev-devel libudev-devel
BuildRequires:  cmake make systemd-rpm-macros gcc-c++

%description
joycond is a linux daemon which uses the evdev devices provided by hid-nintendo
(formerly known as hid-joycon) to implement joycon pairing.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
%cmake .
%cmake_build

%install
%cmake_install 

mkdir -p %buildroot%_unitdir %buildroot%_prefix
mv %buildroot%_sysconfdir/systemd/system/joycond.service %buildroot%_unitdir/joycond.service
mv %buildroot/lib/udev/ %buildroot%_prefix/lib/

%post
%systemd_post joycond.service

%preun
%systemd_preun joycond.service

%postun
%systemd_postun_with_restart joycond.service

%files
%_bindir/joycond
%_udevrulesdir/72-joycond.rules
%_udevrulesdir/89-joycond.rules
%_unitdir/joycond.service
%_sysconfdir/modules-load.d/joycond.conf
