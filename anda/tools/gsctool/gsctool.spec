%define commit c060a44d085fefabd414a026dc3177533f20f0f3
%define shortcommit %(c=%{commit}; echo ${c:0:12})
Name:           gsctool
Version:        git+%{shortcommit}
Release:        1%{?dist}
Summary:        Chromium OS EC utilities

License:      BSD-3-Clause
URL:          https://chromium.googlesource.com/chromiumos/platform/ec  
Source0:      https://chromium.googlesource.com/chromiumos/platform/ec/+archive/%{commit}.tar.gz#/%{name}-git+%{commit}.tar.gz

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  gcc

%description
Chromium OS EC utilities

%prep
%autosetup -c

%build
ls
pushd extra/usb_updater
%make_build


%install
pushd extra/usb_updater
install -D -m 755 gsctool %{buildroot}%{_bindir}/gsctool


%files
%{_bindir}/gsctool


%changelog
* Wed Mar 27 2024 Cappy Ishihara <cappy@cappuchino.xyz>
- initial release
