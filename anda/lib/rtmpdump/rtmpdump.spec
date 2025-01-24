%global commit 6f6bb1353fc84f4cc37138baa99f586750028a01
%global commit_date 20240301
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           rtmpdump
Version:        2.6^%{commit_date}git%{shortcommit}
Release:        1%{?dist}
Summary:        Toolkit for RTMP streams
# The tools are GPLv2+, but the he library is LGPLv2+.
License:        GPLv2+
URL:            https://git.ffmpeg.org/gitweb/%{name}.git
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  gnutls-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  nettle-devel
BuildRequires:  zlib-devel

%description
rtmpdump is a toolkit for RTMP streams. All forms of RTMP are supported.

%package -n librtmp
Summary:        Support library for RTMP streams
License:        LGPLv2+

%description -n librtmp
librtmp is a support library for RTMP streams. All forms of RTMP are supported.

%package -n librtmp-devel
Summary:        Files for librtmp development
License:        LGPLv2+
Requires:       librtmp%{?_isa} = %{version}-%{release}

%description -n librtmp-devel
Development package for librtmp.

%prep
git clone https://git.ffmpeg.org/%{name}.git
%setup -T -D -n %{name}

%build
make SYS=posix CRYPTO=GNUTLS SHARED=yes OPT="%{optflags}"

%install
make CRYPTO=GNUTLS SHARED=yes DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} libdir=%{_libdir} install
find %{buildroot} -name "*.a" -delete

%files
%license COPYING
%doc README
%{_bindir}/rtmpdump
/usr/sbin/rtmpsrv
/usr/sbin/rtmpgw
/usr/sbin/rtmpsuck
%{_mandir}/man1/rtmpdump.1*
%{_mandir}/man8/rtmpgw.8*

%files -n librtmp
%license librtmp/COPYING
%doc ChangeLog
%{_libdir}/librtmp.so.1

%files -n librtmp-devel
%{_includedir}/librtmp/
%{_libdir}/librtmp.so
%{_libdir}/pkgconfig/librtmp.pc
%{_mandir}/man3/librtmp.3*

%changelog
%autochangelog
