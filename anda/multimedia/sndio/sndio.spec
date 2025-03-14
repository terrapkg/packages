Name:		sndio
Version:	1.10.0
Release:	1%?dist
Summary:	A sound library
#Group:		Sound/Utilities

License:	ISC
URL:		https://www.sndio.org
Source0:	https://www.sndio.org/%{name}-%{version}.tar.gz

Provides:	%{name}d = %version-%release
Provides:	%{name}ctl = %version-%release
Provides:	midicat = %version-%release
Provides:	aucat = %version-%release


BuildRequires:	pkgconfig(alsa)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  make gcc
Requires:	%name-libs = %{version}-%{release}

%description
Sndio is a small audio and MIDI framework part of the OpenBSD project and ported to FreeBSD, Linux and NetBSD. It provides a lightweight audio & MIDI server and a fully documented user-space API to access either the server or the hardware directly in a uniform way. Sndio is designed to work for desktop applications, but pays special attention to synchronization mechanisms and reliability required by music applications. Reliability through simplicity are part of the project goals. 

%package	libs
Summary:	Libraries for %{name}

%description libs
This package contains libraries for %{name}.

%package	devel
Summary:	Development files for %{name}
Requires:	%name-libs

%description devel
This package contains development files for %{name}.

%prep
%autosetup

cat<<EOF > sndiod.conf
u sndiod - "sndio" / /usr/sbin/nologin
EOF

cat<<EOF > 100-sndio.rules
polkit.addRule(function(action, subject) {
    if (subject.isInGroup("sndiod")) {
        return polkit.Result.YES;
    }
});
EOF

%build
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--with-libbsd
%make_build

%install
%make_install

# Install sndiod systemd service file
install -Dpm755 contrib/%{name}d.service %{buildroot}%{_unitdir}/%{name}d.service
install -Dpm644 contrib/default.%{name}d %{buildroot}%{_sysconfdir}/default/%{name}d

install -Dpm644 sndiod.conf -t %buildroot%_sysusersdir/
install -Dpm644 100-sndio.rules -t %buildroot%_datadir/polkit-1/rules.d/

# Fix for installing pkgconfig to correct lib64 dir on 64-bit systems.
%dnl %ifnarch %ix86
%dnl %__mkdir_p %{buildroot}%{_libdir}/pkgconfig
%dnl mv %{buildroot}/usr/lib/pkgconfig/sndio.pc %{buildroot}%{_libdir}/pkgconfig
%dnl %endif

%post
%systemd_post %{name}d.service

%preun
%systemd_preun %{name}d.service

%postun
%systemd_postun_with_restart %{name}d.service

%files
%{_bindir}/aucat
%{_bindir}/midicat
%{_bindir}/sndiod
%{_bindir}/sndioctl
%{_datadir}/polkit-1/rules.d/100-sndio.rules
%{_mandir}/man*/*
%{_unitdir}/%{name}d.service
%{_sysconfdir}/default/%{name}d
%{_sysusersdir}/%{name}d.conf

%files	libs
%license LICENSE
%{_libdir}/libsndio.so.7*

%files	devel
%{_libdir}/libsndio.so
%{_libdir}/pkgconfig/sndio.pc
%{_includedir}/sndio.h
