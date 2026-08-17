%global commit 55680f70d2a1e61c193fc78ff1d51c7437803683
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           chromium-ectool
Summary:        Query and send commands to ChromiumOS EC from userspace.
License:        BSD-3-Clause
URL:            https://chromium.googlesource.com/chromiumos/platform/ec/

Version:        %shortcommit
Release:        3%{?dist}
Source0:        https://github.com/coreboot/chrome-ec/archive/refs/heads/release-R100-14526.B-main.tar.gz
# fix warning in util/cbi-util.c
Patch0:         cbi-util-compile.patch
Conflicts:      ectool

BuildRequires:  make gcc libftdi-devel libusb1-devel hostname

%description
A tool to query and send commands to ChromiumOS EC from userspace.

%prep
%autosetup -n chrome-ec-release-R100-14526.B-main -p1

%build
BOARD=host %make_build utils-host

%install
install -Dm755 build/host/util/ectool %{buildroot}%{_bindir}/ectool

%files
%license LICENSE
%doc README.md
%{_bindir}/ectool

%changelog
* Sat Aug 09 2025 Owen Zimmerman <owen@fyralabs.com.com>
- Conflict with coreboot ectool.
* Tue Jan 2 2024 infinitebash <terra@infinitebash.com>
- Initial package.
