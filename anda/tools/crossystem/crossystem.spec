%global commit_date 20260105
%global commit 0ee734db27fe06a92b92e0bdc58c8b7f35dfaf16
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           crossystem
Summary:        Manage ChromeOS firmware
License:        BSD-3-Clause
URL:            https://chromium.googlesource.com/chromiumos/platform/vboot_reference

Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%?dist
Epoch:          1
Source0:        %url/+archive/refs/heads/firmware-R145-16552.2.B.tar.gz
Patch0:         use-flashrom-cros.patch
Patch1:         disable-werror.patch

Requires:       flashrom-cros
BuildRequires:  make gcc openssl-devel flashrom-cros-devel libuuid-devel

Packager:       WeirdTreeThing <bradyn127@protonmail.com>

%description
A tool to manage ChromeOS bootloader flags and get various
info from a ChromeOS system

%prep
%setup -C
%patch -P0 -p1
%patch -P1 -p1

%build
export CFLAGS="$CFLAGS -Wno-implicit-function-declaration"
%make_build

%install
install -Dm755 build/utility/crossystem %{buildroot}%{_bindir}/crossystem

%files
%license LICENSE
%{_bindir}/crossystem

%changelog
* Sun Jan 18 2026 Owen Zimmerman <owen@fyralabs.com>
- Bump, use proper versioning name, update patches and source link

* Fri Oct 25 2024 WeirdTreeThing <bradyn127@protonmail.com>
- initial release
