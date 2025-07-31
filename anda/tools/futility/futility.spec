%define commit 5adf9508431b8c703eb60dde2fed0381079f7423
%define shortcommit %(c=%{commit}; echo ${c:0:12})

Name:           chromium-futility
Version:        git+%{shortcommit}
Release:        1%{?dist}
Summary:        Chromium OS EC utilities

License:        BSD-3-Clause
URL:            https://chromium.googlesource.com/chromiumos/platform/
Source0:        https://chromium.googlesource.com/chromiumos/platform/vboot_reference/+archive/refs/heads/main.tar.gz

BuildRequires:  make libxcrypt libxcrypt-devel
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  glibc
BuildRequires:  gcc
BuildRequires:  nss
BuildRequires:  nss-devel
BuildRequires:  flashrom-cros
BuildRequires:  flashrom-cros-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Chromium OS EC utilities

%prep
%autosetup -c
echo "INCLUDES += -I%{_includedir}" | cat - Makefile > Makefile.new
mv Makefile.new Makefile
ln -s /usr/include/libflashrom.h firmware/include/libflashrom.h

%build
%dnl export CFLAGS="$CFLAGS -I%{_includedir}/libflashrom.h"
%dnl export CFLAGS="$CFLAGS -I%{_includedir}"
%dnl make BUILD=futility
%make_build BUILD=futility CFLAGS="-I%{_includedir} $CFLAGS" V=1

%install
install -Dm 755 futility %{buildroot}%{_bindir}/chromium-futility

%files
%{_bindir}/chromium-futility
%license LICENSE
%doc README docs/

%changelog
* Fri Jul 04 2025 Owen Zimmerman <owen@fyralabs.com>
- initial package
