Name:           qdl
Version:        2.7
Release:        1%{?dist}
Summary:        This tool communicates with USB devices of id 05c6:9008 to upload a flash loader and use this to flash images
URL:            https://github.com/linux-msm/qdl
Source0:        %url/archive/refs/tags/v%version.tar.gz
License:        BSD-3-Clause
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(cmocka)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n qdl-%{version}

%conf
%meson

%build
%meson_build

%install
%meson_install

%files
%{_bindir}/qdl
%{_bindir}/qdl-ramdump
%{_bindir}/qdl-ks
%{_mandir}/man1/qdl.1.*
%{_mandir}/man1/qdl-ramdump.1.*
%{_mandir}/man1/qdl-ks.1.*

%license LICENSE
%doc README.md

%changelog
* Mon Jun 08 2026 Owen Zimmerman <owen@fyralabs.com> - 2.7-1
- Update spec for 2.7

* Mon Feb 02 2026 Owen Zimmerman <owen@fyralabs.com>
- Switch to tagged versions

* Wed Nov 26 2025 metcya <metcya@gmail.com>
- Package manpages

* Sun Nov 23 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
