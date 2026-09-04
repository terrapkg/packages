%global repoversion 0.39.2

Name:           libtrueforce
Version:        1.3.11^%{repoversion}
Epoch:		    1
Release:        1%{?dist}
Summary:        Native Linux implementation of the Logitech Trueforce SDK
License:        GPL-2.0-only
URL:            https://github.com/mescon/logitech-trueforce-linux-driver
Source0:        %{url}/archive/refs/tags/v%{repoversion}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
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
%autosetup -c -n %{name}-%{repoversion}
mv ./logitech-trueforce-linux-driver-%{repoversion}/userspace/%{name}/* .
mv ./logitech-trueforce-linux-driver-%{repoversion}/docs/TRUEFORCE_PROTOCOL.md .
rm -rf ./logitech-trueforce-linux-driver-%{repoversion}

%build
%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} CFLAGS="%(echo %{build_cflags} | sed 's/-fPIE//g') -fPIC"

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
install -D -m644 %{name}.a %{buildroot}%{_libdir}/

%files
%doc README.md TRUEFORCE_PROTOCOL.md
%license COPYING
%{_libdir}/libtrueforce.so.*

%files devel
%{_libdir}/libtrueforce.so
%{_includedir}/trueforce.h

%files static
%{_libdir}/libtrueforce.a


%changelog
* Fri May 01 2026 Luan V. <luanv.oliveira@outlook.com> - 1.3.11^20260430git.df7f149-1
- Initial package
