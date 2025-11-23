%global commit 661ca1cba2984d874effa5ee5864132b079fbba0
%global commit_date 20251120
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           qdl
Version:        0^%commit_date.%shortcommit
Release:        1%?dist
Summary:        This tool communicates with USB devices of id 05c6:9008 to upload a flash loader and use this to flash images
URL:            https://github.com/linux-msm/qdl
Source0:        %{url}/archive/%{commit}/qdl-%{commit}.tar.gz
License:        BSD-3-Clause
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libusb-1.0)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n qdl-%{commit}

%build
%make_build

%install
install -Dm755 qdl %{buildroot}%{_bindir}/qdl
install -Dm755 qdl %{buildroot}%{_bindir}/qdl-ramdump
install -Dm755 qdl %{buildroot}%{_bindir}/ks

%files
%{_bindir}/qdl
%{_bindir}/qdl-ramdump
%{_bindir}/ks
%license LICENSE
%doc README.md

%changelog
* Sun Nov 23 2025 Owen-sz <owen@fyralabs.com>
- Initial commit
