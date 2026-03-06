# BPF-based auto-tuning SPEC file

%define pcpdir	    /var/lib/pcp/pmdas
%define _sbindir    /usr/sbin

%undefine __brp_add_determinism

%define releaseS 2

%bcond_with openrc

Name:           bpftune
Version:        0.4
Release:        2%?dist
Summary:        BPF/tracing tools for auto-tuning Linux
License:        GPLv2 WITH Linux-syscall-note
Packager:       veuxit <erroor234@gmail.com>
URL:            https://github.com/oracle/bpftune
Conflicts:      bpftune-git

Source0:        %{url}/archive/refs/tags/%{version}-%{releaseS}.tar.gz

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
%autosetup -n %{name}-%{version}-%{releaseS}

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

%license LICENSE.txt

%files pcp-pmda
%{pcpdir}/%{name}/*

%license LICENSE.txt

%changelog
* Fri Mar 6 2026 veuxit <erroor234@gmail.com> - 0.4-2
- Initial package release