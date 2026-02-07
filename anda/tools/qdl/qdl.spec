Name:           qdl
Version:        2.4
Release:        1%?dist
Summary:        This tool communicates with USB devices of id 05c6:9008 to upload a flash loader and use this to flash images
URL:            https://github.com/linux-msm/qdl
Source0:        %url/archive/refs/tags/v%version.tar.gz
License:        BSD-3-Clause
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libusb-1.0)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n qdl-%{version}

%build
%make_build
make manpages

%install
install -Dm755 qdl %{buildroot}%{_bindir}/qdl
install -Dm755 qdl %{buildroot}%{_bindir}/qdl-ramdump
install -Dm755 qdl %{buildroot}%{_bindir}/ks
mkdir -p %{buildroot}%{_mandir}/man1
install -Dm644 qdl.1 %{buildroot}%{_mandir}/man1/qdl.1
install -Dm644 qdl-ramdump.1 %{buildroot}%{_mandir}/man1/qdl-ramdump.1
install -Dm644 ks.1 %{buildroot}%{_mandir}/man1/ks.1

%files
%{_bindir}/qdl
%{_bindir}/qdl-ramdump
%{_bindir}/ks
%{_mandir}/man1/qdl.1.*
%{_mandir}/man1/qdl-ramdump.1.*
%{_mandir}/man1/ks.1.*

%license LICENSE
%doc README.md

%changelog
* Mon Feb 02 2026 Owen Zimmerman <owen@fyralabs.com>
- Switch to tagged versions

* Wed Nov 26 2025 metcya <metcya@gmail.com>
- Package manpages

* Sun Nov 23 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
