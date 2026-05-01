%global commit df7f1494f3bd584b8650304be7a37eca4bb49aa5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260430
%global debug_package %{nil}

Name:           libtrueforce
Version:        1.3.11^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Native Linux implementation of the Logitech Trueforce SDK
License:        GPL-2.0-only
URL:            https://github.com/mescon/logitech-rs50-linux-driver
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
Requires:       logitech-rs50-linux-driver
Provides:       trueforce-sdk = %{?epoch:%{epoch}:}%{version}
Packager:       Luan V. <luanv.oliveira@outlook.com>


%description
Native Linux implementation of the Logitech Trueforce SDK
(trueforce_sdk_x64.dll, version 1.3.11). Supports both the RS50 (046d:c276) and
the G Pro Racing Wheel (046d:c272 / 046d:c268) the two wheels use byte-for-byte
identical init and streaming packets, so the same library drives both. See
docs/TRUEFORCE_PROTOCOL.md in the parent repo for the protocol documentation.

%package static
Summary:        Static library for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description static
The %{name}-static package contains the static library for %{name}.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -c -n %{name}-%{commit}
mv ./logitech-rs50-linux-driver-%{commit}/userspace/%{name}/* .
mv ./logitech-rs50-linux-driver-%{commit}/docs/TRUEFORCE_PROTOCOL.md .
rm -rf ./logitech-rs50-linux-driver-%{commit}

%build
%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} CFLAGS="%{build_cflags}"

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
install -D -m644 %{name}.a %{buildroot}%{_libdir}/
install -D -m644 ./udev/99-logitech-rs50-trueforce.rules %{buildroot}/%{_udevrulesdir}/70-logitech-rs50-trueforce.rules

%posttrans
### Skip triggering if udevd isn't accessible
if [ -S /run/udev/control ]; then
    /usr/bin/udevadm control --reload
    /usr/bin/udevadm trigger --subsystem-match=hidraw
fi

%files
%doc README.md TRUEFORCE_PROTOCOL.md
%{_libdir}/*.so.*
%{_udevrulesdir}/70-logitech-rs50-trueforce.rules

%files devel
%{_libdir}/*.so
%{_includedir}/trueforce.h

%files static
%{_libdir}/*.a


%changelog
* Fri May 01 2026 libtrueforce - 1.3.11^20260430git.df7f149-1
- Initial package
