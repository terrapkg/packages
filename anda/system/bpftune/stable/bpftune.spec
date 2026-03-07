# BPF-based auto-tuning SPEC file

%global ver 0.4-2
%global releaseS %(echo '%ver' | sed -E 's/^[^-]+-//')

%define pcpdir	    /var/lib/pcp/pmdas
%define _sbindir    /usr/sbin

%undefine __brp_add_determinism

%bcond_with openrc

Name:           bpftune
Version:        %(echo '%ver' | sed 's/-.*//')
Release:        %{releaseS}%?dist
Summary:        BPF/tracing tools for auto-tuning Linux
License:        GPLv2-only WITH Linux-syscall-note
Packager:       veuxit <erroor234@gmail.com>
URL:            https://github.com/oracle/bpftune
Conflicts:      bpftune-nightly

Source0:        %{url}/archive/refs/tags/%{ver}.tar.gz

Group:          Development/Tools
Requires:       libbpf >= 0.6
Requires:       libnl3
Requires:       libcap
BuildRequires:  libbpf-devel >= 0.6
BuildRequires:  libcap-devel
BuildRequires:	bpftool >= 4.18
BuildRequires:  libnl3-devel
BuildRequires:  clang >= 11
BuildRequires:  clang-libs >= 11
BuildRequires:  llvm >= 11
BuildRequires:  llvm-libs >= 11
BuildRequires:	python3-docutils

%description
Service consisting of daemon (bpftune) and plugins which
support auto-tuning of Linux via BPF observability.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   libbpf-devel >= 0.6
Requires:   libcap-devel
Requires:   bpftool
Requires:   libnl3-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing BPF shared object tuners that use %{name}

%package pcp-pmda
Summary:	Performance Co-Pilot PMDA for bpftune
Requires:   %{name} = %{version}-%{release}
Requires:	pcp
Requires:   python3-pcp 

%description pcp-pmda
The %{name}-pcp-pmda exports tunables and metrics from bpftune
to Performance Co-Pilot (PCP)

%prep
%autosetup -n %{name}-%{ver}

%build
%make_build

%install
%make_install

%post
%systemd_post bpftune.service

%preun
%systemd_preun bpftune.service

%postun
%systemd_postun_with_restart bpftune.service

%files
%defattr(-,root,root)
%{_sysconfdir}/ld.so.conf.d/libbpftune.conf
%{_sbindir}/bpftune
%{_unitdir}/bpftune.service
%{_libdir}/libbpftune.so.%{version}.%{releaseS}
%{_libdir}/bpftune/*
%{_mandir}/*/*
%if %{with openrc}
%{_sysconfdir}/conf.d/bpftune
%{_sysconfdir}/init.d/bpftune
%else
%exclude %{_sysconfdir}/conf.d/bpftune
%exclude %{_sysconfdir}/init.d/bpftune
%endif

%license LICENSE.txt

%files devel
%{_libdir}/libbpftune.so
%{_includedir}/bpftune

%files pcp-pmda
%{pcpdir}/%{name}/*

%changelog
* Fri Mar 6 2026 veuxit <erroor234@gmail.com> - 0.4-2
- Initial package release
