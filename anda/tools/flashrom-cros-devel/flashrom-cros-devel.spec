%global commit_date 20240911
%global commit c1ab7468d28d164a30d598eb3e42a5febaf73bbc
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           flashrom-cros-devel
Version:        %shortcommit
Release:        1%{?dist}
Summary:        Development files for flashrom-cros
License:        GPL-2.0-only
URL:            https://chromium.googlesource.com/chromiumos/third_party/flashrom
Source0:        %url/+archive/refs/heads/release-R130-16033.B.tar.gz
BuildRequires:  gcc gnupg2 libusb1-devel meson pciutils-devel python3-sphinx systemd zlib-devel dmidecode
Requires:       libconfuse libftdi-devel libjaylink-devel pciutils-devel python3-libftdi
Conflicts:      flashrom-devel
Conflicts:      flashrom
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%setup -c

%build
%meson -Dtests=disabled -Ddocumentation=disabled -Duse_internal_dmi=false
%meson_build

%install
install -Dm755 %{_vpath_builddir}/libflashrom.so %{buildroot}%{_libdir}/libflashrom.so
install -Dm755 %{_vpath_builddir}/libflashrom.so.1 %{buildroot}%{_libdir}/libflashrom.so.1
install -Dm755 %{_vpath_builddir}/libflashrom.so.1.0.0 %{buildroot}%{_libdir}/libflashrom.so.1.0.0

%files
%{_libdir}/libflashrom.so
%{_libdir}/libflashrom.so.1
%{_libdir}/libflashrom.so.1.0.0

%changelog
* Fri Jul 04 2025 Owen Zimmerman <owen@fyralabs.com>
- initial package
