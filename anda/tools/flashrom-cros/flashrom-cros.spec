%global commit_date 20240911
%global commit  c1ab7468d28d164a30d598eb3e42a5febaf73bbc
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           flashrom-cros
Version:        %shortcommit
Release:        1%{?dist}
Summary:        Simple program for reading/writing flash chips content (ChromiumOS fork)
License:        GPL-2.0-only
URL:            https://chromium.googlesource.com/chromiumos/third_party/flashrom
Source0:        %url/+archive/refs/heads/release-R130-16033.B.tar.gz
BuildRequires:  gcc gnupg2 libusb1-devel meson pciutils-devel python3-sphinx systemd zlib-devel dmidecode
Requires:       dmidecode udev
Conflicts:      flashrom
Packager:       WeirdTreeThing <bradyn127@protonmail.com>


%description
flashrom is a utility for identifying, reading, writing, verifying and erasing
flash chips. It is designed to flash BIOS/EFI/coreboot/firmware/optionROM
images on mainboards, network/graphics/storage controller cards, and various
other programmer devices.

%prep
%setup -c

%build
%meson -Dtests=disabled -Ddocumentation=disabled -Duse_internal_dmi=false
%meson_build

%install
install -Dm755 %{_vpath_builddir}/flashrom %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Fri Jul 04 2025 Owen Zimmerman <owen@fyralabs.com>
- Add back to terra, conflict with flashrom

* Fri Oct 25 2024 WeirdTreeThing <bradyn127@protonmail.com>
- initial release
