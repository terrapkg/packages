Name:           joycond
Version:        0.1.0
Release:        1%?dist
Summary:        Userspace daemon to combine joy-cons from the hid-nintendo kernel driver
License:        GPL-3.0-or-later
URL:            https://github.com/DanielOgorchock/joycond
Source0:        %url/archive/refs/tags/v%version.tar.gz
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  libevdev-devel libudev-devel
BuildRequires:  cmake make systemd-rpm-macros gcc-c++

%description
joycond is a linux daemon which uses the evdev devices provided by hid-nintendo
(formerly known as hid-joycon) to implement joycon pairing.

%prep
%autosetup

%build
%cmake .
%cmake_build

%install
cd redhat-linux-build/
cp joycond ..
%make_install 

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
